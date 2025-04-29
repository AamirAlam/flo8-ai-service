# Send location updates of the ISS every minute to a table in Google BigQuery

**[View Template](https://n8n.io/workflows/1049-/)**  **Published Date:** 04/21/2021  **Created By:** ghagrawal17  **Categories:** `Development` `Core Nodes` `Data & Storage`  

## Template Description

This workflow allows you to send position updates of the ISS every minute to a table in Google BigQuery.



Cron node: The Cron node will trigger the workflow every minute.

HTTP Request node: This node will make a GET request to the API https://api.wheretheiss.at/v1/satellites/25544/positions to fetch the position of the ISS. This information gets passed on to the next node in the workflow.

Set node: We will use the Set node to ensure that only the data that we set in this node gets passed on to the next nodes in the workflow.

Google BigQuery: This node will send the data from the previous node to the position table in Google BigQuery. If you have created a table with a different name, use that table instead.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Google BigQuery",
      "type": "n8n-nodes-base.googleBigQuery",
      "position": [
        1010,
        240
      ],
      "parameters": {
        "columns": "name, latitude, longitude, timestamp",
        "options": {},
        "tableId": "position",
        "datasetId": "iss",
        "projectId": "supple-cabinet-289219"
      },
      "credentials": {
        "googleBigQueryOAuth2Api": "BigQuery Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        810,
        240
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "latitude",
              "value": "={{$node[\"HTTP Request\"].json[\"0\"][\"latitude\"]}}"
            },
            {
              "name": "longitude",
              "value": "={{$node[\"HTTP Request\"].json[\"0\"][\"longitude\"]}}"
            },
            {
              "name": "timestamp",
              "value": "={{$node[\"HTTP Request\"].json[\"0\"][\"timestamp\"]}}"
            }
          ],
          "string": [
            {
              "name": "name",
              "value": "={{$json[\"0\"][\"name\"]}}"
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
        610,
        240
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
        410,
        240
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
            "node": "Google BigQuery",
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
