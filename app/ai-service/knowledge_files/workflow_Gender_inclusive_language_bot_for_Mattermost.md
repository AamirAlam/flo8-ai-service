# Gender inclusive language bot for Mattermost

**[View Template](https://n8n.io/workflows/982-/)**  **Published Date:** 03/15/2021  **Created By:** Lorena  **Categories:** `Communication`  

## Template Description

This workflow ensures gender inclusive language in Mattermost channels. If someone addresses the group with “guys” or “gals”, a bot promptly replies with: "May I suggest “folks” or “y'all”? We use gender inclusive language here. 😄".

Webhook node**: triggers the workflow when a new message is posted in Mattermost.
IF node**: verifies if the message includes the words "guys" or "gals". If false, it does not take any action. If true, it triggers the Mattermost node.
Mattermost node**: posts the language warning message in the Mattermost channel.


## Template JSON

```
{
  "id": "18",
  "name": "Gender Inclusive Language",
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        150,
        450
      ],
      "parameters": {
        "path": "webhook",
        "options": {},
        "httpMethod": "POST"
      },
      "typeVersion": 1
    },
    {
      "name": "Mattermost1",
      "type": "n8n-nodes-base.mattermost",
      "position": [
        550,
        300
      ],
      "parameters": {
        "message": "May I suggest \"folks\" or \u201cy'all\u201d? We use gender inclusive language here. \ud83d\ude04",
        "channelId": "={{$node[\"Webhook\"].json[\"body\"][\"channel_id\"]}}",
        "attachments": [],
        "otherOptions": {}
      },
      "credentials": {
        "mattermostApi": "n8n Mattermost - Bot"
      },
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        340,
        450
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Webhook\"].json[\"body\"][\"text\"]}}",
              "value2": "guys",
              "operation": "contains"
            },
            {
              "value1": "={{$node[\"Webhook\"].json[\"body\"][\"text\"]}}",
              "value2": "Guys",
              "operation": "contains"
            },
            {
              "value1": "={{$node[\"Webhook\"].json[\"body\"][\"text\"]}}",
              "value2": "bros",
              "operation": "contains"
            },
            {
              "value1": "={{$node[\"Webhook\"].json[\"body\"][\"text\"]}}",
              "value2": "Bros",
              "operation": "contains"
            },
            {
              "value1": "={{$node[\"Webhook\"].json[\"body\"][\"text\"]}}",
              "value2": "dudes",
              "operation": "contains"
            },
            {
              "value1": "={{$node[\"Webhook\"].json[\"body\"][\"text\"]}}",
              "value2": "Dudes",
              "operation": "contains"
            },
            {
              "value1": "={{$node[\"Webhook\"].json[\"body\"][\"text\"]}}",
              "value2": "gals",
              "operation": "contains"
            },
            {
              "value1": "={{$node[\"Webhook\"].json[\"body\"][\"text\"]}}",
              "value2": "Gals",
              "operation": "contains"
            }
          ]
        },
        "combineOperation": "any"
      },
      "typeVersion": 1
    },
    {
      "name": "NoOp",
      "type": "n8n-nodes-base.noOp",
      "position": [
        550,
        550
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "Mattermost1",
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
    "Webhook": {
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
