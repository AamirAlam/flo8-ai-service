# Get DNS entries of any domain with uProc

**[View Template](https://n8n.io/workflows/862-/)**  **Published Date:** 12/30/2020  **Created By:** Miquel Colomer  **Categories:** `Data & Storage`  

## Template Description

Do you want to control the DNS domain entries of your customers or servers?

This workflow gets DNS information of any domain using the uProc Get Domain DNS records tool.

You can use this workflow to check existing DNS records in real-time to ensure that any domain setup is correct.



You need to add your credentials (Email and API Key - real -) located at Integration section to n8n.

You can replace "Create Domain Item" with any integration containing a domain, like Google Sheets, MySQL, or Zabbix server.

Every "uProc" node returns multiple items with the next fields per every item:
type: Contains the DNS record type (A, ALIAS, AAAA, CERT, CNAME, MX, NAPTR, NS, PTR, SOA, SRV, TXT, URL).
values: Contains the DNS record values.

## Template JSON

```
{
  "id": "113",
  "name": "Get DNS entries",
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
      "name": "Get DNS records",
      "type": "n8n-nodes-base.uproc",
      "position": [
        650,
        290
      ],
      "parameters": {
        "tool": "getDomainRecords",
        "group": "internet",
        "domain": "= {{$node[\"Create Domain Item\"].json[\"domain\"]}}",
        "additionalOptions": {}
      },
      "credentials": {
        "uprocApi": "miquel-uproc"
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
            "node": "Get DNS records",
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
    }
  }
}
```
