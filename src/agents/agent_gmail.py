from langgraph.prebuilt import create_react_agent
from langchain_google_community import GmailToolkit

def create_gmail_agent(model):
    toolkit = GmailToolkit().tolist()

    agent = create_react_agent(
        model=model,
        tools=toolkit,
        prompt="What is your name?",
    )

    return agent