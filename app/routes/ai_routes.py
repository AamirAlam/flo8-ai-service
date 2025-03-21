from flask import Blueprint, request, jsonify
import sys
import os
import lancedb

# Add the ai-service directory to the path so we can import from it
sys.path.append(os.path.join(os.path.dirname(__file__), '../ai-service'))
from agent_run import setup_knowledge_query_agent, setup_main_agent
from lancedb_setup import retrieve_similar_docs

ai_bp = Blueprint('ai', __name__, url_prefix='/api/ai')


@ai_bp.route('/', methods=['GET'])
def get_items():
    return jsonify({"response": "Hello, World from AI!"})


@ai_bp.route('/query', methods=['POST'])
def process_query():
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
        # Initialize database connection
        db_path = "./db"
        table_name = "knowledge"
        db = lancedb.connect(db_path)
        
        # Check if table exists, if not return appropriate message
        if table_name not in db.table_names():
            return jsonify({
                "error": "Knowledge database not initialized",
                "message": "Please initialize the database before querying"
            }), 500
        
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
        
        # Return the response
        return jsonify({
            "query": query,
            "knowledge_query": knowledge_query,
            "response": response.data,
            "retrieved_docs_count": len(retrieved_docs),
            "relevant_docs_count": sum(1 for doc in retrieved_docs if doc['_relevance_score'] > 0.7)
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
