# Generate and insert data into a Postgres database

**[View Template](https://n8n.io/workflows/356-/)**  **Published Date:** 05/05/2020  **Created By:** tanaypant  **Categories:** `Data & Storage` `Development`  

## Template Description

This is Workflow 1 in the blog tutorial Database activity monitoring and alerting.

Prerequisites

A Postgres database set up and credentials.
Basic knowledge of JavaScript and SQL.

Nodes

Cron node starts the workflow every minute.
Function node generates sensor data (sensor id (preset), a randomly generated value, timestamp, and notification (preset as false) )
Postgres node inserts the data into a Postgres database.
You can create the database for this workflow with the following SQL statement:

CREATE TABLE n8n (id SERIAL, sensor_id VARCHAR, value INT, time_stamp TIMESTAMP, notification BOOLEAN);


## Template JSON

```
{
  "id": "33",
  "name": "Postgres Data Ingestion",
  "nodes": [
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        300,
        250
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Function",
      "type": "n8n-nodes-base.function",
      "position": [
        500,
        250
      ],
      "parameters": {
        "functionCode": "var today = new Date();\nvar date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();\nvar time = today.getHours() + \":\" + today.getMinutes() + \":\" + today.getSeconds();\nvar dateTime = date+' '+time;\n\nitems[0].json.sensor_id = 'humidity01';\nitems[0].json.value = Math.ceil(Math.random()*100);\nitems[0].json.time_stamp = dateTime;\nitems[0].json.notification = false;\n\nreturn items;"
      },
      "typeVersion": 1
    },
    {
      "name": "Postgres",
      "type": "n8n-nodes-base.postgres",
      "position": [
        680,
        250
      ],
      "parameters": {
        "table": "n8n",
        "columns": "sensor_id,value,time_stamp,notification"
      },
      "credentials": {
        "postgres": "Postgres"
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "Cron": {
      "main": [
        [
          {
            "node": "Function",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Function": {
      "main": [
        [
          {
            "node": "Postgres",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
