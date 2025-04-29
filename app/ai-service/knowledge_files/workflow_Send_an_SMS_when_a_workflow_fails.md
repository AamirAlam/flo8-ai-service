# Send an SMS when a workflow fails

**[View Template](https://n8n.io/workflows/665-/)**  **Published Date:** 09/15/2020  **Created By:** ghagrawal17  **Categories:** `Development` `Communication`  

## Template Description



## Template JSON

```
{
  "id": "56",
  "name": "Send an SMS when a workflow fails",
  "nodes": [
    {
      "name": "Error Trigger",
      "type": "n8n-nodes-base.errorTrigger",
      "position": [
        550,
        260
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Twilio",
      "type": "n8n-nodes-base.twilio",
      "position": [
        750,
        260
      ],
      "parameters": {
        "to": "",
        "from": "",
        "message": "=Your workflow with ID: {{$node[\"Error Trigger\"].json[\"workflow\"][\"id\"]}} and name: {{$node[\"Error Trigger\"].json[\"workflow\"][\"name\"]}} failed to execute."
      },
      "credentials": {
        "twilioApi": "twilio-credentials"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Error Trigger": {
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
