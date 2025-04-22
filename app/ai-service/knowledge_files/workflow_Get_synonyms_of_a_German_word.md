# Get synonyms of a German word

**[View Template](https://n8n.io/workflows/806-/)**  **Published Date:** 12/02/2020  **Created By:** ghagrawal17  **Categories:** `Utility`  

## Template Description



## Template JSON

```
{
  "id": "157",
  "name": "Get synonyms of a German word",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        550,
        260
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "OpenThesaurus",
      "type": "n8n-nodes-base.openThesaurus",
      "position": [
        750,
        260
      ],
      "parameters": {
        "text": "Hallo",
        "options": {}
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "OpenThesaurus",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
