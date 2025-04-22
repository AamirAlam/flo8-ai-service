# Fetch Keyword From Google Sheet and Classify Them Using AI

**[View Template](https://n8n.io/workflows/2945-/)**  **Published Date:** 02/19/2025  **Created By:** Polina Medvedieva  **Categories:** `Data & Storage` `Productivity` `AI` `Langchain`  

## Template Description

Who is this template for

This template is for marketers, SEO specialists, or content managers who need to analyze keywords to identify which ones contain references to a specific area or topic, in this case – IT software, services, tools, or apps.

Use case

Automating the process of scanning a large list of keywords to determine if they reference known IT products or services (like ServiceNow, Salesforce, etc.), and updating a Google Sheet with this classification. This helps in categorizing keywords for targeted SEO campaigns, content creation, or market analysis.

How this workflow works

Fetches keyword data from a Google Sheet
Processes keywords in batches to prevent rate limiting
Uses an AI agent (OpenAI) to analyze each keyword and determine if it contains a reference to an IT service/software
Updates the original Google Sheet with the results in a "Service?" column
Continues processing until all keywords are analyzed

Set up steps

Connect your Google Sheets account credentials
Set the Google Sheet document ID (currently using "Copy of Sheet1 1")
Configure the OpenAI API credentials for the AI agent
Adjust the batch size (currently 6) if needed based on your API rate limits
Ensure the Google Sheet has the required columns: "Number", "Keyword", and "Service?"



The AI agent's prompt is highly customizable to match different identification needs. For example, instead of looking for IT software/services, you could modify the prompt to identify:

Industry-specific terms (healthcare, finance, education)
Geographic references (cities, countries, regions)
Product categories (electronics, clothing, food)
Competitor brand mentions

Here's how you could modify the prompt for different use cases:

Copy
// For identifying educational content keywords
"Check the keyword I provided and define if this keyword relates to educational content, courses, or learning materials and return yes or no."

// For identifying local service keywords
"Check the keyword I provided and determine if it contains location-specific terms (city names, neighborhoods, regions) that suggest local service intent and return yes or no."

// For identifying competitor mentions
"Check the keyword I provided and determine if it mentions any of our competitors (CompetitorA, CompetitorB, CompetitorC) and return yes or no."
`

## Template JSON

```
{
  "meta": {
    "instanceId": "cb484ba7b742928a2048bf8829668bed5b5ad9787579adea888f05980292a4a7",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "53e93a66-468a-4df8-b2cb-58ff0563f83f",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -160,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "70692fd5-d575-49d2-9e3c-71bdddb0782e",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        1000,
        0
      ],
      "parameters": {
        "text": "=keyword: {{ $json.Keyword }}",
        "options": {
          "systemMessage": "=Check the keyword I provided and define if this keyword has a name of the known IT software, service, tool or app as a part of it (for example, ServiceNow or Salesforce) and return yes or no."
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.7
    },
    {
      "id": "587e6283-32c0-4599-a024-2ce0079bdaeb",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        1000,
        240
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "ju5aHhTljmCDxSl9",
          "name": "OpenAi account Polina's"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "0e3e7d09-202e-47cc-8704-16ab70bc4077",
      "name": "Structured Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        1180,
        240
      ],
      "parameters": {
        "jsonSchemaExample": "{\n\t\"Isservice\": \"yes\"\n}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "900ac097-c6de-41c0-8270-c9de60424d5f",
      "name": "Fetch Keywords from Sheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        120,
        0
      ],
      "parameters": {
        "options": {},
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": 1319606837,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1jzDvszQoVDV-jrAunCXqTVsiDxXVLMGqQ1zGXwfy5eU/edit#gid=1319606837",
          "cachedResultName": "Copy of Sheet1 1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1jzDvszQoVDV-jrAunCXqTVsiDxXVLMGqQ1zGXwfy5eU",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1jzDvszQoVDV-jrAunCXqTVsiDxXVLMGqQ1zGXwfy5eU/edit?usp=drivesdk",
          "cachedResultName": "AI + agents"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "DeaHa70CotH7MPX6",
          "name": "Google Sheets account NN DB test"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "73e208d1-e8d8-4c8b-90f3-06202ed73986",
      "name": "Process Keywords in Batches",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        440,
        0
      ],
      "parameters": {
        "options": {},
        "batchSize": 6
      },
      "typeVersion": 3
    },
    {
      "id": "93646bfc-b79d-4ec3-ba8d-8922773fd36b",
      "name": "Prevent API Rate Limiting",
      "type": "n8n-nodes-base.wait",
      "position": [
        720,
        0
      ],
      "webhookId": "035cfc06-099c-453b-aadc-0cce420b8171",
      "parameters": {},
      "typeVersion": 1.1
    },
    {
      "id": "313474f7-a53d-479c-a33e-9327ca29e570",
      "name": "Update Sheet with Analysis Results",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1360,
        0
      ],
      "parameters": {
        "columns": {
          "value": {
            "Number": "={{ $('Process Keywords in Batches').item.json.Number }}",
            "Service?": "={{ $json.output.Isservice }}"
          },
          "schema": [
            {
              "id": "Number",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Number",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Service?",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Service?",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Keyword",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Keyword",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Country",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Country",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Difficulty",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Difficulty",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Volume",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Volume",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CPC",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "CPC",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CPS",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "CPS",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Parent Keyword",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Parent Keyword",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Last Update",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Last Update",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "SERP Features",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "SERP Features",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Global volume",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Global volume",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Traffic potential",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Traffic potential",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Global traffic potential",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Global traffic potential",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "First seen",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "First seen",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Intents",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Intents",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "row_number",
              "type": "string",
              "display": true,
              "removed": true,
              "readOnly": true,
              "required": false,
              "displayName": "row_number",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "Number"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "update",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": 1319606837,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1jzDvszQoVDV-jrAunCXqTVsiDxXVLMGqQ1zGXwfy5eU/edit#gid=1319606837",
          "cachedResultName": "Copy of Sheet1 1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1jzDvszQoVDV-jrAunCXqTVsiDxXVLMGqQ1zGXwfy5eU",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1jzDvszQoVDV-jrAunCXqTVsiDxXVLMGqQ1zGXwfy5eU/edit?usp=drivesdk",
          "cachedResultName": "AI + agents"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "DeaHa70CotH7MPX6",
          "name": "Google Sheets account NN DB test"
        }
      },
      "typeVersion": 4.5
    }
  ],
  "pinData": {},
  "connections": {
    "AI Agent": {
      "main": [
        [
          {
            "node": "Update Sheet with Analysis Results",
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
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Structured Output Parser": {
      "ai_outputParser": [
        [
          {
            "node": "AI Agent",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Fetch Keywords from Sheet": {
      "main": [
        [
          {
            "node": "Process Keywords in Batches",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Prevent API Rate Limiting": {
      "main": [
        [
          {
            "node": "AI Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Process Keywords in Batches": {
      "main": [
        [],
        [
          {
            "node": "Prevent API Rate Limiting",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When clicking \u2018Test workflow\u2019": {
      "main": [
        [
          {
            "node": "Fetch Keywords from Sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Update Sheet with Analysis Results": {
      "main": [
        [
          {
            "node": "Process Keywords in Batches",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
