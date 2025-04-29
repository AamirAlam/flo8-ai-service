# n8n Nodemation basic - getting started on the workflow canvas (1/3)

**[View Template](https://n8n.io/workflows/18-/)**  **Published Date:** 09/16/2019  **Created By:** sven  **Categories:**   

## Template Description

In this video I will show you the workflow canvas and how to use nodes by building your first simple workflow.

> Videotuturial on Youtube



## Template JSON

```
{
  "id": "5",
  "name": "testworkflow",
  "nodes": [
    {
      "name": "FunctionItem",
      "type": "n8n-nodes-base.functionItem",
      "color": "#067325",
      "position": [
        860,
        680
      ],
      "parameters": {
        "functionCode": "item.myVariable = 1;\nitem.myVariable2 = \"this is exciting\";\nreturn item;"
      },
      "typeVersion": 1
    },
    {
      "name": "2 hours Interval",
      "type": "n8n-nodes-base.interval",
      "color": "#FF2A00",
      "notes": "It is the 4 hours interval in which this node gets executed",
      "position": [
        630,
        680
      ],
      "parameters": {
        "unit": "hours",
        "interval": 2
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        1040,
        680
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "data",
              "value": "={{$node[\"FunctionItem\"].data[\"myVariable2\"]}}"
            }
          ]
        },
        "keepOnlySet": true
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "FunctionItem": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "2 hours Interval": {
      "main": [
        [
          {
            "node": "FunctionItem",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
