# Request and Receive Zigbee backup from zigbee2mqtt and save it via SFTP

**[View Template](https://n8n.io/workflows/2371-/)**  **Published Date:** 08/03/2024  **Created By:** Hubschrauber  **Categories:** `Data & Storage` `Development` `Utility` `Core Nodes` `Communication`  

## Template Description

A single workflow with 2 flows/paths that combine to handle the backup sequence for Zigbee device configuration from HomeAssistant / zigbee2mqtt.  This provides a way to automate a periodic capture of Zigbee coordinators and device pairings to speed the recovery process when/if the HomeAssistant instance needs to be rebuilt.  Setting up similar automation without n8n (e.g. shell scripts and system timers) is consiterably more challenging.  n8n makes it easy and this template should remove any other excuse not to do it.

Flow 1
Triggered by Cron/Timer
  set whatever interval for backups
  sends mqtt message to request zigbee2mqtt backup (via separate message)

Flow 2
Triggered by zigbee2mqtt backup message
Extracts zip file from the message and stores somewhere, with a date-stamp in the filename, via sftp

Setup
Create a MQTT connection named "MQTT Account" with the appropriate protocol (mqtt), host, port (1883), username, and password
Create an sftp connection named "SFTP Zigbee Backups" with the appropriate host, port (22), username, and password or key.

Reference
This article describes the mqtt parts.


## Template JSON

```
{
  "nodes": [
    {
      "name": "SFTP zip file content",
      "type": "n8n-nodes-base.ftp",
      "position": [
        1520,
        680
      ],
      "parameters": {
        "path": "=zigbee_backups/zigbee_backup_{{ new Date().toISOString().replaceAll(':','_') }}.zip",
        "protocol": "sftp",
        "operation": "upload"
      },
      "credentials": {
        "sftp": {
          "name": "SFTP Zigbee Backups"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "CRON Monday 2:45 am",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        860,
        440
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "cronExpression",
              "expression": "45 2 * * 1"
            }
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "name": "Send Zigbee2MQTT backup request",
      "type": "n8n-nodes-base.mqtt",
      "position": [
        1040,
        440
      ],
      "parameters": {
        "topic": "zigbee2mqtt/bridge/request/backup",
        "message": "getbackup",
        "options": {},
        "sendInputData": false
      },
      "credentials": {
        "mqtt": {
          "name": "MQTT account"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "MQTT Trigger - Backup Response",
      "type": "n8n-nodes-base.mqttTrigger",
      "position": [
        860,
        680
      ],
      "parameters": {
        "topics": "zigbee2mqtt/bridge/response/backup",
        "options": {}
      },
      "credentials": {
        "mqtt": {
          "name": "MQTT account"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Parse JSON Object from Message Text",
      "type": "n8n-nodes-base.code",
      "position": [
        1080,
        680
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "\nlet containerObject = JSON.parse($json.message);\nlet messageObject = containerObject.data;\nreturn messageObject;"
      },
      "typeVersion": 2
    },
    {
      "name": "Convert to File - base64 to binary",
      "type": "n8n-nodes-base.convertToFile",
      "position": [
        1300,
        680
      ],
      "parameters": {
        "options": {},
        "operation": "toBinary",
        "sourceProperty": "zip"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "CRON Monday 2:45 am": {
      "main": [
        [
          {
            "node": "Send Zigbee2MQTT backup request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "MQTT Trigger - Backup Response": {
      "main": [
        [
          {
            "node": "Parse JSON Object from Message Text",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Convert to File - base64 to binary": {
      "main": [
        [
          {
            "node": "SFTP zip file content",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parse JSON Object from Message Text": {
      "main": [
        [
          {
            "node": "Convert to File - base64 to binary",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
