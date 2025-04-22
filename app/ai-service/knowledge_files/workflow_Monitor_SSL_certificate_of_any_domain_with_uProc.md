# Monitor SSL certificate of any domain with uProc

**[View Template](https://n8n.io/workflows/861-/)**  **Published Date:** 12/30/2020  **Created By:** Miquel Colomer  **Categories:** `Communication` `HITL` `Data & Storage`  

## Template Description

Do you want to check the SSL certificate expiration dates of your customers or servers?

This workflow gets information of an SSL certificate using the uProc Get Certificate by domain tool.
You can use this workflow to query SSL certificates in bulk and send alarms when any certificate has expired.



You need to add your credentials (Email and API Key - real -) located at Integration section to n8n.

You can replace "Create Domain Item" with any integration containing a domain, like Google Sheets, MySQL, or Zabbix server.

Every "uProc" node returns the next fields per every analyzed SSL certificate:
issuer: Contains the issuer.
provider: Contains the provider.
valid_from: Contains the start date.
valid_to: Contains the end date.
serial_number: Contains the serial number.
type: Contains if supports one or multiple domains.
protocol: Contains the protocol.
valid: Contains its validity.
domains: Contains all domains and subdomains supported.

An "IF" node detects if the certificate is valid or not.

Finally, the workflow sends an alarm to a Telegram channel to know if the certificate has expired. 


## Template JSON

```
{
  "id": "110",
  "name": "Get SSL Certificate",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        240,
        290
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Create Domain Item",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        450,
        290
      ],
      "parameters": {
        "functionCode": "item.domain = \"n8n.io\";\nreturn item;"
      },
      "typeVersion": 1
    },
    {
      "name": "Get SSL Certificate",
      "type": "n8n-nodes-base.uproc",
      "position": [
        650,
        290
      ],
      "parameters": {
        "tool": "getDomainCertificate",
        "group": "internet",
        "domain": "= {{$node[\"Create Domain Item\"].json[\"domain\"]}}",
        "additionalOptions": {}
      },
      "credentials": {
        "uprocApi": "miquel-uproc"
      },
      "typeVersion": 1
    },
    {
      "name": "Send Expired Alarm",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1070,
        270
      ],
      "parameters": {
        "text": "=The certificate of the domain {{$node[\"Create Domain Item\"].json[\"domain\"]}} has expired!",
        "chatId": "-1415703867",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "test killia bot"
      },
      "typeVersion": 1
    },
    {
      "name": "Certificate  has  expired?",
      "type": "n8n-nodes-base.if",
      "position": [
        840,
        290
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Get SSL Certificate\"].json[\"message\"][\"valid\"]+\"\"}}",
              "value2": "false"
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
    "Create Domain Item": {
      "main": [
        [
          {
            "node": "Get SSL Certificate",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get SSL Certificate": {
      "main": [
        [
          {
            "node": "Certificate  has  expired?",
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
            "node": "Create Domain Item",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Certificate  has  expired?": {
      "main": [
        [
          {
            "node": "Send Expired Alarm",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
