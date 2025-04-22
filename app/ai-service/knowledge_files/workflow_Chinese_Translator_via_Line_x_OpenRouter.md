# Chinese Translator via Line x OpenRouter

**[View Template](https://n8n.io/workflows/3207-/)**  **Published Date:** 03/18/2025  **Created By:** lin@davoy.tech  **Categories:** `Development` `Core Nodes`  

## Template Description

The Chinese Translator workflow automates the translation of text into Chinese characters, pinyin, and English translations via Line Messaging API. This workflow leverages OpenRouter.ai to call advanced language models such as Qwen for accurate translations and ensures smooth user interaction by providing loading animations and timely replies.

Purpose
This workflow aims to 
Provide users with real-time translations of input text into Chinese characters, pinyin, and English
Deliver seamless user experience through interactive features like loading animations and quick reply messages
Enable easy integration with Line Messaging API for scalable deployment
Key Features
Real-Time Translation : Translates user-inputted text instantly using OpenRouter.ai's standardized API.
Comprehensive Output : Delivers Chinese characters, pinyin, and English translations for each word or phrase.
Interactive User Experience : Incorporates loading animations to inform users that the workflow is processing their request.
Line Integration : Utilizes Line Webhooks and Reply APIs to facilitate communication between users and the translation service.

Data Flow
Receiving Input
Node: Line Webhook
Captures incoming messages from Line users.
Extracts the text content and reply token from the webhook payload.
Loading Animation
Node: Line Loading Animation
Sends a loading animation back to the user, indicating that the workflow is processing the request.
Enhances user experience by providing immediate feedback.
Translation Processing
Node: Use OpenRouter
Sends the extracted text to OpenRouter.ai's API, utilizing the Qwen model for translation.
Requests Chinese characters, pinyin, and English translations for the input text.
Sending Response
Node: Line Reply
Formats the translation results into a readable text message.
Sends the translated text back to the user via Line's Reply API.

Setup Instructions
Prerequisites
Line Developer Account : Create a Line channel to obtain necessary credentials for webhooks and messaging.
OpenRouter.ai Account : Set up an account and configure access to utilize their language models.

Steps to Configure
Set Up Line Webhook :
Navigate to the Line Developers Console and create a new webhook URL.
Copy the generated webhook URL and paste it into the Line Webhook node in n8n.
Configure OpenRouter.ai :
Obtain API credentials from OpenRouter.ai and integrate them into the Use OpenRouter node within the workflow.
Adjust Workflow Settings :
Ensure the timezone is set to Asia/Bangkok .
Verify that all nodes are correctly connected and configured with appropriate credentials.

Intended Audience
This workflow is ideal for:
Language Learners : Seeking quick translations and pronunciation guides for Chinese language studies.
Travelers : Looking to communicate effectively while traveling in Chinese-speaking regions.
Businesses : Aiming to provide multilingual support to customers and clients.

Benefits
Enhanced Learning : Provides comprehensive translations, including pinyin, aiding in language acquisition.
User-Friendly Interface : Real-time loading animations and prompt replies ensure a smooth user experience.
Scalable Deployment : Easily integrates with Line's extensive user base for widespread accessibility.



## Template JSON

```
{
  "id": "iFkGAiVn3yBlykIG",
  "meta": {
    "instanceId": "558d88703fb65b2d0e44613bc35916258b0f0bf983c5d4730c00c424b77ca36a"
  },
  "name": "Chinese Translator",
  "tags": [
    {
      "id": "IhTa6egt1w8uqn9Z",
      "name": "_ACTIVE",
      "createdAt": "2025-03-12T05:07:05.060Z",
      "updatedAt": "2025-03-12T05:07:05.060Z"
    },
    {
      "id": "0xpEHcJjNRRRMtEj",
      "name": "lin",
      "createdAt": "2025-03-12T05:06:24.112Z",
      "updatedAt": "2025-03-12T05:06:24.112Z"
    }
  ],
  "nodes": [
    {
      "id": "3ebfb7f1-b655-405b-8bde-0219fa92d09c",
      "name": "Line Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        -260,
        -20
      ],
      "webhookId": "b2b119e6-6de5-4684-9a51-4706a1c20caf",
      "parameters": {
        "path": "cn",
        "options": {},
        "httpMethod": "POST"
      },
      "typeVersion": 2
    },
    {
      "id": "b7fc7675-f8d7-4e7e-bec3-f9c626ba1728",
      "name": "Use OpenRouter",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        500,
        -20
      ],
      "parameters": {
        "url": "https://openrouter.ai/api/v1/chat/completions",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"model\": \"qwen/qwen-max\",\n  \"messages\": [\n    {\n      \"role\": \"system\",\n      \"content\": \"please provide chinese character, pinyin and translation in english. if the input is in english, you will translate and also provide chinese character, pinyin and translation in english for each word\"\n    },\n     {\n      \"role\": \"user\",\n      \"content\": \"{{ $('Line Webhook').item.json.body.events[0].message.text }}\"\n    }\n  ]\n} ",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "7Y8q0dS2Y1fcvzTl",
          "name": "OpenRouter.ai"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "fed14d64-d3ea-4a17-98d5-28d889ac4ffa",
      "name": "Line Reply",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        880,
        -20
      ],
      "parameters": {
        "url": "https://api.line.me/v2/bot/message/reply",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"replyToken\": \"{{ $('Line Webhook').item.json.body.events[0].replyToken }}\",\n  \"messages\": [\n    {\n      \"type\": \"text\",\n      \"text\": \"{{ $json.choices[0].message.content.replaceAll(\"\\n\",\"\\\\n\").replaceAll(\"\\n\",\"\").removeMarkdown().removeTags().replaceAll('\"',\"\") }}\"\n    }\n  ]\n} ",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "3IEOzxKOUr6OEXyU",
          "name": "Line @405jtfqs LazyChinese"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "63ae844f-dfc3-4e8f-97d0-c0ec4be7858f",
      "name": "Line Loading Animation",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        120,
        -20
      ],
      "parameters": {
        "url": "https://api.line.me/v2/bot/chat/loading/start",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n    \"chatId\": \"{{ $json.body.events[0].source.userId }}\",\n    \"loadingSeconds\": 60\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "3IEOzxKOUr6OEXyU",
          "name": "Line @405jtfqs LazyChinese"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "7e4cc2a0-958c-4111-909c-fba75a428d5e",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -380,
        -100
      ],
      "parameters": {
        "color": 4,
        "width": 360,
        "height": 560,
        "content": "**Webhook from Line**\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou need to set-up this webhook at Line Manager or Line Developer Console\n\nYou'll need to copy Webhook URL from this node to put in Line Console\n\nAlso, don't forget to remove 'test' part when going for production\n\nhttps://developers.line.biz/en/docs/messaging-api/receiving-messages/\n"
      },
      "typeVersion": 1
    },
    {
      "id": "767827b2-fbca-4dbb-b392-749c25a56c93",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        -100
      ],
      "parameters": {
        "color": 4,
        "width": 360,
        "height": 560,
        "content": "**Line Loading Animation**\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThis node is to only give ... loading animation back in Line.\n\nIt seems stupid but it actually tells user that the workflow is running and you are not left waiting without hope\n\nTo authorize, you can fill in the Line Token in the node here, or you can you header authorization (shown at the 'reply message' node)\n\nhttps://developers.line.biz/en/docs/messaging-api/use-loading-indicator/"
      },
      "typeVersion": 1
    },
    {
      "id": "8cdafc15-3bf8-45e9-8081-901d5c5a7880",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        380,
        -100
      ],
      "parameters": {
        "color": 2,
        "width": 360,
        "height": 560,
        "content": "**OpenRouter.ai**\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThis is to call LLMs model at Openrouter.ai \n\nYou can use it to call ChatGPT, Lllama, Qwen, Deepseek, and much more with just standardized API call and top-up only once\n\nhttps://openrouter.ai/docs/quickstart"
      },
      "typeVersion": 1
    },
    {
      "id": "3e2f4acf-771c-4d55-a13e-b4c874136574",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        760,
        -100
      ],
      "parameters": {
        "color": 4,
        "width": 360,
        "height": 560,
        "content": "**Line Reply**\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThis node is to send reply message via Line\n\nhttps://developers.line.biz/en/docs/messaging-api/sending-messages/\n"
      },
      "typeVersion": 1
    },
    {
      "id": "b17eddaf-da3e-4e21-ab33-9e71f385d734",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -380,
        -200
      ],
      "parameters": {
        "color": 5,
        "width": 780,
        "height": 80,
        "content": "## You can test this workflow by adding Line @405jtfqs"
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "timezone": "Asia/Bangkok",
    "callerPolicy": "workflowsFromSameOwner",
    "errorWorkflow": "A8HoJ5iCrAMPbsLh",
    "executionOrder": "v1"
  },
  "versionId": "aba1f2dc-81ea-4144-b88e-5fd37ee6b247",
  "connections": {
    "Line Webhook": {
      "main": [
        [
          {
            "node": "Line Loading Animation",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Use OpenRouter": {
      "main": [
        [
          {
            "node": "Line Reply",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Line Loading Animation": {
      "main": [
        [
          {
            "node": "Use OpenRouter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
