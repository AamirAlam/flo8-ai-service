# Send daily weather updates via a notification in Line

**[View Template](https://n8n.io/workflows/773-/)**  **Published Date:** 11/11/2020  **Created By:** ghagrawal17  **Categories:** `Utility` `Miscellaneous` `Communication`  

## Template Description



## Template JSON

```
{
  "id": "114",
  "name": "Send daily weather updates via a message in Line",
  "nodes": [
    {
      "name": "Line",
      "type": "n8n-nodes-base.line",
      "position": [
        890,
        380
      ],
      "parameters": {
        "message": "=Hey! The temperature outside is {{$node[\"OpenWeatherMap\"].json[\"main\"][\"temp\"]}}\u00b0C.",
        "additionalFields": {}
      },
      "credentials": {
        "lineNotifyOAuth2Api": "line-credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        490,
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
      "name": "OpenWeatherMap",
      "type": "n8n-nodes-base.openWeatherMap",
      "position": [
        690,
        380
      ],
      "parameters": {
        "cityName": "berlin"
      },
      "credentials": {
        "openWeatherMapApi": "owm"
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
            "node": "Line",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
