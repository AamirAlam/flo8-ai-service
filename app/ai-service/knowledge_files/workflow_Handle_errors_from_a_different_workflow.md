# Handle errors from a different workflow

**[View Template](https://n8n.io/workflows/8-/)**  **Published Date:** 08/31/2019  **Created By:** Jan Oberhauser  **Categories:** `Development` `Communication`  

## Template Description



When set as "Error Workflow" on other workflow which does fail will it send an Email with information about which workflow did fail and what went wrong.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Error Trigger",
      "type": "n8n-nodes-base.errorTrigger",
      "position": [
        250,
        500
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Mailgun",
      "type": "n8n-nodes-base.mailgun",
      "position": [
        450,
        500
      ],
      "parameters": {
        "text": "=Error: {{$node[\"Error Trigger\"].data[\"execution\"][\"error\"][\"message\"]}}\n\nStack Trace:\n{{$node[\"Error Trigger\"].data[\"execution\"][\"error\"][\"stack\"]}}",
        "subject": "=Workflow Error:  {{$node[\"Error Trigger\"].data[\"workflow\"][\"name\"]}}",
        "toEmail": "",
        "fromEmail": ""
      },
      "credentials": {
        "mailgunApi": ""
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Error Trigger": {
      "main": [
        [
          {
            "node": "Mailgun",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
