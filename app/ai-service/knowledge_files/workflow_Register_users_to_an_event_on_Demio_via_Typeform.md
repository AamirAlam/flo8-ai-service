# Register users to an event on Demio via Typeform

**[View Template](https://n8n.io/workflows/947-/)**  **Published Date:** 02/18/2021  **Created By:** ghagrawal17  **Categories:** `Communication`  

## Template Description

This workflow allows you to register your audience to an event on Demio via a Typeform submission.



Typeform Trigger node: This node will trigger the workflow when a form response is submitted. Based on your use-case, you may use a different platform. Replace the Typeform Trigger node with a node of that platform. 

Demio node: This node registers a user for an event. It gets the details of the users from the Typeform response.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Typeform Trigger",
      "type": "n8n-nodes-base.typeformTrigger",
      "position": [
        510,
        260
      ],
      "webhookId": "1cbca674-78fb-402e-b225-2aa6f92b5338",
      "parameters": {
        "formId": ""
      },
      "credentials": {
        "typeformApi": "Typeform Burner Account"
      },
      "typeVersion": 1
    },
    {
      "name": "Demio",
      "type": "n8n-nodes-base.demio",
      "position": [
        710,
        260
      ],
      "parameters": {
        "email": "={{$json[\"What's your email address?\"]}}",
        "eventId": 357191,
        "firstName": "={{$json[\"Let's start with your name.\"]}}",
        "operation": "register",
        "additionalFields": {}
      },
      "credentials": {
        "demioApi": "Demio API Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Typeform Trigger": {
      "main": [
        [
          {
            "node": "Demio",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
