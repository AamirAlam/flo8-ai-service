#  AI Data Analyst Agent and Visualization Agent for Large Spreadsheets 

**[View Template](https://n8n.io/workflows/2653-/)**  **Published Date:** 12/18/2024  **Created By:** Derek Cheung  **Categories:** `Development` `Core Nodes` `AI` `Langchain`  

## Template Description

Purpose of workflow:

This workflow transforms spreadsheet data into an interactive, AI-powered knowledge base that enables users to gain deep insights through natural language queries, searchability, and comparative analysis.

How it works:

Data Storage & Integration:
Spreadsheet data is imported into a no-code database (NocoDB)
System connects with an AI data analyst agent
Agent accesses table metadata and column information

Query Processing:
Users input natural language questions
AI agent interprets queries and converts them to database filters
System retrieves relevant data using filter formulas
AI synthesizes responses with analysis and insights

Advanced Capabilities:
Performs comparative analysis across multiple data points
Handles complex multi-part queries

Automatically creates visualizations:
Visualization AI Agent figures out the data and the chart type and generates professional visualization using Quickchart


Step by step setup:
Create account on nocodb.com
Create table by importing csv, copy table id
Create API token https://app.nocodb.com/#/account/tokens
In workflow, settings node, update with table id
In NocoDB tool node, setup authentication with API token created in step 3
Specify the workspace and base fields after connecting to NocoDB 

## Template JSON

```
{
  "id": "c9NyXuogJk6PT8Nb",
  "meta": {
    "instanceId": "2723a3a635131edfcb16103f3d4dbaadf3658e386b4762989cbf49528dccbdbd",
    "templateId": "2085"
  },
  "name": "Data Analyst Agent v3",
  "tags": [],
  "nodes": [
    {
      "id": "e0abec7d-6753-42ed-8339-e1ad612797ac",
      "name": "Chat Trigger",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        40,
        360
      ],
      "webhookId": "cd05f517-9aec-4e7d-bba8-3747bc8f5ddb",
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "9502381d-518a-4eff-a439-c9efdff782b6",
      "name": "Window Buffer Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        1000,
        600
      ],
      "parameters": {},
      "typeVersion": 1.3
    },
    {
      "id": "08621d63-9067-4a92-b6c8-ba129c6adfa0",
      "name": "Extract_Columns",
      "type": "n8n-nodes-base.set",
      "position": [
        640,
        360
      ],
      "parameters": {},
      "typeVersion": 3.4
    },
    {
      "id": "2ee6401a-a45c-4c81-83b5-3995a9a25118",
      "name": "NocoDB",
      "type": "n8n-nodes-base.nocoDbTool",
      "position": [
        1200,
        600
      ],
      "parameters": {},
      "typeVersion": 3
    },
    {
      "id": "8e8ce2e3-890a-46cd-a95e-0c355dde8c06",
      "name": "Settings",
      "type": "n8n-nodes-base.set",
      "position": [
        240,
        360
      ],
      "parameters": {},
      "typeVersion": 3.4
    },
    {
      "id": "3a986007-32dd-4152-93ca-d8a435603708",
      "name": "nocodb_extract_table",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        440,
        360
      ],
      "parameters": {},
      "typeVersion": 4.2
    },
    {
      "id": "2c594b59-95db-4fd9-bea3-06a861de9766",
      "name": "Data Analyst Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        900,
        360
      ],
      "parameters": {},
      "typeVersion": 1.7
    },
    {
      "id": "6b786282-8782-430b-852a-c60b94e05493",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        200,
        280
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "77cd95ff-dece-4770-9d38-a9cacc174368",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        840,
        600
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "f9d28f2e-aea8-4b7f-910b-655fac062fb3",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -680,
        200
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "1bff47ac-5326-468e-ba56-98d9416997da",
  "connections": {
    "NocoDB": {
      "ai_tool": [
        [
          {
            "node": "Data Analyst Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Settings": {
      "main": [
        [
          {
            "node": "nocodb_extract_table",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Chat Trigger": {
      "main": [
        [
          {
            "node": "Settings",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract_Columns": {
      "main": [
        [
          {
            "node": "Data Analyst Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Data Analyst Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Window Buffer Memory": {
      "ai_memory": [
        [
          {
            "node": "Data Analyst Agent",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "nocodb_extract_table": {
      "main": [
        [
          {
            "node": "Extract_Columns",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
