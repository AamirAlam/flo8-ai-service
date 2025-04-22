# Detect web visitors country by IP address with uProc

**[View Template](https://n8n.io/workflows/851-/)**  **Published Date:** 12/28/2020  **Created By:** Miquel Colomer  **Categories:** `Development` `Communication` `Data & Storage`  

## Template Description

Do you want to know where a web visitor lives? 

This workflow enriches any lead by IP address using the uProc.io Location By IP address tool and sends an email in Spanish or English depending on the detected web visitor country.



You need to add your credentials (Email and API Key - real -) located at Integration section to n8n.

Node "Create IP and Email Item" can be replaced by any other supported service with IP and Email values, like Mailchimp, Calendly, or MySQL.

The "uProc" node returns the location of the provided IP address. 

"If" node checks if the web visitor country code belongs to Spain (ES Isocode). If positive, we use the Spanish language in our emails. Otherwise, we will use the English language in our communications.

Depending on the detected country code, we use the Amazon SES node to send the customized email adapted to the right language.

## Template JSON

```
{
  "id": "104",
  "name": "location_by_ip",
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
      "name": "Get Location By IP",
      "type": "n8n-nodes-base.uproc",
      "position": [
        850,
        510
      ],
      "parameters": {
        "ip": "={{$node[\"Create IP and Email Item\"].json[\"ip\"]}}",
        "tool": "getLocationByIp",
        "group": "geographic",
        "additionalOptions": {}
      },
      "credentials": {
        "uprocApi": "miquel-uproc"
      },
      "typeVersion": 1
    },
    {
      "name": "User in Spain?",
      "type": "n8n-nodes-base.if",
      "position": [
        1050,
        510
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Get Location By IP\"].json[\"message\"][\"country_code\"]}}",
              "value2": "ES"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Create IP and Email Item",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        640,
        510
      ],
      "parameters": {
        "functionCode": "item.ip = \"83.46.131.46\";\nitem.email = \"miquel@uproc.io\";\n\nreturn item;"
      },
      "typeVersion": 1
    },
    {
      "name": "Send English Email",
      "type": "n8n-nodes-base.awsSes",
      "position": [
        1270,
        650
      ],
      "parameters": {
        "body": "Hi,\n\nThank you for your signup!",
        "subject": "Welcome aboard",
        "fromEmail": "sample@uproc.io",
        "toAddresses": [
          "={{$node[\"Create IP and Email Item\"].json[\"email\"]}}"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "aws": "ses"
      },
      "typeVersion": 1
    },
    {
      "name": "Send Spanish Email",
      "type": "n8n-nodes-base.awsSes",
      "position": [
        1270,
        420
      ],
      "parameters": {
        "body": "Hola,\n\n\u00a1Gracias por registrarte!",
        "subject": "Bienvenido a bordo",
        "fromEmail": "sample@uproc.io",
        "toAddresses": [
          "={{$node[\"Create IP and Email Item\"].json[\"email\"]}}"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "aws": "ses"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "User in Spain?": {
      "main": [
        [
          {
            "node": "Send Spanish Email",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Send English Email",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Location By IP": {
      "main": [
        [
          {
            "node": "User in Spain?",
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
            "node": "Create IP and Email Item",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create IP and Email Item": {
      "main": [
        [
          {
            "node": "Get Location By IP",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
