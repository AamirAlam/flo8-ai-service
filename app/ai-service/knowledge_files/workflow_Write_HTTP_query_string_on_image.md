# Write HTTP query string on image

**[View Template](https://n8n.io/workflows/3-/)**  **Published Date:** 08/31/2019  **Created By:** Jan Oberhauser  **Categories:** `Core Nodes` `Marketing` `Development`  

## Template Description

Receives data from an incoming HTTP Request
Reads file from internet
Writes data on image
Returns the data

The URL to call will look like this:
http://localhost:5678/webhook-test/webhook/test?name=Jim

Once called it will return an image like this:



## Template JSON

```
{
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        700,
        350
      ],
      "parameters": {
        "path": "test",
        "responseData": "firstEntryBinary",
        "responseMode": "lastNode"
      },
      "typeVersion": 1
    },
    {
      "name": "Edit Image",
      "type": "n8n-nodes-base.editImage",
      "position": [
        1100,
        350
      ],
      "parameters": {
        "text": "=They found the killer it was {{$node[\"Webhook\"].data[\"query\"][\"name\"]}}!",
        "fontSize": "=25",
        "operation": "text",
        "positionX": 150,
        "positionY": 180,
        "lineLength": 18
      },
      "typeVersion": 1
    },
    {
      "name": "Read File URL",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        900,
        350
      ],
      "parameters": {
        "url": "https://www.needpix.com/file_download.php?url=//storage.needpix.com/thumbs/newspaper-412809_1280.jpg",
        "responseFormat": "file"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Read File URL",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Read File URL": {
      "main": [
        [
          {
            "node": "Edit Image",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
