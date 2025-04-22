# Send daily affirmations to Telegram

**[View Template](https://n8n.io/workflows/342-/)**  **Published Date:** 04/06/2020  **Created By:** malgamves  **Categories:** `Development` `Core Nodes` `Communication` `HITL`  

## Template Description



A workflow which allows you to receive daily affirmations via Telegram by querying a REST API triggered by a Cron node. 


I used the affirmations.dev API 

## Template JSON

```
{
  "id": "2",
  "name": "Daily Text Affirmations",
  "nodes": [
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        350,
        380
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 9
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        760,
        380
      ],
      "parameters": {
        "url": "https://affirmations.dev",
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1140,
        380
      ],
      "parameters": {
        "text": "=Hey Daniel, here's your daily affirmation...\n\n{{$node[\"HTTP Request\"].json[\"affirmation\"]}}",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "Telegram Token"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Cron": {
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
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Telegram",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
