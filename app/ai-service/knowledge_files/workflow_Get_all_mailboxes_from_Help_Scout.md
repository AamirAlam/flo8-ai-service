# Get all mailboxes from Help Scout

**[View Template](https://n8n.io/workflows/567-/)**  **Published Date:** 07/29/2020  **Created By:** amudhan  **Categories:** `Communication`  

## Template Description

Companion workflow for Help Scout node docs



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
      "name": "HelpScout",
      "type": "n8n-nodes-base.helpScout",
      "position": [
        450,
        300
      ],
      "parameters": {
        "resource": "mailbox",
        "operation": "getAll"
      },
      "credentials": {
        "helpScoutOAuth2Api": "helpscout_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "HelpScout",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
