# Manage folders in Nextcloud

**[View Template](https://n8n.io/workflows/620-/)**  **Published Date:** 08/25/2020  **Created By:** amudhan  **Categories:** `Development` `Core Nodes` `Data & Storage`  

## Template Description

Companion workflow for enhanced Nextcloud node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        20,
        180
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        420,
        180
      ],
      "parameters": {
        "url": "https://n8n.io/n8n-logo.png",
        "options": {},
        "responseFormat": "file"
      },
      "typeVersion": 1
    },
    {
      "name": "NextCloud",
      "type": "n8n-nodes-base.nextCloud",
      "position": [
        220,
        180
      ],
      "parameters": {
        "path": "n8n",
        "resource": "folder"
      },
      "credentials": {
        "nextCloudApi": "nextcloud_creds"
      },
      "typeVersion": 1
    },
    {
      "name": "NextCloud1",
      "type": "n8n-nodes-base.nextCloud",
      "position": [
        620,
        180
      ],
      "parameters": {
        "path": "n8n/logo.png",
        "binaryDataUpload": true
      },
      "credentials": {
        "nextCloudApi": "nextcloud_creds"
      },
      "typeVersion": 1
    },
    {
      "name": "NextCloud2",
      "type": "n8n-nodes-base.nextCloud",
      "position": [
        820,
        180
      ],
      "parameters": {
        "path": "n8n",
        "resource": "folder",
        "operation": "list"
      },
      "credentials": {
        "nextCloudApi": "nextcloud_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "NextCloud": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "NextCloud1": {
      "main": [
        [
          {
            "node": "NextCloud2",
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
            "node": "NextCloud1",
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
            "node": "NextCloud",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
