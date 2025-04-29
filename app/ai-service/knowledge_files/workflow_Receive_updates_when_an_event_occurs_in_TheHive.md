# Receive updates when an event occurs in TheHive

**[View Template](https://n8n.io/workflows/810-/)**  **Published Date:** 12/03/2020  **Created By:** ghagrawal17  **Categories:**   

## Template Description



## Template JSON

```
{
  "id": "161",
  "name": "Receive updates when an event occurs in TheHive",
  "nodes": [
    {
      "name": "TheHive Trigger",
      "type": "n8n-nodes-base.theHiveTrigger",
      "position": [
        690,
        220
      ],
      "webhookId": "bef3fea8-2d68-43e8-9061-6c17c1059c86",
      "parameters": {
        "events": [
          "*"
        ]
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {}
}
```
