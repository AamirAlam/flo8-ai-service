# Send daily weather updates via push notification

**[View Template](https://n8n.io/workflows/740-/)**  **Published Date:** 10/26/2020  **Created By:** ghagrawal17  **Categories:** `Utility` `Miscellaneous` `Communication`  

## Template Description



## Template JSON

```
{
  "id": "91",
  "name": "Send daily weather updates via a push notification",
  "nodes": [
    {
      "name": "Pushover",
      "type": "n8n-nodes-base.pushover",
      "position": [
        970,
        300
      ],
      "parameters": {
        "message": "=Hey! The temperature outside is {{$node[\"OpenWeatherMap\"].json[\"main\"][\"temp\"]}}\u00b0C.",
        "userKey": "",
        "priority": 0,
        "additionalFields": {
          "title": "Today's Weather"
        }
      },
      "credentials": {
        "pushoverApi": "pushover"
      },
      "typeVersion": 1
    },
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        570,
        300
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
        770,
        300
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
            "node": "Pushover",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
