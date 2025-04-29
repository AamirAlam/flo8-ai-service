# Post unassigned Zendesk tickets to Slack

**[View Template](https://n8n.io/workflows/1265-/)**  **Published Date:** 10/11/2021  **Created By:** Jonathan Bennetts  **Categories:** `Communication` `HITL`  

## Template Description

&gt; This has been updated to support the Query feature added to the Zendesk node in 0.144.0

This workflow will post all New and Open tickets without an agent assigned to a Slack channel on a schedule.



The function node is used in this example to merge multiple inputs into one output message which is then used as the Slack message.

The output in Slack will be similar to the below message, The "TICKET_ID" will be a link to the ticket.

&gt; Unassigned Tickets
TICKET_ID [STATUS] - TICKET_SUBJECT

Usage
Update the Cron schedule, The default value is 16:30 daily.
Update the Credentials in the Zendesk nodes
Update the Credentials and Channel in the Slack Node
Grab a coffee and enjoy!

Zendesk Query
In the Zendesk node we are using the query assignee:none status&lt;pending this returns all New and Open tickets with no assignee allowing us to remove the extra nodes.

## Template JSON

```
{
  "id": 23,
  "name": "Zendesk-to-slack",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        360,
        350
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "color": "#068906",
      "position": [
        360,
        560
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 16,
              "minute": 30
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
        690,
        460
      ],
      "parameters": {
        "functionCode": "// Create our Slack message\n// This will output a list of Ticket URLs with the status and the subject\n// 12345 [STATUS] - Ticket Subject\nlet message = \"*Unassigned Tickets*\\n\\n\";\n\n// Loop the input items\nfor (item of items) {\n  // Append the ticket information to the message\n  message += \"*<\" + item.json.url.replace(\"api/v2\",\"agent\").replace(\".json\",\"\") + \"|\" + item.json.id + \">* [\" + item.json.status.toUpperCase() + \"] - \" + item.json.subject + \"\\n\"; \n}\n\n// Return our message\nreturn [{json: {message}}];"
      },
      "typeVersion": 1
    },
    {
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "position": [
        870,
        460
      ],
      "parameters": {
        "text": "={{$json[\"message\"]}}",
        "channel": "jarvis-test",
        "attachments": [],
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Zendesk",
      "type": "n8n-nodes-base.zendesk",
      "position": [
        510,
        460
      ],
      "parameters": {
        "options": {
          "query": "assignee:none status<pending"
        },
        "operation": "getAll",
        "returnAll": true
      },
      "credentials": {
        "zendeskApi": {
          "id": "1",
          "name": "Zendesk"
        }
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Cron": {
      "main": [
        [
          {
            "node": "Zendesk",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Zendesk": {
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
            "node": "Slack",
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
            "node": "Zendesk",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
