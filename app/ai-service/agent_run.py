import lancedb
import os
import json
import re
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from lancedb_setup import setup_lancedb, retrieve_similar_docs
from typing import List, Dict, Optional
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()

class NodeUi(BaseModel):
    pass  # This will be expanded based on your actual node structure

class Connections(BaseModel):
    pass  # This will be expanded based on your actual connections structure

class WorkflowData(BaseModel):
    nodes: List[NodeUi]
    connections: Connections

class AiResponse(BaseModel):
    response: str
    workflowData: object

def setup_knowledge_query_agent():
    """
    Set up the knowledge query agent.
    """
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    agent = Agent(
        name='Knowledge Query Agent',
        model=OpenAIModel('gpt-4o-mini', api_key=openai_api_key),
        deps_type=str,
        result_type=str,
        system_prompt='From the input text string, please generate a query string to pass to the knowledge base.'
    )

    return agent

def setup_main_agent():
    """
    Set up the main agent.
    """
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    agent = Agent(
        name='Main Agent',
        model=OpenAIModel('gpt-4o-mini', api_key=openai_api_key),
        system_prompt="You are an expert in generating valid n8n workflow JSONs based on user requirements; ensure the structure follows n8n's schema, include necessary nodes, connections, and configurations, use appropriate parameters, placeholders for API keys, and format the JSON correctly for direct import into n8n, responding only with the JSON output without explanations.",
    )

    return agent

def process_query(query, db_path="./db", table_name="knowledge"):
    """
    Process a query using the AI agents and return the response.
    
    Args:
        query (str): The user's query
        db_path (str): Path to the LanceDB database
        table_name (str): Name of the knowledge table
        
    Returns:
        dict: A dictionary containing the JSON response
    """
    # Initialize database connection
    db = lancedb.connect(db_path)
    
    # Check if table exists, if not create it
    if table_name not in db.table_names():
        knowledge_table = setup_lancedb()
    else:
        knowledge_table = db.open_table(table_name)
    
    # Set up the agents
    knowledge_query_agent = setup_knowledge_query_agent()
    main_agent = setup_main_agent()
    
    # Generate knowledge query
    knowledge_query_result = knowledge_query_agent.run_sync(query)
    knowledge_query = knowledge_query_result.data
    
    # Retrieve similar documents
    retrieved_docs = retrieve_similar_docs(knowledge_table, knowledge_query, limit=100)
    
    # Build knowledge context from retrieved documents
    knowledge_context = ""
    for doc in retrieved_docs:
        if doc['_relevance_score'] > 0.7:
            knowledge_context += doc['text']
    
    # Create prompt with context and query
    prompt = f"Context:\n{knowledge_context}\nUser Query:\n{query}\n\nAnswer based on the above context:"
    
    # Get response from main agent
    response = main_agent.run_sync(prompt)
    
    # Parse the response data to extract the JSON
    response_data = response.data.response if isinstance(response.data, AiResponse) else response.data
    
    # Extract JSON from markdown code block if present
    json_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', response_data)
    
    if json_match:
        # Extract the JSON string
        json_str = json_match.group(1)
        try:
            # Parse the JSON string into a Python dictionary
            workflow_json = json.loads(json_str)
            return AiResponse(
                response='Workflow JSON generated successfully',
                workflowData=workflow_json
            ).model_dump()
        except json.JSONDecodeError:
            # If JSON parsing fails, return the original response
            return {"error": "Failed to parse JSON from response", "raw_response": response_data}
    else:
        # If no JSON code block is found, return the original response
        return {"error": "No JSON found in response", "raw_response": response_data}