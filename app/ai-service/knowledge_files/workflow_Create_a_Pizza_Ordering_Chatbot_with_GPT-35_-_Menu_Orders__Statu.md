# Create a Pizza Ordering Chatbot with GPT-3.5 - Menu, Orders & Status Tracking

**[View Template](https://n8n.io/workflows/3049-/)**  **Published Date:** 03/01/2025  **Created By:** Irfan Handoko  **Categories:** `AI` `Langchain`  

## Template Description

Pizza Ordering Chatbot with OpenAI - Menu, Orders & Status Tracking

Introduction
This workflow template is designed to automate order processing for a pizza store using OpenAI and n8n. The chatbot acts as a virtual assistant to handle customer inquiries related to menu details, order placement, and order status tracking.

Features
The chatbot provides an interactive experience for customers by performing the following functions:

Menu Inquiry: When a customer asks about the menu, the chatbot responds with a list of available pizzas, prices, and additional options.
Order Placement: If a customer places an order, the chatbot confirms order details, provides a summary, informs the customer that the order is being processed, and expresses gratitude.
Order Status Tracking: If a customer asks about their order status, the chatbot retrieves details such as order date, pizza type, and quantity, providing real-time updates.

Prerequisites
Before setting up the workflow, ensure you have the following:

OpenAI account** (Sign up here)
OpenAI API key** to interact with GPT-3.5
n8n instance** running locally or on a server (Installation Guide)

Configuration Steps

Step 1: Set Up OpenAI API Credentials
Log in to OpenAI's website.
Navigate to API Keys under your account settings.
Click Create API Key and copy the key for later use.

Step 2: Configure OpenAI Node in n8n
Open n8n and create a new workflow.
Click Add Node and search for OpenAI.
Select OpenAI from the list.
In the OpenAI node settings, click "Create New" under the Credentials section.
Enter a name for the credentials (e.g., "PizzaBot OpenAI Key").
Paste your API Key into the field.
Click Save.

Step 3: Set Up the Chatbot Logic
Connect the AI Agent Builder Node to the OpenAI Node and HTTP Request Node.
Configure the OpenAI Node with the following settings:
   Model: gpt-3.5-turbo
   Prompt: Provide dynamic text based on customer inquiries (e.g., "List available pizzas," "Place an order for Margherita pizza," "Check my order status").
   Temperature: Adjust based on desired creativity (recommended: 0.7).
   Max Tokens: Limit response length (recommended: 150).
Add multiple HTTP Request Node:
   For Get Products: Fetch stored menu data and return details.
   For Order Product: Capture order details, generate an order ID, and confirm with the customer.
   For Get Order: Retrieve order details based on the order ID and display progress.

Step 4: Testing and Deployment
Click Execute Workflow to test the chatbot.
Open the Chat Message node, then copy the chat URL to access the chatbot in your browser.
Interact with the chatbot by asking different queries (e.g., "What pizzas do you have?" or "I want to order a Pepperoni pizza").
Verify responses and adjust prompts or configurations as needed.
Deploy the workflow and integrate it with a messaging platform (e.g., Telegram, WhatsApp, or a website chatbot).

Conclusion
This n8n workflow enables a fully functional pizza ordering chatbot using OpenAI's GPT-3.5. Customers can view menus, place orders, and track their order status efficiently. You can further customize the chatbot by refining prompts, adding new features, or integrating with external databases for order management.

🚀 Happy automating!

## Template JSON

```
{
  "id": "5Y8QXJ3N67wnmR2R",
  "meta": {
    "instanceId": "433fa4b57c582f828a127c9c601af0fc38d9d6424efd30a3ca802a4cc3acd656",
    "templateCredsSetupCompleted": true
  },
  "name": "POC - Chatbot Order by Sheet Data",
  "tags": [],
  "nodes": [
    {
      "id": "cc9ab139-303f-411a-a7c8-5985d92e3040",
      "name": "Calculator",
      "type": "@n8n/n8n-nodes-langchain.toolCalculator",
      "position": [
        1460,
        480
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "97a6d3a8-001c-4c62-84c2-da5b46a286a9",
      "name": "Chat OpenAI",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        740,
        480
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "XXXXXXXXXX",
          "name": "OpenAI Credentials"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "1ad05eb6-0f6a-4da7-9d86-871dfa7cbce1",
      "name": "Window Buffer Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        900,
        480
      ],
      "parameters": {},
      "typeVersion": 1.2
    },
    {
      "id": "f4883308-3e4a-49b1-82f5-c18dc2121c47",
      "name": "Get Products",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        1060,
        480
      ],
      "parameters": {
        "url": "https://n8n.io/webhook/get-products",
        "toolDescription": "Retrieve detailed information about the product menu."
      },
      "typeVersion": 1.1
    },
    {
      "id": "058b1cf5-b8c0-414d-b4c6-e4c016e4d181",
      "name": "Order Product",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        1200,
        480
      ],
      "parameters": {
        "url": "https://n8n.io/webhook/order-product",
        "method": "POST",
        "sendBody": true,
        "parametersBody": {
          "values": [
            {
              "name": "message",
              "value": "={{ $json.chatInput }}",
              "valueProvider": "fieldValue"
            }
          ]
        },
        "toolDescription": "Process product orders."
      },
      "typeVersion": 1.1
    },
    {
      "id": "6e0b433c-1d8f-4cf8-aa06-cc1b8d51e2d9",
      "name": "Get Order",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        1320,
        480
      ],
      "parameters": {
        "url": "https://n8n.io/webhook/get-orders",
        "toolDescription": "Get the order status."
      },
      "typeVersion": 1.1
    },
    {
      "id": "a0ee2e49-52cf-40d8-b108-4357bf562505",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        540,
        160
      ],
      "webhookId": "d925cc6e-6dd7-4459-a917-e68d57ab0e2a",
      "parameters": {
        "public": true,
        "options": {},
        "initialMessages": "Hellooo! \ud83d\udc4b My name is Pizzaro \ud83c\udf55. I'm here to help with your pizza order. How can I assist you?\n\n\ud83d\udce3 INFO: If you\u2019d like to order a pizza, please include your name + pizza type + quantity. Thank you!"
      },
      "typeVersion": 1.1
    },
    {
      "id": "81892405-e09c-4452-99b3-f5edbe49b830",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        780,
        160
      ],
      "parameters": {
        "text": "={{ $json.chatInput }}",
        "options": {
          "systemMessage": "=Your name is Pizzaro, and you are an assistant for handling customer pizza orders.\n\n1. If a customer asks about the menu, provide information on the available products.\n2. If a customer is placing an order, confirm the order details, inform them that the order is being processed, and thank them.\n3. If a customer inquires about their order status, provide the order date, pizza type, and quantity."
        },
        "promptType": "define"
      },
      "executeOnce": false,
      "typeVersion": 1.6
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "6431e20b-e135-43b2-bbcb-ed9c705d1237",
  "connections": {
    "Get Order": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Calculator": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Chat OpenAI": {
      "ai_languageModel": [
        [
          {
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Get Products": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Order Product": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Window Buffer Memory": {
      "ai_memory": [
        [
          {
            "node": "AI Agent",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "When chat message received": {
      "main": [
        [
          {
            "node": "AI Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
