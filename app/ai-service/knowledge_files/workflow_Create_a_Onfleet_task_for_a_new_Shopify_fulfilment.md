# Create a Onfleet task for a new Shopify fulfilment

**[View Template](https://n8n.io/workflows/1531-/)**  **Published Date:** 03/16/2022  **Created By:** James Li  **Categories:** `Miscellaneous`  

## Template Description

Summary

Onfleet is a last-mile delivery software that provides end-to-end route planning, dispatch, communication, and analytics to handle the heavy lifting while you can focus on your customers.

This workflow template automatically creates an Onfleet delivery task when a new fulfillment is created for a Shopify order. 

Configurations

Update the Shopify trigger node with your own Shopify credentials
Update the Onfleet node with your own Onfleet credentials, to register for an Onfleet API key, please visit https://onfleet.com/signup to get started
You can easily change how the Onfleet task is created by mapping to additional data in the Shopify fulfillment object



## Template JSON

```
{
  "id": 13,
  "name": "Creating an Onfleet Task for a new Shopify Fulfillment",
  "nodes": [
    {
      "name": "Shopify Trigger",
      "type": "n8n-nodes-base.shopifyTrigger",
      "position": [
        240,
        440
      ],
      "webhookId": "576e8785-bbb4-426b-a922-da671efced68",
      "parameters": {
        "topic": "fulfillments/create"
      },
      "credentials": {
        "shopifyApi": {
          "id": "6",
          "name": "Shopify account"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Onfleet",
      "type": "n8n-nodes-base.onfleet",
      "position": [
        460,
        440
      ],
      "parameters": {
        "operation": "create",
        "additionalFields": {}
      },
      "credentials": {
        "onfleetApi": {
          "id": "2",
          "name": "Onfleet API Key"
        }
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Shopify Trigger": {
      "main": [
        [
          {
            "node": "Onfleet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
