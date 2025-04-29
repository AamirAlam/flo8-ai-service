# Update time-tracking projects based on Syncro status changes

**[View Template](https://n8n.io/workflows/1492-/)**  **Published Date:** 02/22/2022  **Created By:** Jonathan  **Categories:** `Development` `Core Nodes` `Productivity`  

## Template Description

This workflow is part of an MSP collection, which is publicly available on GitHub.

This workflow archives or unarchives a Clockify projects, depending on a Syncro status. Note that Syncro should be setup with a webhook via 'Notification Set for Ticket - Status was changed'. It doesn't handle merging of tickets, as Syncro doesn't support a 'Notification Set' for merged tickets, so you should change a ticket to 'Resolved' first before merging it.

Prerequisites

A Clockify account and credentials

Nodes

Webhook node triggers the workflow.
IF node filters projects that don't have the status 'Resolved'.
Clockify nodes get all projects that (don't) have the status 'Resolved', based on the IF route.
HTTP Request nodes unarchives unresolved projects, and archives resolved projects, respectively.

## Template JSON

```
{
  "id": "5",
  "name": "Syncro Status Update Clockify",
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        560,
        310
      ],
      "webhookId": "3300d16f-5d43-4ae7-887e-376eecaeec17",
      "parameters": {
        "path": "4500d16f-5d43-4ae7-887e-376eecaeec17",
        "options": {},
        "httpMethod": "POST",
        "responseData": "allEntries",
        "responseMode": "lastNode"
      },
      "typeVersion": 1
    },
    {
      "name": "Clockify",
      "type": "n8n-nodes-base.clockify",
      "position": [
        960,
        310
      ],
      "parameters": {
        "operation": "getAll",
        "returnAll": true,
        "workspaceId": "xxx",
        "additionalFields": {
          "name": "=Ticket {{$node[\"Webhook\"].json[\"body\"][\"attributes\"][\"number\"]}} - {{$node[\"Webhook\"].json[\"body\"][\"attributes\"][\"customer_business_then_name\"]}} [{{$node[\"Webhook\"].json[\"body\"][\"attributes\"][\"id\"]}}]",
          "archived": true
        }
      },
      "credentials": {
        "clockifyApi": "Clockify"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1130,
        310
      ],
      "parameters": {
        "url": "=https://api.clockify.me/api/v1/workspaces/{{$node[\"Clockify\"].parameter[\"workspaceId\"]}}/projects/{{$json[\"id\"]}}",
        "options": {},
        "requestMethod": "PUT",
        "authentication": "headerAuth",
        "bodyParametersUi": {
          "parameter": [
            {
              "name": "archived",
              "value": "false"
            },
            {
              "name": "isPublic",
              "value": "true"
            }
          ]
        },
        "headerParametersUi": {
          "parameter": []
        }
      },
      "credentials": {
        "httpHeaderAuth": "Clockify API"
      },
      "typeVersion": 1
    },
    {
      "name": "IF1",
      "type": "n8n-nodes-base.if",
      "position": [
        730,
        310
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"body\"][\"attributes\"][\"status\"]}}",
              "value2": "Resolved",
              "operation": "notEqual"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Clockify1",
      "type": "n8n-nodes-base.clockify",
      "position": [
        960,
        540
      ],
      "parameters": {
        "operation": "getAll",
        "returnAll": true,
        "workspaceId": "xxx",
        "additionalFields": {
          "name": "=Ticket {{$node[\"Webhook\"].json[\"body\"][\"attributes\"][\"number\"]}} - {{$node[\"Webhook\"].json[\"body\"][\"attributes\"][\"customer_business_then_name\"]}} [{{$node[\"Webhook\"].json[\"body\"][\"attributes\"][\"id\"]}}]",
          "archived": false
        }
      },
      "credentials": {
        "clockifyApi": "Clockify"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1130,
        540
      ],
      "parameters": {
        "url": "=https://api.clockify.me/api/v1/workspaces/{{$node[\"Clockify1\"].parameter[\"workspaceId\"]}}/projects/{{$node[\"Clockify1\"].json[\"id\"]}}",
        "options": {},
        "requestMethod": "PUT",
        "authentication": "headerAuth",
        "bodyParametersUi": {
          "parameter": [
            {
              "name": "archived",
              "value": "true"
            },
            {
              "name": "isPublic",
              "value": "true"
            }
          ]
        },
        "headerParametersUi": {
          "parameter": []
        }
      },
      "credentials": {
        "httpHeaderAuth": "Clockify API"
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "IF1": {
      "main": [
        [
          {
            "node": "Clockify",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Clockify1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Webhook": {
      "main": [
        [
          {
            "node": "IF1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clockify": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clockify1": {
      "main": [
        [
          {
            "node": "HTTP Request1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
