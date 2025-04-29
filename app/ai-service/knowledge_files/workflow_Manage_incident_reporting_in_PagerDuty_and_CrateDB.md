# Manage incident reporting in PagerDuty and CrateDB

**[View Template](https://n8n.io/workflows/609-/)**  **Published Date:** 08/12/2020  **Created By:** ghagrawal17  **Categories:** `Development` `Communication` `Data & Storage`  

## Template Description

This workflow automatically monitors the functionality of a factory. The workflow logs machine data coming from factory sensors in a CrateDB database, generates an incident report in PagerDuty, and notifies the responsible staff members when the temperature of a machine crosses the threshold value.

This workflow builds on a workflow that generates factory data.

Read more about this use case and how to build both workflows with step-by-step instructions in the blog post How to automate your factory's incident reporting.

Prerequisites

A PagerDuty account and credentials
AMQP, an ActiveMQ  connection, and credentials
A CrateDB instance running locally or on a server, and credentials.

Nodes

AMQP Trigger node starts the workflow.
IF node filters sensor values higher than 50°C.
PagerDuty node creates an incident in the account.
Set nodes set the required incident information and sensor data, respectively.
CrateDB nodes ingest the information data and machine sensor data, respectively.
Function node converts degrees from Celsius to Fahrenheit.

## Template JSON

```
{
  "id": "168",
  "name": "Smart Factory Use Case",
  "nodes": [
    {
      "name": "Values higher than 50\u00b0C",
      "type": "n8n-nodes-base.if",
      "position": [
        250,
        550
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$node[\"Data from factory sensors\"].json[\"body\"][\"temperature_celsius\"]}}",
              "value2": 50,
              "operation": "largerEqual"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Data from factory sensors",
      "type": "n8n-nodes-base.amqpTrigger",
      "position": [
        50,
        700
      ],
      "parameters": {
        "sink": "berlin_factory_01",
        "options": {}
      },
      "credentials": {
        "amqp": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Set sensor data",
      "type": "n8n-nodes-base.set",
      "position": [
        450,
        850
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "temeprature_fahrenheit",
              "value": "={{$node[\"Data enrichment (\u00b0C to \u00b0F)\"].json[\"temperature_fahrenheit\"]}}"
            },
            {
              "name": "temperature_celsius",
              "value": "={{$node[\"Data enrichment (\u00b0C to \u00b0F)\"].json[\"body\"][\"temperature_celsius\"]}}"
            },
            {
              "name": "machine_uptime",
              "value": "={{$node[\"Data from factory sensors\"].json[\"body\"][\"machine_id\"][\"uptime\"]}}"
            },
            {
              "name": "time_stamp",
              "value": "={{$node[\"Data from factory sensors\"].json[\"body\"][\"time_stamp\"]}}"
            }
          ],
          "string": [
            {
              "name": "machine_name",
              "value": "={{$node[\"Data from factory sensors\"].json[\"body\"][\"machine_id\"][\"name\"]}}"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "Ingest machine data",
      "type": "n8n-nodes-base.crateDb",
      "position": [
        650,
        850
      ],
      "parameters": {
        "table": "machine_data",
        "columns": "temperature_fahrenheit, temperature_celsius, machine_name, machine_uptime, time_stamp"
      },
      "credentials": {
        "crateDb": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Ingest incident data",
      "type": "n8n-nodes-base.crateDb",
      "position": [
        850,
        450
      ],
      "parameters": {
        "table": "incident_data",
        "columns": "incident_id, html_url, incident_timestamp"
      },
      "credentials": {
        "crateDb": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Set incident info",
      "type": "n8n-nodes-base.set",
      "position": [
        650,
        450
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "incident_id",
              "value": "={{$node[\"Create an incident\"].json[\"id\"]}}"
            },
            {
              "name": "html_url",
              "value": "={{$node[\"Create an incident\"].json[\"html_url\"]}}"
            },
            {
              "name": "incident_timestamp",
              "value": "={{$node[\"Create an incident\"].json[\"created_at\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "Create an incident",
      "type": "n8n-nodes-base.pagerDuty",
      "position": [
        450,
        450
      ],
      "parameters": {
        "title": "=Incident with {{$node[\"Data from factory sensors\"].json[\"body\"][\"machine_id\"][\"name\"]}}",
        "additionalFields": {}
      },
      "credentials": {
        "pagerDutyApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Data enrichment (\u00b0C to \u00b0F)",
      "type": "n8n-nodes-base.function",
      "position": [
        250,
        850
      ],
      "parameters": {
        "functionCode": "temp_fahrenheit = (items[0].json.body.temperature_celsius * 1.8) + 32;\nitems[0].json.temperature_fahrenheit = temp_fahrenheit;\nreturn items;"
      },
      "typeVersion": 1,
      "alwaysOutputData": true
    },
    {
      "name": "Do  nothing",
      "type": "n8n-nodes-base.noOp",
      "position": [
        450,
        640
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Set sensor data": {
      "main": [
        [
          {
            "node": "Ingest machine data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set incident info": {
      "main": [
        [
          {
            "node": "Ingest incident data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create an incident": {
      "main": [
        [
          {
            "node": "Set incident info",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Values higher than 50\u00b0C": {
      "main": [
        [
          {
            "node": "Create an incident",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Do  nothing",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Data from factory sensors": {
      "main": [
        [
          {
            "node": "Data enrichment (\u00b0C to \u00b0F)",
            "type": "main",
            "index": 0
          },
          {
            "node": "Values higher than 50\u00b0C",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Data enrichment (\u00b0C to \u00b0F)": {
      "main": [
        [
          {
            "node": "Set sensor data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
