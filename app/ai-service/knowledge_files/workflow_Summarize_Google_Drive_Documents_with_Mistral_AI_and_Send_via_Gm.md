# Summarize Google Drive Documents with Mistral AI and Send via Gmail

**[View Template](https://n8n.io/workflows/3109-/)**  **Published Date:** 03/09/2025  **Created By:** Swot.AI  **Categories:** `Data & Storage` `Communication` `HITL` `AI` `Langchain`  

## Template Description

This workflow automates document summarization directly from Google Drive, processes the content using Mistral AI, and delivers a clean, styled summary via Gmail. It's ideal for professionals who need quick insights from lengthy documents without manually reading through them.

✅ Key Features:
Google Drive Integration: Fetches a file (PDF/DOCX) from your Drive.
AI Summarization: Uses Mistral AI to extract key points efficiently.
Styled Email Output: Delivers a formatted, easy-to-read summary to your inbox with a timestamp.
Error Handling: Built to skip corrupted files or missing credentials.


🔧 Nodes Breakdown:
1️⃣ Manual Trigger — Starts the workflow manually for easy testing.
2️⃣ Google Drive Node — Downloads a specified file from Google Drive (supports PDF/DOCX).
3️⃣ Mistral Cloud Chat Model Node — Connects to Mistral AI for summarization.
4️⃣ Summarization Chain Node — Breaks the file into chunks, processes content, and generates a concise summary.
5️⃣ Gmail Node — Sends the styled summary directly to the user’s inbox, with custom formatting and current time in the Lagos timezone.

Extra Features:
Dynamic Time Formatting: Supports Lagos timezone (easily adjustable).
HTML Styling: Beautiful email formatting with headers, icons, and line breaks for clarity.
Custom Email Sender Name: Branded output (e.g., "Swot.AI").
Future Expansion: Can extend to WhatsApp or Slack with minor tweaks.

Use Cases:
Legal teams summarizing contracts.
Content creators extracting highlights from research papers.
Business analysts getting insights from reports on-the-go.

Customization Tips:
Change the timezone (Africa/Lagos) to match your preferred location.
Add error-handling nodes for missing files or API failures.
Swap Mistral AI with OpenAI for different summarization behavior.
Change the "Send To" address(email to receive the Summarized texts) with your personal preffered address.**
Change the "Sender Name" from Swot.AI to your preferred Sender Name.**

Why To Use This Workflow?
This automation saves hours of manual reading. It’s perfect for personal productivity, legal analysis, content creation, or business reporting.
With clean formatting and a professional email summary — your team will get instant insights in seconds!

I can make this much better and build others, If Interested: *Swot.ai25@gmail.com*

## Template JSON

```
{
  "id": "Jy1RMuri0WJO5aO4",
  "meta": {
    "instanceId": "c4e0aa659a8ba8396fb6bfa469d1eafbfbfff96c330631376e31cb897259826e",
    "templateCredsSetupCompleted": true
  },
  "name": "Summarize Google Drive Documents with Mistral AI and Send via Gmail",
  "tags": [
    {
      "id": "USkRpjRpntFcI8VH",
      "name": "working",
      "createdAt": "2025-03-09T00:24:01.723Z",
      "updatedAt": "2025-03-09T00:24:01.723Z"
    }
  ],
  "nodes": [
    {
      "id": "680f9002-94fa-48c1-af5f-d2a5305b6291",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        0,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "3fa4ad1a-ce87-44db-b016-bd172c2318eb",
      "name": "Mistral Cloud Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatMistralCloud",
      "position": [
        500,
        240
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "mistralCloudApi": {
          "id": "temjibUluGywOSoS",
          "name": "Mistral Cloud account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "124d62ae-3b46-4e75-a04e-155849fe280d",
      "name": "Download uploaded File from Google Drive",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        220,
        0
      ],
      "parameters": {
        "fileId": {
          "__rl": true,
          "mode": "list",
          "value": "1d0njBA2ZM0zYyJOEbUeFwQmHSYIO7IM2",
          "cachedResultUrl": "https://drive.google.com/file/d/1d0njBA2ZM0zYyJOEbUeFwQmHSYIO7IM2/view?usp=drivesdk",
          "cachedResultName": "Goods and Services Receipt(WCC).pdf"
        },
        "options": {},
        "operation": "download"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "7xFbFgdSc78zERPk",
          "name": "Google Drive account"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "69b7621b-a273-4b0a-be61-4d45bf87618d",
      "name": "Summarization Chain to summarize a file",
      "type": "@n8n/n8n-nodes-langchain.chainSummarization",
      "position": [
        480,
        0
      ],
      "parameters": {
        "options": {
          "binaryDataKey": "data"
        },
        "chunkSize": 800,
        "chunkOverlap": 0,
        "operationMode": "nodeInputBinary"
      },
      "typeVersion": 2
    },
    {
      "id": "573194cd-5f37-422f-b3fa-957187ac3538",
      "name": "Send Summarized text to Gmail",
      "type": "n8n-nodes-base.gmail",
      "position": [
        840,
        0
      ],
      "webhookId": "215c6c67-612c-4b8d-9849-0b796570003d",
      "parameters": {
        "sendTo": "swot.ai25@gmail.com",
        "message": "=<h1 style=\"color: #4CAF50;\">\ud83d\udccc Quick Summary of Your Document! \u2728</h1>\n<p>\n<h2>\ud83d\udcdd Summary:</h2>\n<p>\n{{ $json['response']['text'].replace(\"\\n\", \"<br>\") }}\n<p>\n\n<h3>\ud83d\udcc5 Date Processed: </h3>\n{{ new Date().toLocaleString('en-GB', { timeZone: 'Africa/Lagos' }) }}\n\n\n\n\n\n    ",
        "options": {
          "senderName": "Swot.AI",
          "appendAttribution": false
        },
        "subject": "Here is Your Summarized Response"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "G3K9RkKiyLHtyVzi",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "callerPolicy": "workflowsFromSameOwner",
    "executionOrder": "v1"
  },
  "versionId": "8446e524-8468-4515-8778-be94db41d3e3",
  "connections": {
    "Mistral Cloud Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Summarization Chain to summarize a file",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "When clicking \u2018Test workflow\u2019": {
      "main": [
        [
          {
            "node": "Download uploaded File from Google Drive",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Summarization Chain to summarize a file": {
      "main": [
        [
          {
            "node": "Send Summarized text to Gmail",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Download uploaded File from Google Drive": {
      "main": [
        [
          {
            "node": "Summarization Chain to summarize a file",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
