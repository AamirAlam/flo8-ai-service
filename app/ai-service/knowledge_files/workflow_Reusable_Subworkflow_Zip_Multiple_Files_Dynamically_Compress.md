# Reusable Subworkflow Zip Multiple Files Dynamically (Compress)

**[View Template](https://n8n.io/workflows/2690-/)**  **Published Date:** 01/02/2025  **Created By:** Simon  **Categories:** `Data & Storage` `Core Nodes` `Development`  

## Template Description

📦 Zip Multiple Files Dynamically  

This template enables you to dynamically bundle multiple files into a ZIP archive. Designed to be used as a Subworkflow, it’s modular, flexible, and easy to integrate into various workflows. The output is a single ZIP file with a name that includes the current date, time, and fileName.

Shoutout:
Code from: Tom (mutedjam)

👤 Who is this for?  
This workflow is perfect for:  
🚀 Businesses automating file archiving tasks.  
💻 Developers managing files programmatically.  
📂 Anyone needing a reusable solution for bundling files into ZIP archives.

❓ What problem is this workflow solving?  
Manually zipping multiple files is:  
🕒 Time-consuming.  
🤔 Prone to errors.  

This workflow automates the process and, as a Subworkflow, ensures:  
⚡ Consistent file archiving across different workflows.  
🛠️ Reduced manual effort.  
📈 Streamlined integration into existing automation.

🔧 What this workflow does  
🗂️ Dynamically collects binary files from the input.  
📦 Bundles them into a single ZIP archive.  
🕒 Names the ZIP file with the current date, time, and a customizable fileName.  
✅ Outputs the ZIP file, ready for storage or further processing.  

⚙️ Setup  
🔗 Add this Subworkflow to your existing workflows.  
📥 Pass the binary files as input to the Subworkflow.  
▶️ Call the Subworkflow to generate a ZIP file.

🛠️ How to customize this workflow to your needs  
🌐 File Sources**: Adjust the input nodes in your parent workflow to connect to your preferred file sources.  
📝 File Naming**: Customize the logic for the output fileName in the Subworkflow.  
🚀 Additional Use Cases**: Use this Subworkflow in various scenarios, such as:  
  ✉️ Sending ZIP files via email.  
  ☁️ Uploading ZIP files to cloud storage.  
  🔄 Triggering further automation.

🎉 Why use this as a Subworkflow?  
Instead of building a fixed ZIP functionality for every workflow, this template offers a reusable solution that can be integrated into many different workflows effortlessly. Save time and ensure consistency across your automation projects! 💡


## Template JSON

```
{
  "id": "r3qHlCVCczqTw3pP",
  "meta": {
    "instanceId": "1bc0f4fa5e7d17ac362404cbb49337e51e5061e019cfa24022a8667c1f1ce287"
  },
  "name": "Zip multiple files",
  "tags": [],
  "nodes": [
    {
      "id": "8de50ed2-b298-4701-8747-f6c7158fa15f",
      "name": "Execute Workflow Trigger",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        0,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "5e03dfdd-696e-4a04-99e9-4094ae4371ac",
      "name": "Compression",
      "type": "n8n-nodes-base.compression",
      "position": [
        460,
        0
      ],
      "parameters": {
        "fileName": "=data{{$now.format('yyyy-MM-dd-tt')}}.zip",
        "operation": "compress",
        "binaryPropertyName": "={{ $json.binary_keys }}"
      },
      "typeVersion": 1.1
    },
    {
      "id": "e25abf55-fb05-47d0-ba65-9b4e2f08d856",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -340,
        -100
      ],
      "parameters": {
        "height": 360,
        "content": "## About\nUse me as modular workflow. Instead of building me fixed in your workflow. Just call me when you need me.\n\n\n## Input\nInput can be multiple files \n-imgaes\n-pdfs\n-xlsx,csv....\n\n## Output\nSingle zip file"
      },
      "typeVersion": 1
    },
    {
      "id": "db7b6475-25b5-44de-b37e-70b75c91455e",
      "name": "Prepare Output",
      "type": "n8n-nodes-base.set",
      "position": [
        680,
        0
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "b0c3c3db-584a-48c9-b0ca-7f527d35f5a4",
              "name": "fileName",
              "type": "string",
              "value": "={{ $binary.data.fileName.replaceAll(\" \",\"\") }}"
            }
          ]
        },
        "includeOtherFields": true
      },
      "typeVersion": 3.4
    },
    {
      "id": "6cf6b9ba-e5a3-4d5f-a539-e84d839f7e99",
      "name": "Code Magic",
      "type": "n8n-nodes-base.code",
      "position": [
        240,
        0
      ],
      "parameters": {
        "jsCode": "let binaries = {}, binary_keys = [];\n\nfor (const [index, inputItem] of Object.entries($input.all())) {\n  binaries[`data_${index}`] = inputItem.binary.data;\n  binary_keys.push(`data_${index}`);\n}\n\nreturn [{\n    json: {\n        binary_keys: binary_keys.join(',')\n    },\n    binary: binaries\n}];\n"
      },
      "typeVersion": 2
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "16f64706-0a2a-4f9f-a96f-f149a4874ae4",
  "connections": {
    "Code Magic": {
      "main": [
        [
          {
            "node": "Compression",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Compression": {
      "main": [
        [
          {
            "node": "Prepare Output",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Execute Workflow Trigger": {
      "main": [
        [
          {
            "node": "Code Magic",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
