# Purge n8n execution history located in Mysql

**[View Template](https://n8n.io/workflows/700-/)**  **Published Date:** 10/04/2020  **Created By:** Miquel Colomer  **Categories:** `Data & Storage` `Development`  

## Template Description

This workflow is useful if you have lots of tasks running daily.

MySQL node (or the database used to save data shown in n8n - could be Mongo, Postgres, ... -) remove old entries from execution_entity table that contains the history of the executed workflows.



If you have multiple tasks executed every minute, 1024 rows will be created every day (60 minutes x 24 hours) per every task. This will increase the table size fastly.

SQL query deletes entries older than 30 days taking stoppedAt column as a reference for date calculations.



You only have to setup Mysql connection properly and config cron to execute once per day in a low traffic hour, this way



## Template JSON

```
{
  "id": "60",
  "name": "n8n_mysql_purge_history_greater_than_10_days",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "MySQL",
      "type": "n8n-nodes-base.mySql",
      "position": [
        450,
        300
      ],
      "parameters": {
        "query": "DELETE FROM execution_entity \nWHERE DATE(stoppedAt) < DATE_SUB(CURDATE(), INTERVAL 30 DAY)",
        "operation": "executeQuery"
      },
      "credentials": {
        "mySql": "n8n"
      },
      "typeVersion": 1
    },
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        250,
        460
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 7
            }
          ]
        }
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
            "node": "MySQL",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "MySQL",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
