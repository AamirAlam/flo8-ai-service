# Release a new version via Telegram bot command

**[View Template](https://n8n.io/workflows/1134-/)**  **Published Date:** 06/18/2021  **Created By:** ghagrawal17  **Categories:** `Development`  

## Template Description

This workflow allows you to release a new version via a Telegram bot command. This workflow can be used in your Continous Delivery pipeline.



Telegram Trigger node: This node will trigger the workflow when a message is sent to the bot. If you want to trigger the workflow via a different messaging platform or a service, replace the Telegram Trigger node with the Trigger node of that service.

IF node The IF node checks for the incoming command. If the command is not deploy, the IF node will return false, otherwise true.

Set node: This node extracts the value of the version from the Telegram message and sets the value. This value is used later in the workflow.

GitHub node: This node creates a new version release. It uses the version from the Set node to create the tag.

NoOp node: Adding this node is optional.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Telegram Trigger",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        460,
        320
      ],
      "webhookId": "4d8556a0-8fdf-4228-8ee2-3e3c72f5fc57",
      "parameters": {
        "updates": [
          "message"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        660,
        320
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"message\"][\"text\"]}}",
              "value2": "/deploy",
              "operation": "contains"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "GitHub",
      "type": "n8n-nodes-base.github",
      "position": [
        1060,
        220
      ],
      "parameters": {
        "owner": "n8n-io",
        "resource": "release",
        "releaseTag": "={{$json[\"version\"]}}",
        "repository": "n8n",
        "authentication": "oAuth2",
        "additionalFields": {}
      },
      "credentials": {
        "githubOAuth2Api": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        860,
        220
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "version",
              "value": "={{$json[\"message\"][\"text\"].split(' ')[1]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "NoOp",
      "type": "n8n-nodes-base.noOp",
      "position": [
        860,
        420
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
            "node": "Set",
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
    "Set": {
      "main": [
        [
          {
            "node": "GitHub",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Telegram Trigger": {
      "main": [
        [
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
