# Receive updates of the position of the ISS every minute

**[View Template](https://n8n.io/workflows/880-/)**  **Published Date:** 01/07/2021  **Created By:** ghagrawal17  **Categories:** `Development` `Core Nodes`  

## Template Description

This workflow demonstrates the use of static data in n8n. The workflow is built on the concept of polling.



Cron node: The Cron node triggers the workflow every minute. You can configure the time based on your use-case.

HTTP Request node: This node makes an HTTP Request to an API that returns the position of the ISS.

Set node: In the Set node we set the information that we need in the workflow. Since we only need the timestamp, latitude, and longitude we set this in the node. If you need other information, you can set them in this node.

Function node: The Function node, checks if the incoming data is similar to the data that was returned in the previous execution or not. If the data is different the Function node returns this new node, otherwise, it returns a message 'No New Items'. The data is also stored as static data with the workflow.

Based on your use-case, you can build the workflow further. For example, you can use it send updates to Mattermost or Slack

## Template JSON

```
{
  "nodes": [
    {
      "name": "Function",
      "type": "n8n-nodes-base.function",
      "position": [
        1470,
        380
      ],
      "parameters": {
        "functionCode": "const new_items = [];\n// Get static data stored with the workflow\nconst data = this.getWorkflowStaticData(\"node\");\ndata.timestamp = data.timestamp || [];\nfor (var i = items.length - 1; i >= 0; i--) {\n// Check if data is already present\n  if (data.timestamp.includes(items[i].json.timestamp)) {\n    break;\n  } else {\n// if new data then add it to an array\n    new_items.push({\n      json: {\n        timestamp: items[i].json.timestamp,\n        latitude: items[i].json.latitude,\n        longitude: items[i].json.longitude\n      },\n    });\n  }\n}\ndata.timestamp = items.map((item) => item.json.timestamp);\n// Check if array is empty\nif (new_items.length === 0) {\n  return [{ json: { message: \"No new items\" } }];\n} else {\n// return new items if array is not empty\nconsole.log(new_items);\n  return new_items;\n}\n"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        1270,
        380
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
          "string": []
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
        1070,
        380
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
        870,
        380
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
            "node": "Function",
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
