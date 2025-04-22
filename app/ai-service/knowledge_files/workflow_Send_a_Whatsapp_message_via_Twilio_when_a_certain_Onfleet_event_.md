# Send a Whatsapp message via Twilio when a certain Onfleet event happens

**[View Template](https://n8n.io/workflows/1525-/)**  **Published Date:** 03/16/2022  **Created By:** James Li  **Categories:** `Development` `Communication`  

## Template Description

Summary

Onfleet is a last-mile delivery software that provides end-to-end route planning, dispatch, communication, and analytics to handle the heavy lifting while you can focus on your customers.

This workflow template listens to an Onfleet event and communicates via a Whatsapp message. You can easily streamline this with the recipient of the delivery or your customer support numbers.

Configurations

Update the Onfleet trigger node with your own Onfleet credentials, to register for an Onfleet API key, please visit https://onfleet.com/signup to get started
You can easily change which Onfleet event to listen to. Learn more about Onfleet webhooks with Onfleet Support
Update the Twilio node with your own Twilio credentials, add your own expressions to the to number or simply source the recipient's phone number from the Onfleet event
Toggle To Whatsapp to OFF if you want to simply use Twilio's SMS API

## Template JSON

```
{
  "id": 7,
  "name": "Onfleet Trigger --> Twilio Whatsapp",
  "nodes": [
    {
      "name": "Twilio",
      "type": "n8n-nodes-base.twilio",
      "position": [
        680,
        300
      ],
      "parameters": {
        "message": "=Your delivery is on the way, please visit {{$json[\"body\"][\"data\"][\"task\"][\"trackingURL\"]}} to track your driver's location.",
        "options": {},
        "toWhatsapp": true
      },
      "credentials": {
        "twilioApi": {
          "id": "5",
          "name": "Twilio account"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Onfleet Trigger",
      "type": "n8n-nodes-base.onfleetTrigger",
      "position": [
        460,
        300
      ],
      "webhookId": "db02ef2c-fda1-43f0-84d5-ba4ad7d5dea3",
      "parameters": {
        "triggerOn": "taskCreated",
        "additionalFields": {}
      },
      "credentials": {
        "onfleetApi": {
          "id": "2",
          "name": "Onfleet API Key"
        }
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Onfleet Trigger": {
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
