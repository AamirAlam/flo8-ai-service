# Send the astronomy picture of the day daily to a Telegram channel

**[View Template](https://n8n.io/workflows/828-/)**  **Published Date:** 12/15/2020  **Created By:** ghagrawal17  **Categories:** `Communication` `HITL` `Miscellaneous`  

## Template Description



This is a workflow that sends daily astronomy picture of the day using the NASA node to a channel on Telegram.

Cron node: The Cron node triggers the workflow daily at 8 PM. You can update the time in the Cron node to trigger the workflow at your desired time.

NASA node: After the Cron node triggers the workflow, the NASA node fetches the Astronomy Picture of the Day from the NASA API. You can also get the binary file of the image. Toggle Download Image to true to get the file.

Telegram node: The Telegram node sends the image to a Telegram channel.

If you want to share the image on another platform, you can replace the Telegram node with the node of that platform. For example, if you want to post the image on a channel on Slack, replace the Telegram node with the Slack node.

You can learn to build this workflow on the documentation page of the NASA node.

## Template JSON

```
{
  "id": "174",
  "name": "Send the Astronomy Picture of the day daily to a Telegram channel",
  "nodes": [
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        450,
        300
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 20
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "NASA",
      "type": "n8n-nodes-base.nasa",
      "position": [
        650,
        300
      ],
      "parameters": {
        "download": false,
        "additionalFields": {}
      },
      "credentials": {
        "nasaApi": "NASA"
      },
      "typeVersion": 1
    },
    {
      "name": "Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        850,
        300
      ],
      "parameters": {
        "file": "={{$node[\"NASA\"].json[\"url\"]}}",
        "chatId": "-485365454",
        "operation": "sendPhoto",
        "additionalFields": {
          "caption": "={{$node[\"NASA\"].json[\"title\"]}}"
        }
      },
      "credentials": {
        "telegramApi": "Telegram n8n bot"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Cron": {
      "main": [
        [
          {
            "node": "NASA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "NASA": {
      "main": [
        [
          {
            "node": "Telegram",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
