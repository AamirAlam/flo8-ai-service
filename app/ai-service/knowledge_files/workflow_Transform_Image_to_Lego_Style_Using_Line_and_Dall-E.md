# Transform Image to Lego Style Using Line and Dall-E

**[View Template](https://n8n.io/workflows/2738-/)**  **Published Date:** 01/17/2025  **Created By:** Boriwat Chanruang  **Categories:** `Development` `Core Nodes` `AI` `Langchain`  

## Template Description

Who is this for?
This workflow is designed for:
Content creators**, artists, or hobbyists looking to experiment with AI-generated art.
Small business owners* or *marketers** using LEGO-style designs for branding or promotions.
Developers* or *AI enthusiasts** wanting to automate image transformations through messaging platforms like LINE.

What problem is this workflow solving?
Simplifies the process of creating custom AI-generated LEGO-style images.
Automates the manual effort of transforming user-uploaded images into AI-generated artwork.
Bridges the gap between messaging platforms (LINE) and advanced AI tools (DALL·E).
Provides a seamless system for users to upload an image and receive an AI-transformed output without technical expertise.

What this workflow does
Image Upload via LINE:
   Users send an image to the LINE chatbot.
AI-Powered Prompt Creation:
   GPT generates a prompt to describe the uploaded image for LEGO-style conversion.
AI Image Generation:
   DALL·E 3 processes the prompt and creates a LEGO-style isometric image.
Image Delivery:
   The generated image is returned to the user in LINE.

Setup

Prerequisites
LINE Developer Account** with API credentials.
Access to OpenAI API with DALL·E and GPT-4 capabilities.
A configured n8n instance to run this workflow.

Steps
Environment Setup:
   Add your LINE API Token and OpenAI credentials as environment variables (LINE_API_TOKEN, OPENAI_API_KEY) in n8n.
Configure LINE Webhook:
   Point the LINE webhook to your n8n instance.
Connect OpenAI:
   Set up OpenAI API credentials in the workflow nodes for GPT-4 and DALL·E.
Test Workflow:
   Upload a sample image in LINE and ensure it returns the LEGO-style AI image.

How to customize this workflow to your needs
Localization**:
  Modify response messages in LINE to fit your audience's language and tone.
Integration**:
  Add nodes to send notifications through other platforms like Slack or email.
Image Style**:
  Replace the LEGO-style image prompt with other artistic styles or themes.

Advanced Use Cases
Art Contests:
   Users upload images and receive AI-enhanced outputs for community voting or branding.
Marketing Campaigns:
   Quickly generate creative visual content for ads and promotions using customer-submitted photos.
Education:
   Use the workflow to teach students about AI-generated art and automation through a hands-on approach.

Tips for Optimization
Error Handling**:
  Add fallback nodes to handle invalid images or API errors gracefully.
Logging**:
  Implement a logging mechanism to track requests and outputs for debugging and analytics.
Scalability**:
  Use queue-based systems or cloud scaling to handle large volumes of image requests.

Enhancements
Add sticky notes in n8n to provide inline instructions for configuring each node.
Create a tutorial video or documentation for first-time users to set up and customize the workflow.
Include advanced filters to allow users to select from multiple styles beyond LEGO (e.g., pixel art, watercolor).

This workflow enables seamless interaction between messaging platforms and advanced AI capabilities, making it highly versatile for various creative and business applications.

## Template JSON

```
{
  "meta": {
    "instanceId": "c59c4acfed171bdc864e7c432be610946898c3ee271693e0303565c953d88c1d",
    "templateCredsSetupCompleted": true
  },
  "name": "Transform Image to Lego Style Using Line and Dall-E",
  "tags": [],
  "nodes": [
    {
      "id": "82b62d4e-a263-4232-9bae-4c581db2269c",
      "name": "Receive a Line Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        0,
        0
      ],
      "webhookId": "2a27c148-3977-485f-b197-567c96671023",
      "parameters": {
        "path": "lineimage",
        "options": {},
        "httpMethod": "POST"
      },
      "typeVersion": 2
    },
    {
      "id": "f861c4eb-3d4f-4253-810f-8032602f079b",
      "name": "Receive Line Messages",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        220,
        0
      ],
      "parameters": {
        "url": "=https://api-data.line.me/v2/bot/message/{{ $json.body.events[0].message.id }}/content",
        "options": {},
        "jsonHeaders": "={\n\"Authorization\": \"Bearer YOUR_LINE_BOT_TOKEN\",\n\"Content-Type\": \"application/json\"\n}",
        "sendHeaders": true,
        "specifyHeaders": "json"
      },
      "typeVersion": 4.2
    },
    {
      "id": "da3a9188-028d-4c75-b23f-5f1f4e50784c",
      "name": "Creating an Image using Dall-E",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        860,
        0
      ],
      "parameters": {
        "prompt": "={{ $json.content }}",
        "options": {
          "returnImageUrls": true
        },
        "resource": "image"
      },
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.7
    },
    {
      "id": "36c826e5-eacd-43ad-b663-4d788005e61a",
      "name": "Creating a Prompt for Dall-E (Lego Style)",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        540,
        0
      ],
      "parameters": {
        "text": "Creating the DALL\u00b7E 3 prompt to transform this kind of image into a isometric LEGO image (Only provide me with a prompt).",
        "modelId": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini",
          "cachedResultName": "GPT-4O-MINI"
        },
        "options": {},
        "resource": "image",
        "inputType": "base64",
        "operation": "analyze",
        "binaryPropertyName": "=data"
      },
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.7
    },
    {
      "id": "3c19f931-9ca0-4bd7-b4eb-1628d89bbba1",
      "name": "Send Back an Image through Line",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1160,
        0
      ],
      "parameters": {
        "url": "https://api.line.me/v2/bot/message/reply",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"replyToken\": \"{{ $('Receive a Line Webhook').item.json.body.events[0].replyToken }}\",\n  \"messages\": [\n    {\n      \"type\": \"image\",\n      \"originalContentUrl\": \"{{ $json.url }}\",\n      \"previewImageUrl\": \"{{ $json.url }}\"\n    }\n  ]\n}",
        "sendBody": true,
        "jsonHeaders": "{\n\"Authorization\": \"Bearer YOUR_LINE_BOT_TOKEN\",\n\"Content-Type\": \"application/json\"\n}",
        "sendHeaders": true,
        "specifyBody": "json",
        "specifyHeaders": "json"
      },
      "typeVersion": 4.2
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "",
  "connections": {
    "Receive Line Messages": {
      "main": [
        [
          {
            "node": "Creating a Prompt for Dall-E (Lego Style)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Receive a Line Webhook": {
      "main": [
        [
          {
            "node": "Receive Line Messages",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Creating an Image using Dall-E": {
      "main": [
        [
          {
            "node": "Send Back an Image through Line",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Creating a Prompt for Dall-E (Lego Style)": {
      "main": [
        [
          {
            "node": "Creating an Image using Dall-E",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
