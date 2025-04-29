# Listen on new emails on a IMAP mailbox

**[View Template](https://n8n.io/workflows/154-/)**  **Published Date:** 11/01/2019  **Created By:** mail  **Categories:** `Development` `Core Nodes`  

## Template Description

Listen on new emails on a given IMAP mailbox. Converts the binary XML attachment to a stringified xmlproperty on the $data object and converts it to JSON. The Setnode could be replaced with Function nodes for example to do a conversion/mapping/transformation.



The JSON is ultimately sent to a HTTP Endpoint via POST.

This could be a starter for EDI purposes like receiving or transmitting XML data and conversion via JSON object property mapping.

## Template JSON

```
{
  "id": "1",
  "name": "ImapEmail, XmlToJson, POST-HTTP-Request",
  "nodes": [
    {
      "name": "IMAP Email",
      "type": "n8n-nodes-base.emailReadImap",
      "position": [
        450,
        450
      ],
      "parameters": {
        "options": {
          "allowUnauthorizedCerts": true
        },
        "downloadAttachments": true
      },
      "credentials": {
        "imap": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Move Binary Data",
      "type": "n8n-nodes-base.moveBinaryData",
      "position": [
        600,
        450
      ],
      "parameters": {
        "options": {
          "encoding": "utf8",
          "keepSource": false
        },
        "sourceKey": "attachment_0",
        "setAllData": false,
        "destinationKey": "xml"
      },
      "typeVersion": 1
    },
    {
      "name": "XML",
      "type": "n8n-nodes-base.xml",
      "position": [
        800,
        450
      ],
      "parameters": {
        "options": {
          "ignoreAttrs": true,
          "explicitRoot": true
        },
        "dataPropertyName": "xml"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1210,
        450
      ],
      "parameters": {
        "url": "http://localhost:5679/api/sales-order",
        "options": {
          "bodyContentType": "form-urlencoded"
        },
        "requestMethod": "POST",
        "responseFormat": "string",
        "bodyParametersUi": {
          "parameter": [
            {
              "name": "orderRequest",
              "value": "={{$node[\"Set\"].data}}"
            }
          ]
        },
        "dataPropertyName": "status",
        "allowUnauthorizedCerts": true
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        960,
        450
      ],
      "parameters": {
        "values": {
          "number": []
        }
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {
    "errorWorkflow": "2"
  },
  "connections": {
    "Set": {
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
    "XML": {
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
    "IMAP Email": {
      "main": [
        [
          {
            "node": "Move Binary Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Move Binary Data": {
      "main": [
        [
          {
            "node": "XML",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
