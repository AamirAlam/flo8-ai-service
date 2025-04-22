# Translate cocktail instructions using DeepL

**[View Template](https://n8n.io/workflows/998-/)**  **Published Date:** 03/23/2021  **Created By:** ghagrawal17  **Categories:** `Development` `Core Nodes` `Utility`  

## Template Description

This workflow allows you to translate cocktail instructions using DeepL.



HTTP Request node: This node will make a GET request to the API https://www.thecocktaildb.com/api/json/v1/1/random.php to fetch a random cocktail. This information gets passed on to the next node in the workflow. Based on your use case, replace the node with the node from where you might receive the data.

DeepL node: This node will translate the cocktail instructions that we got from the previous node to French. To translate the instructions in your language, select your language instead.


## Template JSON

```
{
  "nodes": [
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        510,
        320
      ],
      "parameters": {
        "url": "https://www.thecocktaildb.com/api/json/v1/1/random.php",
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "DeepL",
      "type": "n8n-nodes-base.deepL",
      "position": [
        710,
        320
      ],
      "parameters": {
        "text": "={{$json[\"drinks\"][0][\"strInstructions\"]}}",
        "translateTo": "FR",
        "additionalFields": {}
      },
      "credentials": {
        "deepLApi": "DeepL API Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "HTTP Request": {
      "main": [
        [
          {
            "node": "DeepL",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
