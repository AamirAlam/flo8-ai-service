# Receive updates when an event occurs in Taiga

**[View Template](https://n8n.io/workflows/686-/)**  **Published Date:** 09/21/2020  **Created By:** ghagrawal17  **Categories:**   

## Template Description



## Template JSON

```
{
  "id": "70",
  "name": "Receive updates when an event occurs in Taiga",
  "nodes": [
    {
      "name": "Taiga Trigger",
      "type": "n8n-nodes-base.taigaTrigger",
      "position": [
        690,
        260
      ],
      "webhookId": "53939c3e-7dc6-4fdf-94d8-d29f92f8fa12",
      "parameters": {
        "projectId": 385605
      },
      "credentials": {
        "taigaCloudApi": "taiga"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {}
}
```
