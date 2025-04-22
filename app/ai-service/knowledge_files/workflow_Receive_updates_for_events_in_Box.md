# Receive updates for events in Box

**[View Template](https://n8n.io/workflows/560-/)**  **Published Date:** 07/27/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Box Trigger node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "Box Trigger",
      "type": "n8n-nodes-base.boxTrigger",
      "position": [
        1027,
        368
      ],
      "webhookId": "0e56bb0c-8e81-42de-a902-c0ab31834bd8",
      "parameters": {
        "events": [
          "FOLDER.MOVED",
          "FOLDER.DOWNLOADED"
        ],
        "targetId": "118847708963",
        "targetType": "file"
      },
      "credentials": {
        "boxOAuth2Api": "box_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
