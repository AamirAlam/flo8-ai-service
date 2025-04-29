# Translate text from English to German

**[View Template](https://n8n.io/workflows/743-/)**  **Published Date:** 10/27/2020  **Created By:** ghagrawal17  **Categories:** `Utility`  

## Template Description



## Template JSON

```
{
  "id": "92",
  "name": "Translate text from English to German",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        270,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Google Translate",
      "type": "n8n-nodes-base.googleTranslate",
      "position": [
        470,
        300
      ],
      "parameters": {
        "text": "Hello from n8n!",
        "translateTo": "de",
        "authentication": "oAuth2"
      },
      "credentials": {
        "googleTranslateOAuth2Api": "google-translate"
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
            "node": "Google Translate",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
