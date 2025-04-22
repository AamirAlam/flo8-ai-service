# Send a message on Mattermost when you get a reply in Emelia

**[View Template](https://n8n.io/workflows/1039-/)**  **Published Date:** 04/14/2021  **Created By:** ghagrawal17  **Categories:** `Communication`  

## Template Description

This workflow allows you to send a message on Mattermost when a lead replies to your email.



Emelia Trigger node: The Emelia Trigger node will trigger the workflow when a lead sends a reply to a campaign

Mattermost node: This node will send a message to the Leads channel in Mattermost with the information about the reply. Based on your use case, you may want to send the message to a different channel. You may even want to use a different service. Replace the node with the service where you want to send a message.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Mattermost",
      "type": "n8n-nodes-base.mattermost",
      "position": [
        650,
        200
      ],
      "parameters": {
        "message": "={{$json[\"contact\"][\"firstName\"]}} from {{$json[\"contact\"][\"company\"]}} has replied back to your campaign.",
        "channelId": "qx9yo1i9z3bg5qcy5a1oxnh69c",
        "attachments": [],
        "otherOptions": {}
      },
      "credentials": {
        "mattermostApi": "Mattermost Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Emelia Trigger",
      "type": "n8n-nodes-base.emeliaTrigger",
      "position": [
        450,
        200
      ],
      "webhookId": "f53bc370-a8cb-4748-8f81-be7ae9b94972",
      "parameters": {
        "events": [
          "replied"
        ],
        "campaignId": "6054d068b374b64365740101"
      },
      "credentials": {
        "emeliaApi": "Emelia API Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Emelia Trigger": {
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
