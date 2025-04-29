# N8N Español - Telegram Welcome Bot

**[View Template](https://n8n.io/workflows/872-/)**  **Published Date:** 01/02/2021  **Created By:** The { AI } rtist  **Categories:** `Communication` `HITL`  

## Template Description



Este workflow te permite crear un Bot para dar la Bienvenida y despedida en tu grupo de telegram.

How To, Paso a Paso: https://comunidad-n8n.com/construye-tu-bot-con-n8n

Comunidad de telegram: https://t.me/comunidadn8n



## Template JSON

```
{
  "id": "27",
  "name": "N8N Espa\u00f1ol - BOT",
  "nodes": [
    {
      "name": "Saludos-IF",
      "type": "n8n-nodes-base.if",
      "position": [
        450,
        450
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Saludos-TelegramTrigger\"].json[\"message\"][\"new_chat_member\"][\"first_name\"]}}",
              "operation": "isEmpty"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Saludos-IF1",
      "type": "n8n-nodes-base.if",
      "position": [
        490,
        630
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Saludos-TelegramTrigger\"].json[\"message\"][\"left_chat_member\"][\"first_name\"]}}",
              "operation": "isEmpty"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "S-Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        700,
        660
      ],
      "parameters": {
        "text": "=\u2716\ufe0f {{$node[\"Saludos-TelegramTrigger\"].json[\"message\"][\"left_chat_member\"][\"first_name\"]}} DEP. \ud83d\ude4f Que los Dioses te protejan.",
        "chatId": "=@comunidadn8n",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "N8N Espa\u00f1ol - BOT"
      },
      "typeVersion": 1
    },
    {
      "name": "Saludos-TelegramTrigger",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        260,
        560
      ],
      "webhookId": "4ef8c98e-e617-4d36-9c6d-04fae7e9298c",
      "parameters": {
        "updates": [
          "*"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "N8N Espa\u00f1ol - BOT"
      },
      "typeVersion": 1
    },
    {
      "name": "S-Telegram2",
      "type": "n8n-nodes-base.telegram",
      "position": [
        730,
        460
      ],
      "parameters": {
        "text": "=\u2714\ufe0f {{$node[\"Saludos-TelegramTrigger\"].json[\"message\"][\"new_chat_member\"][\"first_name\"]}}, \u00a1bienvenid@ a N8N en Espa\u00f1oll!  \ud83d\ude4c",
        "chatId": "=@comunidadn8n",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "N8N Espa\u00f1ol - BOT"
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "Saludos-IF": {
      "main": [
        [],
        [
          {
            "node": "S-Telegram2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Saludos-IF1": {
      "main": [
        [],
        [
          {
            "node": "S-Telegram",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Saludos-TelegramTrigger": {
      "main": [
        [
          {
            "node": "Saludos-IF1",
            "type": "main",
            "index": 0
          },
          {
            "node": "Saludos-IF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
