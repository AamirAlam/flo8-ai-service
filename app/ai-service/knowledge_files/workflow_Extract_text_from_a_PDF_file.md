# Extract text from a PDF file

**[View Template](https://n8n.io/workflows/585-/)**  **Published Date:** 08/04/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Read PDF node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        680,
        400
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Read Binary File",
      "type": "n8n-nodes-base.readBinaryFile",
      "position": [
        880,
        400
      ],
      "parameters": {
        "filePath": "/data/pdf.pdf"
      },
      "typeVersion": 1
    },
    {
      "name": "Read PDF",
      "type": "n8n-nodes-base.readPDF",
      "position": [
        1090,
        400
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "connections": {
    "Read Binary File": {
      "main": [
        [
          {
            "node": "Read PDF",
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
            "node": "Read Binary File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
