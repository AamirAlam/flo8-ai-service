# Create an array of objects

**[View Template](https://n8n.io/workflows/767-/)**  **Published Date:** 11/05/2020  **Created By:** ghagrawal17  **Categories:**   

## Template Description

You can use the Function node to create an array of objects. 

## Template JSON

```
{
  "nodes": [
    {
      "name": "Mock Data",
      "type": "n8n-nodes-base.function",
      "position": [
        802,
        307
      ],
      "parameters": {
        "functionCode": "return [\n  {\n    json: {\n      id: 1,\n      name: \"Jim\"\n    }\n  },\n  {\n    json: {\n      id: 2,\n      name: \"Stefan\"\n    }\n  },\n  {\n    json: {\n      id: 3,\n      name: \"Hans\"\n    }\n  }\n];"
      },
      "typeVersion": 1
    },
    {
      "name": "Create an array of objects",
      "type": "n8n-nodes-base.function",
      "position": [
        1052,
        307
      ],
      "parameters": {
        "functionCode": "return [\n  {\n    json: {\n      data_object: items.map(item => item.json),\n    },\n  }\n];\n"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Mock Data": {
      "main": [
        [
          {
            "node": "Create an array of objects",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
