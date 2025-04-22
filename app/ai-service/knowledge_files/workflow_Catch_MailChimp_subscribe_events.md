# Catch MailChimp subscribe events

**[View Template](https://n8n.io/workflows/516-/)**  **Published Date:** 07/15/2020  **Created By:** amudhan  **Categories:**   

## Template Description

Companion workflow for Mailchimp Trigger node docs



## Template JSON

```
{
  "nodes": [
    {
      "name": "Mailchimp Trigger",
      "type": "n8n-nodes-base.mailchimpTrigger",
      "position": [
        870,
        370
      ],
      "parameters": {
        "list": "0a5a4ca5de",
        "events": [
          "subscribe"
        ],
        "sources": [
          "api",
          "admin",
          "user"
        ]
      },
      "credentials": {
        "mailchimpApi": "mailchimp_creds"
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
