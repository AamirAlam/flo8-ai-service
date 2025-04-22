# Convert the JSON data received from the CocktailDB API in XML

**[View Template](https://n8n.io/workflows/661-/)**  **Published Date:** 09/14/2020  **Created By:** ghagrawal17  **Categories:** `Development` `Core Nodes`  

## Template Description



## Template JSON

```
{
  "id": "55",
  "name": "Convert the JSON data received from the CocktailDB API in XML",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        440,
        260
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        650,
        260
      ],
      "parameters": {
        "url": "https://www.thecocktaildb.com/api/json/v1/1/random.php",
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "XML",
      "type": "n8n-nodes-base.xml",
      "position": [
        850,
        260
      ],
      "parameters": {
        "mode": "jsonToxml",
        "options": {}
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "HTTP Request": {
      "main": [
        [
          {
            "node": "XML",
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
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
