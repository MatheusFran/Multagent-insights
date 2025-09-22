from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from pypdf import PdfReader
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from langchain.tools.retriever import create_retriever_tool
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document


class RetrievalTool:
    def __init__(self, path):
        self.path = path
        self.docs = []

    def _load_split(self):
        text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=100, chunk_overlap=50
        )
        for file in os.listdir(self.path):
            if file.endswith(".pdf"):
                file_path = os.path.join(self.path, file)
                reader = PdfReader(file_path)

                text = ""
                for page in reader.pages:
                    text += page.extract_text()

                doc = Document(
                    page_content=text,
                    metadata={"source": file}
                )

                doc_splits = text_splitter.split_documents([doc])
                self.docs.extend(doc_splits)

    def _embeddings(self):
        embeddings = SentenceTransformer("all-MiniLM-L6-v2")

        vectorstore = InMemoryVectorStore.from_documents(
            documents=self.docs, embedding=embeddings
        )
        retriever = vectorstore.as_retriever()
        return retriever

    def _create_retriever(self):
        retriever = self._embeddings()
        retriever_tool = create_retriever_tool(
            retriever,
            "retriever_pdf_docs",
            "Pesquisa e retorna informação dos documentos jurídicos e compliance da empresa",
        )
        return retriever_tool

    def __call__(self, *args, **kwargs):
        self._load_split()
        self._create_retriever()


def create_rag_agent(pdf_path, model):
    retriever_tool = RetrievalTool(pdf_path)

    agent_rag = create_react_agent(
        model=model,
        tools=[retriever_tool],
        prompt=(
            "Você é um agente do RAG para análise de conformidade de documentos.\n\n"
            "INSTRUÇÕES:\n"
            "- Use a ferramenta retriever_pdf_docs para buscar informações relevantes\n"
            "- Forneça respostas precisas com base nos documentos recuperados\n"
            "- Se não encontrar informações relevantes, diga isso claramente\n"
            "- Cite o documento de origem sempre que possível"
        ),
        name="rag_agent",
    )

    return agent_rag
