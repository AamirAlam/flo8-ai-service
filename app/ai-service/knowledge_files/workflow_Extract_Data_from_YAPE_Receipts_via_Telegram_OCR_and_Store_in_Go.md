# ⚛️🐋🤖 Extract Data from YAPE Receipts via Telegram OCR and Store in Google Sheets

**[View Template](https://n8n.io/workflows/3073-/)**  **Published Date:** 03/03/2025  **Created By:** Jesús Pérez   **Categories:** `Data & Storage` `Productivity` `Communication` `HITL` `Development` `Core Nodes` `AI` `Langchain`  

## Template Description

Detailed Technical Description
This n8n workflow automates Yape payment receipt processing, integrating Telegram bot, AI-powered OCR, and Google Sheets automation. By leveraging ChatGPT Vision Computing, it extracts and structures transaction details, eliminating the need for manual entry. Ideal for freelancers, businesses, and finance teams, this workflow ensures error-free, real-time financial tracking. The AI agent powered by DeepSeek refines and formats the extracted text, storing it in Google Sheets for easy accessibility and reporting. Users can track payments, monitor cash flow, and generate financial reports without any manual work. This seamless integration boosts efficiency, reduces errors, and automates financial record-keeping with 100% accuracy.

🛠️ Technologies Used:
✅n8n – Workflow orchestrator.
✅Telegram – Handles image reception and notifications.
✅Google Drive – Manages file creation and storage.
✅Google Sheets – Automatically logs extracted data into spreadsheets.

🤖Artificial Intelligence:
✅ChatGPT Vision Computing – Performs OCR on payment receipts.
✅DeepSeek AI – Organizes and converts extracted data into a structured format.

📌 pre-conditions:
📩 A Telegram Bot – Must be created to receive images. Setup Guide
🔑 Google Sheets API Key – Required to store extracted data. Setup Guide
⚛️ ChatGPT API Key – Used for OCR and AI text extraction. Get it here
🐋 DeepSeek API Key – Processes extracted text into structured data. Get it here
1️⃣ Image Reception & OCR Processing 📩
The user attaches a Yape payment receipt image to the Telegram bot conversation. 🤳🏻

2️⃣ Analyze Image (OCR) 👁️‍🗨️
A ⚛️ChatGPT Vision Computing model processes the image and extracts all visible text, ensuring high-accuracy OCR for structured data extraction.

3️⃣ Analyze and format text
Intelligent Data Processing with AI 🤖
The extracted text is sent to a 🐋DeepSeek-based AI agent that:
Identifies and structures key transaction details (amount, date, sender, transaction ID, etc.).
Converts the data into a structured JSON format.

4️⃣ Data Storage in Google Sheets 📊
Google Drive integration is established.
If the Google Sheets file does not exist, it is automatically created.

Extracted data is automatically recorded in the corresponding spreadsheet, enabling effortless tracking and streamlined financial organization.

🚀 Benefits:
✅ Time-saving – Eliminates manual payment processing.
✅ Error-free data entry – Reduces human mistakes in record-keeping.
✅ 100% automation – No manual intervention required.
✅ Seamless integration – Easily connects with other workflows.





💡NOTE: The extracted transaction data will be stored in a Google Sheets file with the following columns:

|      Column Name      | Description                                               |
|:---------------------:|-----------------------------------------------------------|
| id                | Unique identifier for each transaction.                   |
| beneficiaryName   | Name of the recipient of the payment.                     |
| amount            | Payment amount in the specified currency.                 |
| currency          | Currency used for the transaction (e.g., PEN, USD).       |
| company           | The entity or service handling the transaction.           |
| date              | Date of the transaction in a human-readable format.       |
| hour              | Time of the transaction.                                  |
| originalDate      | The exact date extracted from the receipt.                |
| dateToISO         | Standardized ISO 8601 date format.                        |
| operation         | Type of financial operation (e.g., deposit, transfer).    |
| operationNumber   | Unique operation number provided by the payment system.   |
| beneficiaryNumber | Account or phone number of the recipient.                 |
| commission        | Any commission or fee charged for the transaction.        |
| account           | Account number or reference used for the payment.         |
| channel           | Payment method used (e.g., app, POS, bank transfer).      |
| agentCode         | Identifier of the agent or entity processing the payment. |

This workflow is perfect for businesses, freelancers, and individuals who need a fully automated solution to process Yape payment receipts efficiently. By leveraging AI-powered OCR and structured data extraction, it eliminates manual effort, reduces errors, and ensures that all transactions are accurately logged in Google Sheets. Whether you're managing personal finances, freelance payments, or business transactions, this system provides a seamless, hands-free approach to financial tracking, allowing you to focus on what truly matters.

## Template JSON

```
{
  "id": "1Pv5C6tDnHKLP42m",
  "meta": {
    "instanceId": "776aed41e1386255bdcc5feb11ff26417e83dd7ef78fc4f1d04858678b48a66f",
    "templateCredsSetupCompleted": true
  },
  "name": "Extract Data from YAPE Receipts via Telegram OCR and Store in Google Sheets",
  "tags": [
    {
      "id": "xZhfVLCNfp6aB2RH",
      "name": "Agente",
      "createdAt": "2025-03-04T07:58:57.181Z",
      "updatedAt": "2025-03-04T07:58:57.181Z"
    }
  ],
  "nodes": [
    {
      "id": "556d84c0-06f4-487d-8ae5-9b95e2405168",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        720,
        -340
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "77d801b4-01b0-404d-8c8d-5a6631c5dcfd",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -880,
        -340
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "96ee5290-a18a-4f06-900f-76e18cf5d01e",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -380,
        -340
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "2432598f-f665-4af2-b4c5-1436fa3ac4fa",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        180,
        -340
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "d4d83da2-6ea4-462a-999c-6acb76045e41",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        180,
        400
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "cdf5c835-2e62-4e43-a133-d06b3deb6261",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        180,
        40
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "f7e07754-7daa-4eb0-9988-f0c410cdd909",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1520,
        -340
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "2c0d137c-d9cf-4f6a-a17c-b6406940f21c",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1920,
        -340
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "0bb7d6ee-53a7-4774-bf67-503d38b54fee",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2460,
        -340
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "7d08bb2e-19f7-4e09-9057-9ec595eca07b",
      "name": "Sticky Note11",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1520,
        140
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "c80b2310-3cd4-42fe-826a-af0498339f2a",
      "name": "\ud83d\udece\ufe0fTelegram Listener",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        -300,
        -160
      ],
      "webhookId": "d618052b-6fbf-41eb-8f5d-94ec3d1e52a3",
      "parameters": {},
      "typeVersion": 1.1
    },
    {
      "id": "7eec866f-c414-4039-b2d6-c71e8be0e84a",
      "name": "\ud83d\udd00 Message Classifier",
      "type": "n8n-nodes-base.switch",
      "position": [
        -60,
        -160
      ],
      "parameters": {},
      "typeVersion": 3.2
    },
    {
      "id": "1c3196df-9e55-4740-bc3d-dad52b4c42a1",
      "name": "Sticky Note9",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -380,
        140
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "04b483a8-4dd1-457c-b986-a1be02c1a3ea",
      "name": "Sticky Note12",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -340,
        -180
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "65bcfc3a-6c2f-4854-b06b-b97b81a1671b",
      "name": "Sticky Note13",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -100,
        -180
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "0f553483-1028-49a3-8909-af240c61e350",
      "name": "Sticky Note14",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -360,
        -320
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "c8574753-3971-4b46-819e-a93cb43868ec",
      "name": "\ud83d\udd00 Start Command Handle",
      "type": "n8n-nodes-base.switch",
      "position": [
        260,
        -240
      ],
      "parameters": {},
      "typeVersion": 3.2
    },
    {
      "id": "8dfcb5c5-0a3a-4be1-835d-43ae8058529c",
      "name": "\u2709\ufe0f Send Welcome Message",
      "type": "n8n-nodes-base.telegram",
      "position": [
        500,
        -240
      ],
      "webhookId": "6166a70a-dfc2-49f3-816d-40f9f43771e4",
      "parameters": {},
      "typeVersion": 1.2
    },
    {
      "id": "cdfc4a26-f699-41a9-8139-ef8b46c0abb4",
      "name": "Sticky Note15",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        180,
        680
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "4e81ffe0-53f5-41c2-a9bd-2121791631bd",
      "name": "Sticky Note16",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        180,
        -60
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "fab3c3d3-49f8-42f2-82e8-c9b7532c3f3a",
      "name": "\ud83d\uddc2\ufe0fSelect Best Quality Image",
      "type": "n8n-nodes-base.code",
      "notes": "Process the message to get the file_id of the image",
      "position": [
        240,
        500
      ],
      "parameters": {},
      "notesInFlow": true,
      "typeVersion": 2
    },
    {
      "id": "05bac483-aaf3-494b-8cf6-629d2379cf62",
      "name": "Sticky Note17",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        180,
        300
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "cf8f52ca-ba7f-4645-af92-f35cf568e5c4",
      "name": "\ud83d\uddbc\ufe0fRetrieve Image Attachment",
      "type": "n8n-nodes-base.telegram",
      "position": [
        380,
        120
      ],
      "webhookId": "f0ac13cf-72df-4bb8-8a80-b6baba880b06",
      "parameters": {},
      "typeVersion": 1.2
    },
    {
      "id": "d89cb70a-e043-4273-8a64-e4e820a30193",
      "name": "\ud83d\uddbc\ufe0fDownload High-Quality Image",
      "type": "n8n-nodes-base.telegram",
      "position": [
        480,
        500
      ],
      "webhookId": "f0ac13cf-72df-4bb8-8a80-b6baba880b06",
      "parameters": {},
      "typeVersion": 1.2
    },
    {
      "id": "c50cdead-3d99-4cb5-ad69-852f869bb2d5",
      "name": "\ud83d\udcc4 Extract Text with OCR",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        840,
        -180
      ],
      "parameters": {},
      "typeVersion": 1.8
    },
    {
      "id": "31c8539d-9947-4ff4-abf8-c219134a8737",
      "name": "\ud83e\udd16 AI Data Processor",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        1140,
        -180
      ],
      "parameters": {},
      "typeVersion": 1.7
    },
    {
      "id": "8b78d2f1-5045-470d-9e0c-8e77a1553573",
      "name": "\ud83e\udde0 AI Model for Processing",
      "type": "@n8n/n8n-nodes-langchain.lmChatDeepSeek",
      "position": [
        1100,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "e6fec2a6-adaa-4d10-a485-10309843e4f6",
      "name": "Sticky Note18",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        720,
        140
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "1c9d91e4-c891-46ca-97c1-9d1304ca2cd7",
      "name": "\ud83d\udd0d Find Google Sheet in Drive",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        1640,
        -120
      ],
      "parameters": {},
      "typeVersion": 3,
      "alwaysOutputData": false
    },
    {
      "id": "098a5510-3385-46bf-831e-5983d3971fa1",
      "name": "\ud83d\udd04 Prepare Data for Insertion",
      "type": "n8n-nodes-base.code",
      "position": [
        2000,
        -120
      ],
      "parameters": {},
      "typeVersion": 2
    },
    {
      "id": "332f9c11-a32a-45c7-8837-18a6ff1f9f70",
      "name": "\ud83d\udcd1 Insert Data into Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        2240,
        -120
      ],
      "parameters": {},
      "typeVersion": 4.5
    },
    {
      "id": "3165b063-3271-4ca8-a2a9-7a06c58fea01",
      "name": "Sticky Note19",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2460,
        140
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "d534f380-0059-4064-9560-d2a6a9f1ebe0",
      "name": "\u2709\ufe0f Send Analysis Result to User",
      "type": "n8n-nodes-base.telegram",
      "position": [
        2580,
        -200
      ],
      "webhookId": "6f98701d-3b50-4920-904a-2dfae8b5817e",
      "parameters": {},
      "typeVersion": 1.2
    },
    {
      "id": "eddd1ab0-a4f7-45d7-8694-d064081b4c1d",
      "name": "Sticky Note20",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1920,
        140
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "271694c5-f43e-45a7-8e16-635fe1d888a3",
      "name": "Sticky Note21",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2740,
        -200
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "c1cb5829-a6b3-45a8-91da-3bc257f50a4d",
  "connections": {
    "\ud83e\udd16 AI Data Processor": {
      "main": [
        [
          {
            "node": "\ud83d\udd0d Find Google Sheet in Drive",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "\ud83d\udd00 Message Classifier": {
      "main": [
        [
          {
            "node": "\ud83d\udd00 Start Command Handle",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "\ud83d\uddbc\ufe0fRetrieve Image Attachment",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "\ud83d\uddc2\ufe0fSelect Best Quality Image",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "\ud83d\udece\ufe0fTelegram Listener": {
      "main": [
        [
          {
            "node": "\ud83d\udd00 Message Classifier",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "\ud83d\udd00 Start Command Handle": {
      "main": [
        [
          {
            "node": "\u2709\ufe0f Send Welcome Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "\ud83d\udcc4 Extract Text with OCR": {
      "main": [
        [
          {
            "node": "\ud83e\udd16 AI Data Processor",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "\ud83e\udde0 AI Model for Processing": {
      "ai_languageModel": [
        [
          {
            "node": "\ud83e\udd16 AI Data Processor",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "\ud83d\udd04 Prepare Data for Insertion": {
      "main": [
        [
          {
            "node": "\ud83d\udcd1 Insert Data into Google Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "\ud83d\udd0d Find Google Sheet in Drive": {
      "main": [
        [
          {
            "node": "\ud83d\udd04 Prepare Data for Insertion",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    },
    "\ud83d\uddbc\ufe0fRetrieve Image Attachment": {
      "main": [
        [
          {
            "node": "\ud83d\udcc4 Extract Text with OCR",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "\ud83d\uddc2\ufe0fSelect Best Quality Image": {
      "main": [
        [
          {
            "node": "\ud83d\uddbc\ufe0fDownload High-Quality Image",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "\ud83d\uddbc\ufe0fDownload High-Quality Image": {
      "main": [
        [
          {
            "node": "\ud83d\udcc4 Extract Text with OCR",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "\ud83d\udcd1 Insert Data into Google Sheets": {
      "main": [
        [
          {
            "node": "\u2709\ufe0f Send Analysis Result to User",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
