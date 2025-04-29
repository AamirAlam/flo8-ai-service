# Get Weather Forecast via Telegram

**[View Template](https://n8n.io/workflows/346-/)**  **Published Date:** 04/07/2020  **Created By:** tanaypant  **Categories:** `Utility` `Miscellaneous` `Communication` `HITL`  

## Template Description



A workflow to receive weather updates on demand using a Telegram bot. The workflow is triggered using the Telegram Trigger node by issuing a message to the Telegram bot. The OpenWeatherMap node queries the weather API and returns the result using the Telegram node.



## Template JSON

```
{
  "id": "2",
  "name": "Telegram Weather Workflow",
  "nodes": [
    {
      "name": "Telegram Trigger",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        270,
        220
      ],
      "parameters": {
        "updates": [
          "message"
        ]
      },
      "credentials": {
        "telegramApi": "Telegram"
      },
      "typeVersion": 1
    },
    {
      "name": "OpenWeatherMap",
      "type": "n8n-nodes-base.openWeatherMap",
      "position": [
        480,
        220
      ],
      "parameters": {
        "cityName": "berlin,de"
      },
      "credentials": {
        "openWeatherMapApi": "OpenWeatherMap"
      },
      "typeVersion": 1
    },
    {
      "name": "Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        670,
        220
      ],
      "parameters": {
        "text": "=Right now, we have {{$node[\"OpenWeatherMap\"].json[\"weather\"][0][\"description\"]}}. The temperature is {{$node[\"OpenWeatherMap\"].json[\"main\"][\"temp\"]}}\u00b0C but it really feels like {{$node[\"OpenWeatherMap\"].json[\"main\"][\"feels_like\"]}}\u00b0C \ud83d\ude42",
        "chatId": "={{$node[\"Telegram Trigger\"].json[\"message\"][\"chat\"][\"id\"]}}",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "Telegram"
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "OpenWeatherMap": {
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
    "Telegram Trigger": {
      "main": [
        [
          {
            "node": "OpenWeatherMap",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
