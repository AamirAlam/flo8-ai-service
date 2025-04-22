# Generate and queue factory sensor data in AMQP

**[View Template](https://n8n.io/workflows/608-/)**  **Published Date:** 08/12/2020  **Created By:** ghagrawal17  **Categories:** `Development` `Communication`  

## Template Description

This workflow generates sensor data, which is used in another workflow for managing factory incident reports.

Read more about this use case and how to build both workflows with step-by-step instructions in the blog post How to automate your factory’s incident reporting.

Prerequisites

AMQP, an ActiveMQ  connection, and credentials

Nodes

Interval node triggers the workflow every second.
Set node set the necessary values for the items that are addeed to the queue.
AMQP Sender node sends a raw message to add to the queue.

## Template JSON

```
{
  "id": "167",
  "name": "Smart Factory Data Generator",
  "nodes": [
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        650,
        300
      ],
      "parameters": {
        "values": {
          "number": [],
          "string": [
            {
              "name": "machine_id.name",
              "value": "n8n_cr8"
            },
            {
              "name": "temperature_celsius",
              "value": "={{Math.floor(Math.random() * 100);}}"
            },
            {
              "name": "machine_id.uptime",
              "value": "={{Math.floor(Math.random() * 100);}}"
            },
            {
              "name": "time_stamp",
              "value": "={{Date.now();}}"
            }
          ],
          "boolean": []
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "Interval",
      "type": "n8n-nodes-base.interval",
      "position": [
        450,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "AMQP Sender",
      "type": "n8n-nodes-base.amqp",
      "position": [
        850,
        300
      ],
      "parameters": {
        "sink": "berlin_factory_01",
        "options": {
          "dataAsObject": true
        }
      },
      "credentials": {
        "amqp": ""
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
            "node": "AMQP Sender",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Interval": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
