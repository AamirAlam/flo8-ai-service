# Receive updates on a subscriber added in ConvertKit

**[View Template](https://n8n.io/workflows/644-/)**  **Published Date:** 09/10/2020  **Created By:** ghagrawal17  **Categories:**   

## Template Description



## Template JSON

```
{
  "id": "28",
  "name": "Receive updates when a subscriber is added through a form in ConvertKit",
  "nodes": [
    {
      "name": "ConvertKit Trigger",
      "type": "n8n-nodes-base.convertKitTrigger",
      "position": [
        690,
        260
      ],
      "webhookId": "55336480-7be1-4432-8fc8-d860572c1c18",
      "parameters": {
        "event": "formSubscribe",
        "formId": 1657198
      },
      "credentials": {
        "convertKitApi": "convertkit"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {}
}
```
