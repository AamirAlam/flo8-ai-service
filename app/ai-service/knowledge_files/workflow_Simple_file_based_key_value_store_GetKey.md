# Simple file based key value store (GetKey)

**[View Template](https://n8n.io/workflows/1408-/)**  **Published Date:** 01/24/2022  **Created By:** Peter  **Categories:**   

## Template Description

Read a value by key from a local json file.

Related workflow: WriteKey

Create a subfolder in your n8n homedir: /home/node/.n8n/local-files. In docker look at the data path and create a subfolder local-files.
Set the correct access rights chmod 1000.1000 local-files.

Put the workflow code in a new workflow named GetKey.

Create another workflow with a function item:

return  {
  file: '/4711.json', // 4711 should be your workflow id
  key: 'MyKey',
  default: 'Optional returned value if key is empty / not exists'
}

Pipe the function item to an Execution Workflow that calls the GetKey workflow.

It would be nice if we could get someday a shiny built-in n8n node that does the job. :)

## Template JSON

```
{
  "id": 11,
  "name": "Storage: GetKey",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        240,
        280
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Config",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        420,
        280
      ],
      "parameters": {
        "functionCode": "return {\n  file: '/home/node/.n8n/local-files' + item.file,\n  key: item.key,\n  default: item.default\n}"
      },
      "typeVersion": 1
    },
    {
      "name": "Read Binary File",
      "type": "n8n-nodes-base.readBinaryFile",
      "position": [
        600,
        280
      ],
      "parameters": {
        "filePath": "={{$json[\"file\"]}}"
      },
      "typeVersion": 1,
      "continueOnFail": true,
      "alwaysOutputData": true
    },
    {
      "name": "BinaryToJSON",
      "type": "n8n-nodes-base.moveBinaryData",
      "position": [
        780,
        280
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1,
      "alwaysOutputData": true
    },
    {
      "name": "ReturnValue",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        960,
        280
      ],
      "parameters": {
        "functionCode": "const key = $node[\"Config\"].json[\"key\"]\nconst defaultValue = $node[\"Config\"].json[\"default\"]\n\nlet value\nif (item) {\n  value = item[key] || defaultValue\n} else {\n  value = defaultValue\n}\n\nreturn {\n  [ key ]: value\n}"
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
            "node": "Read Binary File",
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
            "node": "ReturnValue",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Read Binary File": {
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
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Config",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
