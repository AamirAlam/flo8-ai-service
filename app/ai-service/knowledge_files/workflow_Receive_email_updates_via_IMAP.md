# Receive email updates via IMAP

**[View Template](https://n8n.io/workflows/587-/)**  **Published Date:** 08/04/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for IMAP Email node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "IMAP Email",
      "type": "n8n-nodes-base.emailReadImap",
      "position": [
        760,
        400
      ],
      "parameters": {
        "options": {
          "allowUnauthorizedCerts": false
        }
      },
      "credentials": {
        "imap": "imap_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
