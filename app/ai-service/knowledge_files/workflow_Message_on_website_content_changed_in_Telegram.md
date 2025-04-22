# Message on website content changed in Telegram

**[View Template](https://n8n.io/workflows/1471-/)**  **Published Date:** 02/18/2022  **Created By:** MC Naveen  **Categories:** `Development` `Core Nodes` `Communication` `HITL`  

## Template Description

I wanted a system to monitor website content changes and notify me. So I made it using n8n.

Especially my competitor blogs. I wanted to know how often they are posting new articles. (I used their sitemap.xml file) (The below workflow may vary)

In the Below example, I used HackerNews for example.

Explanation:

First HTTP Request node crawls the webpage and grabs the website source code
Then wait for x minutes
Again, HTTP Node crawls the webpage
If Node compares both results are equal if anything is changed. It’ll go to the false branch and notify me in telegram.

Workflow:



Sample Response:




## Template JSON

```
{
  "nodes": [
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        520,
        440
      ],
      "parameters": {
        "url": "https://news.ycombinator.com/",
        "options": {},
        "responseFormat": "string"
      },
      "typeVersion": 1
    },
    {
      "name": "Wait",
      "type": "n8n-nodes-base.wait",
      "position": [
        680,
        440
      ],
      "webhookId": "e5f84b2f-2568-4f5b-a72b-ed54838c768b",
      "parameters": {
        "unit": "minutes",
        "amount": 5
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        880,
        440
      ],
      "parameters": {
        "url": "https://news.ycombinator.com/",
        "options": {},
        "responseFormat": "string"
      },
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        1100,
        440
      ],
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{$node[\"HTTP Request\"].json[\"data\"]}} {{$node[\"HTTP Request\"].json[\"data\"]}}",
              "value2": "="
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        320,
        440
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "mode": "everyX",
              "unit": "minutes",
              "value": 5
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Telegram1",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1320,
        520
      ],
      "parameters": {
        "text": "Something got changed",
        "chatId": "1234",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": {
          "id": "4",
          "name": "n8n test bot"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "NoOp",
      "type": "n8n-nodes-base.noOp",
      "position": [
        1320,
        320
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "NoOp",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Telegram1",
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
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wait": {
      "main": [
        [
          {
            "node": "HTTP Request1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Wait",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request1": {
      "main": [
        [
          {
            "node": "IF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
