# Send SMS alerts based on database queries (Twilio and Postgres)

**[View Template](https://n8n.io/workflows/357-/)**  **Published Date:** 05/05/2020  **Created By:** tanaypant  **Categories:** `Data & Storage` `Development` `Communication`  

## Template Description

This workflow automatically queries a Postgres database to find outlier readings for which SMS notifications have not been sent.
This is Workflow 2 in the blog tutorial Database activity monitoring and alerting.

Prerequisites

A Postgres database set up and credentials
A Twilio account and credentials

Nodes

Cron node triggers the workflow every minute, so the database is queried at regular intervals.
Postgres nodes extract values from, and update values in the database.
Twilio node sends an alert SMS about the outlier reading to a specified phone number.
Set node sets the notification value to true.

## Template JSON

```
{
  "id": "34",
  "name": "Monitoring and alerting",
  "nodes": [
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        250,
        200
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Postgres",
      "type": "n8n-nodes-base.postgres",
      "position": [
        450,
        200
      ],
      "parameters": {
        "query": "SELECT * FROM n8n WHERE value > 70 AND notification = false;",
        "operation": "executeQuery"
      },
      "credentials": {
        "postgres": "Postgres"
      },
      "typeVersion": 1
    },
    {
      "name": "Twilio",
      "type": "n8n-nodes-base.twilio",
      "position": [
        650,
        200
      ],
      "parameters": {
        "to": "",
        "from": "",
        "message": "=\ud83d\udea8 The Sensor ({{$node[\"Postgres\"].json[\"sensor_id\"]}}) showed a reading of {{$node[\"Postgres\"].json[\"value\"]}}."
      },
      "credentials": {
        "twilioApi": "Twilio"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        850,
        200
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "id",
              "value": "={{$node[\"Postgres\"].json[\"id\"]}}"
            }
          ],
          "boolean": [
            {
              "name": "notification",
              "value": true
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "Postgres1",
      "type": "n8n-nodes-base.postgres",
      "position": [
        1050,
        200
      ],
      "parameters": {
        "table": "n8n",
        "columns": "notification",
        "operation": "update"
      },
      "credentials": {
        "postgres": "Postgres"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Set": {
      "main": [
        [
          {
            "node": "Postgres1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Cron": {
      "main": [
        [
          {
            "node": "Postgres",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Twilio": {
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
    "Postgres": {
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
