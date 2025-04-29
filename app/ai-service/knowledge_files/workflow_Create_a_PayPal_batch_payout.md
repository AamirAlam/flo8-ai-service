# Create a PayPal batch payout

**[View Template](https://n8n.io/workflows/438-/)**  **Published Date:** 06/30/2020  **Created By:** ivov  **Categories:** `Sales` `Finance & Accounting`  

## Template Description


                                                                  

## Template JSON

```
{
  "name": "",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        540,
        240
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "PayPal",
      "type": "n8n-nodes-base.payPal",
      "position": [
        730,
        240
      ],
      "parameters": {
        "senderBatchId": "123",
        "additionalFields": {}
      },
      "credentials": {
        "payPalApi": "paypal-credentials"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "PayPal",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
