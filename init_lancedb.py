#!/usr/bin/env python3
"""
Initialize the LanceDB database with sample knowledge.
"""
import os
import sys
from pathlib import Path
import lancedb
from lancedb.embeddings import get_registry
from lancedb.pydantic import LanceModel, Vector
from lancedb.table import LanceTable
from lancedb.rerankers import LinearCombinationReranker

# Get OpenAI API key from environment
openai_api_key = os.environ.get('OPENAI_API_KEY')
if not openai_api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    sys.exit(1)

# Set up embedding function
openai_func = get_registry().get("openai").create(
    name="text-embedding-3-small", 
    apiKey=openai_api_key
)

class Document(LanceModel):
    """
    Defines the schema for documents to be stored in the LanceDB table.
    """
    id: str
    text: str = openai_func.SourceField()
    vector: Vector(openai_func.ndims()) = openai_func.VectorField()

def chunk_text(text, max_tokens=8192):
    """
    Simple chunking based on character count
    Approximate tokens by characters (rough estimate: 4 chars ≈ 1 token)
    """
    char_limit = max_tokens * 4
    for i in range(0, len(text), char_limit):
        yield text[i:i + char_limit]

def create_lancedb_table(db_path, table_name, overwrite=True):
    """
    Connect to LanceDB and create a table for storing knowledge documents.
    """
    db = lancedb.connect(db_path)
    mode = 'overwrite' if overwrite else 'create'
    table = db.create_table(table_name, schema=Document, mode=mode)
    table.create_fts_index('text', replace=True, use_tantivy=False)
    return table

def add_documents_to_table(table, knowledge_base_dir, max_tokens=8192):
    """
    Add markdown documents from a local directory to the LanceDB table.
    """
    docs = []
    knowledge_base = Path(knowledge_base_dir)

    for md_file in knowledge_base.glob('*.md'):
        print(f'Processing {md_file.name}')
        with open(md_file, 'r', encoding='utf-8') as f:
            text = f.read()
            for i, chunk in enumerate(chunk_text(text, max_tokens=max_tokens)):
                doc_id = f'{md_file.stem}_{i}'
                docs.append({'id': doc_id, 'text': chunk})

    if docs:
        table.add(docs)
        print(f'Added {len(docs)} documents (chunks) to the table.')
    else:
        print('No documents found or added.')

def init_database():
    """Initialize the LanceDB database with sample knowledge."""
    print("Initializing LanceDB database...")
    
    # Create and populate the database
    db_path = './db'
    table_name = 'knowledge'
    knowledge_files_dir = './knowledge_files'
    
    # Create the table
    table = create_lancedb_table(db_path, table_name, overwrite=True)
    
    # Add documents to the table
    add_documents_to_table(table, knowledge_files_dir)
    
    print(f"Database initialized successfully at {db_path}")
    print(f"Table '{table_name}' created and populated with knowledge from {knowledge_files_dir}")

if __name__ == "__main__":
    print("Starting database initialization...")
    init_database()
    print("Database initialization complete.")
