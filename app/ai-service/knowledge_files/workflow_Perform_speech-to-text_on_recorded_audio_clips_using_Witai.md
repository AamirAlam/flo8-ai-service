# Perform speech-to-text on recorded audio clips using Wit.ai

**[View Template](https://n8n.io/workflows/437-/)**  **Published Date:** 06/30/2020  **Created By:** amudhan  **Categories:** `Development` `Core Nodes`  

## Template Description

This workflow performs speech-to-text on recorded audio clips using Wit.ai.

To get started, replace your Wit.ai Server Access Token in the Authorization header.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Read Binary File",
      "type": "n8n-nodes-base.readBinaryFile",
      "position": [
        450,
        300
      ],
      "parameters": {
        "filePath": "/data/demo1.wav"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        650,
        300
      ],
      "parameters": {
        "url": "https://api.wit.ai/speech?v=20200513",
        "options": {
          "bodyContentType": "raw"
        },
        "requestMethod": "POST",
        "jsonParameters": true,
        "sendBinaryData": true,
        "headerParametersJson": "={{JSON.parse('{\"Authorization\":\"Bearer {your_token_goes_here}\", \"Content-Type\":\"audio/wav\"}')}}"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Read Binary File": {
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
