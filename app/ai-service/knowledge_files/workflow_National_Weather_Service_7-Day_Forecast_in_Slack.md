# National Weather Service 7-Day Forecast in Slack

**[View Template](https://n8n.io/workflows/2947-/)**  **Published Date:** 02/19/2025  **Created By:** Alex Kim  **Categories:** `Development` `Core Nodes` `Communication` `HITL`  

## Template Description

Weather via Slack 🌦️💬

Overview
This workflow provides real-time weather updates via Slack using a custom Slack command:  
/weather [cityname]

Users can type this command in Slack (e.g., /weather New York), and the workflow will fetch and post the latest forecast, including temperature, wind conditions, and a short weather summary.

While this workflow is designed for Slack, users can modify it to send weather updates via email, Discord, Microsoft Teams, or any other communication platform.

How It Works
Webhook Trigger – The workflow is triggered when a user runs /weather [cityname] in Slack.
Geocoding with OpenStreetMap – The city name is converted into latitude and longitude coordinates.
Weather Data from NOAA – The coordinates are used to retrieve detailed weather data from the National Weather Service (NWS) API.
Formatted Weather Report – The workflow extracts relevant weather details, such as:
   Temperature (°F/°C)
   Wind speed and direction
   Short forecast summary
Slack Notification – The weather forecast is posted back to the Slack channel in a structured format.

Requirements
A custom Slack app with:
  The ability to create a Slash Command (/weather)
  OAuth permissions to post messages in Slack
An n8n instance to host and execute the workflow

Customization
Replace Slack messaging with email, Discord, Microsoft Teams, Telegram, or another service.
Modify the weather data format for different output preferences.
Set up scheduled weather updates for specific locations.

Use Cases
Instantly check the weather for any location directly in Slack.
Automate weather reports for team members or projects.
Useful for remote teams, outdoor event planning, or general weather tracking.

Setup Instructions
Create a custom Slack app:
   Go to api.slack.com/apps and create a new app.
   Add a Slash Command (/weather) with the webhook URL from n8n.
   Enable OAuth scopes for sending messages.
Deploy the webhook – Ensure it can receive and process Slack commands.
Run the workflow – Type /weather [cityname] in Slack and receive instant weather updates.


## Template JSON

```
{
  "id": "B6UHILmjPWa7ViQ4",
  "meta": {
    "instanceId": "ecc960f484e18b0e09045fd93acf0d47f4cfff25cc212ea348a08ac3aae81850",
    "templateCredsSetupCompleted": true
  },
  "name": "Weather via Slack",
  "tags": [
    {
      "id": "2KlkHxhULPP42BS6",
      "name": "App 72",
      "createdAt": "2025-02-19T21:15:27.390Z",
      "updatedAt": "2025-02-19T21:15:27.390Z"
    },
    {
      "id": "aw8suPYTKfXDtMZl",
      "name": "Utility",
      "createdAt": "2025-02-10T14:41:49.045Z",
      "updatedAt": "2025-02-10T14:41:49.045Z"
    }
  ],
  "nodes": [
    {
      "id": "9aea370b-7eb9-4742-9663-6628513e4de3",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        -340,
        -300
      ],
      "webhookId": "41a60a4f-66d0-433b-aa43-b225dffa6761",
      "parameters": {
        "path": "slack1",
        "options": {},
        "httpMethod": "POST"
      },
      "typeVersion": 2
    },
    {
      "id": "c982487f-076a-48e8-9a35-78e8fbfb8936",
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "position": [
        560,
        -300
      ],
      "webhookId": "4840f197-e116-4ef5-9372-0abd063e4aad",
      "parameters": {
        "text": "={{\n  JSON.parse($node[\"NWS1\"].json.data).properties.periods\n  .map(period => \n    `*${period.name}*\\n` +\n    `Temp: ${period.temperature}\u00b0${period.temperatureUnit}\\n` +\n    `Wind: ${period.windSpeed} ${period.windDirection}\\n` +\n    `Forecast: ${period.shortForecast}`\n  )\n  .join(\"\\n\\n\")\n}}\n",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "list",
          "value": "C0889718P8S",
          "cachedResultName": "n8n"
        },
        "otherOptions": {},
        "authentication": "oAuth2"
      },
      "credentials": {
        "slackOAuth2Api": {
          "id": "GSiEiuKBz8GR5qiD",
          "name": "AlexK Slack account"
        }
      },
      "typeVersion": 2.3
    },
    {
      "id": "7d42112a-0590-4a09-ba0e-dbdf1eddccf2",
      "name": "OpenStreetMap",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -100,
        -300
      ],
      "parameters": {
        "url": "https://nominatim.openstreetmap.org/search",
        "options": {
          "response": {
            "response": {
              "fullResponse": true
            }
          }
        },
        "sendQuery": true,
        "sendHeaders": true,
        "queryParameters": {
          "parameters": [
            {
              "name": "q",
              "value": "={{ $('Webhook').item.json.body.text }}"
            },
            {
              "name": "format",
              "value": "json"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "User-Agent",
              "value": "alexk1919 (alex@alexk1919.com)"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "565a0123-9059-4e6e-be97-96e0875c1b84",
      "name": "NWS",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        120,
        -300
      ],
      "parameters": {
        "url": "=https://api.weather.gov/points/{{ $json.body[0].lat }},{{ $json.body[0].lon }}",
        "options": {
          "response": {
            "response": {
              "fullResponse": true
            }
          }
        },
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "User-Agent",
              "value": "alexk1919 (alex@alexk1919.com)"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "3505e6c2-6e66-4abd-a1bb-75a1d8fc9a08",
      "name": "NWS1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        340,
        -300
      ],
      "parameters": {
        "url": "=https://api.weather.gov/gridpoints/{{$json[\"data\"] ? JSON.parse($json[\"data\"]).properties.gridId : \"\"}}\n/{{$json[\"data\"] ? JSON.parse($json[\"data\"]).properties.gridX : \"\"}}\n,{{$json[\"data\"] ? JSON.parse($json[\"data\"]).properties.gridY : \"\"}}\n/forecast",
        "options": {
          "response": {
            "response": {
              "fullResponse": true
            }
          }
        },
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "User-Agent",
              "value": "alexk1919 (alex@alexk1919.com)"
            }
          ]
        }
      },
      "typeVersion": 4.2
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "4244c90f-02e9-42fc-9873-3f8074f6ecf4",
  "connections": {
    "NWS": {
      "main": [
        [
          {
            "node": "NWS1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "NWS1": {
      "main": [
        [
          {
            "node": "Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack": {
      "main": [
        []
      ]
    },
    "Webhook": {
      "main": [
        [
          {
            "node": "OpenStreetMap",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenStreetMap": {
      "main": [
        [
          {
            "node": "NWS",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
