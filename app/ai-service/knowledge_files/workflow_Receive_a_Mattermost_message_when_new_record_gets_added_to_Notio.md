# Receive a Mattermost message when new record gets added to Notion

**[View Template](https://n8n.io/workflows/1089-/)**  **Published Date:** 05/21/2021  **Created By:** ghagrawal17  **Categories:** `Communication`  

## Template Description

This workflow allows you to receive a Mattermost message when meeting notes get added to the Notion.

Prerequisites
Create a table in Notion similar to this: Meeting Notes
Follow the steps mentioned in the documentation, to create credentials for the Notion Trigger node.
Create create credentials for Mattermost.



Notion Trigger: The Notion Trigger node will trigger the workflow when new data gets added to Notion.

IF node: This node will check if the notes belong to the team Marketing. If the team is Marketing the node will true, otherwise false.

Mattermost node: This node will send a message about the new data in the channel 'Marketing' in Mattermost. If you have a different channel, use that instead. You can even replace the Mattermost node with nodes of other messaging platforms, like Slack, Telegram, Discord, etc.

NoOp node: Adding this node here is optional, as the absence of this node won't make a difference to the functioning of the workflow.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Notion Trigger",
      "type": "n8n-nodes-base.notionTrigger",
      "position": [
        270,
        350
      ],
      "parameters": {
        "event": "pageAddedToDatabase",
        "pollTimes": {
          "item": [
            {
              "mode": "everyHour"
            }
          ]
        },
        "databaseId": "6ea34c0d-67e8-4614-ad5c-68c665a34763"
      },
      "credentials": {
        "notionApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        470,
        350
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"Team\"]}}",
              "value2": "Marketing"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Mattermost",
      "type": "n8n-nodes-base.mattermost",
      "position": [
        670,
        250
      ],
      "parameters": {
        "message": "=New meeting notes were added.\nAgenda: {{$json[\"Agenda\"]}}\nDate: {{$json[\"Date\"][\"start\"]}}\nLink: https://notion.so/{{$json[\"id\"].replace(/-/g,'')}}",
        "channelId": "64cae1bh6pggtcupfd4ztwby4r",
        "attachments": [],
        "otherOptions": {}
      },
      "credentials": {
        "mattermostApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "NoOp",
      "type": "n8n-nodes-base.noOp",
      "position": [
        668,
        495
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
            "node": "Mattermost",
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
    "Notion Trigger": {
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
