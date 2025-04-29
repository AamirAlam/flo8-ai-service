# UTM Link Creator & QR Code Generator with Scheduled Google Analytics Reports

**[View Template](https://n8n.io/workflows/2921-/)**  **Published Date:** 02/17/2025  **Created By:** Marketing Canopy  **Categories:** `Data & Storage` `Development` `Core Nodes` `Communication` `HITL` `AI` `Langchain`  

## Template Description

UTM Link Creator & QR Code Generator with Scheduled Google Analytics Reports

This workflow enables marketers to generate UTM-tagged links, convert them into QR codes, and automate performance tracking in Google Analytics with scheduled reports every 7 days. This solution helps monitor traffic sources from different marketing channels and optimize campaign performance based on analytics data.

Prerequisites

Before implementing this workflow, ensure you have the following:

Google Analytics 4 (GA4) Account & Access

Ensure you have a GA4 property set up.
Access to the GA4 Data API to schedule performance tracking. Refer to the Google Analytics Data API Overview for more information.

Airtable Account & API Key

Create an Airtable base to store UTM links, QR codes, and analytics data.
Obtain an Airtable API key from your Account Settings. Detailed instructions are available in the Airtable API Authentication Guide.

Step-by-Step Guide to Setting Up the Workflow

1. Generate UTM Links

Create a form or interface to input:

Base URL** (e.g., https://example.com)
Campaign Name** (utm_campaign)
Source** (utm_source)
Medium** (utm_medium)
Term** (Optional: utm_term)
Content** (Optional: utm_content)

Append UTM parameters to generate a trackable URL.

2. Store UTM Links & QR Codes in Airtable

Set up an Airtable base with the following columns:

UTM Link**
QR Code**
Campaign Name**
Source**
Medium**
Date Created**

Adjust as needed based on your tracking requirements. For guidance on setting up your Airtable base and using the API, refer to the Airtable Web API Documentation.

3. Convert UTM Links to QR Codes

Use a QR code generator API (e.g., goqr.me, qrserver.com) to generate QR codes for each UTM link and store them in Airtable.

4. Schedule Google Analytics Performance Reports (Every 7 Days)

Use the Google Analytics Data API to pull weekly performance reports based on UTM parameters.
Extract key metrics such as:
  Sessions
  Users
  Bounce Rate
  Conversions
  Revenue (if applicable)
Store the data in Airtable for tracking and analysis.

Adjust timeframe as needed


For more details on accessing and using the Google Analytics Data API, consult the Google Analytics Data API Overview.

Benefits of This Workflow

✅ Track Marketing Campaigns: Easily monitor which channels drive traffic.

✅ Automate QR Code Creation: Seamless integration of UTM links with QR codes.

✅ Scheduled Google Analytics Reports: No manual reporting—everything runs automatically.

✅ Improve Data-Driven Decisions: Optimize ad spend and marketing strategies based on performance insights.

This version ensures proper Markdown structure, includes relevant documentation links, and improves readability. Let me know if you need any further refinements! 🚀


## Template JSON

```
{
  "id": "SJrqDqTBIAyaZQkq",
  "meta": {
    "instanceId": "73d9d5380db181d01f4e26492c771d4cb5c4d6d109f18e2621cf49cac4c50763",
    "templateCredsSetupCompleted": true
  },
  "name": "UTM Link Creator & QR Code Generator with Scheduled Google Analytics Reports",
  "tags": [],
  "nodes": [
    {
      "id": "5efbd956-51b6-4f94-aebc-07e3e691f7eb",
      "name": "OpenAI Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        -180,
        480
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
          "id": "95QGJD3XSz0piaNU",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "a1acd323-ed07-41b4-a51e-614afe361893",
      "name": "Window Buffer Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        0,
        480
      ],
      "parameters": {
        "sessionKey": "={{ $json.timestamp }}",
        "sessionIdType": "customKey",
        "contextWindowLength": 200
      },
      "typeVersion": 1.3
    },
    {
      "id": "c3c2b5fa-c294-4306-a050-dccd592477fa",
      "name": "Google Analytics",
      "type": "n8n-nodes-base.googleAnalyticsTool",
      "position": [
        160,
        480
      ],
      "parameters": {
        "metricsGA4": {
          "metricValues": [
            {
              "listName": "sessions"
            }
          ]
        },
        "propertyId": {
          "__rl": true,
          "mode": "list",
          "value": "404306108",
          "cachedResultUrl": "https://analytics.google.com/analytics/web/#/p404306108/",
          "cachedResultName": "East Coast Concrete Coating"
        },
        "dimensionsGA4": {
          "dimensionValues": [
            {},
            {
              "listName": "sourceMedium"
            }
          ]
        },
        "additionalFields": {}
      },
      "credentials": {
        "googleAnalyticsOAuth2": {
          "id": "sVZ61SpNfC2D1Z7V",
          "name": "Google Analytics account"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "cbc7b539-2fa6-493b-a66c-13db8d8d420c",
      "name": "Create UTM Link & Send To Database",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -440,
        -80
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "5358f2cc-bdb0-4e9b-a6b9-93418f83db02",
      "name": "Set UTM Parameters For Link",
      "type": "n8n-nodes-base.set",
      "position": [
        -220,
        -80
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "28d0a36d-5b03-4b74-9941-ef0e1aab86bf",
              "name": "website_url",
              "type": "string",
              "value": "https://ecconcretecoating.com/"
            },
            {
              "id": "1a2ee174-4684-4246-813f-b67285af48b8",
              "name": "campaign_id",
              "type": "string",
              "value": "12246"
            },
            {
              "id": "e15a846d-6e37-4fbf-a9f4-b3fce3441295",
              "name": "campaign_source",
              "type": "string",
              "value": "google"
            },
            {
              "id": "f15e2bb1-08a6-48c4-8458-b753864e9364",
              "name": "campaign_medium",
              "type": "string",
              "value": "display"
            },
            {
              "id": "548900ab-aa2c-498f-bbd9-a787306e72db",
              "name": "campaign_name",
              "type": "string",
              "value": "summerfun"
            },
            {
              "id": "fd8d1bd4-a75d-4c49-b795-8fda7c377b66",
              "name": "campaign_term",
              "type": "string",
              "value": "conretecoating"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "45daf73a-01c2-40ab-8546-7fdd489e2a1c",
      "name": "Create UTM Link With Parameters",
      "type": "n8n-nodes-base.code",
      "position": [
        40,
        -140
      ],
      "parameters": {
        "jsCode": "const items = $input.all();\nconst updatedItems = items.map((item) => {\n  const utmUrl = `${item?.json?.website_url}?utm_source=${item?.json?.campaign_source}&utm_medium=${item?.json?.campaign_medium}&utm_campaign=${item?.json?.campaign_name}&utm_term=${item?.json?.campaign_term}&utm_content=${item?.json?.campaign_id}`;\n  item.json.utmUrl = utmUrl;\n  return item;\n});\nreturn updatedItems;\n"
      },
      "typeVersion": 2
    },
    {
      "id": "a621984d-eea5-464d-9be3-e620e779abd5",
      "name": "Submit UTM Link To Database",
      "type": "n8n-nodes-base.airtable",
      "position": [
        280,
        -200
      ],
      "parameters": {
        "base": {
          "__rl": true,
          "mode": "list",
          "value": "appIXd8a8JeB9bPaL",
          "cachedResultUrl": "https://airtable.com/appIXd8a8JeB9bPaL",
          "cachedResultName": "Untitled Base"
        },
        "table": {
          "__rl": true,
          "mode": "list",
          "value": "tblXyFxXMHraieGCa",
          "cachedResultUrl": "https://airtable.com/appIXd8a8JeB9bPaL/tblXyFxXMHraieGCa",
          "cachedResultName": "UTM_URL"
        },
        "columns": {
          "value": {
            "URL": "={{ $json.utmUrl }}"
          },
          "schema": [
            {
              "id": "id",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": true,
              "required": false,
              "displayName": "id",
              "defaultMatch": true
            },
            {
              "id": "URL",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "URL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "id"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "upsert"
      },
      "credentials": {
        "airtableTokenApi": {
          "id": "0ApVmNsLu7aFzQD6",
          "name": "Airtable Personal Access Token account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "19074462-d719-4fdf-bc59-d6b2ecd1ce20",
      "name": "Create QR Code With Submitted QR Link",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        280,
        -20
      ],
      "parameters": {
        "url": "=https://quickchart.io/qr?text={{ $json.utmUrl }}&size=300&margin=10&ecLevel=H&dark=000000&light=FFFFFF\n",
        "options": {}
      },
      "typeVersion": 4.2
    },
    {
      "id": "a8c22bb2-f8eb-4e5f-b288-9c25e0aeb648",
      "name": "Schedule Google Analytics Report To Marketing Manager",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -460,
        280
      ],
      "parameters": {
        "rule": {
          "interval": [
            {}
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "268c110c-2b7c-4450-b5b0-5d5326eac17f",
      "name": "Google Analytics Data Analysis Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        -100,
        280
      ],
      "parameters": {
        "text": "={{ $json.timestamp }}",
        "options": {
          "systemMessage": "\"You are an advanced data analytics AI specializing in executive reporting. Your task is to analyze the provided dataset and generate a structured executive summary that highlights key insights, trends, and actionable takeaways. Structure your summary in the following format:\n\nOverview \u2013 Briefly describe the dataset and its significance.\nKey Performance Indicators (KPIs) \u2013 Highlight the most important metrics and compare them to previous periods if applicable.\nTrends & Insights \u2013 Identify patterns, growth areas, declines, and anomalies.\nOpportunities & Recommendations \u2013 Provide strategic recommendations based on the insights.\nConclusion \u2013 Summarize the key takeaways concisely.\n*Ensure the tone is professional, clear, and tailored for executives who require quick, data-driven insights without unnecessary details.\""
        },
        "promptType": "define"
      },
      "typeVersion": 1.7
    },
    {
      "id": "1b012731-e67b-4e0d-95b7-a7f587754a05",
      "name": "Send Summary Report To Marketing Manager",
      "type": "n8n-nodes-base.gmail",
      "position": [
        300,
        280
      ],
      "webhookId": "a9b88615-c7e2-4b56-891a-98f4d6b34220",
      "parameters": {
        "sendTo": "john@marketingcanopy.com",
        "message": "={{ $json.output }}",
        "options": {},
        "subject": "Google Analytics Metrics Summary Report"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "pIXP1ZseBP4Z5CCp",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "9da758e1-8aed-446b-a074-8fee5405583f",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -540,
        -280
      ],
      "parameters": {
        "width": 500,
        "height": 400,
        "content": "Create a marketing link with UTM parameters. Easily store in database and have QR code created and ready as well.\n\nType in requirements:\nwebsite URL\ncampaign id\ncampaign source\ncampaign medium\ncampaign name\ncampaign term\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "92f5df8d-88ca-4b58-b544-c0b2d3578a73",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        -380
      ],
      "parameters": {
        "color": 4,
        "width": 580,
        "height": 540,
        "content": "Code node creates the URL with UTM parameters. \n\nIt then sends to your Airtable database to store for records. It also creates a QR code with the embedded link to be used for materials. \n\nSample Airtable Setup:\n-Website Link UTM column"
      },
      "typeVersion": 1
    },
    {
      "id": "408af10c-4b0e-4d94-b02d-5d887fb150c3",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -540,
        180
      ],
      "parameters": {
        "color": 5,
        "width": 1340,
        "height": 460,
        "content": "Schedule a Google Analytics Reports with Medium/Source to track UTM link performance. Update the reporting fields to fit your business needs. You can track traffic, conversions and other engagement metrics.\n\n*Sample Google Report Metrics: Sessions. Update metrics as needed."
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "6e6641fd-a59c-49e9-af43-1b2b9b458544",
  "connections": {
    "Google Analytics": {
      "ai_tool": [
        [
          {
            "node": "Google Analytics Data Analysis Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model1": {
      "ai_languageModel": [
        [
          {
            "node": "Google Analytics Data Analysis Agent",
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
            "node": "Google Analytics Data Analysis Agent",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "Set UTM Parameters For Link": {
      "main": [
        [
          {
            "node": "Create UTM Link With Parameters",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Submit UTM Link To Database": {
      "main": [
        []
      ]
    },
    "Create UTM Link With Parameters": {
      "main": [
        [
          {
            "node": "Create QR Code With Submitted QR Link",
            "type": "main",
            "index": 0
          },
          {
            "node": "Submit UTM Link To Database",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create UTM Link & Send To Database": {
      "main": [
        [
          {
            "node": "Set UTM Parameters For Link",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Analytics Data Analysis Agent": {
      "main": [
        [
          {
            "node": "Send Summary Report To Marketing Manager",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send Summary Report To Marketing Manager": {
      "main": [
        []
      ]
    },
    "Schedule Google Analytics Report To Marketing Manager": {
      "main": [
        [
          {
            "node": "Google Analytics Data Analysis Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
