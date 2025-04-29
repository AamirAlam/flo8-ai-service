# Automatically issue training certificates and send via Gmail

**[View Template](https://n8n.io/workflows/3114-/)**  **Published Date:** 03/09/2025  **Created By:** Nathan Lee  **Categories:** `Core Nodes` `Marketing` `Development` `Communication` `HITL`  

## Template Description

1. Workflow Overview

This n8n workflow automates the generation and delivery of student completion certificates.

Features:
Retrieves student data from the n8n integrated datastore and processes it.
Loads a certificate template image and inserts the student's name and unique ID.
Generates a completion certificate and sends it automatically via email.

By using this workflow, the certificate issuance process can be streamlined and efficiently managed.

2. Prerequisites
To execute this workflow, you need to set up the following:

✅ Gmail OAuth2 Integration (Required for sending certificates via Gmail in n8n)  
✅ n8n Training Customer Datastore Connection (Ensure access to student data from the datastore)  
✅ Google Fonts Installation (Required for using Courier New and Comic Sans MS fonts)  

3. Key Features & Roles

📌 Node List & Functions

When clicking 'Test workflow' (Manual Trigger)  
   Triggers the workflow manually for testing

Customer Datastore (n8n training)  
   Retrieves student data from n8n's datastore

Get Email & Name (Set Node)  
   Extracts the student's name and email

Generate Crypto (UUID Generation)  
   Creates a unique ID for each certificate

Load Image (HTTP Request)  
   Loads the certificate template image

Write Text(name) / Write Text(uuid) (Edit Image)  
   Inserts the student's name and UUID onto the image to generate the certificate

Send Email (Gmail Node)  
   Automatically sends the generated certificate via email

4. Workflow Process (Step-by-Step)

1️⃣ Retrieve Student Data - Fetches name and email from the n8n Training Customer Datastore
2️⃣ Generate UUID - Creates a unique ID for each certificate
3️⃣ Load Certificate Template Image - Fetches the template via HTTP request
4️⃣ Insert Name and UUID into the Image
5️⃣ Send Certificate via Gmail

5. Expected Outputs

Upon successful execution,** the student receives an email with the certificate image attached.
Example of the sent email:**
    Dear John Doe,
  
  You have successfully completed this training program. Please find your completion certificate attached.
  Completion Date: 2025.02.22
  
  Best regards,
  Data Popcorn Team
  Certificate Sharing Method:** The certificate can be downloaded and shared via email.

## Template JSON

```
{
  "meta": {
    "instanceId": "a8fb7fd31983317952de5fe842ded2643867d47ad03573d086b1bc8ab17aa03b",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "7d656159-546a-4250-b0d8-a32f441ca139",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -220,
        960
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "fd65ad82-7bb5-4db1-a258-23c5ef5a0ad2",
      "name": "Customer Datastore (n8n training)",
      "type": "n8n-nodes-base.n8nTrainingCustomerDatastore",
      "position": [
        40,
        960
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "d900545f-d640-4c0e-88ec-ce3e35344dde",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -20,
        640
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "798ac317-0a5c-4bd5-a420-43cc71da5c7f",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        740,
        880
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "5dc5127e-92de-490e-af1e-2e654a502857",
      "name": "Sticky Note9",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1100,
        880
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "98ea16c7-804e-4358-8255-b8662fde54f2",
      "name": "Sticky Note10",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1880,
        880
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "02de8ba7-4460-47ac-8def-153d826e5d0b",
      "name": "Sticky Note11",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        460,
        880
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "0494d17c-55f2-4899-98b4-42a296984418",
      "name": "Sticky Note12",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -20,
        880
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "2cfa592f-c392-4c3d-861e-189fbc7c3e16",
      "name": "Sticky Note13",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1380,
        880
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "7f7ec25f-95c8-4c51-9238-7e8fece972c5",
      "name": "Write Text(name)",
      "type": "n8n-nodes-base.editImage",
      "onError": "continueRegularOutput",
      "position": [
        1440,
        960
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "31e2a831-77fc-40fc-9794-50409e5af0f9",
      "name": "Write Text(uuid)",
      "type": "n8n-nodes-base.editImage",
      "position": [
        1660,
        960
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "8a6ac21d-3d1c-4db9-8532-651d0666dc5d",
      "name": "Get Email & Name",
      "type": "n8n-nodes-base.set",
      "position": [
        240,
        960
      ],
      "parameters": {},
      "typeVersion": 3.4
    },
    {
      "id": "c030a257-de4c-4d35-804f-886bce7c7d5c",
      "name": "Generate Crypto",
      "type": "n8n-nodes-base.crypto",
      "position": [
        520,
        960
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "f00027db-a66b-4561-94f0-cffc46344fba",
      "name": "Load Image",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        840,
        960
      ],
      "parameters": {},
      "typeVersion": 4.2
    },
    {
      "id": "67ec87f8-e2e2-4eb7-8be9-12b57a58a844",
      "name": "Get Info",
      "type": "n8n-nodes-base.editImage",
      "onError": "continueRegularOutput",
      "position": [
        1160,
        960
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "5f148b64-7ba3-4439-9624-07969c18f7b1",
      "name": "Send Email",
      "type": "n8n-nodes-base.gmail",
      "position": [
        1960,
        960
      ],
      "webhookId": "ef7b21c5-d760-4192-8c90-f75b8f0e2752",
      "parameters": {},
      "typeVersion": 2.1
    },
    {
      "id": "e09baae4-c616-49cb-b296-10f9b5484192",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        720,
        1140
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "3663c33c-2de4-4abc-be42-bd71a10c7313",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1640,
        1140
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Get Info": {
      "main": [
        [
          {
            "node": "Write Text(name)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Load Image": {
      "main": [
        [
          {
            "node": "Get Info",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate Crypto": {
      "main": [
        [
          {
            "node": "Load Image",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Email & Name": {
      "main": [
        [
          {
            "node": "Generate Crypto",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Write Text(name)": {
      "main": [
        [
          {
            "node": "Write Text(uuid)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Write Text(uuid)": {
      "main": [
        [
          {
            "node": "Send Email",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Customer Datastore (n8n training)": {
      "main": [
        [
          {
            "node": "Get Email & Name",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When clicking \u2018Test workflow\u2019": {
      "main": [
        [
          {
            "node": "Customer Datastore (n8n training)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
