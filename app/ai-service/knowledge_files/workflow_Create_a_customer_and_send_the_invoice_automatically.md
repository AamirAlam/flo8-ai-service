# Create a customer and send the invoice automatically

**[View Template](https://n8n.io/workflows/949-/)**  **Published Date:** 02/19/2021  **Created By:** ghagrawal17  **Categories:** `Finance & Accounting`  

## Template Description

This workflows allows you to create a customer and an invoice and send the invoice to the customer.



QuickBooks node: This node will create a new customer in QuickBooks.

QuickBooks1 node: This node will create an invoice for the customer that we created in the previous node.

QuickBooks2 node: This node will send the invoice that we created in the previous node.

## Template JSON

```
{
  "nodes": [
    {
      "name": "QuickBooks2",
      "type": "n8n-nodes-base.quickbooks",
      "position": [
        870,
        300
      ],
      "parameters": {
        "email": "",
        "resource": "invoice",
        "invoiceId": "={{$json[\"Id\"]}}",
        "operation": "send"
      },
      "credentials": {
        "quickBooksOAuth2Api": "QuickBooks OAuth Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "QuickBooks1",
      "type": "n8n-nodes-base.quickbooks",
      "position": [
        670,
        300
      ],
      "parameters": {
        "Line": [
          {
            "Amount": 100,
            "itemId": "1",
            "DetailType": "SalesItemLineDetail",
            "Description": "Consulting service"
          }
        ],
        "resource": "invoice",
        "operation": "create",
        "CustomerRef": "={{$json[\"Id\"]}}",
        "additionalFields": {}
      },
      "credentials": {
        "quickBooksOAuth2Api": "QuickBooks OAuth Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "QuickBooks",
      "type": "n8n-nodes-base.quickbooks",
      "position": [
        470,
        300
      ],
      "parameters": {
        "operation": "create",
        "displayName": "Jack Ryan",
        "additionalFields": {
          "PrimaryEmailAddr": "jack@ryan.com"
        }
      },
      "credentials": {
        "quickBooksOAuth2Api": "QuickBooks OAuth Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "QuickBooks": {
      "main": [
        [
          {
            "node": "QuickBooks1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "QuickBooks1": {
      "main": [
        [
          {
            "node": "QuickBooks2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
