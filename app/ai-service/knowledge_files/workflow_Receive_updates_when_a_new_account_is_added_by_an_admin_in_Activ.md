# Receive updates when a new account is added by an admin in ActiveCampaign

**[View Template](https://n8n.io/workflows/488-/)**  **Published Date:** 07/12/2020  **Created By:** tanaypant  **Categories:**   

## Template Description



## Template JSON

```
{
  "id": "112",
  "name": "Receive updates when a new account is added by an admin in ActiveCampaign",
  "nodes": [
    {
      "name": "ActiveCampaign Trigger",
      "type": "n8n-nodes-base.activeCampaignTrigger",
      "position": [
        700,
        250
      ],
      "parameters": {
        "events": [
          "account_add"
        ],
        "sources": [
          "admin"
        ]
      },
      "credentials": {
        "activeCampaignApi": ""
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {}
}
```
