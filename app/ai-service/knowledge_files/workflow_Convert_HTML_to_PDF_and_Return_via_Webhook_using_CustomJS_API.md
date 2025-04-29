# Convert HTML to PDF and Return via Webhook using CustomJS API

**[View Template](https://n8n.io/workflows/3331-/)**  **Published Date:** 03/26/2025  **Created By:** CustomJS  **Categories:**   

## Template Description

!
n8n Workflow: HTML to PDF Generator

This n8n workflow converts HTML content into a styled PDF and returns it as a response via a webhook. The workflow receives HTML input, processes it using CustomJS's PDF toolkit, and sends back the resulting PDF to the original webhook requester.

@custom-js/n8n-nodes-pdf-toolkit

Features:

Webhook Trigger**: Accepts incoming requests with HTML content.
HTML to PDF Conversion**: Uses CustomJS to transform HTML into a PDF.
Response**: Sends the generated PDF back to the webhook response.

Requirements:

Self-hosted** n8n instance
A CustomJS API key for HTML to PDF conversion
HTML content** to be converted into a PDF

Workflow Steps:

Webhook Trigger:

   Accepts incoming HTTP requests with HTML content.
   This data is passed to the next node for processing.

HTML to PDF Conversion:

   Uses the CustomJS node to convert the incoming HTML into a PDF document.
   You can customize the HTML content to match the design requirements.

Respond to Webhook:

   Sends the generated PDF as a binary response to the original webhook request.

Setup Guide:

1. Configure CustomJS API
Sign up at CustomJS.
Retrieve your API key from the profile page.

Add your API key as n8n credentials.

2. Design Workflow

Create a Webhook:

   Set up a webhook to trigger the workflow when HTML content is received.

Prepare HTML Content:

   The incoming request should include the HTML content you wish to convert into a PDF.

Configure HTML to PDF Node:

   Use the HTML to PDF node to convert the provided HTML into a PDF.
   The node uses the HTML input to generate a PDF using the CustomJS API.

Respond with the PDF:

   The Respond to Webhook node will send the generated PDF back to the original requester as a binary response.

Example HTML Input:

Hello CustomJS!
CustomJS provides the missing toolset for your no-code projects

Result PDF


## Template JSON

```
{
  "meta": {
    "instanceId": "fcf18fc485cc336a31bc65574fd28e124660f468281b7aad773616b17903afe6",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "37bd6cc9-3cc4-442e-94c1-42972c0fce0d",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        80,
        0
      ],
      "webhookId": "060dbacf-0feb-43d4-b4ac-44011a7dd1a4",
      "parameters": {
        "path": "060dbacf-0feb-43d4-b4ac-44011a7dd1a4",
        "options": {},
        "responseMode": "responseNode"
      },
      "typeVersion": 2
    },
    {
      "id": "3c05c0e4-7121-46d0-b35c-fc39cdd35ae7",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        580,
        0
      ],
      "parameters": {
        "options": {},
        "respondWith": "binary"
      },
      "typeVersion": 1.1
    },
    {
      "id": "3f5ba2a7-148d-4921-b2ca-9dee17a2b278",
      "name": "HTML to PDF",
      "type": "@custom-js/n8n-nodes-pdf-toolkit.html2Pdf",
      "position": [
        340,
        0
      ],
      "parameters": {
        "htmlInput": "<h1>Hello CustomJS!</h1>\n<h2>CustomJS provides the missing toolset for your no-code projects</h2>"
      },
      "credentials": {
        "customJsApi": {
          "id": "SZkqeEHVYyWhaGem",
          "name": "CustomJS account"
        }
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "HTML to PDF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTML to PDF": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
