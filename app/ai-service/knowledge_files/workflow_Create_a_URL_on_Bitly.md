# Create a URL on Bitly

**[View Template](https://n8n.io/workflows/442-/)**  **Published Date:** 07/01/2020  **Created By:** sshaligr  **Categories:** `Utility`  

## Template Description



## Template JSON

```
{
  "id": "5",
  "name": "new",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        490,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Bitly",
      "type": "n8n-nodes-base.bitly",
      "position": [
        830,
        300
      ],
      "parameters": {
        "longUrl": "https://calendar.usc.edu/event/curricular_practical_training_cpt_information_session_8120?utm_campaign=widget&utm_medium=widget&utm_source=USC+Event+Calendar#.Xv0UlpNKhQK",
        "additionalFields": {}
      },
      "credentials": {
        "bitlyApi": "test"
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
            "node": "Bitly",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
