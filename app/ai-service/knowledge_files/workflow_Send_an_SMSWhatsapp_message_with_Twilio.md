# Send an SMS/Whatsapp message with Twilio

**[View Template](https://n8n.io/workflows/401-/)**  **Published Date:** 06/12/2020  **Created By:** tanaypant  **Categories:** `Development` `Communication`  

## Template Description



## Template JSON

```
{
  "name": "A workflow with the Twilio node",
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
      "name": "Twilio",
      "type": "n8n-nodes-base.twilio",
      "position": [
        430,
        300
      ],
      "parameters": {},
      "credentials": {
        "twilioApi": ""
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
            "node": "Twilio",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
