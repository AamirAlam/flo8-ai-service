# Create, add an attachment, and send a draft using Microsoft Outlook

**[View Template](https://n8n.io/workflows/867-/)**  **Published Date:** 12/31/2020  **Created By:** ghagrawal17  **Categories:** `Development` `Core Nodes` `Communication` `HITL`  

## Template Description

This workflow allows you to create, add an attachment, and send a draft using the Microsoft Outlook node.



Microsoft Outlook node: This node creates a draft message with HTML content. You can either set the content as Text or HTML. You can also add the recipients to the draft in this node.

HTTP Request node: This node fetches the logo of n8n from a URL and returns the binary data. You might want to fetch files from your machine or another email or a database. You can replace this node with the relevant node.

Microsoft Outlook1 node: This node adds the attachment that we receive from the previous node to the draft message that we created.

Microsoft Outlook2 node: This node sends the draft message to a recipient. Since we didn't mention the recipient in the Microsoft Outlook node, we add the recipient in this node. You can also enter multiple recipients.

## Template JSON

```
{
  "id": "193",
  "name": "Create, add an attachment, and send a draft using the Microsoft Outlook node",
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
      "name": "Microsoft Outlook",
      "type": "n8n-nodes-base.microsoftOutlook",
      "position": [
        450,
        300
      ],
      "parameters": {
        "subject": "Hello from n8n!",
        "resource": "draft",
        "bodyContent": "<h1>Hello from n8n!</h1> <p>We are sending this email using the Microsoft Outlook node in <a href=\"https://n8n.io\">n8n</a></p> <p>Best,</p> <p>Sender</p>",
        "additionalFields": {
          "bodyContentType": "html"
        }
      },
      "credentials": {
        "microsoftOutlookOAuth2Api": "Micrsoft Outlook Credentials"
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
        "url": "https://n8n.io/n8n-logo.png",
        "options": {},
        "responseFormat": "file"
      },
      "typeVersion": 1
    },
    {
      "name": "Microsoft Outlook1",
      "type": "n8n-nodes-base.microsoftOutlook",
      "position": [
        850,
        300
      ],
      "parameters": {
        "resource": "messageAttachment",
        "messageId": "={{$node[\"Microsoft Outlook\"].json[\"id\"]}}",
        "additionalFields": {
          "fileName": "n8n.png"
        }
      },
      "credentials": {
        "microsoftOutlookOAuth2Api": "Micrsoft Outlook Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Microsoft Outlook2",
      "type": "n8n-nodes-base.microsoftOutlook",
      "position": [
        1050,
        300
      ],
      "parameters": {
        "resource": "draft",
        "messageId": "={{$node[\"Microsoft Outlook\"].json[\"id\"]}}",
        "operation": "send",
        "additionalFields": {
          "recipients": "abc@example.com"
        }
      },
      "credentials": {
        "microsoftOutlookOAuth2Api": "Micrsoft Outlook Credentials"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Microsoft Outlook1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Microsoft Outlook": {
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
    "Microsoft Outlook1": {
      "main": [
        [
          {
            "node": "Microsoft Outlook2",
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
            "node": "Microsoft Outlook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
