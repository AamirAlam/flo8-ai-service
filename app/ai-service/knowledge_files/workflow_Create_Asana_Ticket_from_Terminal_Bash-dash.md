# Create Asana Ticket from Terminal Bash-dash

**[View Template](https://n8n.io/workflows/987-/)**  **Published Date:** 03/17/2021  **Created By:** Jan Oberhauser  **Categories:** `Productivity`  

## Template Description

This workflow allows creating a new Asana task via bash-dash 



Example usage:
\- asana My new task

Example bash-dash config:
commands[asana]="http://localhost:5678/webhook/asana"


## Template JSON

```
{
  "nodes": [
    {
      "name": "Asana",
      "type": "n8n-nodes-base.asana",
      "position": [
        450,
        500
      ],
      "parameters": {
        "name": "={{$json[\"query\"][\"parameter\"]}}",
        "workspace": "",
        "authentication": "oAuth2",
        "otherProperties": {
          "projects": [
            ""
          ]
        }
      },
      "credentials": {
        "asanaOAuth2Api": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        250,
        500
      ],
      "webhookId": "b43ae7e2-a058-4738-8d49-ac76db6e8166",
      "parameters": {
        "path": "asana",
        "options": {
          "responsePropertyName": "response"
        },
        "responseMode": "lastNode"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        650,
        500
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "response",
              "value": "=Created Asana Task:  {{$json[\"permalink_url\"]}}"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Asana": {
      "main": [
        [
          {
            "node": "Set",
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
            "node": "Asana",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
