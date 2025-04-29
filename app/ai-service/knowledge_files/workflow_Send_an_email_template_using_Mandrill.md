# Send an email template using Mandrill

**[View Template](https://n8n.io/workflows/571-/)**  **Published Date:** 07/30/2020  **Created By:** amudhan  **Categories:** `Development` `Communication`  

## Template Description

Companion workflow for Mandrill node docs

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
      "name": "Mandrill",
      "type": "n8n-nodes-base.mandrill",
      "position": [
        450,
        300
      ],
      "parameters": {
        "options": {},
        "toEmail": "user@example.com",
        "template": "welcomeemailv2",
        "fromEmail": "example@yourdomain.com"
      },
      "credentials": {
        "mandrillApi": "mandrill_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Mandrill",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
