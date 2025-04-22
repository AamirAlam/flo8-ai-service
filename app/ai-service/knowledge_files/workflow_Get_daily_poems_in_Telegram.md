# Get daily poems in Telegram

**[View Template](https://n8n.io/workflows/975-/)**  **Published Date:** 03/09/2021  **Created By:** Lorena  **Categories:** `Development` `Core Nodes` `Communication` `HITL` `Miscellaneous`  

## Template Description

This workflow posts a poem translated into English every day in a Telegram chat.



Cron node: triggers the workflow every day at 10:00. You can change the time and interval based on your use case. 

HTTP Request node: makes an HTTP request to the Poemist API that returns a random poem.

LingvaNex node: translates the returned poems into English.

Telegram node: takes in the translated poem and posts it in the chat.

## Template JSON

```
{
  "id": "3",
  "name": "Daily poems in Telegram",
  "nodes": [
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        -250,
        400
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 10
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        350,
        400
      ],
      "parameters": {
        "text": "=\u2712\ufe0f Poem of the day:\n{{$node[\"HTTP Request\"].json[\"0\"][\"title\"]}} by {{$node[\"HTTP Request\"].json[\"0\"][\"poet\"][\"name\"]}}\n\n{{$node[\"HTTP Request\"].json[\"0\"][\"content\"]}}\n\u2601\ufe0f",
        "chatId": "123456789",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "telegram_bot"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -50,
        400
      ],
      "parameters": {
        "url": "https://www.poemist.com/api/v1/randompoems",
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "LingvaNex",
      "type": "n8n-nodes-base.lingvaNex",
      "position": [
        150,
        400
      ],
      "parameters": {
        "text": "={{$node[\"HTTP Request\"].json[\"0\"][\"content\"]}}",
        "options": {},
        "translateTo": "en_GB"
      },
      "credentials": {
        "lingvaNexApi": "lingvanex_API"
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
    "LingvaNex": {
      "main": [
        [
          {
            "node": "Telegram",
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
            "node": "LingvaNex",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
