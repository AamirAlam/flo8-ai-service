import lancedb
import os
import json
import re
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from lancedb_setup import setup_lancedb, retrieve_similar_docs
from typing import List, Dict, Optional, Any
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()

class NodeUi(BaseModel):
    name: str
    parameters: Dict[str, Any]
    position: List[int]
    type: str
    typeVersion: int

class Connections(BaseModel):
    main: Optional[List[List[Dict[str, Any]]]] = None

class WorkflowData(BaseModel):
    nodes: List[NodeUi]
    connections: Dict[str, Connections]

class AiResponse(BaseModel):
    text: str
    instruction: Optional[str] = None
    workflowData: Optional[Dict[str, Any]] = None

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
        system_prompt="You are an expert in generating valid n8n workflow JSONs based on user requirements; ensure the structure follows n8n's schema, include necessary nodes, connections, and configurations, use appropriate parameters, placeholders for API keys, and format the JSON correctly for direct import into n8n, responding only with the JSON output without explanations. Include a text message to hint about the result in a text key, this will only be used for information purposes also include a instruction key to provide instructions if needed (import, run, requestcontext, requestData:Telegram). Include a workflowData key to provide the workflow JSON.",
        result_type=AiResponse
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

    # print('prompt response ', response.data)
    
    # Check if response.data is an AiResponse object
    if isinstance(response.data, AiResponse):
        # Already properly formatted, return as is
        return response.data.model_dump()
    else:
        # If response.data is a string or other format, try to extract JSON
        response_data = response.data
        
        # Try to parse as JSON first
        try:
            # If it's already valid JSON, parse it
            if isinstance(response_data, str):
                # Extract JSON from markdown code block if present
                json_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', response_data)
                
                if json_match:
                    json_str = json_match.group(1)
                    workflow_json = json.loads(json_str)
                else:
                    # Try parsing the whole string as JSON
                    workflow_json = json.loads(response_data)
                
                # Check if it has the expected structure
                if "nodes" in workflow_json and "connections" in workflow_json:
                    print("workflow_json from first if")
                    # It appears to be just the workflowData part
                    return AiResponse(
                        response="Workflow JSON generated successfully",
                        workflowData=workflow_json
                    ).model_dump()
                elif "workflowData" in workflow_json:
                    print("workflow_json from second if")
                    # It already has the right structure
                    if "response" not in workflow_json:
                        workflow_json["response"] = "Workflow JSON generated successfully"
                    return workflow_json
            print("workflow_json from else")
            # If we got here, the structure doesn't match expectations
            return {
                "response": "Workflow JSON structure doesn't match expected format",
                "rawOutput": response_data
            }
            
        except (json.JSONDecodeError, TypeError, ValueError) as e:
            # If JSON parsing fails, return the original response
            return {
                "error": f"Failed to parse response: {str(e)}",
                "rawOutput": response_data
            }


