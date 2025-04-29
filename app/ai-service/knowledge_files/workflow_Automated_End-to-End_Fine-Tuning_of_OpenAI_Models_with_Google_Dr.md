# Automated End-to-End Fine-Tuning of OpenAI Models with Google Drive Integration

**[View Template](https://n8n.io/workflows/2781-/)**  **Published Date:** 01/23/2025  **Created By:** Davide  **Categories:** `Development` `Core Nodes` `Data & Storage` `AI` `Langchain`  

## Template Description

1. How it Works  
This n8n workflow automates fine-tuning OpenAI models through these key steps:  
Manual Trigger**:  
  Starts with the "When clicking ‘Test workflow’" event to initiate the process.  
  Downloads a .jsonl file from Google Drive   
Upload to OpenAI**:  
  Uploads the .jsonl file to OpenAI via the "Upload File" node (with purpose "fine-tune").  
Create Fine-tuning Job**:  
  Sends a POST request to the endpoint https://api.openai.com/v1/fine_tuning/jobs with:  
        {  
      "training_file": "{{ $json.id }}",  
      "model": "gpt-4o-mini-2024-07-18"  
    }  
      OpenAI automatically starts training the model based on the provided file.  
Interaction with the Trained Model**:  
  An "AI Agent" uses the custom model (e.g., ft:gpt-4o-mini-2024-07-18:n3w-italia::XXXX7B) to respond to chat messages.  

2. Set up Steps  
To configure the workflow:  
Prepare the Training File:  
   Create a .jsonl file following the specified syntax (e.g., travel assistant Q/A examples).  
   Upload it to Google Drive and update the ID in the "Google Drive" node.  

Configure Credentials:  
   Google Drive: Connect an account via OAuth2 (googleDriveOAuth2Api).  
   OpenAI: Add your API key in the "OpenAI Chat Model" and "Upload File" nodes.  

Customize the Model:  
   In the "OpenAI Chat Model" node, specify the name of your fine-tuned model (e.g., ft:gpt-4o-mini-...).  
   Update the HTTP request body (Create Fine-tuning Job) if needed (e.g., a different base model).  

Start the Workflow:  
   Use the manual trigger ("Test workflow") to begin the upload and training process.  
   Test the model via the "Chat Trigger" (chat messages).  

Integrated Documentation:  
   Follow the instructions in the Sticky Notes to:  
     Properly format the .jsonl (Step 1).  
     Monitor progress on OpenAI (Step 2, link: https://platform.openai.com/finetune/).  

Note: Ensure the .jsonl file adheres to OpenAI’s required structure and that credentials are valid.

## Template JSON

```
{
  "id": "gAzsjTGbfWuvAObi",
  "meta": {
    "instanceId": "a4bfc93e975ca233ac45ed7c9227d84cf5a2329310525917adaf3312e10d5462",
    "templateCredsSetupCompleted": true
  },
  "name": "Fine-tuning with OpenAI models",
  "tags": [
    {
      "id": "2VG6RbmUdJ2VZbrj",
      "name": "Google Drive",
      "createdAt": "2024-12-04T16:50:56.177Z",
      "updatedAt": "2024-12-04T16:50:56.177Z"
    },
    {
      "id": "paTcf5QZDJsC2vKY",
      "name": "OpenAI",
      "createdAt": "2024-12-04T16:52:10.768Z",
      "updatedAt": "2024-12-04T16:52:10.768Z"
    }
  ],
  "nodes": [
    {
      "id": "ff65c2db-6a94-4e56-a10c-2538c9617df6",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        220,
        320
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "208fc618-0543-4552-bd65-9c808c879d88",
      "name": "Google Drive",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        440,
        320
      ],
      "parameters": {
        "fileId": {
          "__rl": true,
          "mode": "list",
          "value": "1wvlEcbxFIENvqL-bACzlLEfy5gA6uF9J",
          "cachedResultUrl": "https://drive.google.com/file/d/1wvlEcbxFIENvqL-bACzlLEfy5gA6uF9J/view?usp=drivesdk",
          "cachedResultName": "test_fine_tuning.jsonl"
        },
        "options": {
          "binaryPropertyName": "data.jsonl",
          "googleFileConversion": {
            "conversion": {
              "docsToFormat": "application/pdf"
            }
          }
        },
        "operation": "download"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "HEy5EuZkgPZVEa9w",
          "name": "Google Drive account"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "3580d925-c8c9-446f-bfa4-faae5ed3f44a",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        500,
        800
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.7
    },
    {
      "id": "d309da46-c44e-47b7-bb46-5ee6fe7e6964",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        220,
        800
      ],
      "webhookId": "88151d03-e7f5-4c9a-8190-7cff8e849ca2",
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.1
    },
    {
      "id": "84b896f7-d1dd-4485-a088-3c7f8154a406",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        380,
        1000
      ],
      "parameters": {
        "model": "ft:gpt-4o-mini-2024-07-18:n3w-italia::AsVfsl7B",
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "CDX6QM4gLYanh0P4",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "3bff93e4-70c3-48c7-b0b3-d2a9881689c4",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        220,
        560
      ],
      "parameters": {
        "width": 556.5145228215765,
        "height": 211.35269709543567,
        "content": "# Step 2\n\nOnce the .jsonl file for training is uploaded (See the entire process here.: https://platform.openai.com/finetune/), a \"new model\" will be created and made available via your API. OpenAI will automatically train it based on the uploaded .jsonl file. If the training is successful, the new model will be accessible via API.\n\neg. ft:gpt-4o-mini-2024-07-18:n3w-italia::XXXXX7B"
      },
      "typeVersion": 1
    },
    {
      "id": "ea67edd7-986d-47cd-bc1a-5df49851e27b",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        220,
        -5.676348547717737
      ],
      "parameters": {
        "width": 777.3941908713687,
        "height": 265.161825726141,
        "content": "# Step 1\n\nCreate the training file .jsonl with the following syntax and upload it to Drive.\n\n{\"messages\": [{\"role\": \"system\", \"content\": \"You are an experienced and helpful travel assistant.\"}, {\"role\": \"user\", \"content\": \"What documents are needed to travel to the United States?\"}, {\"role\": \"assistant\", \"content\": \"To travel to the United States, you will need a valid passport and an ESTA authorization, which you can apply for online. Make sure to check the specific requirements based on your nationality.\"}]}\n....\n\nThe file will be uploaded here: https://platform.openai.com/storage/files\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "87df3b85-01ac-41db-b5b6-a236871fa4e2",
      "name": "Upload File",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        660,
        320
      ],
      "parameters": {
        "options": {
          "purpose": "fine-tune"
        },
        "resource": "file",
        "binaryPropertyName": "data.jsonl"
      },
      "credentials": {
        "openAiApi": {
          "id": "CDX6QM4gLYanh0P4",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.8
    },
    {
      "id": "c8ec10d4-ff83-461f-94ac-45b68d298276",
      "name": "Create Fine-tuning Job",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        900,
        320
      ],
      "parameters": {
        "url": "https://api.openai.com/v1/fine_tuning/jobs",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"training_file\": \"{{ $json.id }}\",\n  \"model\": \"gpt-4o-mini-2024-07-18\"\n} ",
        "sendBody": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "headerParameters": {
          "parameters": [
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "0WeSLPyZXOxqMuzn",
          "name": "OpenAI API"
        }
      },
      "typeVersion": 4.2
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "a4aa95f5-132b-4aa3-a7f5-3bb316e00133",
  "connections": {
    "Upload File": {
      "main": [
        [
          {
            "node": "Create Fine-tuning Job",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Drive": {
      "main": [
        [
          {
            "node": "Upload File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "When chat message received": {
      "main": [
        [
          {
            "node": "AI Agent",
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
            "node": "Google Drive",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
