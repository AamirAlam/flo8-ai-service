# Send n8n Error Reports to LINE

**[View Template](https://n8n.io/workflows/3141-/)**  **Published Date:** 03/12/2025  **Created By:** lin@davoy.tech  **Categories:** `Development` `Core Nodes`  

## Template Description

This workflow template, "n8n Error Report to LINE," is designed to streamline error handling by sending real-time notifications to your LINE account whenever an error occurs in any of your n8n workflows. By integrating with the LINE Messaging API , this template ensures you stay informed about workflow failures, allowing you to take immediate action and minimize downtime.

Whether you're a developer managing multiple workflows or a business owner relying on automation, this template provides a simple yet powerful way to monitor and resolve errors efficiently.

Who Is This Template For?

Developers: Who manage complex n8n workflows and need real-time error notifications.
DevOps Teams: Looking to enhance monitoring and incident response for automated systems.
Business Owners: Who rely on n8n workflows for critical operations and want to ensure reliability.
Automation Enthusiasts: Seeking tools to simplify error tracking and improve workflow performance.

What Problem Does This Workflow Solve?
When automating processes with n8n, errors can occur due to various reasons such as misconfigurations, API changes, or unexpected inputs. Without proper error handling, these issues may go unnoticed, leading to delays or disruptions. This workflow solves that problem by:

1) Automatically detecting errors in your n8n workflows.
2) Sending instant notifications to your LINE account with details about the failed workflow, including its name and execution URL. Allowing you to quickly identify and resolve issues, ensuring smooth operation of your automated systems.

What This Workflow Does
1) Error Trigger:
The workflow is triggered automatically whenever an error occurs in any n8n workflow configured to use this error-handling flow.
2) Send Notification via LINE:
Using the LINE Push API , the workflow sends a message to your LINE account with key details about the error, such as the workflow name and execution URL.

You can also customize the notification message to include additional information or format it to suit your preferences.

Setup Guide

Pre-Requisites
Access to the LINE Developers Console with a registered bot and access to the Push API.
https://developers.line.biz/console/
[API Reference](
https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message)
Basic knowledge of n8n workflows and JSON formatting.
An active n8n instance where you can configure error workflows.

Step-by-Step Setup
Configure the Error Trigger:
Set this workflow as the default error workflow in your n8n instance. 
https://docs.n8n.io/flow-logic/error-handling/
Set Up LINE Push API:
Replace &lt;UID HERE&gt; in the HTTP Request node with your LINE user ID to ensure notifications are sent to the correct account.



## Template JSON

```
{
  "id": "ePnGZtZ8zLcf1UZZ",
  "meta": {
    "instanceId": "558d88703fb65b2d0e44613bc35916258b0f0bf983c5d4730c00c424b77ca36a",
    "templateCredsSetupCompleted": true
  },
  "name": "n8n Error Report to Line",
  "tags": [
    {
      "id": "0xpEHcJjNRRRMtEj",
      "name": "lin",
      "createdAt": "2025-03-12T05:06:24.112Z",
      "updatedAt": "2025-03-12T05:06:24.112Z"
    },
    {
      "id": "U1ozjO3iXQZWUyfG",
      "name": "_Blueprint",
      "createdAt": "2025-03-12T06:24:40.268Z",
      "updatedAt": "2025-03-12T06:24:40.268Z"
    }
  ],
  "nodes": [
    {
      "id": "c45a01a5-289b-4927-8bba-4bb1029a7129",
      "name": "Error Trigger",
      "type": "n8n-nodes-base.errorTrigger",
      "position": [
        -240,
        -80
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "1e3f7a7e-8be4-4fec-973f-befb477e6957",
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        40,
        -80
      ],
      "parameters": {
        "url": "https://api.line.me/v2/bot/message/push",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n    \"to\": \"<UID HERE>\",\n    \"messages\":[\n        {\n            \"type\":\"text\",\n            \"text\":\"\ud83d\udea8Your n8n flow is dead.\ud83d\udea8\\n\\nName: {{ $json.workflow.name }} \\nURL: {{ $json.execution.url }}\"\n        }\n    ]\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "lKd3b2nc8uNJ148Z",
          "name": "Line @271dudsw MiniBear"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "5bcf04cc-2c3e-4e37-a134-fcc42326afc3",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -340,
        -400
      ],
      "parameters": {
        "width": 660,
        "content": "## Error Handling\n\nYou can set this workflow as error workflow\n\nhttps://docs.n8n.io/flow-logic/error-handling/#create-and-set-an-error-workflow"
      },
      "typeVersion": 1
    },
    {
      "id": "22b66275-e111-45c8-b7bc-b6c03b55fd02",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -300,
        -220
      ],
      "parameters": {
        "color": 5,
        "height": 300,
        "content": "## Error Trigger\n\nThis flow will get trigger when the error occur. You can set only one error flow for all your flows.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "5a2c1b3b-2546-47e6-bb9f-b9b8d7c63d65",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -40,
        -220
      ],
      "parameters": {
        "color": 4,
        "width": 320,
        "height": 300,
        "content": "## Send Line Message\n\nTo send message to notify you via Line Account -- Please replace <UID HERE> with your own UID\n"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "4a774ee1-96b8-4a81-858d-6c5b0d24ba03",
  "connections": {
    "Error Trigger": {
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
