# Receive updates on an order created in Shopify

**[View Template](https://n8n.io/workflows/547-/)**  **Published Date:** 07/22/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Shopify Trigger node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "Shopify Trigger",
      "type": "n8n-nodes-base.shopifyTrigger",
      "position": [
        450,
        450
      ],
      "webhookId": "fd11b3d8-ff82-4902-89cc-c93b36ae38e7",
      "parameters": {
        "topic": "orders/create"
      },
      "credentials": {
        "shopifyApi": "shopify_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
