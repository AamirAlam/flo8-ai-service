# Send Github notifications to Discord Webhook

**[View Template](https://n8n.io/workflows/471-/)**  **Published Date:** 07/10/2020  **Created By:** rangelstoilov  **Categories:** `Development` `Core Nodes` `Communication` `HITL`  

## Template Description

This will send your Github notifications to a discord webhook.

Since Github doesn't send push notifications to mobile devices other then @mention this is a great workaround to receive notifications on Discord with this.

Using a github trigger was not a good option as there is no trigger for notifications only events (which don't work on org repos). Using http request on notifications api is way better.

++TAGGING USER IN MESSATGE:++
Change ** with your discord Id to get tagged when sending notifications. To find your own id type in any channel backslash followed by your username with the 4 digit hash code

You can copy this by clicking on your username next to your profile picture 

Example:
\@username#9999

Enjoy!

## Template JSON

```
{
  "nodes": [
    {
      "name": "@Get Issue",
      "type": "n8n-nodes-base.httpRequest",
      "maxTries": 3,
      "position": [
        1050,
        590
      ],
      "parameters": {
        "url": "https://api.github.com/notifications",
        "options": {},
        "authentication": "basicAuth",
        "queryParametersUi": {
          "parameter": [
            {
              "name": "since",
              "value": "={{$node[\"@Get Date 1 min ago\"].json[\"since\"]}}"
            }
          ]
        },
        "headerParametersUi": {
          "parameter": [
            {
              "name": "User-Agent",
              "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
            }
          ]
        }
      },
      "credentials": {
        "httpBasicAuth": "Github Auth"
      },
      "retryOnFail": true,
      "typeVersion": 1
    },
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        710,
        590
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "mode": "everyX",
              "unit": "minutes",
              "value": 1
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Discord",
      "type": "n8n-nodes-base.discord",
      "position": [
        1610,
        580
      ],
      "parameters": {
        "text": "=Notifications In last minutes: <@userIdForTagging>\n{{$node[\"Function\"].json[\"reportMessage\"]}}"
      },
      "typeVersion": 1
    },
    {
      "name": "Function",
      "type": "n8n-nodes-base.function",
      "position": [
        1230,
        590
      ],
      "parameters": {
        "functionCode": "const newItems = [];\n\nfor (const item of items[0].json) {\n     newItems.push(`- [${item.reason}] => ${item.subject.title} @ ${item.subject.url.replace('api.','').replace('/repos','')}`);\n  }\n\nreturn [{json: {reportMessage: `${newItems.join('\\r\\n')}`, hasNotifications: items[0].json.length > 0}}];\n"
      },
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        1400,
        590
      ],
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{$node[\"Function\"].json[\"hasNotifications\"]}}",
              "value2": true
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "@Get Date 1 min ago",
      "type": "n8n-nodes-base.function",
      "position": [
        860,
        590
      ],
      "parameters": {
        "functionCode": "const date = new Date(new Date().setMinutes(new Date().getMinutes() - (1))).toISOString()\nreturn [{json: {since: date}}];"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "Discord",
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
            "node": "@Get Date 1 min ago",
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
            "node": "IF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "@Get Issue": {
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
    "@Get Date 1 min ago": {
      "main": [
        [
          {
            "node": "@Get Issue",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
