import os

from langgraph_supervisor import create_supervisor
from langchain.chat_models import init_chat_model

from src.agents.agent_rag import create_rag_agent
from src.agents.agent_sql import create_sql_agent
from dotenv import load_dotenv

load_dotenv()

supervisor_prompt = """
    Você é um supervisor, gerenciando 3 agentes:
    - um agente gerenciador de SQL/banco de dados,ele executa querys no banco de dados do sistema
    - um agente RAG, ele aplica técnicas de RAG em documentos juridicos e de compliance da empresa, que nao ficam no banco de dados
    - um agente de gmail, que executa envios de email informando os dados analisados
    Atribua trabalho a um agente por vez, não ligue para os agentes em paralelo.
    Somente faça o trabalho de analisar de maneira técnica as informações, como um agent de Business Intelligence.
"""

def create_supervisor():
    llm = init_chat_model()

    agent_rag = create_rag_agent(pdf_path='', model=llm)
    agent_sql = create_sql_agent(db_uri=os.getenv("URI_POSTGRES"), model=llm)
    agent_gmail = create_sql_agent(model=llm)

    supervisor = create_supervisor(
        model=llm,
        agents=[agent_rag, agent_sql, agent_gmail],
        prompt=supervisor_prompt,
        add_handoff_messages=True,
        output_mode="full_history"
    ).compile()

    return supervisor
