# Receive updates of the position of the ISS and add it to a table in TimescaleDB

**[View Template](https://n8n.io/workflows/917-/)**  **Published Date:** 02/02/2021  **Created By:** ghagrawal17  **Categories:** `Development` `Core Nodes` `Data & Storage`  

## Template Description

This workflow allows you to receive updates about the positiong of the ISS and add it to a table in TimescaleDB.



Cron node: The Cron node triggers the workflow every minute. You can configure the time based on your use-case.

HTTP Request node: This node makes an HTTP Request to an API that returns the position of the ISS. Based on your use-case you may want to fetch data from a different URL. Enter the URL in the URL field.

Set node: In the Set node we set the information that we need in the workflow. Since we only need the timestamp, latitude, and longitude we set this in the node. If you need other information, you can set them in this node.

TimescaleDB node: This node stores the information in a table named iss. You can use a different table as well.

## Template JSON

```
{
  "nodes": [
    {
      "name": "TimescaleDB",
      "type": "n8n-nodes-base.timescaleDb",
      "position": [
        1110,
        260
      ],
      "parameters": {
        "table": "iss",
        "columns": "latitude, longitude, timestamp"
      },
      "credentials": {
        "timescaleDb": "TimescaleDB"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        910,
        260
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "latitude",
              "value": "={{$json[\"0\"][\"latitude\"]}}"
            },
            {
              "name": "longitude",
              "value": "={{$json[\"0\"][\"longitude\"]}}"
            },
            {
              "name": "timestamp",
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
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        710,
        260
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
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        510,
        260
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
    }
  ],
  "connections": {
    "Set": {
      "main": [
        [
          {
            "node": "TimescaleDB",
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
