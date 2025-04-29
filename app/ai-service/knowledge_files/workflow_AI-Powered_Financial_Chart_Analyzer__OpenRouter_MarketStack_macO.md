# AI-Powered Financial Chart Analyzer | OpenRouter, MarketStack, macOS Shortcuts

**[View Template](https://n8n.io/workflows/2970-/)**  **Published Date:** 02/22/2025  **Created By:** Udit Rawat  **Categories:** `AI` `Langchain`  

## Template Description

The AI-Powered Financial Chart Analyzer is a cutting-edge automation tool that streamlines financial analysis using n8n workflows, AI agents, and MacOS Shortcuts. It enables users to capture, process, and analyze candlestick charts for both stocks and cryptocurrencies. By integrating powerful tools like ChatGPT-4o-mini (via OpenRouter), MarketStack, and SerpAPI, this automation provides real-time market insights, technical analysis, and AI-driven stock trend predictions.

Workflow

The Webhook node will receive image data from a macOS shortcut in Base64 format.  
The Convert to File node will convert the Base64 image into a binary file.  
The AI Agent node will process the binary image. It utilizes OpenRouter, Windows buffer memory, MarketStack, and the SerpAPI tool.  
Remember to use a model capable of processing images; otherwise, the workflow will throw an error.  
We use the MarketStack tool to fetch the latest stock data; however, it is rarely used.  
SerpAPI is used for market research, such as news and insights about stocks.  
Finally, the Markdown node converts Markdown to HTML.  
The response is then sent to the Webhook.

Use Case

Traders & Investors: Quickly analyze candlestick charts and identify trading opportunities.

Financial Analysts: Automate chart interpretation and data aggregation for in-depth reports.

AI & Automation Enthusiasts: Experiment with AI-driven financial workflows using n8n.

Business Owners: Gain real-time stock insights to make informed investment decisions.

Setup Instructions

Install MacOS Shortcut

Download the MacOS Shortcut provided with this product and double-click on it to install.
If you don’t have the Shortcuts app (parent app) installed, first download it from the App Store, then follow Step 1.

Set Up Workflow

Import the n8n workflow provided with this product.

Set Up Credentials

🔹Webhook Authentication

Create an API key (you can use a key generation tool or simply use a custom string).
Add the API key to your n8n Webhook and MacOS Shortcut.
If you prefer not to use authentication, remove it from both the n8n Webhook and the MacOS Shortcut.

🔹OpenRouter API Setup

Get a free API key from OpenRouter and add it to your workflow.
Free API keys have usage limits.
OpenRouter provides multiple models—ensure that the selected model supports image processing.

🔹MarketStack API Setup

Get a free API key from MarketStack and use it in your workflow.
Free API keys have usage limits.

🔹SerpAPI Setup
Get a free API key from SerpAPI and use it in your workflow.
Free API keys have usage limits.

Disclaimer

This tool is designed for educational and informational purposes only. The AI-generated insights should not be considered as financial advice. Users should conduct their own research before making investment decisions. AgentsOps is not responsible for any financial losses incurred from using this automation.


## Template JSON

```
{
  "id": "NFXqNvAllRP8bkeF",
  "meta": {
    "instanceId": "d16fb7d4b3eb9b9d4ad2ee6a7fbae593d73e9715e51f583c2a0e9acd1781c08e",
    "templateCredsSetupCompleted": true
  },
  "name": "Sell: Process Candlestick Chart Using OpenRouter-ChatGPT, MarketStack, SerpAPI",
  "tags": [
    {
      "id": "XZIQK6NdzGvgbZFd",
      "name": "Sell",
      "createdAt": "2025-01-15T12:28:48.424Z",
      "updatedAt": "2025-01-15T12:28:48.424Z"
    }
  ],
  "nodes": [
    {
      "id": "e75844d9-3056-4bea-9e2d-3ed2a9b4a31a",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        -200,
        0
      ],
      "webhookId": "bc6e3d41-982b-4805-a797-9491e4841823",
      "parameters": {},
      "typeVersion": 2
    },
    {
      "id": "0c322986-784b-459c-a409-b73f5c6257e6",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1100,
        0
      ],
      "parameters": {},
      "typeVersion": 1.1
    },
    {
      "id": "3823c07d-f8a8-42a5-a41c-329b5f236559",
      "name": "Fields_Data",
      "type": "n8n-nodes-base.set",
      "position": [
        60,
        0
      ],
      "parameters": {},
      "typeVersion": 3.4
    },
    {
      "id": "715bec0a-1785-4edf-bc29-e3fe1d6e0d80",
      "name": "Base64_To_Binary_Image",
      "type": "n8n-nodes-base.convertToFile",
      "position": [
        300,
        0
      ],
      "parameters": {},
      "typeVersion": 1.1
    },
    {
      "id": "ba20d547-e30a-46ee-887d-05542f5da0c9",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        520,
        0
      ],
      "parameters": {},
      "typeVersion": 1.7
    },
    {
      "id": "e9cf2f4c-3409-4716-abf5-a7cf9486104a",
      "name": "OpenRouter Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
      "position": [
        180,
        220
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "d4659fd2-5300-4d42-8577-8b8692e66167",
      "name": "Window Buffer Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        340,
        220
      ],
      "parameters": {},
      "typeVersion": 1.3
    },
    {
      "id": "2d5487cd-b7d6-4873-b707-b85425d30325",
      "name": "Calculator",
      "type": "@n8n/n8n-nodes-langchain.toolCalculator",
      "position": [
        540,
        220
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "0ab65c38-48b4-4a40-9a0b-cbf9a1305fb9",
      "name": "Marketstack",
      "type": "n8n-nodes-base.marketstackTool",
      "position": [
        660,
        220
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "1dbd28df-3b0a-4c01-9ec3-b8fa8a0f940a",
      "name": "SerpAPI",
      "type": "@n8n/n8n-nodes-langchain.toolSerpApi",
      "position": [
        780,
        220
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "d07a89c8-0411-444e-aa71-15ddbc27f4e1",
      "name": "Markdown",
      "type": "n8n-nodes-base.markdown",
      "position": [
        880,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "a2f2688b-d654-452f-b7d8-f0a48a1e2a4c",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -820,
        -320
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "f03269cc-f4d8-433a-a746-be13a2788dde",
  "connections": {
    "SerpAPI": {
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
    "Webhook": {
      "main": [
        [
          {
            "node": "Fields_Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Agent": {
      "main": [
        [
          {
            "node": "Markdown",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Markdown": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
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
    "Fields_Data": {
      "main": [
        [
          {
            "node": "Base64_To_Binary_Image",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Marketstack": {
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
    "OpenRouter Chat Model": {
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
    "Base64_To_Binary_Image": {
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
