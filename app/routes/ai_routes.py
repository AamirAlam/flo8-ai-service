from flask import Blueprint, request, jsonify
import sys
import os

# Add the ai-service directory to the path so we can import from it
sys.path.append(os.path.join(os.path.dirname(__file__), '../ai-service'))
from agent_run import process_query
from agent_run import process_query_v2

ai_bp = Blueprint('ai', __name__, url_prefix='/api/ai')


@ai_bp.route('/', methods=['GET'])
def get_items():
    return jsonify({"response": "Hello, World from AI!"})


@ai_bp.route('/query', methods=['POST'])
def handle_query():
    """
    Process a query using the AI agents and return the response.
    
    Expected JSON body:
    {
        "query": "Your question or request here"
    }
    """
    # Check if request contains JSON data
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    # Get the query from the request
    data = request.get_json()
    query = data.get('query')
    
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    
    try:
        # Process the query using the agent_run module
        result = process_query(query)
        
        # Return the response
        return jsonify(result) 
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@ai_bp.route('/query-v2', methods=['POST'])
def handle_query_v2():
    """
    Process a query using the AI agents and return the response.
    
    Expected JSON body:
    {
        "text": "build me an app",
        "credentialData": {},
        "workflowData": {},
        "errorData": {}
    }
    
    Returns:
    {
        "text": "response message",
        "instruction": "import|run|requestcontext|requestData:Telegram", (optional)
        "workflowData": {} (optional)
    }
    """
    # Check if request contains JSON data
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    # Get the query from the request
    data = request.get_json()
    text = data.get('text')
    context = data.get('context')
    credentialData = context.get('credentialData', {})
    workflowData = context.get('workflowData', {})
    errorData = context.get('errorData', {})

    print("context", context)
    print("credentialData", credentialData)
    print("workflowData", workflowData)
    print("errorData", errorData)
    
    if not text:
        return jsonify({"error": "Text parameter is required"}), 400
    
    try:
        # Process the query using the agent_run module
        result = process_query_v2(
            text=text,
            credentialData=credentialData,
            workflowData=workflowData,
            errorData=errorData
        )
        
        # Return the response
        return jsonify(result) 
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
