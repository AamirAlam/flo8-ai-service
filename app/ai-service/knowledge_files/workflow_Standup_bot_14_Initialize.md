# Standup bot (1/4): Initialize

**[View Template](https://n8n.io/workflows/1472-/)**  **Published Date:** 02/18/2022  **Created By:** Jonathan  **Categories:**   

## Template Description

This is the first of 4 workflows for a Mattermost Standup Bot. This workflow will create a default configuration file.

You can set the default configuration in the Set node (Use Default Config) the values are:

config.slashCmdToken - The token Mattermost provides when you make a new Slash Command
config.mattermostBaseUrl - The base URL for your Mattermost instance
config.botUserToken - The User token for your Mattermost bot
config.n8nWebhookUrl - The URL for your "Action from MM" webhook in the "Standup Bot - Worker" workflow
config.botUserId - The UserID for your Mattermost Bot user

The config file is saved under /home/node/.n8n/standup-bot-config.json

This workflow only needs to be run once manually as part of the setup .

## Template JSON

```
{
  "id": 111,
  "name": "Standup Bot - Initialize",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        240,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Write Binary File",
      "type": "n8n-nodes-base.writeBinaryFile",
      "position": [
        880,
        300
      ],
      "parameters": {
        "fileName": "/home/node/.n8n/standup-bot-config.json"
      },
      "typeVersion": 1
    },
    {
      "name": "Move Binary Data",
      "type": "n8n-nodes-base.moveBinaryData",
      "position": [
        660,
        300
      ],
      "parameters": {
        "mode": "jsonToBinary",
        "options": {
          "encoding": "utf8",
          "fileName": "standup-bot-config.json"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Use Default Config",
      "type": "n8n-nodes-base.set",
      "position": [
        440,
        300
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "config.slashCmdToken",
              "value": "xxxxx"
            },
            {
              "name": "config.mattermostBaseUrl",
              "value": "https://mattermost.yourdomain.tld"
            },
            {
              "name": "config.botUserToken",
              "value": "xxxxx"
            },
            {
              "name": "config.n8nWebhookUrl",
              "value": "https://n8n.yourdomain.tld/webhook/standup-bot/action/f6f9b174745fa4651f750c36957d674c"
            },
            {
              "name": "config.botUserId",
              "value": "xxxxx"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Move Binary Data": {
      "main": [
        [
          {
            "node": "Write Binary File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Use Default Config": {
      "main": [
        [
          {
            "node": "Move Binary Data",
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
            "node": "Use Default Config",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
