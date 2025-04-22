# Write JSON to Disk (Binary)

**[View Template](https://n8n.io/workflows/101-/)**  **Published Date:** 10/11/2019  **Created By:** mike  **Categories:**   

## Template Description

The “Write Binary File” expects binary data. The JSON data is, however, JSON ;) There should really be a node that allows moving data around between both of them. For now, it can be done with a Function-Node. At least till a proper one is in place. The first node is example data, wich you can customize or replace. The second node named “Make Binary” is the important one with the custom code which makes the data binary and writes it to the correct location.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Write Binary File",
      "type": "n8n-nodes-base.writeBinaryFile",
      "position": [
        800,
        350
      ],
      "parameters": {
        "fileName": "test.json"
      },
      "typeVersion": 1
    },
    {
      "name": "Make Binary",
      "type": "n8n-nodes-base.function",
      "position": [
        600,
        350
      ],
      "parameters": {
        "functionCode": "items[0].binary = {\n  data: {\n    data: new Buffer(JSON.stringify(items[0].json, null, 2)).toString('base64')\n  }\n};\nreturn items;"
      },
      "typeVersion": 1
    },
    {
      "name": "Create Example Data",
      "type": "n8n-nodes-base.function",
      "position": [
        390,
        350
      ],
      "parameters": {
        "functionCode": "items[0].json = {\n  \"text\": \"asdf\",\n  \"number\": 1\n};\nreturn items;"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Make Binary": {
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
    "Create Example Data": {
      "main": [
        [
          {
            "node": "Make Binary",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
