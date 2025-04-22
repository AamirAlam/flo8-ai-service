# Get execute command data and transfer to JSON

**[View Template](https://n8n.io/workflows/156-/)**  **Published Date:** 11/02/2019  **Created By:** jan  **Categories:**   

## Template Description

Shows how it is possible to use the data of a command line tool which returns JSON.

Example shows how:
to bring data in flow
to use data directly in a node

Note that the 'execute command' node is not available on n8n Cloud.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Execute Command",
      "type": "n8n-nodes-base.executeCommand",
      "position": [
        600,
        350
      ],
      "parameters": {
        "command": "echo \"{ \\\"value1\\\": true, \\\"value2\\\": 1 }\""
      },
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        800,
        450
      ],
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{JSON.parse($node[\"Execute Command\"].data[\"stdout\"]).value1}}",
              "value2": true
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "To Flow Data",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        800,
        250
      ],
      "parameters": {
        "functionCode": "item = JSON.parse(item.stdout);\nreturn item;"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Execute Command": {
      "main": [
        [
          {
            "node": "To Flow Data",
            "type": "main",
            "index": 0
          },
          {
            "node": "IF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
