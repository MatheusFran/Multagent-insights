from langchain.chat_models import init_chat_model
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langgraph.prebuilt import create_react_agent

load_dotenv()


def create_sql_agent(db_uri, model):
    db = SQLDatabase.from_uri(db_uri)

    toolkit = SQLDatabaseToolkit(db=db, llm=model)
    tools = toolkit.get_tools()

    for tool in tools:
        print(f"{tool.name}: {tool.description}\n")

    prompt = f"""
    Você é um agente projetado para interagir com um banco de dados SQL.
    Dada uma pergunta de entrada, crie uma consulta {db.dialect} sintaticamente correta para ser executada,
    em seguida, observe os resultados da consulta e retorne a resposta. A menos que o usuário
    especifique um número específico de exemplos que deseja obter, sempre limite sua
    consulta a, no máximo, 5 resultados.

    Você pode ordenar os resultados por uma coluna relevante para retornar os exemplos
    mais interessantes no banco de dados. Nunca consulte todas as colunas de uma tabela específica,
    solicite apenas as colunas relevantes para a pergunta.

    Você DEVE verificar sua consulta duas vezes antes de executá-la. Se ocorrer um erro ao
    executar uma consulta, reescreva-a e tente novamente.

    NÃO crie nenhuma instrução DML (INSERT, UPDATE, DELETE, DROP etc.) no
    banco de dados.

    Para começar, você deve SEMPRE consultar as tabelas no banco de dados para ver o que
    pode consultar. NÃO pule esta etapa.

    Em seguida, você deve consultar o esquema das tabelas mais relevantes.
    """

    agent = create_react_agent(
        model=model,
        tools=tools,
        prompt=prompt,
    )

    return agent
