#!/usr/bin/env python3
"""
Test script for the Flask API with AI integration.
This script tests the /api/ai/query endpoint by sending a POST request with a query.
"""
import requests
import json
import sys

def test_query_endpoint(query):
    """Test the query endpoint with the given query."""
    url = "http://localhost:5001/api/ai/query"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "query": query
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        # Print status code
        print(f"Status Code: {response.status_code}")
        
        # Print response headers
        print("\nResponse Headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
        
        # Print response body
        print("\nResponse Body:")
        if response.status_code == 200:
            response_json = response.json()
            print(json.dumps(response_json, indent=2))
        else:
            print(response.text)
            
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    # Get query from command line arguments or use default
    query = sys.argv[1] if len(sys.argv) > 1 else "How do I create a workflow in n8n?"
    
    print(f"Testing API with query: '{query}'")
    test_query_endpoint(query)
