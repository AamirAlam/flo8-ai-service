# Compress binary files to zip format

**[View Template](https://n8n.io/workflows/908-/)**  **Published Date:** 01/27/2021  **Created By:** ghagrawal17  **Categories:** `Data & Storage` `Development` `Core Nodes`  

## Template Description

This workflow allows you to compress binary files to zip format.




HTTP Request node: The workflow uses the HTTP Request node to fetch files from the internet. If you want to fetch files from your local machine, replace it with the Read Binary File or Read Binary Files node.

Compression node: The Compression node compresses the file into a zip. If you want to compress the files to gzip, then select the gzip format instead.

Based on your use-case, you may want to write the files to your disk or upload it to Google Drive or Box. If you want to write the compressed file to your disk, replace the Dropbox node with the Write Binary File node, or if you want to upload the file to a different service, use the respective node.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Dropbox",
      "type": "n8n-nodes-base.dropbox",
      "position": [
        1090,
        290
      ],
      "parameters": {
        "path": "/images.zip",
        "binaryData": true
      },
      "credentials": {
        "dropboxApi": "Dropbox Tokens Test"
      },
      "typeVersion": 1
    },
    {
      "name": "Compression",
      "type": "n8n-nodes-base.compression",
      "position": [
        890,
        290
      ],
      "parameters": {
        "fileName": "images.zip",
        "operation": "compress",
        "outputFormat": "zip",
        "binaryPropertyName": "logo, workflow_image"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        690,
        290
      ],
      "parameters": {
        "url": "https://n8n.io/n8n-logo.png",
        "options": {},
        "responseFormat": "file",
        "dataPropertyName": "logo"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        490,
        290
      ],
      "parameters": {
        "url": "https://docs.n8n.io/assets/img/final-workflow.f380b957.png",
        "options": {},
        "responseFormat": "file",
        "dataPropertyName": "workflow_image"
      },
      "typeVersion": 1
    },
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        290,
        290
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "connections": {
    "Compression": {
      "main": [
        [
          {
            "node": "Dropbox",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request": {
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
            "node": "Compression",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
