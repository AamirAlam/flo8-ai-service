# Simplest way to create a Stripe Payment Link

**[View Template](https://n8n.io/workflows/2195-/)**  **Published Date:** 03/26/2024  **Created By:** Emmanuel Bernard  **Categories:** `Development` `Core Nodes`  

## Template Description

🎉 Do you want to master AI automation, so you can save time and build cool stuff? 

I’ve created a welcoming Skool community for non-technical yet resourceful learners.

👉🏻 Join the AI Atelier 👈🏻

Accepting payments via credit card online is a crucial component for the majority of businesses. Stripe provides a robust suite of tools for processing payments, yet many people still find it challenging to create a simple payment page and distribute it to their customers.

📋 Blog post
📺 Youtube Video

This n8n workflow aims to offer the simplest and most direct method for generating a Stripe payment link.

Features
Quick Stripe Payment Link Creation:** Simply enter a title and select a price to create a Stripe payment link in seconds.

Set Up Steps
Connect your Stripe credentials. 
Fill the config node (currency).

This n8n workflow template is crafted to significantly reduce the creation time of a Stripe Payment link.

Created by the n8ninja.

## Template JSON

```
{
  "meta": {
    "instanceId": "8418cffce8d48086ec0a73fd90aca708aa07591f2fefa6034d87fe12a09de26e"
  },
  "nodes": [
    {
      "id": "4503cef2-4882-43c6-bdb9-b94c75da5776",
      "name": "Create Stripe Product",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        780,
        300
      ],
      "parameters": {
        "url": "https://api.stripe.com/v1/products",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "contentType": "form-urlencoded",
        "authentication": "predefinedCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "name",
              "value": "={{ $json.title }}"
            },
            {
              "name": "default_price_data[unit_amount]",
              "value": "={{ $json.price }}"
            },
            {
              "name": "default_price_data[currency]",
              "value": "={{ $json.currency }}"
            }
          ]
        },
        "nodeCredentialType": "stripeApi"
      },
      "credentials": {
        "stripeApi": {
          "id": "qjose8z3RR7Xzm7b",
          "name": "Stripe Dev"
        }
      },
      "typeVersion": 4.1
    },
    {
      "id": "80306e70-b57f-4697-9a9f-1835d2525c2f",
      "name": "Create payment link",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        980,
        300
      ],
      "parameters": {
        "url": "https://api.stripe.com/v1/payment_links",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "contentType": "form-urlencoded",
        "authentication": "predefinedCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "line_items[0][price]",
              "value": "={{ $json.default_price }}"
            },
            {
              "name": "line_items[0][quantity]",
              "value": "1"
            }
          ]
        },
        "nodeCredentialType": "stripeApi"
      },
      "credentials": {
        "stripeApi": {
          "id": "qjose8z3RR7Xzm7b",
          "name": "Stripe Dev"
        }
      },
      "typeVersion": 4.1
    },
    {
      "id": "31d7450e-0f44-4c16-aec4-fe9213ff7c83",
      "name": "Config",
      "type": "n8n-nodes-base.set",
      "notes": "Setup your flow",
      "position": [
        580,
        300
      ],
      "parameters": {
        "include": "selected",
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "038b54b7-9559-444e-8653-c5256a5b784e",
              "name": "currency",
              "type": "string",
              "value": "EUR"
            },
            {
              "id": "e86962bb-7af4-41be-94f6-6ee6b8569eef",
              "name": "price",
              "type": "number",
              "value": "={{ $json.price * 100}}"
            }
          ]
        },
        "includeFields": "title",
        "includeOtherFields": true
      },
      "notesInFlow": true,
      "typeVersion": 3.3
    },
    {
      "id": "10fb462a-8302-4281-9cd3-68bc00e69177",
      "name": "Creation Form",
      "type": "n8n-nodes-base.formTrigger",
      "position": [
        380,
        300
      ],
      "webhookId": "1c6fe52c-48ab-4688-b5ae-7e24361aa603",
      "parameters": {
        "path": "my-form-id",
        "formTitle": "Create a payment link",
        "formFields": {
          "values": [
            {
              "fieldLabel": "title",
              "requiredField": true
            },
            {
              "fieldType": "number",
              "fieldLabel": "price",
              "requiredField": true
            }
          ]
        },
        "responseMode": "responseNode"
      },
      "typeVersion": 2
    },
    {
      "id": "daf2d495-f31f-45e0-945a-a6e94be43b25",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        580,
        0
      ],
      "parameters": {
        "color": 6,
        "width": 275.01592825011585,
        "height": 261.76027109756643,
        "content": "# Setup\n### 1/ Add Your credentials\n[Stripe](https://docs.n8n.io/integrations/builtin/credentials/stripe/)\n\n### 2/ And fill the config node\n# \ud83d\udc47"
      },
      "typeVersion": 1
    },
    {
      "id": "9d298026-d858-4613-97c1-ac0cbd895ece",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        880,
        160
      ],
      "parameters": {
        "color": 7,
        "width": 202.64787116404852,
        "height": 85.79488430601403,
        "content": "### Crafted by the\n## [\ud83e\udd77 n8n.ninja](https://n8n.ninja)"
      },
      "typeVersion": 1
    },
    {
      "id": "5c8a17a3-7b2c-4760-a48a-02549f766967",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1200,
        300
      ],
      "parameters": {
        "options": {},
        "redirectURL": "={{ $json.url }}",
        "respondWith": "redirect"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Config": {
      "main": [
        [
          {
            "node": "Create Stripe Product",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Creation Form": {
      "main": [
        [
          {
            "node": "Config",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create payment link": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create Stripe Product": {
      "main": [
        [
          {
            "node": "Create payment link",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
