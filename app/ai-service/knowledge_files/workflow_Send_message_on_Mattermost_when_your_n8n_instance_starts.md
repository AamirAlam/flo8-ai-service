# Send message on Mattermost when your n8n instance starts

**[View Template](https://n8n.io/workflows/1058-/)**  **Published Date:** 04/28/2021  **Created By:** ghagrawal17  **Categories:** `Communication`  

## Template Description

This workflow allows you to receive a message on Mattermost when your n8n instance starts.



n8n Trigger node: The n8n Trigger node will trigger the workflow whenever the instance starts.

Mattermost node: This node will send a message on Mattermost, notifying you when n8n starts.

## Template JSON

```
{
  "nodes": [
    {
      "name": "n8n Trigger",
      "type": "n8n-nodes-base.n8nTrigger",
      "position": [
        450,
        200
      ],
      "parameters": {
        "events": [
          "init"
        ]
      },
      "typeVersion": 1
    },
    {
      "name": "Mattermost",
      "type": "n8n-nodes-base.mattermost",
      "position": [
        650,
        200
      ],
      "parameters": {
        "message": "=Your n8n instance started at {{$json[\"timestamp\"]}}",
        "channelId": "toyi3uoycf8rirtm7d5jm15sso",
        "attachments": [],
        "otherOptions": {}
      },
      "credentials": {
        "mattermostApi": "Mattermost Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "n8n Trigger": {
      "main": [
        [
          {
            "node": "Mattermost",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
