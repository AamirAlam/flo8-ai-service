# Download and Merge Multiple PDFs from URLs with the CustomJS API

**[View Template](https://n8n.io/workflows/3281-/)**  **Published Date:** 03/21/2025  **Created By:** CustomJS  **Categories:** `Development` `Core Nodes`  

## Template Description


This n8n template demonstrates how to download multiple PDF files from public URLs and merge them into a single PDF using the PDF Toolkit from www.customjs.space.

@custom-js/n8n-nodes-pdf-toolkit

What this workflow does

Defines** an array of PDF URLs.
Splits** the array to process each URL individually.
Downloads** each PDF using an HTTP Request.
Merges** all downloaded PDFs using the Merge PDF node from the @custom-js/n8n-nodes-pdf-toolkit.
Writes** the final merged PDF to disk.

Requirements

A free CustomJS account.
An API Key saved in n8n as credentials of type CustomJS account.

Notice

Community nodes can only be installed on self-hosted instances of n8n.

Usage

Get API key from customJS

Sign up to customJS platform.
Navigate to your profile page
Press "Show" button to get API key

Set Credentials for CustomJS API on n8n

Copy and paster your API key generated from CustomJS here.

Design workflow

A Manual Trigger for starting workflow.
A code node that returns URLs of PDF files as an array
Split Out node for concurrent processing
HTTP node for downloading PDF file locally
Merge PDFs node for merging files
Write to Disk node for saving merged PDF file.

You can replace logic for triggering and returning results.
For example, you can trigger this workflow by calling a webhook and get a result as a response from webhook. Simply replace Manual Trigger and Write to Disk nodes.

Perfect for

Bundling reports or invoices.
Generating document sets from external sources.
Automating PDF handling without writing custom code.


## Template JSON

```
{
  "meta": {
    "instanceId": "b503899dfd9ae32bbf8e1f446a1f2c9b3c59f80c79b274c49b1606b7ae9579e1",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "19f32c25-df26-426d-8e28-f1d29c8571b1",
      "name": "Split Out",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        -200,
        -240
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "data"
      },
      "typeVersion": 1
    },
    {
      "id": "7360c3f9-2e11-4839-b105-ecab66a39af2",
      "name": "HTTP Request1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        20,
        -240
      ],
      "parameters": {
        "url": "={{ $json.data }}",
        "options": {}
      },
      "typeVersion": 4.2
    },
    {
      "id": "49cb0c7b-c9d8-4bf1-afa5-5afab9e7967e",
      "name": "Read/Write Files from Disk2",
      "type": "n8n-nodes-base.readWriteFile",
      "position": [
        460,
        -240
      ],
      "parameters": {
        "options": {},
        "fileName": "test.pdf",
        "operation": "write"
      },
      "typeVersion": 1
    },
    {
      "id": "05ef1b18-481d-40f8-a6b3-712bb9ba2b6f",
      "name": "Read/Write Files from Disk3",
      "type": "n8n-nodes-base.readWriteFile",
      "position": [
        680,
        -240
      ],
      "parameters": {
        "options": {},
        "fileSelector": "test.pdf"
      },
      "typeVersion": 1
    },
    {
      "id": "c8f0971c-e1e0-4add-83cb-932902f80b56",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -640,
        -240
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "b83c51ea-9afc-411a-baad-429776e843f3",
      "name": "PDF Array",
      "type": "n8n-nodes-base.code",
      "position": [
        -420,
        -240
      ],
      "parameters": {
        "jsCode": "return { data: [\n  \"https://www.intewa.com/fileadmin/documents/pdf-file.pdf\", \"https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf\"\n]}"
      },
      "typeVersion": 2
    },
    {
      "id": "b122b6e4-2dfa-4f1f-8547-36ba91ca93f9",
      "name": "Merge PDF",
      "type": "@custom-js/n8n-nodes-pdf-toolkit.mergePdfs",
      "position": [
        240,
        -240
      ],
      "parameters": {},
      "credentials": {
        "customJsApi": {
          "id": "BFGbk0a71fKWY967",
          "name": "CustomJS account"
        }
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Merge PDF": {
      "main": [
        [
          {
            "node": "Read/Write Files from Disk2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "PDF Array": {
      "main": [
        [
          {
            "node": "Split Out",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split Out": {
      "main": [
        [
          {
            "node": "HTTP Request1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request1": {
      "main": [
        [
          {
            "node": "Merge PDF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Read/Write Files from Disk2": {
      "main": [
        [
          {
            "node": "Read/Write Files from Disk3",
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
            "node": "PDF Array",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
