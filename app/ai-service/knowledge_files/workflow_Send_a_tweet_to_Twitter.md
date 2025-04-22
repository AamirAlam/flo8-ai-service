# Send a tweet to Twitter

**[View Template](https://n8n.io/workflows/445-/)**  **Published Date:** 07/03/2020  **Created By:** amudhan  **Categories:** `Marketing`  

## Template Description

Companion workflow for Twitter node docs.



## Template JSON

```
{
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
      "name": "Twitter",
      "type": "n8n-nodes-base.twitter",
      "position": [
        450,
        300
      ],
      "parameters": {
        "text": "This is a test workflow for the twitter node",
        "additionalFields": {}
      },
      "credentials": {
        "twitterOAuth1Api": "twitter-credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Twitter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
