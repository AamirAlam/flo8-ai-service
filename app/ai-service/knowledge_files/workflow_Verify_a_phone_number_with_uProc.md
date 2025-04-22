# Verify a phone number with uProc

**[View Template](https://n8n.io/workflows/863-/)**  **Published Date:** 12/30/2020  **Created By:** Miquel Colomer  **Categories:** `Data & Storage`  

## Template Description

Do you want to avoid communication problems when launching phone calls? 

This workflow verifies landline and mobile phone numbers using the uProc Get Parsed and validated phone tool with worldwide coverage.



You need to add your credentials (Email and API Key - real -) located at Integration section to n8n.

Node "Create Phone Item" can be replaced by any other supported service with phone values, like databases (MySQL, Postgres), or Typeform.

The "uProc" node returns the next fields per every parsed and validated phone number:
country_prefix: contains the international country phone prefix number.
country_code: contains the 2-digit ISO country code of the phone number.
local_number: contains the phone number without international prefix.
formatted: contains a formatted version of the phone number, according to country detected.
valid: detects if the phone number has a valid format and prefix.
type: the phone number type (mobile, landline, or something else).

"If" node checks if the phone number is valid.

You can use the result to mark invalid phone numbers in your database or discard them from future telemarketing campaigns.

## Template JSON

```
{
  "id": "114",
  "name": "Verify phone numbers",
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
      "name": "Create Phone Item",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        640,
        510
      ],
      "parameters": {
        "functionCode": "item.phone = \"+34605281220\";\nreturn item;"
      },
      "typeVersion": 1
    },
    {
      "name": "Parse and Validate Phone",
      "type": "n8n-nodes-base.uproc",
      "position": [
        850,
        510
      ],
      "parameters": {
        "tool": "getPhoneParsed",
        "phone": "={{$node[\"Create Phone Item\"].json[\"phone\"]}}",
        "additionalOptions": {}
      },
      "credentials": {
        "uprocApi": "miquel-uproc"
      },
      "typeVersion": 1
    },
    {
      "name": "Phone is Valid?",
      "type": "n8n-nodes-base.if",
      "position": [
        1050,
        510
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Parse and Validate Phone\"].json[\"message\"][\"valid\"]+\"\"}}",
              "value2": "true"
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
    "Create Phone Item": {
      "main": [
        [
          {
            "node": "Parse and Validate Phone",
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
            "node": "Create Phone Item",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parse and Validate Phone": {
      "main": [
        [
          {
            "node": "Phone is Valid?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
