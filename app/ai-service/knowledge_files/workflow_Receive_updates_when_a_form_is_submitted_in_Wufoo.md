# Receive updates when a form is submitted in Wufoo

**[View Template](https://n8n.io/workflows/703-/)**  **Published Date:** 10/05/2020  **Created By:** ghagrawal17  **Categories:**   

## Template Description



## Template JSON

```
{
  "id": "78",
  "name": "Receive updates when a form is submitted in Wufoo",
  "nodes": [
    {
      "name": "Wufoo Trigger",
      "type": "n8n-nodes-base.wufooTrigger",
      "position": [
        1290,
        140
      ],
      "webhookId": "106376c5-b49c-412f-8463-4db23a23c057",
      "parameters": {
        "form": "n8n"
      },
      "credentials": {
        "wufooApi": "wufoo"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {}
}
```
