# Stripe Payment Order Sync – Auto Retrieve Customer & Product Purchased

**[View Template](https://n8n.io/workflows/3391-/)**  **Published Date:** 03/31/2025  **Created By:** Mateo Fiorito Rocha  **Categories:** `Development` `Core Nodes`  

## Template Description

Overview

This automation template is designed to streamline your payment processing by automatically triggering upon a successful Stripe payment. The workflow retrieves the complete payment session and filters the information to display only the customer name, customer email, and the purchased product details. This template is perfect for quickly integrating Stripe transactions into your inventory management, CRM, or notification systems.

Step-by-Step Setup Instructions

Stripe Account Configuration:
   Ensure you have an active Stripe account.
   Connect your Stripe Credentials.
  
Retrieve Product and Customer Data:
   Utilize Stripe’s API within the automation to fetch the purchased product details.
   Retrieve customer information such as: email and full name.

Integration and Response:
   Map the retrieved data to your desired format.
   Trigger subsequent nodes or actions such as sending a confirmation email, updating a CRM system, or logging the transaction.

Pre-Conditions and Requirements

Stripe Account:** A valid Stripe account with access to API keys and webhook configurations.
API Keys:** Ensure you have your Stripe secret and publishable keys ready.

Customization Guidance

Data Mapping:** Customize the filtering node to match your specific data schema or to include additional data fields if needed.
Additional Actions:** Integrate further nodes to handle post-payment actions like sending SMS notifications, updating order statuses, or generating invoices.

Enjoy seamless integration and enhanced order management with this automation template!

## Template JSON

```
{
  "id": "YVNJOltj0jMQatGz",
  "meta": {
    "instanceId": "143d2ab55c8bffb06f8b9c7ad30335764fdc48bbbacecbe2218dadb998a32213",
    "templateCredsSetupCompleted": true
  },
  "name": "Stripe Payment Order Sync \u2013 Auto Retrieve Customer & Product Purchased",
  "tags": [],
  "nodes": [
    {
      "id": "90322fe5-5536-41c3-ac08-ea87a856781b",
      "name": "Stripe Trigger on Payment Event",
      "type": "n8n-nodes-base.stripeTrigger",
      "position": [
        0,
        0
      ],
      "webhookId": "e85ac894-bb67-436c-ad39-308a00c8e922",
      "parameters": {
        "events": [
          "checkout.session.completed"
        ]
      },
      "credentials": {
        "stripeApi": {
          "id": "ClCB0WooGxls3WGM",
          "name": "Stripe Test"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "3feb0b03-921e-4bfd-8a50-b2b6b47e9497",
      "name": "Extract Session Information",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        300,
        0
      ],
      "parameters": {
        "url": "=https://api.stripe.com/v1/checkout/sessions/{{ $json.data.object.id }}",
        "options": {},
        "sendQuery": true,
        "authentication": "predefinedCredentialType",
        "queryParameters": {
          "parameters": [
            {
              "name": "expand[]",
              "value": "line_items"
            }
          ]
        },
        "nodeCredentialType": "stripeApi"
      },
      "credentials": {
        "stripeApi": {
          "id": "ClCB0WooGxls3WGM",
          "name": "Stripe Test"
        },
        "httpHeaderAuth": {
          "id": "9UNc6IDuBlNCX6zd",
          "name": "PDF to Text"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "5a436d1c-88e9-492e-8fe0-33a5706de1b3",
      "name": "Filter Information",
      "type": "n8n-nodes-base.set",
      "position": [
        560,
        0
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "95a68e0f-b74c-4ca2-8143-14b469aa6bfb",
              "name": "Customer Name",
              "type": "string",
              "value": "={{ $json.customer_details.name }}"
            },
            {
              "id": "7634efa6-04f3-4dac-8509-56aae29fcc79",
              "name": "Customer Email",
              "type": "string",
              "value": "={{ $json.customer_details.email }}"
            },
            {
              "id": "10e71e07-6dd3-410c-a774-1eeffe2be7a5",
              "name": "Product Purchased",
              "type": "string",
              "value": "={{ $json.line_items.data[0].description }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "e3f6ba06-36d9-4b41-9c5a-cec669ce507b",
  "connections": {
    "Extract Session Information": {
      "main": [
        [
          {
            "node": "Filter Information",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Stripe Trigger on Payment Event": {
      "main": [
        [
          {
            "node": "Extract Session Information",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
