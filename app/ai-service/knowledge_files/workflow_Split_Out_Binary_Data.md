# Split Out Binary Data

**[View Template](https://n8n.io/workflows/1621-/)**  **Published Date:** 05/05/2022  **Created By:** Tom  **Categories:** `Development` `Core Nodes` `Data & Storage`  

## Template Description

This workflows helps with processing binary data.

You'll often have binary objects with keys such as attachment_0, attachment_1, attachment_2, etc. attached to your items, for example when reading an incoming email.

This binary data is hard to process because it's not an array you can simply loop through.

This workflow solves this problem by providing a Function node that takes all incoming items and all their binary data and then returning a single item for each file with a data key containing your binary file.

Incoming binary data:


Processed binary data:


## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        240,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Split Up Binary Data",
      "type": "n8n-nodes-base.function",
      "position": [
        900,
        300
      ],
      "parameters": {
        "functionCode": "let results = [];\n\nfor (item of items) {\n    for (key of Object.keys(item.binary)) {\n        results.push({\n            json: {\n                fileName: item.binary[key].fileName\n            },\n            binary: {\n                data: item.binary[key],\n            }\n        });\n    }\n}\n\nreturn results;"
      },
      "typeVersion": 1
    },
    {
      "name": "Download Example Data",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        460,
        300
      ],
      "parameters": {
        "url": "https://static.thomasmartens.eu/n8n/three_more_files.zip",
        "options": {},
        "responseFormat": "file"
      },
      "typeVersion": 1
    },
    {
      "name": "Decompress Example Data",
      "type": "n8n-nodes-base.compression",
      "position": [
        680,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        420,
        120
      ],
      "parameters": {
        "width": 400,
        "height": 360,
        "content": "## Example Data\nThe first two nodes simply fetch some example data to work with.\n\nIn the real world, you'd probably process incoming emails, uploaded FTP files or something similar instead."
      },
      "typeVersion": 1
    },
    {
      "name": "Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        860,
        120
      ],
      "parameters": {
        "width": 320,
        "height": 360,
        "content": "## Transformation\nThis is where the magic happens. Incoming files are split up into individual items, each with a single binary data object under the `data` key."
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Download Example Data": {
      "main": [
        [
          {
            "node": "Decompress Example Data",
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
            "node": "Download Example Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Decompress Example Data": {
      "main": [
        [
          {
            "node": "Split Up Binary Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
