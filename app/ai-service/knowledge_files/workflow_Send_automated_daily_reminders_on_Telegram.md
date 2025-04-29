# Send automated daily reminders on Telegram

**[View Template](https://n8n.io/workflows/1387-/)**  **Published Date:** 01/08/2022  **Created By:** Nicholas Lewanowicz  **Categories:** `Communication` `HITL`  

## Template Description

A goal for 2022 is to write 1 thing I do each day. This workflow will automatically remind you on telegram to write something you did yesterday, optionally you can enable the second workflow which will allow you to reply to the message and have it recorded in a google sheet.

Note: Make sure to configure your Telegram credentials!

## Template JSON

```
{
  "id": 1,
  "name": "Daily Journal Reminder",
  "nodes": [
    {
      "name": "Morning reminder",
      "type": "n8n-nodes-base.cron",
      "notes": "Trigger very morning",
      "position": [
        220,
        60
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 6
            }
          ]
        }
      },
      "notesInFlow": true,
      "typeVersion": 1,
      "alwaysOutputData": true
    },
    {
      "name": "format reminder",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        460,
        60
      ],
      "parameters": {
        "functionCode": "\n// Creates message with todays date\nconst today = new Date()\nconst yesterday = new Date(today)\n\nyesterday.setDate(yesterday.getDate() - 1)\nconst message = `What did you do: ${yesterday.toISOString().split('T')[0]}`\n\nreturn {message};"
      },
      "typeVersion": 1
    },
    {
      "name": "Send journal reminder",
      "type": "n8n-nodes-base.telegram",
      "position": [
        700,
        60
      ],
      "parameters": {
        "text": "={{$node[\"format reminder\"].json[\"message\"]}}",
        "chatId": "666884239",
        "additionalFields": {}
      },
      "credentials": {},
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "format reminder": {
      "main": [
        [
          {
            "node": "Send journal reminder",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Morning reminder": {
      "main": [
        [
          {
            "node": "format reminder",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
