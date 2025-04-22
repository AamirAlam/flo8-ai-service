# Generate dynamic contents for EMAILS or HTML pages

**[View Template](https://n8n.io/workflows/1790-/)**  **Published Date:** 09/11/2022  **Created By:** Miquel Colomer  **Categories:** `Communication` `Core Nodes` `HITL`  

## Template Description



Disclaimer: This template contains a community node and therefore only works for n8n self-hosted users==

This is Miquel from Aprende n8n and Automate with n8n.

We have created a new community node Document Generator that generates dynamic content using templates.

You can compose complex content with no SETs or FUNCTION ITEMs nodes using this node, like:
Send one email with a list of items in the body (i.e., one email with the last entries of an RSS feed).
Send one email per item (i.e., one invoice per email).

Emails are just a sample. You can create complex dynamic content to:
Send messages to Telegram/Slack.
Create WordPress entries.
Create HTML pages for your website.
Create tickets.

And more! The sky is your limit ;)

If you want to use this workflow, install the community node n8n-nodes-document-generator from Settings &gt; Community nodes. Type "n8n-nodes-document-generator", check "I understand the risks..." and click on "Install":


Later, copy and paste this workflow into your n8n.

You will get this workflow:


This workflow uses the Customer Datastore node to generate sample input items.

You can render one template with all items (enable "Render All Items with One Template"):


or one template per input item:


Visit the oficial NPM page to see more samples.

Learning n8n by yourself is nice, but a bit tricky :) We offer n8n training video courses at Aprende n8n. If you need custom trainings, let us know.

Additionally, you can contact us at Automate with n8n if you need the next services:
Custom installations.
Custom nodes.
Monitor and alarms.
Delegate 12/5 or 24/7 workflow issue resolutions.
Automated backups of your workflows.
HTTP integrations of non-supported APIs.
Complex workflows.

I hope you will enjoy this new node and this workflow.

Automate your life! Automate it with n8n!




## Template JSON

```
{
  "meta": {
    "instanceId": "14c5980141526fbb38db85208103f515afa76de9c8760a23a1771b4ed940dc7b"
  },
  "nodes": [
    {
      "id": "4704e44a-80c6-41b4-a0b9-ece060d53836",
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -220,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "74a78b35-b453-4345-8cd9-9d8a62961c29",
      "name": "Customer Datastore",
      "type": "n8n-nodes-base.n8nTrainingCustomerDatastore",
      "position": [
        20,
        300
      ],
      "parameters": {
        "operation": "getAllPeople",
        "returnAll": true
      },
      "typeVersion": 1
    },
    {
      "id": "10b633de-e5e5-4fd2-bb4b-7a16bac5f69c",
      "name": "Item Lists",
      "type": "n8n-nodes-base.itemLists",
      "position": [
        220,
        300
      ],
      "parameters": {
        "options": {},
        "operation": "sort",
        "sortFieldsUi": {
          "sortField": [
            {
              "fieldName": "name"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "aa90be4e-f548-459f-822b-a3dc1d20d58e",
      "name": "One item per template",
      "type": "n8n-nodes-document-generator.DocumentGenerator",
      "position": [
        660,
        160
      ],
      "parameters": {
        "template": "Date: {{created}}\nTo: {{name}} <{{email}}>\nAddress: {{country}}\nDetails:\n{{#each lines}}\n- \"{{description}}\" x {{quantity}} = {{amount}}\u20ac + {{vat}}\u20ac = {{total}}\u20ac\n{{/each}}\nTotal invoice: {{total}}\u20ac"
      },
      "typeVersion": 1
    },
    {
      "id": "914c4c67-81df-45ec-9eea-3efb96383dfc",
      "name": "All items, one template",
      "type": "n8n-nodes-document-generator.DocumentGenerator",
      "position": [
        660,
        400
      ],
      "parameters": {
        "template": "<html>\n<head>\n</head>\n<body>\nNew customers in last 24h:\n<ul id=\"customer_list\">\n  {{#each items}}\n  <li>{{name}}: {{email}}</li>\n  {{/each}}\n</ul>\n</body>\n</html>",
        "oneTemplate": true
      },
      "typeVersion": 1
    },
    {
      "id": "bc1821d1-7d08-4208-aa5e-7290f5604e91",
      "name": "Add lines",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        440,
        160
      ],
      "parameters": {
        "functionCode": "item.lines = [\n  {\n    concept: \"Service\",\n    description: \"Design of HTML banners\",\n    quantity: 1,\n    amount: 22,\n    vat: 22 * 0.21,\n    total: 22 * 1.21\n  },\n  {\n    concept: \"Service\",\n    description: \"Design of PNG banners\",\n    quantity: 1,\n    amount: 33,\n    vat: 33 * 0.21,\n    total: 33 * 1.21\n  }\n]\n\nitem.date = \"2022-01-12\";\nitem.total = 133.10;\n\nreturn item;"
      },
      "typeVersion": 1
    },
    {
      "id": "99ccf5f0-6d82-4a9c-a314-711249fbdfc9",
      "name": "Send one TEXT email per item",
      "type": "n8n-nodes-base.emailSend",
      "position": [
        880,
        160
      ],
      "parameters": {
        "html": "={{ $json[\"text\"] }}",
        "options": {},
        "subject": "=Invoice for {{ $node[\"Add lines\"].json[\"name\"] }}",
        "toEmail": "mcolomer@n8nhackers.com",
        "fromEmail": "mcolomer@n8nhackers.com"
      },
      "credentials": {
        "smtp": {
          "id": "54",
          "name": "SMTP account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "3bc12345-da46-4c1f-8fe3-5bb0683cbcda",
      "name": "Send one HTML Email per list",
      "type": "n8n-nodes-base.emailSend",
      "position": [
        880,
        400
      ],
      "parameters": {
        "html": "={{ $json[\"text\"] }}",
        "options": {},
        "subject": "New customers",
        "toEmail": "mcolomer@n8nhackers.com",
        "fromEmail": "mcolomer@n8nhackers.com"
      },
      "credentials": {
        "smtp": {
          "id": "54",
          "name": "SMTP account"
        }
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Add lines": {
      "main": [
        [
          {
            "node": "One item per template",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Item Lists": {
      "main": [
        [
          {
            "node": "All items, one template",
            "type": "main",
            "index": 0
          },
          {
            "node": "Add lines",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Customer Datastore": {
      "main": [
        [
          {
            "node": "Item Lists",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Customer Datastore",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "One item per template": {
      "main": [
        [
          {
            "node": "Send one TEXT email per item",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "All items, one template": {
      "main": [
        [
          {
            "node": "Send one HTML Email per list",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
