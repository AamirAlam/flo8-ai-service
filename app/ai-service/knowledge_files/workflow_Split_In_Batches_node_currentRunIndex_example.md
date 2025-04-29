# Split In Batches node currentRunIndex example

**[View Template](https://n8n.io/workflows/996-/)**  **Published Date:** 03/19/2021  **Created By:** ghagrawal17  **Categories:**   

## Template Description

This workflow demonstrates how to use currentRunIndex to get the running index.



Function node: This node generates mock data for the workflow. Replace it with the node whose data you want to split into batches.

SplitInBatches node: This node splits the data with the batch size equal to 1. Based on your use-case, set the value of the Batch Size.

IF node: This node checks the running index. If the running index equals 5 the node returns true and breaks the loop.
The node uses the expression {{$node["SplitInBatches"].context["currentRunIndex"];}}, which returns the running index.

Set node: This node prints a message Loop Ended. Based on your use-case, connect the false output of the IF node to the input of the node you want to execute if the condition is false.


## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        430,
        310
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Function",
      "type": "n8n-nodes-base.function",
      "position": [
        630,
        310
      ],
      "parameters": {
        "functionCode": "const newItems = [];\n\nfor (let i=0;i<10;i++) {\n  newItems.push({json:{i}});\n}\n\nreturn newItems;"
      },
      "typeVersion": 1
    },
    {
      "name": "SplitInBatches",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        830,
        310
      ],
      "parameters": {
        "options": {},
        "batchSize": 1
      },
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        1030,
        460
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$node[\"SplitInBatches\"].context[\"currentRunIndex\"];}}",
              "value2": 5,
              "operation": "equal"
            }
          ],
          "boolean": []
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        1230,
        360
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "Message",
              "value": "Loop Ended"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "SplitInBatches",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Function": {
      "main": [
        [
          {
            "node": "SplitInBatches",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "SplitInBatches": {
      "main": [
        [
          {
            "node": "IF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Function",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
