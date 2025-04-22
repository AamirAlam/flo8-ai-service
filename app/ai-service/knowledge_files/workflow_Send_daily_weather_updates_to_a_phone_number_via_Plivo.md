# Send daily weather updates to a phone number via Plivo

**[View Template](https://n8n.io/workflows/1005-/)**  **Published Date:** 03/26/2021  **Created By:** ghagrawal17  **Categories:** `Utility` `Miscellaneous` `Development` `Communication`  

## Template Description

This workflow allows you to send daily weather updates via an SMS message using the Plivo node.



Cron node: The Cron node will trigger the workflow daily at 9 AM.

OpenWeatherMap node: This node will return data about the current weather in Berlin. To get the weather updates for your city, you can enter the name of your city instead.

Plivo node: This node will send an SMS with the weather update, which was sent by the previous node.


## Template JSON

```
{
  "nodes": [
    {
      "name": "Plivo",
      "type": "n8n-nodes-base.plivo",
      "position": [
        1030,
        400
      ],
      "parameters": {
        "message": "=Hey! The temperature outside is {{$node[\"OpenWeatherMap\"].json[\"main\"][\"temp\"]}}\u00b0C."
      },
      "credentials": {
        "plivoApi": "Plivo API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "OpenWeatherMap",
      "type": "n8n-nodes-base.openWeatherMap",
      "position": [
        830,
        400
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
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        630,
        400
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
    }
  ],
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
            "node": "Plivo",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
