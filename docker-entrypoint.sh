#!/bin/bash
set -e

# Create necessary directories
mkdir -p /app/db
mkdir -p /app/knowledge_files

# Create a sample knowledge file if it doesn't exist
if [ ! -f "/app/knowledge_files/sample_knowledge.md" ]; then
  echo "Creating sample knowledge file..."
  cat > /app/knowledge_files/sample_knowledge.md << 'EOL'
# Sample Knowledge

## Introduction to AI

Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions. The term may also be applied to any machine that exhibits traits associated with a human mind such as learning and problem-solving.

## Machine Learning

Machine Learning is a subset of artificial intelligence that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it to learn for themselves.

## Natural Language Processing

Natural Language Processing (NLP) is a field of artificial intelligence that gives computers the ability to understand text and spoken words in much the same way human beings can. NLP combines computational linguistics—rule-based modeling of human language—with statistical, machine learning, and deep learning models.

## Computer Vision

Computer Vision is a field of artificial intelligence that trains computers to interpret and understand the visual world. Using digital images from cameras and videos and deep learning models, machines can accurately identify and classify objects — and then react to what they "see."
EOL
  echo "Sample knowledge file created."
else
  echo "Sample knowledge file already exists."
fi

# Create a Python script to initialize the database
cat > /app/init_lancedb.py << 'EOL'
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
    db_path = '/app/db'
    table_name = 'knowledge'
    knowledge_files_dir = '/app/knowledge_files'
    
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
EOL

# Run the initialization script
echo "Initializing LanceDB database..."
python /app/init_lancedb.py

# Execute the command passed to docker
exec "$@"
