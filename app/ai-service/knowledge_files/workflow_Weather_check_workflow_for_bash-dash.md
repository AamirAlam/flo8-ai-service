# Weather check workflow for bash-dash

**[View Template](https://n8n.io/workflows/986-/)**  **Published Date:** 03/17/2021  **Created By:** Jan Oberhauser  **Categories:** `Utility` `Miscellaneous`  

## Template Description

This workflow returns the current weather at a predefined or given city and returns it so that it can be displayed with bash-dash.



By default does it return the weather in Berlin if no city got defined. That default can be changed in the "Set City" node.

Example usage:
\- weather london

Example bash-dash config:
commands[weather]="http://localhost:5678/webhook/weather"


## Template JSON

```
{
  "nodes": [
    {
      "name": "OpenWeatherMap",
      "type": "n8n-nodes-base.openWeatherMap",
      "position": [
        900,
        300
      ],
      "parameters": {
        "cityName": "={{ $json[\"city\"] }}",
        "language": "en"
      },
      "credentials": {
        "openWeatherMapApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Webhook GET",
      "type": "n8n-nodes-base.webhook",
      "position": [
        500,
        300
      ],
      "webhookId": "a31f0bbd-a583-470e-9a1e-29a9ce778122",
      "parameters": {
        "path": "weather",
        "options": {
          "responsePropertyName": "data"
        },
        "responseMode": "lastNode"
      },
      "typeVersion": 1
    },
    {
      "name": "Set City",
      "type": "n8n-nodes-base.set",
      "position": [
        700,
        300
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "city",
              "value": "={{ $json[\"query\"][\"parameter\"] || 'berlin,de' }}"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "Create Response",
      "type": "n8n-nodes-base.set",
      "position": [
        1100,
        300
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "data",
              "value": "=It has {{$json[\"main\"][\"temp\"]}}\\xE2\\x84\\x83  and feels like {{$json[\"main\"][\"feels_like\"]}}\\xE2\\x84\\x83  in {{$json[\"name\"]}}"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Set City": {
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
    "Webhook GET": {
      "main": [
        [
          {
            "node": "Set City",
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
            "node": "Create Response",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
