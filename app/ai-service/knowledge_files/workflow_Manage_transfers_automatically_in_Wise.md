# Manage transfers automatically in Wise

**[View Template](https://n8n.io/workflows/992-/)**  **Published Date:** 03/18/2021  **Created By:** ghagrawal17  **Categories:** `Finance & Accounting`  

## Template Description

This workflow allows you to create a quote and a transfer, execute the transfer and get the information of the transfer using the Wise node.



Wise node: This node will create a new quote in Wise.

Wise1 node: This node will create a new transfer for the quote that we created in the previous node.

Wise2 node: This node will execute the transfer that we created in the previous node.

Wise3 node: This node will return the information of the transfer that we executed in the previous node.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Wise",
      "type": "n8n-nodes-base.wise",
      "position": [
        470,
        320
      ],
      "parameters": {
        "amount": 500,
        "resource": "quote",
        "operation": "create",
        "profileId": 16138858,
        "sourceCurrency": "EUR",
        "targetCurrency": "EUR",
        "targetAccountId": 147767974
      },
      "credentials": {
        "wiseApi": "Wise API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Wise1",
      "type": "n8n-nodes-base.wise",
      "position": [
        660,
        320
      ],
      "parameters": {
        "quoteId": "={{$json[\"id\"]}}",
        "resource": "transfer",
        "operation": "create",
        "profileId": 16138858,
        "targetAccountId": 147767974,
        "additionalFields": {
          "reference": "Thank you for the contribution"
        }
      },
      "credentials": {
        "wiseApi": "Wise API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Wise2",
      "type": "n8n-nodes-base.wise",
      "position": [
        870,
        320
      ],
      "parameters": {
        "resource": "transfer",
        "operation": "execute",
        "profileId": 16138858,
        "transferId": "={{$json[\"id\"]}}"
      },
      "credentials": {
        "wiseApi": "Wise API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Wise3",
      "type": "n8n-nodes-base.wise",
      "position": [
        1070,
        320
      ],
      "parameters": {
        "resource": "transfer",
        "transferId": "={{$node[\"Wise1\"].json[\"id\"]}}"
      },
      "credentials": {
        "wiseApi": "Wise API Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Wise": {
      "main": [
        [
          {
            "node": "Wise1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wise1": {
      "main": [
        [
          {
            "node": "Wise2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wise2": {
      "main": [
        [
          {
            "node": "Wise3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
