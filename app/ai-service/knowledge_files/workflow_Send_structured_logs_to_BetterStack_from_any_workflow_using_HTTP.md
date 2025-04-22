# Send structured logs to BetterStack from any workflow using HTTP Request

**[View Template](https://n8n.io/workflows/3400-/)**  **Published Date:** 04/01/2025  **Created By:** Audun  **Categories:** `Development` `Core Nodes`  

## Template Description

Send structured logs to BetterStack from any workflow using HTTP Request

Who is this for?

This workflow is perfect for automation builders, developers, and DevOps teams using n8n who want to send structured log messages to BetterStack Logs. Whether you're monitoring mission-critical workflows or simply want centralized visibility into process execution, this reusable log template makes integration easy.

What problem is this workflow solving?

Logging failures or events across multiple workflows typically requires duplicated logic. This workflow solves that by acting as a shared log sender, letting you forward consistent log entries from any other workflow using the Execute Workflow node.

What this workflow does

Accepts level (e.g., "info", "warn", "error") and message fields via Execute Workflow Trigger
Sends the structured log to your BetterStack ingestion endpoint via HTTP Request
Uses HTTP Header Auth for secure delivery
Includes a manual trigger for testing and a sample call to demonstrate usage
Comes with clear sticky notes to help you get started

Setup

Copy your BetterStack Logs ingestion URL.
Create a Header Auth credential in n8n with your Authorization: Bearer YOUR_API_KEY.
Replace the URL in the HTTP Request node with your BetterStack endpoint.
Optionally modify the test data or log levels for custom scenarios.
Use Execute Workflow in any of your workflows to send logs here.

## Template JSON

```
{
  "meta": {
    "instanceId": "568298fde06d3db80a2eea77fe5bf45f0c7bb898dea20b769944e9ac7c6c5a80"
  },
  "nodes": [
    {
      "id": "72babb83-0530-4809-9f6f-d9afaf91fd59",
      "name": "Send Log to BetterStack",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        80,
        140
      ],
      "parameters": {
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"message\":\"{{ $json.message }}\",\n  \"level\": \"{{ $json.level }}\"\n} ",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "NAa1bu8yteVhXxxV",
          "name": "Header Auth BetterStack"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "863b184b-05c0-47b7-82c1-166bdf25a32a",
      "name": "Recieve log message",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "notes": "from another workflow",
      "position": [
        -140,
        140
      ],
      "parameters": {
        "workflowInputs": {
          "values": [
            {
              "name": "level"
            },
            {
              "name": "message"
            }
          ]
        }
      },
      "notesInFlow": true,
      "typeVersion": 1.1
    },
    {
      "id": "e696b65e-5249-43b2-9a33-4e59fc616f21",
      "name": "Test workflow",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -260,
        -120
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "f7b51eae-4016-4072-9539-b66ea8646508",
      "name": "Send test log message",
      "type": "n8n-nodes-base.executeWorkflow",
      "notes": "using workflow",
      "position": [
        -40,
        -120
      ],
      "parameters": {
        "options": {},
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{$workflow.id}}"
        },
        "workflowInputs": {
          "value": {
            "level": "error",
            "message": "This is a test log message"
          },
          "schema": [
            {
              "id": "level",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "level",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "message",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "message",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": true
        }
      },
      "notesInFlow": true,
      "typeVersion": 1.2
    },
    {
      "id": "72457cde-ea6f-406a-8d5e-70878114dd3e",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -440,
        60
      ],
      "parameters": {
        "width": 860,
        "height": 280,
        "content": "## Send log entries to BetterStack\nThis workflow can be used in two ways:\n1. Save it as a separate workflow to\nuse if from multiple worflows.\n2. Embed it into one workflow to just\nuse it from one."
      },
      "typeVersion": 1
    },
    {
      "id": "442976e5-1306-4c9b-a3e6-5693ae6d132c",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -440,
        -240
      ],
      "parameters": {
        "color": 7,
        "width": 660,
        "height": 280,
        "content": "## Demo\nThis is just a demo of how to call the workflow.\nKeep it here, replace it with your own workflow or delete it."
      },
      "typeVersion": 1
    },
    {
      "id": "4175c168-1f59-4213-8bc4-a71dd62c3bd9",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        20,
        100
      ],
      "parameters": {
        "color": 3,
        "height": 200,
        "content": "### Edit me"
      },
      "typeVersion": 1
    },
    {
      "id": "c69c7c62-f4b5-4b14-b6be-8e9f3b8a38cd",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -780,
        -240
      ],
      "parameters": {
        "color": 6,
        "width": 300,
        "height": 580,
        "content": "### \ud83e\uddfe Log to BetterStack\n\n**\ud83d\udc4b Hello! I'm Audun / xqus** \n\ud83d\udd17 My work: [xqus.com](https://xqus.com)\n\ud83d\udcb8 n8n shop: [xqus.gumroad.com](https://xqus.gumroad.com)\n\n\nThis workflow sends log messages to [BetterStack Logs](https://betterstack.com/logs) using a POST request.\n\n#### \u2705 Usage:\n1. **From other workflows**  \n   \u2192 Use the **Execute Workflow** node and pass in `level` and `message`.\n\n2. **As standalone**  \n   \u2192 Manually trigger for testing, or embed it into a single workflow.\n\n#### \ud83d\udd27 Setup:\n1. Set your **BetterStack Logs endpoint URL** in the HTTP Request node.  \n2. Add your **Header Auth** credentials: `Authorization: Bearer YOUR_TOKEN`\n"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Test workflow": {
      "main": [
        [
          {
            "node": "Send test log message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Recieve log message": {
      "main": [
        [
          {
            "node": "Send Log to BetterStack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
