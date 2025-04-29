# Receive updates when a billing plan is activated in PayPal

**[View Template](https://n8n.io/workflows/653-/)**  **Published Date:** 09/12/2020  **Created By:** ghagrawal17  **Categories:**   

## Template Description



## Template JSON

```
{
  "id": "46",
  "name": "Receive updates when a billing plan is activated in PayPal",
  "nodes": [
    {
      "name": "PayPal Trigger",
      "type": "n8n-nodes-base.payPalTrigger",
      "position": [
        1130,
        620
      ],
      "webhookId": "242a300e-b5a0-45a2-87bc-40def6fe56ef",
      "parameters": {
        "events": [
          "BILLING.PLAN.ACTIVATED"
        ]
      },
      "credentials": {
        "payPalApi": "paypal"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {}
}
```