def process_query_v2(text, credentialData=None, workflowData=None, errorData=None, db_path="./db", table_name="knowledge"):
    """
    Process a query using the AI agents and return the response.
    
    Args:
        text (str): The user's query
        credentialData (dict): Credential data
        workflowData (dict): Workflow data
        errorData (dict): Error data
        db_path (str): Path to the LanceDB database
        table_name (str): Name of the knowledge table
        
    Returns:
        dict: A dictionary containing the JSON response with format:
        {
            "text": str,
            "instruction": Optional[str],  # 'import' | 'run' | 'requestcontext' | 'requestData:Telegram'
            "workflowData": Optional[Dict]
        }
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
    knowledge_query_result = knowledge_query_agent.run_sync(text)
    knowledge_query = knowledge_query_result.data
    
    # Retrieve similar documents
    retrieved_docs = retrieve_similar_docs(knowledge_table, knowledge_query, limit=100)
    
    # Build knowledge context from retrieved documents
    knowledge_context = ""
    for doc in retrieved_docs:
        if doc['_relevance_score'] > 0.7:
            knowledge_context += doc['text']
    
    # Create prompt with context and query
    prompt = f"Context from knowledge base:\n{knowledge_context}\n"
    
    if credentialData:
        prompt += f"Credential information available: {', '.join(credentialData.keys())}\n"
    
    if workflowData:
        prompt += f"Current workflow data:\n{json.dumps(workflowData)}\n"
    
    if errorData:
        prompt += f"Error data:\n{json.dumps(errorData)}\n"
    
    prompt += f"User Query:\n{text}\n\n"
    prompt += "Answer based on the above context and provide appropriate instruction if needed (import, run, requestcontext, requestData:Telegram)."
    
    # Get response from main agent
    response = main_agent.run_sync(prompt)
    
    # Process the response
    if isinstance(response.data, AiResponse):
        # Already properly formatted, return as is
        print("Response data1:", response.data)
        return response.data.model_dump()
    else:
        # If response.data is a string or other format, try to extract JSON
        response_data = response.data

        print("Response data:", response_data)
        
        # Try to parse as JSON first
        try:
            # If it's already valid JSON, parse it
            if isinstance(response_data, str):
                # Check if the response looks like a complete response object
                if response_data.strip().startswith('{') and ('instruction' in response_data or 'text' in response_data):
                    try:
                        parsed_response = json.loads(response_data)
                        # If it has the expected structure, return it directly
                        if 'text' in parsed_response:
                            # If workflowData is a string, try to parse it as JSON
                            if 'workflowData' in parsed_response and isinstance(parsed_response['workflowData'], str):
                                try:
                                    parsed_response['workflowData'] = json.loads(parsed_response['workflowData'])
                                except json.JSONDecodeError:
                                    pass  # Keep as string if it can't be parsed
                            return parsed_response
                    except json.JSONDecodeError:
                        pass  # Continue with other parsing methods
                
                # Extract JSON from markdown code block if present
                json_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', response_data)
                
                if json_match:
                    json_str = json_match.group(1)
                    parsed_json = json.loads(json_str)
                else:
                    # Try parsing the whole string as JSON
                    try:
                        # Check if the string itself is valid JSON
                        parsed_json = json.loads(response_data)
                    except json.JSONDecodeError:
                        # If it's not valid JSON but contains a JSON-like structure
                        # Try to extract JSON from the text
                        json_pattern = r'(\{[\s\S]*\})'
                        json_match = re.search(json_pattern, response_data)
                        
                        if json_match:
                            try:
                                potential_json = json_match.group(1)
                                parsed_json = json.loads(potential_json)
                            except json.JSONDecodeError:
                                # If not JSON, treat as plain text response
                                return {
                                    "text": response_data
                                }
                        else:
                            # If not JSON, treat as plain text response
                            return {
                                "text": response_data
                            }
                
                # Check if it has the expected structure for a workflow
                if "nodes" in parsed_json and "connections" in parsed_json:
                    # It appears to be just the workflowData part
                    return {
                        "text": "Workflow JSON generated successfully",
                        "instruction": "import",
                        "workflowData": parsed_json
                    }
                elif "text" in parsed_json and isinstance(parsed_json["text"], str):
                    # If text field contains a JSON string that looks like a workflow
                    try:
                        workflow_json = json.loads(parsed_json["text"])
                        if "nodes" in workflow_json and "connections" in workflow_json:
                            return {
                                "text": parsed_json.get("instruction", "Workflow JSON generated successfully"),
                                "instruction": parsed_json.get("instruction", "import"),
                                "workflowData": workflow_json
                            }
                    except (json.JSONDecodeError, TypeError):
                        # If text is not a valid JSON string, return the parsed JSON as is
                        return parsed_json
                else:
                    # Unknown structure, return as workflowData
                    return {
                        "text": "Data processed successfully",
                        "workflowData": parsed_json
                    }
            
            # If we got here, the structure doesn't match expectations
            return {
                "text": "Unable to process response in expected format",
                "workflowData": response_data if isinstance(response_data, dict) else None
            }
            
        except (json.JSONDecodeError, TypeError, ValueError) as e:
            # If JSON parsing fails, return the original response as text
            return {
                "text": response_data if isinstance(response_data, str) else f"Error processing response: {str(e)}"
            }