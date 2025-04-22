# Send a message to a channel on Twake

**[View Template](https://n8n.io/workflows/595-/)**  **Published Date:** 08/07/2020  **Created By:** ghagrawal17  **Categories:** `Productivity`  

## Template Description



## Template JSON

```
{
  "id": "1",
  "name": "Send a message on Twake",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        600,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Twake",
      "type": "n8n-nodes-base.twake",
      "position": [
        800,
        300
      ],
      "parameters": {
        "content": "",
        "channelId": "",
        "additionalFields": {}
      },
      "credentials": {
        "twakeCloudApi": ""
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
            "node": "Twake",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
