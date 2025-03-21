import lancedb
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from lancedb_setup import setup_lancedb,retrieve_similar_docs

def setup_knowledge_query_agent():
    """
    Set up the knowledge query agent.
    """
    agent = Agent(
        name='Knowledge Query Agent',
        model=OpenAIModel('gpt-4o-mini'),
        deps_type=str,
        result_type=str,
        system_prompt='From the input text string, please generate a query string to pass to the knowledge base.'
    )

    return agent

def setup_main_agent():
    """
    Set up the main agent.
    """
    agent = Agent(
        name='Main Agent',
        model=OpenAIModel('gpt-4o-mini'),
        system_prompt="You are an expert in generating valid n8n workflow JSONs based on user requirements; ensure the structure follows n8n's schema, include necessary nodes, connections, and configurations, use appropriate parameters, placeholders for API keys, and format the JSON correctly for direct import into n8n, responding only with the JSON output without explanations.",
    )

    return agent


def main():
    """
    Main execution flow for the application.
    """
    db_path = "./db"
    table_name = "knowledge"
    db = lancedb.connect(db_path)

    knowledge_table = db.open_table(table_name) if db.table_names() else setup_lancedb()

    knowledge_query_agent = setup_knowledge_query_agent()

    agent = setup_main_agent()

    message_history = None

    while True:
        query = input("Enter your query: ")
        if query == 'exit':
            break

        res = knowledge_query_agent.run_sync(query)
        knowledge_query = res.data
        print('Knowledge Query:', knowledge_query)

        retrieved_docs = retrieve_similar_docs(knowledge_table, knowledge_query, limit=100)

        knowledge_context = ""
        for doc in retrieved_docs:
            if doc['_relevance_score'] > 0.7:
                knowledge_context += doc['text']

        prompt = f"Context:\n{knowledge_context}\nUser Query:\n{query}\n\nAnswer based on the above context:"
        response = agent.run_sync(prompt, message_history=message_history)
        print(response.data)

        message_history = response.all_messages()


main()