# Receive updates on a new invoice via Invoice Ninja

**[View Template](https://n8n.io/workflows/535-/)**  **Published Date:** 07/17/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Invoice Ninja Trigger node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "Invoice Ninja Trigger",
      "type": "n8n-nodes-base.invoiceNinjaTrigger",
      "position": [
        890,
        400
      ],
      "webhookId": "97be21b3-ebf5-48cf-b291-5d954657a544",
      "parameters": {
        "event": "create_invoice"
      },
      "credentials": {
        "invoiceNinjaApi": "invoice_ninja_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
