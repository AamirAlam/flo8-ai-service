# Send daily weather updates via a message using the Gotify node

**[View Template](https://n8n.io/workflows/774-/)**  **Published Date:** 11/11/2020  **Created By:** ghagrawal17  **Categories:** `Utility` `Miscellaneous` `Communication`  

## Template Description



## Template JSON

```
{
  "id": "115",
  "name": "Send daily weather updates via a message using the Gotify node",
  "nodes": [
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        490,
        340
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
      "name": "OpenWeatherMap",
      "type": "n8n-nodes-base.openWeatherMap",
      "position": [
        690,
        340
      ],
      "parameters": {
        "cityName": "berlin"
      },
      "credentials": {
        "openWeatherMapApi": "owm"
      },
      "typeVersion": 1
    },
    {
      "name": "Gotify",
      "type": "n8n-nodes-base.gotify",
      "position": [
        890,
        340
      ],
      "parameters": {
        "message": "=Hey! The temperature outside is {{$node[\"OpenWeatherMap\"].json[\"main\"][\"temp\"]}}\u00b0C.",
        "additionalFields": {
          "title": "Today's Weather Update"
        }
      },
      "credentials": {
        "gotifyApi": "gotify-credentials"
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
            "node": "OpenWeatherMap",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenWeatherMap": {
      "main": [
        [
          {
            "node": "Gotify",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
