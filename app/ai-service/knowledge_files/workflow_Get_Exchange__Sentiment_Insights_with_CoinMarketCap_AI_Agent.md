# Get Exchange & Sentiment Insights with CoinMarketCap AI Agent

**[View Template](https://n8n.io/workflows/3423-/)**  **Published Date:** 04/03/2025  **Created By:** Don Jayamaha Jr  **Categories:** `AI` `Langchain`  

## Template Description

Analyze exchange data, market indexes, and community sentiment from CoinMarketCap—powered by AI.  

This sub-agent provides access to exchange listings, token holdings, metadata, and high-level metrics like the CMC 100 Index and the Fear & Greed Index. It’s designed for use within your larger CoinMarketCap AI Analyst system or as a standalone workflow.

This agent can be triggered by a supervisor or manually used with message and sessionId inputs.

Supported Tools (5 Total)

🔍 Exchange Map  
Get CoinMarketCap IDs, names, and slugs for exchanges (used as lookup before deeper queries).  

🧾 Exchange Info  
Metadata including launch date, social links, country, and operational status.  

💰 Exchange Assets  
Token balances, wallet addresses, and total USD value held by a specific exchange.

📈 CoinMarketCap 100 Index  
Constituents and weights of the CMC 100 Index, updated live.

😱 Fear & Greed Index  
Market sentiment score updated daily, ranging from Extreme Fear to Extreme Greed.

What You Can Do with This Agent  
🔹 Map exchanges to retrieve their ID and slug  
🔹 Analyze exchange holdings by token and blockchain  
🔹 Pull metadata for major CEXs like Binance or Coinbase  
🔹 Compare global sentiment using the Fear & Greed Index  
🔹 Access index data to understand CMC’s top 100 crypto asset breakdown

Example Queries You Can Use  
✅ "What is the latest Fear and Greed Index reading?"  
✅ "Get a list of all exchanges on CoinMarketCap."  
✅ "What tokens are held by Binance?"  
✅ "Retrieve metadata for Coinbase."  
✅ "Show me the top assets in the CMC 100 Index."  

Agent Architecture  
AI Brain**: GPT-4o-mini  
Memory**: Window buffer memory using sessionId  
Tools**: 5 API-connected nodes  
Trigger**: External input via message and sessionId  

Setup Instructions  
Get a CoinMarketCap API Key  
   Apply here: https://coinmarketcap.com/api/  
Configure n8n Credentials  
   Use HTTP Header Auth to store your CoinMarketCap API key.  
Optional: Trigger from a Supervisor  
   Connect to a parent agent using Execute Workflow with message and sessionId inputs.  
Test Sample Prompts  
   “Get all exchanges”, “Fetch CMC index”, “Show Binance token holdings”

Sticky Notes Included  

Exchange & Community Guide – Explains agent purpose and component connections  

Usage & Examples – Walkthrough for sample use cases  

Error Handling & Licensing – Includes API error code reference and licensing details

✅ Final Notes  
This agent is part of a broader CoinMarketCap AI Analyst System. Visit my Creator profile to download all available sub-agents and supervisor flows.

Understand exchange behavior and community sentiment—automated with AI and CoinMarketCap.

## Template JSON

```
{
  "id": "kbJb4VMD3SZlcS2u",
  "meta": {
    "instanceId": "a5283507e1917a33cc3ae615b2e7d5ad2c1e50955e6f831272ddd5ab816f3fb6",
    "templateCredsSetupCompleted": true
  },
  "name": "CoinMarketCap_Exchange_and_Community_Agent_Tool",
  "tags": [],
  "nodes": [
    {
      "id": "c055762a-8fe7-4141-a639-df2372f30060",
      "name": "When Executed by Another Workflow",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        -160,
        340
      ],
      "parameters": {
        "workflowInputs": {
          "values": [
            {
              "name": "sessionId"
            },
            {
              "name": "message"
            }
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "3609967c-f7c4-4be5-8cf5-1213dcf8cd39",
      "name": "CoinMarketCap Exchange and Community Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        300,
        340
      ],
      "parameters": {
        "text": "={{ $json.message }}",
        "options": {
          "systemMessage": "You are a **digital asset intelligence agent** designed to provide deep insights into the cryptocurrency ecosystem by querying CoinMarketCap's API. You support data retrieval across exchanges, community sentiment, and index tracking.\n\n---\n\n### \ud83d\udee0\ufe0f Available Tools & Capabilities\n\n#### 1. \ud83d\udd0d **Exchange Map**\n- **Purpose:** Retrieve a list of all registered cryptocurrency exchanges.\n- **Endpoint:** `https://pro-api.coinmarketcap.com/v1/exchange/map`\n- **Query Parameters:** \n  - `slug` (recommended starting point)\n  - `listing_status`, `start`, `limit`, `crypto_id`\n- **Returns:** Exchange ID, name, slug \u2014 essential for identifying exchanges.\n- **Usage:** Use first to acquire the `id` needed by other tools.\n\n---\n\n#### 2. \ud83e\uddfe **Exchange Info**\n- **Purpose:** Obtain metadata for a specific exchange.\n- **Endpoint:** `https://pro-api.coinmarketcap.com/v1/exchange/info`\n- **Required Parameter:** `id` (from Exchange Map)\n- **Returns:** Description, launch year, country, website/Twitter links, and status.\n\n---\n\n#### 3. \ud83d\udcb0 **Exchange Assets**\n- **Purpose:** View on-chain token holdings of an exchange.\n- **Endpoint:** `https://pro-api.coinmarketcap.com/v1/exchange/assets`\n- **Required Parameter:** `id` (from Exchange Map)\n- **Returns:** Token balances, wallet addresses, blockchain platform, and USD value.\n\n---\n\n#### 4. \ud83d\udcc8 **CMC 100 Index**\n- **Purpose:** Get the latest CoinMarketCap 100 Index data.\n- **Endpoint:** `https://pro-api.coinmarketcap.com/v3/index/cmc100-latest`\n- **Returns:** Constituents of the index and their weights.\n\n---\n\n#### 5. \ud83d\ude31 **Fear and Greed Index (Latest)**\n- **Purpose:** Access current crypto market sentiment.\n- **Endpoint:** `https://pro-api.coinmarketcap.com/v3/fear-and-greed/latest`\n- **Returns:** Sentiment index score and classification (e.g., Fear, Greed).\n\n---\n\n### \u26a0\ufe0f Error Trap: API Response Overload\nIf the API response returns **too much data** and exceeds the GPT model's token limit:\n- Notify the user with the message:  \n  **\"\u26a0\ufe0f The requested data exceeds the processing capacity of this model. Please refine your query by limiting results or filtering data.\"**\n- Suggest parameters like `limit`, `start`, or using a specific `id` or `slug` to reduce data size.\n\n---\n\nKeep responses structured, insightful, and performant. Always validate if required parameters are available before invoking a tool. Prioritize `Exchange Map` for ID resolution before calling `Exchange Info` or `Exchange Assets`.\n\n"
        },
        "promptType": "define"
      },
      "typeVersion": 1.8
    },
    {
      "id": "811480ce-f2c9-4400-b585-1a3609b5bef0",
      "name": "Exchange and Community Agent Brain",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        -320,
        620
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini",
          "cachedResultName": "gpt-4o-mini"
        },
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "yUizd8t0sD5wMYVG",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "007b07fd-2abe-4bdd-80ef-8883e0cbfcec",
      "name": "Exchange and Community Agent Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        -140,
        620
      ],
      "parameters": {},
      "typeVersion": 1.3
    },
    {
      "id": "669566d0-3dc5-413e-a8b5-80cf4aeaa54d",
      "name": "Exchange Map",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        60,
        620
      ],
      "parameters": {
        "url": "https://pro-api.coinmarketcap.com/v1/exchange/map",
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "parametersQuery": {
          "values": [
            {
              "name": "slug"
            }
          ]
        },
        "toolDescription": "Get a map of all crypto exchanges with CoinMarketCap ID, name, and slug.\n\n1st query with only the slug only, if error then try others.",
        "parametersHeaders": {
          "values": [
            {
              "name": "Accept"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "OKXROn8aWkgAOvvV",
          "name": "CoinMarketCap Standard"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "03b3e44f-a740-414c-a011-de4d571b7968",
      "name": "Exchange Info",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        280,
        620
      ],
      "parameters": {
        "url": "https://pro-api.coinmarketcap.com/v1/exchange/info",
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "parametersQuery": {
          "values": [
            {
              "name": "id"
            }
          ]
        },
        "toolDescription": "Get metadata for a crypto exchange including description, launch date, country, and links.",
        "parametersHeaders": {
          "values": [
            {
              "name": "Accept"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "OKXROn8aWkgAOvvV",
          "name": "CoinMarketCap Standard"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "65c2b8ab-7d6d-415e-a436-0a9c14af2457",
      "name": "CMC 100 Index",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        740,
        620
      ],
      "parameters": {
        "url": "https://pro-api.coinmarketcap.com/v3/index/cmc100-latest",
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "toolDescription": "Returns the latest CoinMarketCap 100 Index value, including constituents and their weights.",
        "parametersHeaders": {
          "values": [
            {
              "name": "Accept"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "OKXROn8aWkgAOvvV",
          "name": "CoinMarketCap Standard"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "51a94f35-4405-4e53-9fa5-91911759802d",
      "name": "Fear and Greed Latest",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        980,
        620
      ],
      "parameters": {
        "url": "https://pro-api.coinmarketcap.com/v3/fear-and-greed/latest",
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "toolDescription": "Returns the latest value from the CMC Crypto Fear and Greed Index.",
        "parametersHeaders": {
          "values": [
            {
              "name": "Accept"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "OKXROn8aWkgAOvvV",
          "name": "CoinMarketCap Standard"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "26240549-9b41-4b6a-bf24-d61c8ee155ca",
      "name": "Exchange Assets",
      "type": "@n8n/n8n-nodes-langchain.toolHttpRequest",
      "position": [
        520,
        620
      ],
      "parameters": {
        "url": "https://pro-api.coinmarketcap.com/v1/exchange/assets",
        "sendQuery": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "parametersQuery": {
          "values": [
            {
              "name": "id"
            }
          ]
        },
        "toolDescription": "Returns token holdings of a specific exchange including wallet addresses, platform, balance, and USD value.",
        "parametersHeaders": {
          "values": [
            {
              "name": "Accept"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "OKXROn8aWkgAOvvV",
          "name": "CoinMarketCap Standard"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "22b5608c-467e-41ff-81d9-559d110b872d",
      "name": "Exchange & Community Guide",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1520,
        -680
      ],
      "parameters": {
        "width": 1200,
        "height": 720,
        "content": "# \ud83e\udde0 CoinMarketCap_Exchange_and_Community_Agent_Tool Guide\n\nThis agent handles **exchange-level** data, **community sentiment**, and **index insights** using CoinMarketCap API endpoints.\n\n## \ud83d\udd0c Supported Tools\n1. `/v1/exchange/map` \u2013 Get exchange ID, name, and slug\n2. `/v1/exchange/info` \u2013 Metadata: launch date, social, location\n3. `/v1/exchange/assets` \u2013 Token holdings of exchange\n4. `/v3/index/cmc100-latest` \u2013 CoinMarketCap 100 Index info\n5. `/v3/fear-and-greed/latest` \u2013 Sentiment index (0\u2013100)\n\n## \ud83e\udde0 Agent Components:\n- **\ud83e\udde0 Brain**: GPT-4o Mini\n- **\ud83d\udcbe Memory**: Conversation state handler\n- **\u2699\ufe0f Tools**: 5 direct API endpoints\n\n## \ud83e\udde9 Trigger Parameters:\n- `message` \u2013 Main query prompt\n- `sessionId` \u2013 Contextual memory key\n\n## \ud83d\udd11 Notes:\n- Use `Exchange Map` to get valid `id` before calling `Exchange Info` or `Assets`\n- Fear & Greed index returns daily updated data points\n- Index tools return structured component weights"
      },
      "typeVersion": 1
    },
    {
      "id": "dd38cd37-bff7-4200-94e4-a7f2a0f3b979",
      "name": "Usage & Examples",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -80,
        -680
      ],
      "parameters": {
        "color": 5,
        "width": 840,
        "height": 920,
        "content": "## \ud83d\udccc Usage Instructions\n\n### \u2705 Step 1: Provide Inputs\nUse `slug` for exchanges or `id` for metadata/assets. \n\n### \u2705 Step 2: Trigger from Supervisor Agent\nThe main workflow will send `message` and `sessionId`.\n\n### \u2705 Step 3: Results Output\nReturns JSON with insights on exchanges or index data.\n\n---\n\n## \ud83d\udd0d Example Prompts\n\n### 1\ufe0f\u20e3 Show latest Fear & Greed score\n```plaintext\nGET /v3/fear-and-greed/latest\n```\n\n### 2\ufe0f\u20e3 Get Binance exchange token holdings\n```plaintext\n1. GET /v1/exchange/map?slug=binance\n2. Use ID to query /v1/exchange/assets?id=...\n```\n\n### 3\ufe0f\u20e3 What coins make up the CMC 100 Index?\n```plaintext\nGET /v3/index/cmc100-latest\n```\n\n### 4\ufe0f\u20e3 Show info on Coinbase\n```plaintext\n1. /v1/exchange/map?slug=coinbase\n2. /v1/exchange/info?id=...\n```"
      },
      "typeVersion": 1
    },
    {
      "id": "ce0e7093-9fe0-4b9c-8cf5-50cdfef45d94",
      "name": "Errors & Licensing",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1020,
        -680
      ],
      "parameters": {
        "color": 3,
        "width": 640,
        "height": 500,
        "content": "## \u26a0\ufe0f Error Handling Tips\n\n| Error Code | Meaning |\n|------------|---------|\n| `400` | Bad Request \u2013 missing/invalid param |\n| `401` | Unauthorized \u2013 check API key |\n| `429` | Rate Limit Exceeded |\n| `500` | CoinMarketCap server error |\n\n### \u26a0\ufe0f Large Response Warning\nIf result data exceeds memory limits:\n- Prompt: _\u201c\u26a0\ufe0f Data too large, refine query with limit or filters.\u201d_\n\n---\n\n**Need Help?**  \n\ud83c\udf10 Connect on LinkedIn:  \n\ud83d\udd17 [http://linkedin.com/in/donjayamahajr](http://linkedin.com/in/donjayamahajr)\n\n\u00a9 2025 Treasurium Capital Limited Company. All rights reserved.\nThis AI workflow architecture, including logic, design, and prompt structures, is the intellectual property of Treasurium Capital Limited Company. Unauthorized reproduction, redistribution, or resale is prohibited under U.S. copyright law. Licensed use only."
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "faf44acc-2d07-4185-877c-b57f9c8c88bb",
  "connections": {
    "Exchange Map": {
      "ai_tool": [
        [
          {
            "node": "CoinMarketCap Exchange and Community Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "CMC 100 Index": {
      "ai_tool": [
        [
          {
            "node": "CoinMarketCap Exchange and Community Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Exchange Info": {
      "ai_tool": [
        [
          {
            "node": "CoinMarketCap Exchange and Community Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Exchange Assets": {
      "ai_tool": [
        [
          {
            "node": "CoinMarketCap Exchange and Community Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Fear and Greed Latest": {
      "ai_tool": [
        [
          {
            "node": "CoinMarketCap Exchange and Community Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "When Executed by Another Workflow": {
      "main": [
        [
          {
            "node": "CoinMarketCap Exchange and Community Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Exchange and Community Agent Brain": {
      "ai_languageModel": [
        [
          {
            "node": "CoinMarketCap Exchange and Community Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Exchange and Community Agent Memory": {
      "ai_memory": [
        [
          {
            "node": "CoinMarketCap Exchange and Community Agent",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
