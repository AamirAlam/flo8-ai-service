# Check for preview for a link 

**[View Template](https://n8n.io/workflows/935-/)**  **Published Date:** 02/11/2021  **Created By:** ghagrawal17  **Categories:** `Development`  

## Template Description

This workflow allows you to check for preview for a link and return the preview if it exists.



Peekalink node: This node checks if a preview is available for a URL or not. If a preivew is available the node returns true, otherwise false.

IF node: The IF node checks the output from the previous node. If the condition is true the node connected to the true branch is executed. If the condition is false the node connected to the false branch is executed.

Peekalink1 node: This node will fetch the preview of the URL. Based on your use-case, you can connect the Slack node, Mattermost node etc. to get the response on these platforms.

NoOp node: Adding this node here is optional, as the absence of this node won't make a difference to the functioning of the workflow. We've added this as it can sometimes help others with a better understanding of the workflow, visually.

## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        310,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Peekalink",
      "type": "n8n-nodes-base.peekalink",
      "position": [
        510,
        300
      ],
      "parameters": {
        "url": "https://n8n1.io",
        "operation": "isAvailable"
      },
      "credentials": {
        "peekalinkApi": "Peekalink API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        710,
        300
      ],
      "parameters": {
        "conditions": {
          "string": [],
          "boolean": [
            {
              "value1": "={{$json[\"isAvailable\"]}}",
              "value2": true
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Peekalink1",
      "type": "n8n-nodes-base.peekalink",
      "position": [
        910,
        200
      ],
      "parameters": {
        "url": "={{$node[\"Peekalink\"].parameter[\"url\"]}}"
      },
      "credentials": {
        "peekalinkApi": "Peekalink API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "NoOp",
      "type": "n8n-nodes-base.noOp",
      "position": [
        910,
        400
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "Peekalink1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "NoOp",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Peekalink": {
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
            "node": "Peekalink",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
