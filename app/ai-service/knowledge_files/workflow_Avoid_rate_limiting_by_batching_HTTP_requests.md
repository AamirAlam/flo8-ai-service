# Avoid rate limiting by batching HTTP requests

**[View Template](https://n8n.io/workflows/1243-/)**  **Published Date:** 09/27/2021  **Created By:** ghagrawal17  **Categories:** `Development` `Core Nodes`  

## Template Description

This workflow demonstrates the use of the Split In Batches node and the Wait node to avoid API rate limits.

Customer Datastore node: The workflow fetches data from the Customer Datastore node. Based on your use case, replace it with a relevant node.

Split In Batches node: This node splits the items into a single item. Based on the API limit, you can configure the Batch Size.

HTTP Request node: This node makes API calls to a placeholder URL. If the Split In Batches node returns 5 items, the HTTP Request node will make 5 different API calls.

Wait node: This node will pause the workflow for the time you specify. On resume, the Split In Batches node gets executed node, and the next batch is processed.

Replace Me (NoOp node): This node is optional. If you want to continue your workflow and process the items, replace this node with the corresponding node(s).

## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Customer Datastore",
      "type": "n8n-nodes-base.n8nTrainingCustomerDatastore",
      "position": [
        450,
        300
      ],
      "parameters": {
        "operation": "getAllPeople",
        "returnAll": true
      },
      "typeVersion": 1
    },
    {
      "name": "SplitInBatches",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        650,
        300
      ],
      "parameters": {
        "options": {},
        "batchSize": 1
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        850,
        300
      ],
      "parameters": {
        "url": "https://jsonplaceholder.typicode.com/posts",
        "options": {},
        "requestMethod": "POST",
        "bodyParametersUi": {
          "parameter": [
            {
              "name": "id",
              "value": "={{$json[\"id\"]}}"
            },
            {
              "name": "name",
              "value": "={{$json[\"name\"]}}"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Wait",
      "type": "n8n-nodes-base.wait",
      "position": [
        950,
        100
      ],
      "webhookId": "b809abfb-8e02-4b31-90b9-0005be656312",
      "parameters": {
        "unit": "seconds",
        "amount": 4
      },
      "typeVersion": 1
    },
    {
      "name": "Replace Me",
      "type": "n8n-nodes-base.noOp",
      "position": [
        1050,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "connections": {
    "Wait": {
      "main": [
        [
          {
            "node": "SplitInBatches",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Replace Me",
            "type": "main",
            "index": 0
          },
          {
            "node": "Wait",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "SplitInBatches": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Customer Datastore": {
      "main": [
        [
          {
            "node": "SplitInBatches",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Customer Datastore",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
