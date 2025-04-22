# Send location updates of the ISS to a topic in MQTT

**[View Template](https://n8n.io/workflows/1069-/)**  **Published Date:** 05/04/2021  **Created By:** ghagrawal17  **Categories:** `Development` `Core Nodes` `Communication`  

## Template Description

This workflow allows you to send position updates of the ISS every minute to a topic in MQTT using the MQTT node.



Cron node: The Cron node will trigger the workflow every minute.

HTTP Request node: This node will make a GET request to the API https://api.wheretheiss.at/v1/satellites/25544/positions to fetch the position of the ISS. This information gets passed on to the next node in the workflow.

Set node: We will use the Set node to ensure that only the data that we set in this node gets passed on to the next nodes in the workflow.

AWS SQS: This node will send the data from the previous node to the iss-position topic. If you have created a topic with a different one, you can use that topic instead.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        490,
        360
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        690,
        360
      ],
      "parameters": {
        "url": "https://api.wheretheiss.at/v1/satellites/25544/positions",
        "options": {},
        "queryParametersUi": {
          "parameter": [
            {
              "name": "timestamps",
              "value": "={{Date.now()}}"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        890,
        360
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "Name",
              "value": "={{$json[\"0\"][\"name\"]}}"
            },
            {
              "name": "Latitude",
              "value": "={{$json[\"0\"][\"latitude\"]}}"
            },
            {
              "name": "Longitude",
              "value": "={{$json[\"0\"][\"longitude\"]}}"
            },
            {
              "name": "Timestamp",
              "value": "={{$json[\"0\"][\"timestamp\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "MQTT",
      "type": "n8n-nodes-base.mqtt",
      "position": [
        1090,
        360
      ],
      "parameters": {
        "topic": "iss-position",
        "options": {}
      },
      "credentials": {
        "mqtt": "mqtt"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Set": {
      "main": [
        [
          {
            "node": "MQTT",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
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
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
