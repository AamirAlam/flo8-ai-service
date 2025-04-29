# Update Shopify order tags when a Onfleet event happens

**[View Template](https://n8n.io/workflows/1545-/)**  **Published Date:** 03/22/2022  **Created By:** James Li  **Categories:** `Sales`  

## Template Description

Summary

Onfleet is a last-mile delivery software that provides end-to-end route planning, dispatch, communication, and analytics to handle the heavy lifting while you can focus on your customers.

This workflow template automatically updates the tags for a Shopify Order when an Onfleet event occurs.

Configurations

Update the Onfleet trigger node with your own Onfleet credentials, to register for an Onfleet API key, please visit https://onfleet.com/signup to get started
You can easily change which Onfleet event to listen to. Learn more about Onfleet webhooks with Onfleet Support
Update the Shopify node with your Shopify credentials and add your own tags to the Shopify Order





## Template JSON

```
{
  "name": "Updating Shopify tags on Onfleet events",
  "nodes": [
    {
      "name": "Onfleet Trigger",
      "type": "n8n-nodes-base.onfleetTrigger",
      "position": [
        460,
        300
      ],
      "webhookId": "6d6a2bee-f83e-4ebd-a1d5-8708c34393dc",
      "parameters": {
        "triggerOn": "taskDelayed",
        "additionalFields": {}
      },
      "typeVersion": 1
    },
    {
      "name": "Shopify",
      "type": "n8n-nodes-base.shopify",
      "position": [
        680,
        300
      ],
      "parameters": {
        "operation": "update",
        "updateFields": {
          "tags": ""
        }
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Onfleet Trigger": {
      "main": [
        [
          {
            "node": "Shopify",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
