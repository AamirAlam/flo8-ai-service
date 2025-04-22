# Send daily weather updates to a phone number using the Vonage node

**[View Template](https://n8n.io/workflows/723-/)**  **Published Date:** 10/16/2020  **Created By:** ghagrawal17  **Categories:** `Utility` `Miscellaneous` `Communication`  

## Template Description



## Template JSON

```
{
  "id": "84",
  "name": "Send daily weather updates to a phone number using the Vonage node",
  "nodes": [
    {
      "name": "Vonage",
      "type": "n8n-nodes-base.vonage",
      "position": [
        770,
        260
      ],
      "parameters": {
        "to": "1234",
        "from": "Vonage APIs",
        "message": "=Hey! The temperature outside is {{$node[\"OpenWeatherMap\"].json[\"main\"][\"temp\"]}}\u00b0C.",
        "additionalFields": {}
      },
      "credentials": {
        "vonageApi": "vonage"
      },
      "typeVersion": 1
    },
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        370,
        260
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
        570,
        260
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
            "node": "Vonage",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
