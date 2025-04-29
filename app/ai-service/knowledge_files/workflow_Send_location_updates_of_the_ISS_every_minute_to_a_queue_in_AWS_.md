# Send location updates of the ISS every minute to a queue in AWS SQS

**[View Template](https://n8n.io/workflows/1047-/)**  **Published Date:** 04/20/2021  **Created By:** ghagrawal17  **Categories:** `Development` `Core Nodes` `Communication`  

## Template Description

This workflow allows you to send position updates of the ISS every minute to a queue using the AWS SQS node.



Cron node: The Cron node will trigger the workflow every minute.

HTTP Request node: This node will make a GET request to the API https://api.wheretheiss.at/v1/satellites/25544/positions to fetch the position of the ISS. This information gets passed on to the next node in the workflow.

Set node: We will use the Set node to ensure that only the data that we set in this node gets passed on to the next nodes in the workflow.

AWS SQS: This node will send the data from the previous node to the iss-position queue. If you have created a queue with a different one, you can use that queue instead.

## Template JSON

```
{
  "nodes": [
    {
      "name": "AWS SQS",
      "type": "n8n-nodes-base.awsSqs",
      "position": [
        1050,
        360
      ],
      "parameters": {
        "queue": "",
        "options": {}
      },
      "credentials": {
        "aws": "AWS SQS Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        850,
        360
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "Latitude",
              "value": "={{$node[\"HTTP Request\"].json[\"0\"][\"latitude\"]}}"
            },
            {
              "name": "Longitude",
              "value": "={{$node[\"HTTP Request\"].json[\"0\"][\"longitude\"]}}"
            },
            {
              "name": "Timestamp",
              "value": "={{$node[\"HTTP Request\"].json[\"0\"][\"timestamp\"]}}"
            }
          ],
          "string": [
            {
              "name": "Name",
              "value": "={{$node[\"HTTP Request\"].json[\"0\"][\"name\"]}}"
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
        650,
        360
      ],
      "parameters": {
        "url": "https://api.wheretheiss.at/v1/satellites/25544/positions",
        "options": {},
        "queryParametersUi": {
          "parameter": [
            {
              "name": "timestamps",
              "value": "={{Date.now();}}"
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
        450,
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
    }
  ],
  "connections": {
    "Set": {
      "main": [
        [
          {
            "node": "AWS SQS",
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
