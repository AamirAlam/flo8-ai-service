# Create a contact in ActiveCampaign

**[View Template](https://n8n.io/workflows/412-/)**  **Published Date:** 06/18/2020  **Created By:** tanaypant  **Categories:** `Marketing`  

## Template Description



## Template JSON

```
{
  "name": "",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        600,
        250
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "ActiveCampaign",
      "type": "n8n-nodes-base.activeCampaign",
      "position": [
        800,
        250
      ],
      "parameters": {
        "email": "",
        "updateIfExists": true,
        "additionalFields": {
          "lastName": "",
          "firstName": ""
        }
      },
      "credentials": {
        "activeCampaignApi": "ActiveCampaign"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "ActiveCampaign",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
