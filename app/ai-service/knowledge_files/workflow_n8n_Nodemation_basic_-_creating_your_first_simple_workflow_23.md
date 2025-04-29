# n8n Nodemation basic - creating your first simple workflow (2/3)

**[View Template](https://n8n.io/workflows/19-/)**  **Published Date:** 09/16/2019  **Created By:** sven  **Categories:** `Development` `Core Nodes`  

## Template Description

In this video we will create a simple n8n Nodemation workflow to receive date via webhook, alter the data and send it to a webserver. We will be using webhook, function and http request node together.

> Youtube Video



## Template JSON

```
{
  "id": "4",
  "name": "greeting",
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        720,
        410
      ],
      "parameters": {
        "path": "greetinghook"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1120,
        410
      ],
      "parameters": {
        "url": "https://webhook.site/c0a47a6f-6a71-4d18-baef-51f694f7c56b",
        "requestMethod": "POST",
        "responseFormat": "string",
        "bodyParametersUi": {
          "parameter": [
            {
              "name": "greeting",
              "value": "={{$node[\"FunctionItem\"].data[\"greeting\"]}}"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "FunctionItem",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        930,
        410
      ],
      "parameters": {
        "functionCode": "item.greeting = `Hello ${item.query.name}, have fun at the ${item.query.event}!`;\nitem.greeting = \"Hello \" + item.query.name + \", have fun at the \" + item.query.event + \"!\";\nreturn item;"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "FunctionItem",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "FunctionItem": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
