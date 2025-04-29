# Integrate Xero with FileMaker using Webhooks

**[View Template](https://n8n.io/workflows/2499-/)**  **Published Date:** 10/25/2024  **Created By:** Stathis Askaridis  **Categories:** `Data & Storage` `Development` `Core Nodes`  

## Template Description

Integrate Xero with FileMaker using Webhooks

Workflow Description

This n8n workflow automates the integration between Xero and FileMaker, allowing for seamless data transfer between the two platforms. By listening for webhooks from Xero (e.g., new invoices, payments, or contacts), this workflow ensures that data is automatically sent and recorded in a FileMaker database.

Who is This For?

This workflow template is ideal for:
Accountants** who need a streamlined process to sync financial data between Xero and FileMaker.
Business Owners** looking to automate data entry and improve accuracy across their systems.
Developers** building solutions for clients that require integration between accounting software and databases.
Operations Teams** focused on minimizing manual work and improving efficiency.

Key Steps

Xero Webhook Trigger: The workflow starts by capturing events from Xero via a webhook.
Data Processing: Transforms and maps the incoming data to match FileMaker’s required format.
FileMaker Node: Utilizes the FileMaker node to create or update records directly in the FileMaker database.
Logging & Error Handling: Tracks successful entries and manages any errors with automated alerts.

Setup Instructions

Set Up the Xero Webhook:
   Create a webhook in Xero and point it to your n8n webhook node URL.
   Configure the types of events to trigger the workflow (e.g., new invoices or payments).
   Xero will then send some test calls to test you are doing proper hash control.

Connect the FileMaker Node:
   Set up your FileMaker node with the appropriate credentials and database configuration.
   Map the fields between the incoming Xero data and your FileMaker database structure.
Customize Data Processing:
   Adjust data transformations as needed to ensure compatibility with your FileMaker schema.
Test and Deploy:
   Run the workflow with sample data to ensure everything is functioning correctly.
   Monitor the execution log to verify data transfer and make any adjustments as needed.
Error Handling Configuration:
   Configure error-handling nodes or alerts to notify you of any issues during data processing.

Benefits

This setup facilitates real-time data synchronization between Xero and FileMaker, reducing the need for manual data entry and improving overall operational efficiency.

## Template JSON

```
{
  "meta": {
    "instanceId": "5663a0748c6a6e6071d13694c60722e799714f53ff7a9bfdda15fbadbaeebb76"
  },
  "nodes": [
    {
      "id": "9bd2c2f7-d837-451e-8a25-a185713edefb",
      "name": "Crypto",
      "type": "n8n-nodes-base.crypto",
      "position": [
        1640,
        660
      ],
      "parameters": {
        "type": "SHA256",
        "value": "={{$json[\"source_data\"]}}",
        "action": "hmac",
        "secret": "1",
        "encoding": "base64",
        "dataPropertyName": "target_data"
      },
      "typeVersion": 1
    },
    {
      "id": "75aca737-5e31-4022-8827-375cf8717a06",
      "name": "Move Binary Data",
      "type": "n8n-nodes-base.moveBinaryData",
      "position": [
        1240,
        660
      ],
      "parameters": {
        "options": {},
        "setAllData": false,
        "destinationKey": "raw_data"
      },
      "typeVersion": 1
    },
    {
      "id": "f1ece5d1-a38f-4548-80b4-a77f07c0cc95",
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        1440,
        660
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "source_data",
              "value": "={{$json[\"raw_data\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "id": "251bd7d1-e955-4b2c-a020-e0b2e3ebb5cc",
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        1860,
        660
      ],
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{$node[\"Crypto\"].json[\"target_data\"]}}",
              "value2": "={{$node[\"Xero Webhook\"].json[\"headers\"][\"x-xero-signature\"]}}"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "3a7041d6-e86b-414f-9d26-94c1ffe893cc",
      "name": "Success",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        2080,
        540
      ],
      "parameters": {
        "options": {
          "responseCode": 200
        },
        "respondWith": "noData"
      },
      "typeVersion": 1
    },
    {
      "id": "8dfe4916-2fce-4d51-8a41-66cb4e31bdf5",
      "name": "Unauthorised",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        2080,
        740
      ],
      "parameters": {
        "options": {
          "responseCode": 401
        },
        "respondWith": "noData"
      },
      "typeVersion": 1
    },
    {
      "id": "81b08d6b-065c-4e61-87b7-6428963339e2",
      "name": "Create webhook record",
      "type": "n8n-nodes-base.filemaker",
      "position": [
        2320,
        540
      ],
      "parameters": {
        "action": "create",
        "layout": "Webhooks",
        "fieldsParametersUi": {
          "fields": [
            {
              "name": "json",
              "value": "={{$node[\"Set\"].json[\"source_data\"]}}"
            }
          ]
        }
      },
      "credentials": {
        "fileMaker": {
          "id": "T1MTy9Xu5m7Nubie",
          "name": "Kounio FileMaker"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "48d977ee-64df-4788-8808-70cd6c7bf5f7",
      "name": "Perform processWebhook script",
      "type": "n8n-nodes-base.filemaker",
      "position": [
        2540,
        540
      ],
      "parameters": {
        "action": "performscript",
        "layout": "Webhooks",
        "script": "processWebhook",
        "scriptParam": "={{ $json.response.recordId }}"
      },
      "credentials": {
        "fileMaker": {
          "id": "T1MTy9Xu5m7Nubie",
          "name": "Kounio FileMaker"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "d6f4d1d4-4e69-4279-88e2-ea27036cea20",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2600,
        420
      ],
      "parameters": {
        "content": "## Script Parameter\nPasses the record id as script parameter to be used in your processWebhook script"
      },
      "typeVersion": 1
    },
    {
      "id": "72b3f208-803b-45c5-b38d-eeef4425a2ba",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1620,
        540
      ],
      "parameters": {
        "width": 158.74371859296477,
        "height": 121.3065326633166,
        "content": "## Input\nAdd your Xero webhook secret here"
      },
      "typeVersion": 1
    },
    {
      "id": "54f36def-0ac9-4769-818f-2e8991f196a5",
      "name": "Xero Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        1040,
        660
      ],
      "webhookId": "4cf50a61-b550-4ee6-984d-ad8c94e2b5c2",
      "parameters": {
        "path": "4cf50a61-b550-4ee6-984d-ad8c94e2b5c2",
        "options": {
          "rawBody": true
        },
        "httpMethod": "POST",
        "responseMode": "responseNode"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "Success",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Unauthorised",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set": {
      "main": [
        [
          {
            "node": "Crypto",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Crypto": {
      "main": [
        [
          {
            "node": "IF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Success": {
      "main": [
        [
          {
            "node": "Create webhook record",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Xero Webhook": {
      "main": [
        [
          {
            "node": "Move Binary Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Move Binary Data": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create webhook record": {
      "main": [
        [
          {
            "node": "Perform processWebhook script",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
