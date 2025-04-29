# Add a check condition for a loop in n8n

**[View Template](https://n8n.io/workflows/1130-/)**  **Published Date:** 06/17/2021  **Created By:** ghagrawal17  **Categories:** `Marketing`  

## Template Description

This workflow demonstrates the use of $runIndex expression. It demonstrates how the expression can be used to avoid an infinite loop.

The workflow will create 5 Tweets with the content 'Hello from n8n!'.

You can use this workflow by replacing the Twitter node with any other node(s) and updating the condition in the IF node.

## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        600,
        150
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$runIndex}}",
              "value2": 4
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "NoOp",
      "type": "n8n-nodes-base.noOp",
      "position": [
        750,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Twitter",
      "type": "n8n-nodes-base.twitter",
      "position": [
        440,
        300
      ],
      "parameters": {
        "text": "Hello from n8n!",
        "additionalFields": {}
      },
      "credentials": {
        "twitterOAuth1Api": "Dummy Account"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "Twitter",
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
    "Twitter": {
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
            "node": "Twitter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
