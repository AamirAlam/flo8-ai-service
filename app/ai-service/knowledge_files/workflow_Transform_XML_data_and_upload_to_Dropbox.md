# Transform XML data and upload to Dropbox

**[View Template](https://n8n.io/workflows/13-/)**  **Published Date:** 09/04/2019  **Created By:** Jan Oberhauser  **Categories:** `Data & Storage` `Development` `Core Nodes`  

## Template Description



Download XML data
Convert it to JSON
Change title in data
Convert back to XML
Upload file to Dropbox   

## Template JSON

```
{
  "nodes": [
    {
      "name": "To JSON",
      "type": "n8n-nodes-base.xml",
      "position": [
        700,
        300
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "Change title",
      "type": "n8n-nodes-base.set",
      "position": [
        900,
        300
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "slideshow.title",
              "value": "New Title Name"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Get XML Data",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        500,
        300
      ],
      "parameters": {
        "url": "https://httpbin.org/xml",
        "responseFormat": "string"
      },
      "typeVersion": 1
    },
    {
      "name": "Dropbox",
      "type": "n8n-nodes-base.dropbox",
      "position": [
        1300,
        300
      ],
      "parameters": {
        "path": "/my-xml-file.xml",
        "fileContent": "={{$node[\"To XML\"].data[\"data\"]}}"
      },
      "credentials": {
        "dropboxApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "To XML",
      "type": "n8n-nodes-base.xml",
      "position": [
        1100,
        300
      ],
      "parameters": {
        "mode": "jsonToxml",
        "options": {}
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "To XML": {
      "main": [
        [
          {
            "node": "Dropbox",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "To JSON": {
      "main": [
        [
          {
            "node": "Change title",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Change title": {
      "main": [
        [
          {
            "node": "To XML",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get XML Data": {
      "main": [
        [
          {
            "node": "To JSON",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
