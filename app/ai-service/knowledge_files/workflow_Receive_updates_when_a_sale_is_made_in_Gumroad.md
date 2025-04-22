# Receive updates when a sale is made in Gumroad

**[View Template](https://n8n.io/workflows/650-/)**  **Published Date:** 09/10/2020  **Created By:** ghagrawal17  **Categories:**   

## Template Description



## Template JSON

```
{
  "id": "34",
  "name": "Receive updates when a sale is made in Gumroad",
  "nodes": [
    {
      "name": "Gumroad Trigger",
      "type": "n8n-nodes-base.gumroadTrigger",
      "position": [
        1310,
        700
      ],
      "webhookId": "d72f9547-0530-4733-9e8b-3e3b1beec2eb",
      "parameters": {
        "resource": "sale"
      },
      "credentials": {
        "gumroadApi": "gumroad"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {}
}
```
