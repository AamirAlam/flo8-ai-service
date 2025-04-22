# Send an SMS to a number whenever you go out

**[View Template](https://n8n.io/workflows/870-/)**  **Published Date:** 01/01/2021  **Created By:** ghagrawal17  **Categories:** `Development` `Communication`  

## Template Description

This workflow allows you to send an SMS to a number whenever you go out. 



Pushcut is an app for iOS that lets you create smart notifications to kick off shortcuts, URLs, and online automation. 

You can have multiple actions for a notification. You can use the IF node to check which action was selected and build the workflow accordingly. 

Pushcut Trigger node: This node triggers the workflow when an action is selected by the user. 

Twilio node: The Twilio node sends an SMS with the input given by the user. 

Based on your use-case, you might want to do something else, for example, send a Tweet, dim or turn off your Philips Hue lights, add activity to Strava or play music on Spotify. Replace the Twilio node with these nodes to customize the workflow as per your needs.

## Template JSON

```
{
  "id": "92",
  "name": "Send an SMS to a number whenever you go out",
  "nodes": [
    {
      "name": "Pushcut Trigger",
      "type": "n8n-nodes-base.pushcutTrigger",
      "position": [
        470,
        300
      ],
      "webhookId": "",
      "parameters": {
        "actionName": "Leaving Home"
      },
      "credentials": {
        "pushcutApi": "Pushcut Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Twilio",
      "type": "n8n-nodes-base.twilio",
      "position": [
        670,
        300
      ],
      "parameters": {
        "to": "123",
        "from": "123",
        "message": "=I'm {{$node[\"Pushcut Trigger\"].json[\"input\"]}}"
      },
      "credentials": {
        "twilioApi": "twilio"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Pushcut Trigger": {
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
