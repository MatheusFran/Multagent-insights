from langgraph_supervisor import create_supervisor
from langchain.chat_models import init_chat_model

from prompts import supervisor_prompt
from src.agents.agent_rag import create_rag_agent
from src.agents.agent_sql import create_sql_agent


def create_supervisor():
    llm = init_chat_model()

    agent_rag = create_rag_agent(pdf_path='', model=llm)
    agent_sql = create_sql_agent(db_uri='', model=llm)
    agent_gmail = create_sql_agent(model=llm)

    supervisor = create_supervisor(
        model=llm,
        agents=[agent_rag, agent_sql, agent_gmail],
        prompt=supervisor_prompt,
        add_handoff_messages=True,
        output_mode="full_history"
    ).compile()

    return supervisor
