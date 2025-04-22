# Send daily weather updates via a push notification using Spontit

**[View Template](https://n8n.io/workflows/796-/)**  **Published Date:** 11/30/2020  **Created By:** ghagrawal17  **Categories:** `Utility` `Miscellaneous` `Communication`  

## Template Description



## Template JSON

```
{
  "id": "141",
  "name": "Send daily weather updates via a push notification using Spontit",
  "nodes": [
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        810,
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
        1010,
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
      "name": "Spontit",
      "type": "n8n-nodes-base.spontit",
      "position": [
        1210,
        340
      ],
      "parameters": {
        "content": "=Hey! The temperature outside is {{$node[\"OpenWeatherMap\"].json[\"main\"][\"temp\"]}}\u00b0C.",
        "additionalFields": {
          "pushTitle": "Today's Weather Update"
        }
      },
      "credentials": {
        "spontitApi": "spontit"
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
            "node": "Spontit",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
