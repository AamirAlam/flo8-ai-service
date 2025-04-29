# Receive updates when an event occurs in Asana

**[View Template](https://n8n.io/workflows/654-/)**  **Published Date:** 09/12/2020  **Created By:** ghagrawal17  **Categories:**   

## Template Description



## Template JSON

```
{
  "id": "47",
  "name": "Receive updates when an event occurs in Asana",
  "nodes": [
    {
      "name": "Asana-Trigger",
      "type": "n8n-nodes-base.asanaTrigger",
      "position": [
        1490,
        860
      ],
      "webhookId": "0de3b493-efb6-472c-9deb-80d28c89d28d",
      "parameters": {
        "resource": "Tweets",
        "workspace": "Engineering"
      },
      "credentials": {
        "asanaApi": "asana"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {}
}
```
