# Handle verification for Twitter webhook

**[View Template](https://n8n.io/workflows/1440-/)**  **Published Date:** 02/06/2022  **Created By:** ghagrawal17  **Categories:** `Development` `Core Nodes`  

## Template Description

This workflow handles the incoming call from Twitter and sends the required response for verification.

On registering the webhook with the Twitter Account Activity API, Twitter expects a signature in response. Twitter also randomly ping the webhook to ensure it is active and secure.



Webhook node: Use the displayed URL to register with the Account Activity API.

Crypto node: In the Secret field, enter your API Key Secret from Twitter.

Set node: This node generates the response expected by the Twitter API.


Learn more about connecting n8n with Twitter in the Getting Started with Twitter Webhook article.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        460,
        300
      ],
      "webhookId": "0db0a40c-e5d1-463f-8252-03599f1303e6",
      "parameters": {
        "path": "0db0a40c-e5d1-463f-8252-03599f1303e6",
        "options": {},
        "responseMode": "lastNode"
      },
      "typeVersion": 1
    },
    {
      "name": "Crypto",
      "type": "n8n-nodes-base.crypto",
      "position": [
        660,
        300
      ],
      "parameters": {
        "type": "SHA256",
        "value": "={{$json[\"query\"][\"crc_token\"]}}",
        "action": "hmac",
        "secret": "API KEY SECRET",
        "encoding": "base64"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        840,
        300
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "response_token",
              "value": "=sha256={{$json[\"data\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Crypto": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Webhook": {
      "main": [
        [
          {
            "node": "Crypto",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
