# Translate instructions using LingvaNex

**[View Template](https://n8n.io/workflows/797-/)**  **Published Date:** 11/30/2020  **Created By:** ghagrawal17  **Categories:** `Development` `Core Nodes` `Miscellaneous`  

## Template Description



## Template JSON

```
{
  "id": "145",
  "name": "Translate cocktail instructions using LingvaNex",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "LingvaNex",
      "type": "n8n-nodes-base.lingvaNex",
      "position": [
        650,
        300
      ],
      "parameters": {
        "text": "={{$node[\"HTTP Request\"].json[\"drinks\"][0][\"strInstructions\"]}}",
        "options": {},
        "translateTo": "it_IT"
      },
      "credentials": {
        "lingvaNexApi": "LingvaNex"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        450,
        300
      ],
      "parameters": {
        "url": "https://www.thecocktaildb.com/api/json/v1/1/random.php",
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
            "node": "LingvaNex",
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
