# Verify an email recipient with uProc

**[View Template](https://n8n.io/workflows/850-/)**  **Published Date:** 12/27/2020  **Created By:** Miquel Colomer  **Categories:** `Data & Storage`  

## Template Description

Do you want to avoid bounces in your Email Marketing campaigns? 

This workflow verifies emails using the uProc.io email verifier.



You need to add your credentials (Email and API Key - real -) located at Integration section to n8n.

Node "Create Email Item" can be replaced by any other supported service with email value, like Mailchimp, Calendly, MySQL, or Typeform.

The "uProc" node returns a status per checked email (deliverable, undeliverable, spamtrap, softbounce,...). 

"If" node checks if "deliverable" status exists. If value is not present, you can mark email as invalid to discard bounces. If "deliverable" status is present, you can use email in your Email Marketing campaigns.

If you need to know detailed indicators of any email, you can use the tool "Communication" > "Check Email Exists (Extended)" to get advanced information.



## Template JSON

```
{
  "id": "103",
  "name": "verify email",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        440,
        510
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Create Email Item",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        640,
        510
      ],
      "parameters": {
        "functionCode": "item.email = \"mcolomer@gmail.com\";\nreturn item;"
      },
      "typeVersion": 1
    },
    {
      "name": "Check Email Exists",
      "type": "n8n-nodes-base.uproc",
      "position": [
        850,
        510
      ],
      "parameters": {
        "tool": "checkEmailExists",
        "email": "={{$node[\"Create Email Item\"].json[\"email\"]}}",
        "additionalOptions": {}
      },
      "credentials": {
        "uprocApi": "miquel-uproc"
      },
      "typeVersion": 1
    },
    {
      "name": "Email Exists?",
      "type": "n8n-nodes-base.if",
      "position": [
        1050,
        510
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Check Email Exists\"].json[\"message\"][\"response\"]}}",
              "value2": "deliverable"
            }
          ]
        }
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Create Email Item": {
      "main": [
        [
          {
            "node": "Check Email Exists",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check Email Exists": {
      "main": [
        [
          {
            "node": "Email Exists?",
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
            "node": "Create Email Item",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
