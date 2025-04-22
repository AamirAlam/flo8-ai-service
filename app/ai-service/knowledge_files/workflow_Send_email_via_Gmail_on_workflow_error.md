# Send email via Gmail on workflow error

**[View Template](https://n8n.io/workflows/696-/)**  **Published Date:** 10/01/2020  **Created By:** Trey  **Categories:** `Communication` `HITL`  

## Template Description



Send an email via Gmail when a workflow error occurs.

The email subject line will contain the workflow name; the message body will contain the following information:

Workflow name
Error message
Last node executed
Execution URL
Stacktrace

Error workflows do not need to be activated in order to be used, but they do need to be selected in the Settings menu of whatever workflows you want to use it.

To use this workflow, you'll need to:
Create and select credentials in the Gmail node
Choose the email recipient(s) in the Gmail node
Save and select the created workflow as the "Error Workflow" in the Settings menu of whatever workflows you want to email on error

## Template JSON

```
{
  "nodes": [
    {
      "name": "Error Trigger",
      "type": "n8n-nodes-base.errorTrigger",
      "position": [
        450,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Gmail",
      "type": "n8n-nodes-base.gmail",
      "position": [
        650,
        300
      ],
      "parameters": {
        "toList": [
          "recipient@email.com"
        ],
        "message": "=Workflow: {{$json[\"workflow\"][\"name\"]}}\nError: {{$json[\"execution\"][\"error\"][\"message\"]}}\nLast node executed: {{$json[\"execution\"][\"lastNodeExecuted\"]}}\nExecution URL: {{$json[\"execution\"][\"url\"]}}\nStacktrace:\n{{$json[\"execution\"][\"error\"][\"stack\"]}}",
        "subject": "=n8n Workflow Failure:  {{$json[\"workflow\"][\"name\"]}}",
        "resource": "message",
        "additionalFields": {}
      },
      "credentials": {
        "gmailOAuth2": "TBD"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Error Trigger": {
      "main": [
        [
          {
            "node": "Gmail",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
