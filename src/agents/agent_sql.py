from langchain.chat_models import init_chat_model
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langgraph.prebuilt import create_react_agent


def create_sql_agent(db_uri="sqlite:///Chinook.db",model):

    db = SQLDatabase.from_uri(db_uri)

    toolkit = SQLDatabaseToolkit(db=db, llm=model)
    tools = toolkit.get_tools()

    for tool in tools:
        print(f"{tool.name}: {tool.description}\n")

    prompt = f"""
    You are an agent designed to interact with a SQL database.
    Given an input question, create a syntactically correct {db.dialect} query to run,
    then look at the results of the query and return the answer. Unless the user
    specifies a specific number of examples they wish to obtain, always limit your
    query to at most 5 results.

    You can order the results by a relevant column to return the most interesting
    examples in the database. Never query for all the columns from a specific table,
    only ask for the relevant columns given the question.

    You MUST double check your query before executing it. If you get an error while
    executing a query, rewrite the query and try again.

    DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the
    database.

    To start you should ALWAYS look at the tables in the database to see what you
    can query. Do NOT skip this step.

    Then you should query the schema of the most relevant tables.
    """

    agent = create_react_agent(
        model=model,
        tools=tools,
        prompt=prompt,
    )

    return agent
