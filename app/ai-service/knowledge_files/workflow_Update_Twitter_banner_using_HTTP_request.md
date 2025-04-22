# Update Twitter banner using HTTP request

**[View Template](https://n8n.io/workflows/1338-/)**  **Published Date:** 11/23/2021  **Created By:** ghagrawal17  **Categories:** `Development` `Core Nodes`  

## Template Description

This workflow demonstrates the use of the HTTP Request node to upload binary files for form-data-multipart type. This example workflow updates the Twitter banner.



HTTP Request node: This node fetches an image from Unsplash. Replace this node with any other node to fetch the image file.

HTTP Request1 node: This node uploads the Twitter Profile Banner. The Twitter API requires OAuth 1.0 authentication. Follow the Twitter documentation to learn how to configure the authentication.

## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Start",
      "type": "n8n-nodes-base.start",
      "position": [
        250,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        450,
        300
      ],
      "parameters": {
        "url": "https://unsplash.com/photos/lUDMZUWFUXE/download?ixid=MnwxMjA3fDB8MXxhbGx8Mnx8fHx8fDJ8fDE2MzczMjY4Mjc&force=true",
        "options": {},
        "responseFormat": "file",
        "headerParametersUi": {
          "parameter": []
        }
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        650,
        300
      ],
      "parameters": {
        "url": "https://api.twitter.com/1.1/account/update_profile_banner.json",
        "options": {},
        "requestMethod": "POST",
        "authentication": "oAuth1",
        "jsonParameters": true,
        "sendBinaryData": true,
        "binaryPropertyName": "banner:data"
      },
      "credentials": {
        "oAuth1Api": {
          "id": "300",
          "name": "Unnamed credential"
        }
      },
      "typeVersion": 1
    }
  ],
  "connections": {
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
