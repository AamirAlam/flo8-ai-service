# Simple file based key value store (WriteKey)

**[View Template](https://n8n.io/workflows/1407-/)**  **Published Date:** 01/24/2022  **Created By:** Peter  **Categories:**   

## Template Description

Store a key with a value in a local json file. Multiple keys could be saved in a single file.

Related workflow: GetKey

Create a subfolder in your n8n homedir: /home/node/.n8n/local-files. In docker look at the data path and create a subfolder local-files.
Set the correct access rights chmod 1000.1000 local-files.

Put the workflow code in a new workflow named WriteKey.

Create another workflow with a function item:

return  {
  file: '/4711.json', // 4711 should be your workflow id
  key: 'MyKey',
  value: 'MyValue'
}

Pipe the function item to an Execution Workflow that calls the WriteKey workflow.

It would be nice if we could get someday a shiny built-in n8n node that does the job. :)

## Template JSON

```
{
  "id": 12,
  "name": "Storage: WriteKey",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        60,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Write Binary File",
      "type": "n8n-nodes-base.writeBinaryFile",
      "position": [
        420,
        740
      ],
      "parameters": {
        "fileName": "={{$node[\"Config\"].json[\"file\"]}}",
        "dataPropertyName": "=data"
      },
      "typeVersion": 1
    },
    {
      "name": "Config",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        600,
        300
      ],
      "parameters": {
        "functionCode": "return {\n  file: '/home/node/.n8n/local-files' + item.file,\n  key: item.key,\n  value: item.value\n}"
      },
      "typeVersion": 1
    },
    {
      "name": "Read Binary Files",
      "type": "n8n-nodes-base.readBinaryFiles",
      "position": [
        240,
        520
      ],
      "parameters": {
        "fileSelector": "={{$json[\"file\"]}}"
      },
      "typeVersion": 1,
      "continueOnFail": true,
      "alwaysOutputData": true
    },
    {
      "name": "SetKeyValue",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        600,
        520
      ],
      "parameters": {
        "functionCode": "const key = $node[\"Config\"].json[\"key\"]\nconst value = $node[\"Config\"].json[\"value\"]\nitem[key] = value\n\nreturn item;"
      },
      "typeVersion": 1
    },
    {
      "name": "BinaryToJSON",
      "type": "n8n-nodes-base.moveBinaryData",
      "position": [
        420,
        520
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1,
      "alwaysOutputData": true
    },
    {
      "name": "JSONToBinary",
      "type": "n8n-nodes-base.moveBinaryData",
      "position": [
        240,
        740
      ],
      "parameters": {
        "mode": "jsonToBinary",
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "SplitInBatches",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        420,
        300
      ],
      "parameters": {
        "options": {},
        "batchSize": 1
      },
      "typeVersion": 1
    },
    {
      "name": "Repeat",
      "type": "n8n-nodes-base.if",
      "position": [
        600,
        740
      ],
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{$node[\"SplitInBatches\"].context[\"noItemsLeft\"]}}",
              "value2": true
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Done",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        800,
        740
      ],
      "parameters": {
        "functionCode": "console.log('Done!');\n\nreturn item;"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Config": {
      "main": [
        [
          {
            "node": "Read Binary Files",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Repeat": {
      "main": [
        [
          {
            "node": "Done",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "SplitInBatches",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "SetKeyValue": {
      "main": [
        [
          {
            "node": "JSONToBinary",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "BinaryToJSON": {
      "main": [
        [
          {
            "node": "SetKeyValue",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "JSONToBinary": {
      "main": [
        [
          {
            "node": "Write Binary File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "SplitInBatches": {
      "main": [
        [
          {
            "node": "Config",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Read Binary Files": {
      "main": [
        [
          {
            "node": "BinaryToJSON",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Write Binary File": {
      "main": [
        [
          {
            "node": "Repeat",
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
            "node": "SplitInBatches",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
