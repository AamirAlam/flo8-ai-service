# Currency Conversion Workflow

**[View Template](https://n8n.io/workflows/2691-/)**  **Published Date:** 01/02/2025  **Created By:** Mauricio Perera  **Categories:** `Development` `Core Nodes`  

## Template Description

Purpose: This workflow exemplifies a sophisticated yet pragmatic mechanism for automating currency conversions by leveraging simple HTTP queries routed through a webhook. By intercepting user requests, sourcing real-time exchange rate data via Google search results, and formatting the data into actionable responses, it obviates the reliance on third-party APIs. This efficiency renders it an indispensable instrument for diverse applications, including dynamic pricing strategies for AI-driven systems, financial data automation, and real-time currency computation within complex workflows. The workflow's architectural simplicity ensures seamless integration across professional and academic domains, optimizing both scalability and reliability.

Workflow Steps:
Capture Conversion Query:
   The workflow initiates by intercepting user input delivered as a GET request through a configured webhook. Inputs should adhere to a structured syntax, such as 5usd to mxn, to ensure flawless processing.
   Testing Tip: Use tools like Postman or a browser to test GET requests and verify that the Webhook receives inputs correctly.
Fetch Exchange Rate:
   Utilizing the HTTP Request node, a Google search query is executed to retrieve current exchange rate data. This method ensures the workflow remains economical and adaptable while circumventing API dependencies.
Extract Conversion Data:
   By processing the returned HTML from Google's search results, this node extracts precise exchange rate figures and contextual information critical for accurate conversions.
   Error Handling: If extraction fails, verify that the input format is correct and update CSS selectors to reflect any changes in Google's HTML structure.
Format Currency Response:
   The extracted data undergoes refinement and is formatted into a structured, user-friendly string that conveys the conversion results with clarity and precision.
Send Conversion Response:
   The workflow culminates by dispatching the formatted response back to the request origin, completing the loop with efficiency and reliability.

Required Configuration:
Configure the Webhook node to accommodate GET requests. The query parameters should follow the format: https://your-webhook-url/currency-converter?q=5usd+to+mxn.
Inputs must adhere strictly to the predefined syntax (e.g., 5usd to mxn). Deviations may induce processing errors or yield erroneous outputs.

Customization Options:
The Extract Conversion Data node’s CSS selectors can be fine-tuned to align with modifications in Google’s HTML structure, ensuring long-term operability.
Adjustments to the Format Currency Response node enable bespoke output formatting, incorporating additional metadata or altering the response structure to meet specific project requisites.

Advanced Features:
This workflow’s modular design supports seamless integration into expansive systems. For instance, an e-commerce platform could employ it to dynamically localize product pricing based on user geolocation.
Enhanced functionality can be achieved by appending nodes to log conversions, monitor performance metrics, or trigger auxiliary workflows conditioned on conversion outputs.

Expected Results:
For a query like 5usd to mxn, the workflow generates a response formatted as: 5 USD = 95 MXN. This output is optimized for readability and practical application.

Use Case Examples:
AI Integration:** Enables artificial intelligence agents to process real-time price conversions efficiently across diverse currencies, enhancing their computational capabilities.
Financial Operations:** Automates precise currency conversions for corporate reports, international transactions, and market analytics.
Personal Financial Planning:** Assists users in calculating currency conversions for investment decisions or travel budgeting with minimal manual effort.
E-commerce Applications:** Facilitates dynamic price adjustments on online marketplaces, displaying localized prices to augment user experience and conversion rates.
Workflow Integration:** Embeds seamlessly into larger systems, such as CRMs or ERPs, to streamline financial operations and enhance interoperability.

Key Benefits:
No API Dependency:** By leveraging publicly available data from Google, the workflow eliminates the complexities and costs associated with API integration, reducing overhead and enhancing accessibility.
Precision and Currency:** Ensures accurate and real-time results by querying Google directly.
Flexibility:** Designed to adapt to various operational contexts and input formats, making it a versatile asset in computational and commercial applications.

Tags:
currency conversion, automation, webhook, data extraction, AI integration, financial automation, e-commerce, real-time data, scalable workflows.

## Template JSON

```
{
  "id": "pDDOf7oK0FAxGLtm",
  "meta": {
    "instanceId": "92786e96ce436aecd3a1d62d818a74e51ca684bb36c805928bef93a3b46549ad"
  },
  "tags": [],
  "nodes": [
    {
      "id": "6346b221-a6ca-4938-a37e-7e564b43735b",
      "name": "Fetch Exchange Rate",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -100,
        160
      ],
      "parameters": {},
      "typeVersion": 4.2
    },
    {
      "id": "a07c206e-b044-4acb-b50c-c81406370355",
      "name": "Extract Conversion Data",
      "type": "n8n-nodes-base.html",
      "position": [
        220,
        160
      ],
      "parameters": {},
      "executeOnce": true,
      "retryOnFail": false,
      "typeVersion": 1.2,
      "alwaysOutputData": true
    },
    {
      "id": "b07c69c6-f956-423b-8457-d706139f94e2",
      "name": "Format Currency Response",
      "type": "n8n-nodes-base.set",
      "position": [
        560,
        160
      ],
      "parameters": {},
      "typeVersion": 3.4
    },
    {
      "id": "23a66449-3d22-40f9-b3c3-22fa4daf5c39",
      "name": "Capture Conversion Query",
      "type": "n8n-nodes-base.webhook",
      "position": [
        -420,
        160
      ],
      "webhookId": "974e55e6-7898-41ec-8981-d265fb814213",
      "parameters": {},
      "typeVersion": 2
    },
    {
      "id": "f017000a-1fd0-4041-925d-1086c00727d7",
      "name": "Send Conversion Response",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        920,
        160
      ],
      "parameters": {},
      "typeVersion": 1.1
    },
    {
      "id": "44529e37-f945-45ca-8364-abb1f7c890f1",
      "name": "Note - Webhook",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -480,
        20
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "f3cca102-159c-4062-90d8-c0c753a7bff9",
      "name": "Note - HTTP Request",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -160,
        20
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "507cbf79-be3c-4d2e-b16f-74342a0ac51d",
      "name": "Note - HTML Extract",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        160,
        20
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "484992d6-3aad-4190-8894-7d8c360c12f6",
      "name": "Note - Format Response",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        520,
        20
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "029a1ab8-2005-46d9-b1c4-01299a17ea12",
      "name": "Note - Send Response",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        880,
        20
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "11e4c097-dfb8-4c1d-8851-3988751c9927",
  "connections": {
    "Fetch Exchange Rate": {
      "main": [
        [
          {
            "node": "Extract Conversion Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Conversion Data": {
      "main": [
        [
          {
            "node": "Format Currency Response",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Capture Conversion Query": {
      "main": [
        [
          {
            "node": "Fetch Exchange Rate",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format Currency Response": {
      "main": [
        [
          {
            "node": "Send Conversion Response",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
