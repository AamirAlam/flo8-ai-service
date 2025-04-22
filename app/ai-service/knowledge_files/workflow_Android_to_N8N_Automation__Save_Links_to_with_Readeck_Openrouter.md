# Android to N8N Automation | Save Links to with Readeck, Openrouter, SerpAPI

**[View Template](https://n8n.io/workflows/3117-/)**  **Published Date:** 03/10/2025  **Created By:** Udit Rawat  **Categories:** `Development` `Core Nodes` `AI` `Langchain`  

## Template Description

This workflow is for automating and centralizing your bookmarking process using AI-powered tagging and seamless integration between your Android device and a self-hosted Read Deck platform (https://readeck.org/en/). This workflow eliminates manual entry, organizes links with smart AI-generated tags, and ensures your bookmarks are always accessible, searchable, and secure.



How It Works

📱 Android Shortcut Integration

Use the HTTP Shortcuts app to create a 1-tap trigger that sends URLs and titles from your Android phone directly to n8n.

🤖 AI-Powered Tagging & Processing
Leverage ChatGPT-4 to analyze content context and auto-generate relevant tags (e.g., “Tech Tutorials,” “Productivity Tools”).
Extract clean titles and URLs from messy shared data (even from apps like Twitter or Reddit).

🔗 Readeck Integration
Automatically save processed bookmarks to your self-hosted Readeck-like platform with structured metadata (title, URL, tags).

⚡ Silent Automation
It runs in the background—no pop-ups or interruptions.

🔒 Pro Security
Optional authentication (API tokens, headers) to protect your data.

Use Case
Perfect for researchers, content creators, or anyone drowning in tabs who wants to:

Save articles, videos, or social posts in one click.
Organize bookmarks with AI-generated tags.
Build a personal knowledge base that’s always accessible.

Tutorial

1️⃣ Set Up Android Shortcut
Install "HTTP Shortcuts" and configure it to send data to your n8n webhook.
Enable “Share Menu” to trigger bookmarks from any app.

2️⃣ Configure n8n Workflow
Import the template and add your Read Deck API token (or similar service).

3️⃣ Test & Scale
Share a link from your phone—watch it appear in Read Deck instantly!

Add error handling or notifications for advanced use.

Note: For self-hosted platforms, ensure your instance is publicly accessible (or use a VPN).

Why Choose This Workflow?
Zero Manual Entry: Save hours of copying/pasting.
AI Organization: Say goodbye to chaotic bookmark folders.
Privacy First: Host your data on your terms.

Transform your bookmarking chaos into a streamlined system—try “Save: Bookmark” today! 🚀

## Template JSON

```
{
  "id": "duORucUF1eNJFOXp",
  "meta": {
    "instanceId": "d16fb7d4b3eb9b9d4ad2ee6a7fbae593d73e9715e51f583c2a0e9acd1781c08e",
    "templateCredsSetupCompleted": true
  },
  "name": "Sell: Android Webhooks",
  "tags": [
    {
      "id": "XZIQK6NdzGvgbZFd",
      "name": "Sell",
      "createdAt": "2025-01-15T12:28:48.424Z",
      "updatedAt": "2025-01-15T12:28:48.424Z"
    }
  ],
  "nodes": [
    {
      "id": "49c1e95f-2339-4783-bd7d-122692ca29e1",
      "name": "SerpAPI",
      "type": "@n8n/n8n-nodes-langchain.toolSerpApi",
      "position": [
        840,
        200
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "serpApi": {
          "id": "w7auLMttmcRSgY7R",
          "name": "Auto: SerpAPI"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "c3db131d-2f76-4c07-a130-3da7813c5fa2",
      "name": "Auto-fixing Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserAutofixing",
      "position": [
        980,
        200
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "4ad243d0-24df-41f8-bc1a-809163b236ce",
      "name": "Structured Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        1120,
        420
      ],
      "parameters": {
        "jsonSchemaExample": "{\n\t\"tags\": [\"AI Apps\", \"Articles\", \"Github\"]\n}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "e0fc52ce-53c1-4e6e-9378-6a664f186946",
      "name": "Get Webhook Content",
      "type": "n8n-nodes-base.webhook",
      "position": [
        0,
        0
      ],
      "webhookId": "fadadd65-756f-45a1-9593-c682600b0495",
      "parameters": {
        "path": "android",
        "options": {},
        "httpMethod": "POST",
        "responseMode": "responseNode",
        "authentication": "basicAuth"
      },
      "credentials": {
        "httpBasicAuth": {
          "id": "RMsm5KvysSzsGpDE",
          "name": "Unnamed credential"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "00cb8828-a466-4739-a46e-a246aa7b1788",
      "name": "Extractor URL & Title",
      "type": "@n8n/n8n-nodes-langchain.informationExtractor",
      "position": [
        220,
        0
      ],
      "parameters": {
        "text": "={{ $json.body.data }}",
        "options": {},
        "schemaType": "fromJson",
        "jsonSchemaExample": "{\n\t\"title\": \"Title of content.\",\n\t\"url\": \"URL of the content.\"\n}"
      },
      "typeVersion": 1
    },
    {
      "id": "c44e6de8-a1a3-4d8e-941c-ef2b507f5faf",
      "name": "If Title and URL provided",
      "type": "n8n-nodes-base.if",
      "position": [
        580,
        0
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "0a4aeb10-3ab5-4232-a380-b41352ac55da",
              "operator": {
                "type": "string",
                "operation": "notEmpty",
                "singleValue": true
              },
              "leftValue": "={{ $json.output.url }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "6cc2348b-1f91-405a-a5ab-df61db0511ba",
      "name": "Content Tagging Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "onError": "continueRegularOutput",
      "position": [
        800,
        -20
      ],
      "parameters": {
        "text": "={{ $json.output.url }}",
        "options": {
          "systemMessage": "Act as an SEO analyst. Use the SerpAPI tool to retrieve detailed information about the provided URL. Analyze the page's content, meta tags, and search engine data to generate human-readable, SEO-friendly tags using natural language phrases (no hyphens). If no relevant tags can be derived, default to the website\u2019s cleaned hostname. Follow these steps:\n\nRetrieve Data: Use SerpAPI to fetch the URL\u2019s metadata (title, description), content keywords, and related entities.\n\nAnalyze Content: Identify primary topics, entities, and high-frequency keywords. Prioritize natural language phrases, and always use title case (e.g., \u201cMachine Learning\u201d instead of \u201cmachine-learning\u201d).\n\nGenerate Tags: Create 2-3 tags with spaces (no hyphens/special characters) and in Title case.\n- Fallback Rule: If content is insufficient, use the website\u2019s hostname (e.g., https://news.example.com \u2192 example). Clean the hostname by removing www, subdomains, and protocols.\n\nValidate: Ensure tags are readable, relevant, and aligned with SerpAPI\u2019s keyword/trend data (e.g., search volume, user intent)."
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.7
    },
    {
      "id": "1e9f7ea2-02d0-4116-a9cc-7f1ab573a7e2",
      "name": "OpenRouter GPT 40 Mini",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
      "position": [
        200,
        180
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "openRouterApi": {
          "id": "ddH6iNlm09UxrXvu",
          "name": "Auto: OpenRouter"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "5ce1b81a-0fbc-4ecb-ab8d-098aca7be467",
      "name": "Buffer Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        680,
        200
      ],
      "parameters": {
        "sessionKey": "={{ $('Get Webhook Content').item.json.headers['cf-ray'] }}",
        "sessionIdType": "customKey",
        "contextWindowLength": 20
      },
      "typeVersion": 1.3
    },
    {
      "id": "185f7332-3a63-41f9-83eb-3af4e4ebd1e2",
      "name": "Create Bookmark",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Create bookmark on ReadDeck",
      "position": [
        1160,
        -20
      ],
      "parameters": {
        "url": "https://readeck.agentsops.pro/api/bookmarks",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "labels",
              "value": "={{ $json.output.tags }}"
            },
            {
              "name": "title",
              "value": "={{ $('If Title and URL provided').item.json.output.title }}"
            },
            {
              "name": "url",
              "value": "={{ $('Extractor URL & Title').item.json.output.url }}"
            }
          ]
        },
        "genericAuthType": "httpHeaderAuth",
        "headerParameters": {
          "parameters": [
            {
              "name": "accept",
              "value": "application/json"
            },
            {
              "name": "content-type",
              "value": "application/json"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "aE5iIuGK9nf08RwX",
          "name": "Auto: Readeck"
        }
      },
      "notesInFlow": true,
      "typeVersion": 4.2
    },
    {
      "id": "613a461d-f941-4149-b71c-050c25d17648",
      "name": "If Bookmark Created",
      "type": "n8n-nodes-base.if",
      "position": [
        1380,
        -20
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "bc4d7840-40bd-4b02-a4a5-9967fcec0ca2",
              "operator": {
                "type": "number",
                "operation": "equals"
              },
              "leftValue": "={{ $json.status }}",
              "rightValue": 202
            },
            {
              "id": "ef47dc64-8ebe-4b66-aa2b-917702097d4c",
              "operator": {
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $json.message }}",
              "rightValue": "Link submited"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "4879057b-e3da-4c6d-9a77-44fed749c119",
      "name": "Bookmark Created",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1600,
        -20
      ],
      "parameters": {
        "options": {},
        "respondWith": "text",
        "responseBody": "Your bookmark has been successfully created! You can now easily access this content anytime from your bookmarks section."
      },
      "typeVersion": 1.1
    },
    {
      "id": "c81bfb95-258e-40fe-a006-f789b0fdf9b9",
      "name": "Bookmark Not Created",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1600,
        -200
      ],
      "parameters": {
        "options": {},
        "respondWith": "text",
        "responseBody": "Bookmarking this content is not possible at the moment. Please try again later or check if bookmarking is supported for this type of content."
      },
      "typeVersion": 1.1
    },
    {
      "id": "e9c5e016-bd00-4ec8-bc25-3866ef950bf8",
      "name": "Title & URL Not Found",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        800,
        -180
      ],
      "parameters": {
        "options": {},
        "respondWith": "text",
        "responseBody": "Bookmarking this content is not possible at the moment. Please try again later or check if bookmarking is supported for this type of content."
      },
      "typeVersion": 1.1
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "2968d4c9-1aec-4357-bb40-76567b325ee5",
  "connections": {
    "SerpAPI": {
      "ai_tool": [
        [
          {
            "node": "Content Tagging Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Buffer Memory": {
      "ai_memory": [
        [
          {
            "node": "Content Tagging Agent",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "Create Bookmark": {
      "main": [
        [
          {
            "node": "If Bookmark Created",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Webhook Content": {
      "main": [
        [
          {
            "node": "Extractor URL & Title",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If Bookmark Created": {
      "main": [
        [
          {
            "node": "Bookmark Created",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Bookmark Not Created",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Content Tagging Agent": {
      "main": [
        [
          {
            "node": "Create Bookmark",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extractor URL & Title": {
      "main": [
        [
          {
            "node": "If Title and URL provided",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenRouter GPT 40 Mini": {
      "ai_languageModel": [
        [
          {
            "node": "Extractor URL & Title",
            "type": "ai_languageModel",
            "index": 0
          },
          {
            "node": "Content Tagging Agent",
            "type": "ai_languageModel",
            "index": 0
          },
          {
            "node": "Auto-fixing Output Parser",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Structured Output Parser": {
      "ai_outputParser": [
        [
          {
            "node": "Auto-fixing Output Parser",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Auto-fixing Output Parser": {
      "ai_outputParser": [
        [
          {
            "node": "Content Tagging Agent",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "If Title and URL provided": {
      "main": [
        [
          {
            "node": "Content Tagging Agent",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Title & URL Not Found",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
