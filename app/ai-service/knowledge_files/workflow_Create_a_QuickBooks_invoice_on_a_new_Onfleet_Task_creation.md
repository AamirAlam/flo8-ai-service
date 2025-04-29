# Create a QuickBooks invoice on a new Onfleet Task creation

**[View Template](https://n8n.io/workflows/1546-/)**  **Published Date:** 03/22/2022  **Created By:** James Li  **Categories:** `Finance & Accounting`  

## Template Description

Summary

Onfleet is a last-mile delivery software that provides end-to-end route planning, dispatch, communication, and analytics to handle the heavy lifting while you can focus on your customers.

This workflow template listens to an Onfleet event and interacts with the QuickBooks API. You can easily streamline this with your QuickBooks invoices or other entities. Typically, you can create an invoice when an Onfleet task is created to allow your customers to pay ahead of an upcoming delivery.

Configurations

Update the Onfleet trigger node with your own Onfleet credentials, to register for an Onfleet API key, please visit https://onfleet.com/signup to get started
You can easily change which Onfleet event to listen to. Learn more about Onfleet webhooks with Onfleet Support
Update the QuickBooks Online node with your QuickBooks credentials

## Template JSON

```
{
  "name": "Create a QuickBooks invoice on a new Onfleet Task creation",
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
        "triggerOn": "taskCreated",
        "additionalFields": {}
      },
      "typeVersion": 1
    },
    {
      "name": "QuickBooks Online",
      "type": "n8n-nodes-base.quickbooks",
      "position": [
        680,
        300
      ],
      "parameters": {
        "Line": [],
        "resource": "invoice",
        "operation": "create",
        "additionalFields": {
          "Balance": 0,
          "TxnDate": "",
          "ShipAddr": "",
          "BillEmail": ""
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
            "node": "QuickBooks Online",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
