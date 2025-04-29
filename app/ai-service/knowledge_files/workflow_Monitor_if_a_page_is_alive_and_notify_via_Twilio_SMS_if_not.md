# Monitor if a page is alive and notify via Twilio SMS if not

**[View Template](https://n8n.io/workflows/2524-/)**  **Published Date:** 11/04/2024  **Created By:** Rui Borges  **Categories:** `Development` `Core Nodes` `Communication`  

## Template Description

Workflow Purpose

This workflow periodically checks a service's availability and sends an SMS notification if the service is down.

High-Level Steps

Schedule Trigger: The workflow is triggered at a specified interval, such as every minute.
HTTP Request: An HTTP request is sent to the URL of the service being monitored.
If: The HTTP status code of the response is checked.
If the status code is 200 (OK), the workflow ends.
If the status code is not 200, indicating a potential issue, an SMS notification is sent using Twilio.

Setup
Setting up this workflow is relatively straightforward and should only take a few minutes:

Create a new n8n workflow.
Add the nodes: Schedule Trigger, HTTP Request, If, and Twilio.
Configure the nodes:
Schedule Trigger: Specify the desired interval.
HTTP Request: Enter the URL of the service to be monitored.
If: Set the condition to check for a status code other than 200.
Twilio: Enter the Twilio account credentials and the phone numbers for sending and receiving the SMS notification.
Connect the nodes: Connect the nodes as shown in the workflow diagram.
Activate the workflow: Save the workflow and activate it.

Additional Notes

The workflow can be customized by changing the interval, the URL, the Twilio credentials, and the SMS message.
This workflow is a simple example, and more complex workflows can be created to meet specific needs.

## Template JSON

```
{
  "id": "ppsHlJlSpHPQJp4Q",
  "meta": {
    "instanceId": "558d88703fb65b2d0e44613bc35916258b0f0bf983c5d4730c00c424b77ca36a"
  },
  "tags": [],
  "nodes": [
    {
      "id": "6615e821-d47d-4df9-aa10-4aebdd9e6737",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -1100,
        -540
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "minutes"
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "456b6ea3-1360-4a6c-a862-84c022db78e4",
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -740,
        -540
      ],
      "parameters": {
        "url": "",
        "options": {
          "response": {
            "response": {
              "fullResponse": true
            }
          }
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "d1155cfc-c27a-40c5-8d70-c0705ce24c9b",
      "name": "Twilio",
      "type": "n8n-nodes-base.twilio",
      "position": [
        -240,
        -520
      ],
      "parameters": {
        "to": "",
        "from": "",
        "message": "Service Down",
        "options": {}
      },
      "credentials": {
        "twilioApi": {
          "id": "Izc7tLRJsN06wezO",
          "name": "Twilio account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "f4a781ab-96bf-4801-95d4-df8f8fbd1f8a",
      "name": "If",
      "type": "n8n-nodes-base.if",
      "position": [
        -520,
        -540
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "75b05c45-447e-407b-847f-5ed909b3c325",
              "operator": {
                "type": "number",
                "operation": "equals"
              },
              "leftValue": "={{ $json.statusCode }}",
              "rightValue": 200
            }
          ]
        }
      },
      "typeVersion": 2.2
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "1918412f-8dd2-404c-ad68-0b48f09ff7fc",
  "connections": {
    "If": {
      "main": [
        [],
        [
          {
            "node": "Twilio",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request": {
      "main": [
        [
          {
            "node": "If",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Schedule Trigger": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
