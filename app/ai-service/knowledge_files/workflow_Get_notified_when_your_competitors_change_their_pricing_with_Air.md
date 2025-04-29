# Get notified when your competitors change their pricing with Airtop and Slack

**[View Template](https://n8n.io/workflows/3480-/)**  **Published Date:** 04/08/2025  **Created By:** Cesar @ Airtop AI  **Categories:** `Data & Storage` `Productivity` `Communication` `HITL` `Development` `Core Nodes`  

## Template Description

About the Automation

Staying on top of competitor pricing changes can be a full-time job. Manual price tracking is time-consuming and prone to errors, especially when dealing with complex pricing structures and multiple subscription tiers. Paid competitor price monitoring tools like Competera, Visualping and Fluxguard can be expensive. What if you could automate this process and get instant alerts when competitors adjust their pricing?

How to easily monitor competitor pricing

With this automation, you'll learn how to set up automated price monitoring system using Airtop's built-in node in n8n. By the end, your system will automatically track competitor pricing changes and notify you of any modifications.

What You'll Need

A free Airtop API Key
Google Sheets account with a copy of this sheet
URLs of competitors' pricing pages

Understanding the Process

This automation continuously monitors competitor pricing pages and compares them against your baseline data. The workflow:

Tracks all different pricing plans (monthly, yearly, etc.).
Monitors feature changes across different tiers.
Detects and logs pricing structure modifications.
Alerts you via Slack when changes are detected

Setting Up Your Automation

We've created a ready-to-use blueprint for seamless price monitoring. Here's how to get started:

Connect your Google Sheets
Set up your Airtop API connection
Define update frequency

Customization Options

Enhance the basic template with these popular modifications:

Add other notification channels (Email, Telegram, etc.).
Include feature comparison tracking.
Set up threshold-based alerts for significant price changes
Track historical pricing trends

Real-World Applications

Case Study 1: A B2B SaaS company can use this automation to track competitors' pricing changes. When they identify a market-wide pricing shift, they can adjust their strategy proactively within minutes.

Case Study 2: An online Ecommerce retailer automates monitoring of 100+ competitor products, maintaining optimal pricing positions and increasing profit margins.

Best Practices

To ensure accurate tracking:

Include detailed baseline data for each pricing tier
Specify both monthly and annual pricing clearly
List all features included in each plan
Update your baseline data whenever you verify changes
Include any promotional pricing or special offers
Document currency and regional variations if applicable

Example Structure in Google Sheets:

Competitor: Acme Tools
Basic Plan:
Monthly: $29
Annual: $290 ($24.17/mo)
Features: 5 users, 10GB storage, basic support
Pro Plan:
Monthly: $79
Annual: $790 ($65.83/mo)
Features: 20 users, 50GB storage, priority support

What's Next?

After setting up your price monitoring automation, consider the following:

Creating automated competitive analysis reports
Setting up market trend analysis
Implementing automatic pricing recommendations
Expanding monitoring to feature changes

Happy monitoring!

## Template JSON

```
{
  "id": "XY0cZQwrhzOkisSt",
  "meta": {
    "instanceId": "660cf2c29eb19fa42319afac3bd2a4a74c6354b7c006403f6cba388968b63f5d",
    "templateCredsSetupCompleted": true
  },
  "name": "Monitor Competitor Pricing",
  "tags": [
    {
      "id": "a8B9vqj0vNLXcKVQ",
      "name": "template",
      "createdAt": "2025-04-04T15:38:37.785Z",
      "updatedAt": "2025-04-04T15:38:37.785Z"
    }
  ],
  "nodes": [
    {
      "id": "056f47d7-5a06-4714-beb5-c53ffb663ed1",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        0,
        -180
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "a8e5d613-bf15-4ebf-9191-4a17e86baba1",
      "name": "Get Pricing URLs",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        220,
        -180
      ],
      "parameters": {
        "options": {},
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1MER5ftlYyfPZR-N9ZwwVT7Ea0wwqQYxln8l1HuBqjhA/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1MER5ftlYyfPZR-N9ZwwVT7Ea0wwqQYxln8l1HuBqjhA",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1MER5ftlYyfPZR-N9ZwwVT7Ea0wwqQYxln8l1HuBqjhA/edit?usp=drivesdk",
          "cachedResultName": "Copy of Monitor Pricing"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "CwpCAR1HwgHZpRtJ",
          "name": "Google Drive"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "7ee84bd6-cc49-46cd-bde2-04ec53773bb8",
      "name": "Check pricing",
      "type": "n8n-nodes-base.airtop",
      "position": [
        440,
        -260
      ],
      "parameters": {
        "url": "={{ $json[\"Pricing URL\"] }}",
        "prompt": "=This is a pricing page. Please summarize it concisely by including every plan. For each plan, list the price and the top 3 features it includes. Compare the current plan to the previous plan described here: \n[{{ $json.Pricing }}].\n\nRETURN ONLY 3 FIELDS:\n1. `pricing_summary` - A textual description of the pricing, including the  plan's name, price, and top 3 features.\n2. `differences_summary` - If there are significant differences in the PRICES between the previous plan and the current one, summarize the differences concisely in a textual description, focusing only on the changes in prices.\n3. `status` - In a status field, return [DIFF] if the new plan and pricing are substantially different from the previous one, [SIMILAR] if they are similar, or [NEW] if the previous pricing is empty.\n\n- important, do not guess or estimate, just report things that are clearly mentioned in pricing page\n",
        "resource": "extraction",
        "operation": "query",
        "sessionMode": "new",
        "additionalFields": {
          "outputSchema": "{\n  \"type\": \"object\",\n  \"properties\": {\n    \"pricing_summary\": {\n      \"type\": \"string\",\n      \"description\": \"A textual description of the pricing, including the plan's name, price, and top 3 features.\"\n    },\n    \"differences_summary\": {\n      \"type\": \"string\",\n      \"description\": \"A concise summary of the differences between the previous and current plans, focusing on changes.\"\n    },\n    \"status\": {\n      \"type\": \"string\",\n      \"description\": \"Indicates if the new plan is substantially different from the previous one.\"\n    }\n  },\n  \"required\": [\n    \"pricing_summary\",\n    \"differences_summary\",\n    \"status\"\n  ],\n  \"additionalProperties\": false,\n  \"$schema\": \"http://json-schema.org/draft-07/schema#\"\n}"
        }
      },
      "credentials": {
        "airtopApi": {
          "id": "byhouJF8RLH5DkmY",
          "name": "Airtop"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "b6c89c9e-d87c-427d-a214-f5540036d3fd",
      "name": "Parse response",
      "type": "n8n-nodes-base.code",
      "position": [
        880,
        -180
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "const response = JSON.parse($json.data.modelResponse)\n\nreturn { json: {\n  ...response,\n  row_number: $json['row_number'],\n  \"Pricing URL\": $json[\"Pricing URL\"]\n}}"
      },
      "typeVersion": 2
    },
    {
      "id": "7783075b-3ae3-4032-9506-16d24e9f25f6",
      "name": "Merge",
      "type": "n8n-nodes-base.merge",
      "position": [
        660,
        -180
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combineBy": "combineByPosition"
      },
      "typeVersion": 3.1
    },
    {
      "id": "7466f2a8-8b72-48f5-94a4-c150e6bc5584",
      "name": "Update pricing",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1320,
        -280
      ],
      "parameters": {
        "columns": {
          "value": {
            "Time": "={{ $now }}",
            "Pricing": "={{ $json.pricing_summary }}",
            "row_number": "={{ $json.row_number }}",
            "Pricing URL": "="
          },
          "schema": [
            {
              "id": "Pricing URL",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Pricing URL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Pricing",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Pricing",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Time",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Time",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "row_number",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": true,
              "required": false,
              "displayName": "row_number",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "row_number"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "update",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1MER5ftlYyfPZR-N9ZwwVT7Ea0wwqQYxln8l1HuBqjhA/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1MER5ftlYyfPZR-N9ZwwVT7Ea0wwqQYxln8l1HuBqjhA",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1MER5ftlYyfPZR-N9ZwwVT7Ea0wwqQYxln8l1HuBqjhA/edit?usp=drivesdk",
          "cachedResultName": "Copy of Monitor Pricing"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "CwpCAR1HwgHZpRtJ",
          "name": "Google Drive"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "3c2d84a5-1080-4e49-a43e-f643e454e463",
      "name": "Notify pricing change",
      "type": "n8n-nodes-base.slack",
      "position": [
        1320,
        -80
      ],
      "webhookId": "539892f2-e877-4dd5-85e7-d10e1be6daf1",
      "parameters": {
        "text": "={{ $json[\"Pricing URL\"] + \" - \" + $json.differences_summary }}",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "list",
          "value": "C087FK3J0MC",
          "cachedResultName": "pricing-changes"
        },
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": {
          "id": "NgjAmOgS9xRg1RlU",
          "name": "Slack account"
        }
      },
      "typeVersion": 2.3
    },
    {
      "id": "174132d5-3273-4b8b-a51f-ccbce9f21f93",
      "name": "Filter out similar",
      "type": "n8n-nodes-base.filter",
      "position": [
        1100,
        -180
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "5142d433-519e-4e9d-ab8e-3a97d1177b51",
              "operator": {
                "type": "string",
                "operation": "notContains"
              },
              "leftValue": "={{ $json.status }}",
              "rightValue": "SIMILAR"
            }
          ]
        }
      },
      "typeVersion": 2.2
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "c6b3fa69-c354-44b6-b472-1b530fca23e7",
  "connections": {
    "Merge": {
      "main": [
        [
          {
            "node": "Parse response",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check pricing": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parse response": {
      "main": [
        [
          {
            "node": "Filter out similar",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Pricing URLs": {
      "main": [
        [
          {
            "node": "Check pricing",
            "type": "main",
            "index": 0
          },
          {
            "node": "Merge",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Filter out similar": {
      "main": [
        [
          {
            "node": "Update pricing",
            "type": "main",
            "index": 0
          },
          {
            "node": "Notify pricing change",
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
            "node": "Get Pricing URLs",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
