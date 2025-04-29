# Monitor Strava and send email updates

**[View Template](https://n8n.io/workflows/876-/)**  **Published Date:** 01/06/2021  **Created By:** jason  **Categories:** `Communication` `Core Nodes` `HITL` `Productivity`  

## Template Description

Allow your friends to get updates when you do not meet your workout goals so that they can help you get to where you need to be!

Monitors your Strava account and sends an email to three accountability partners each day if you have not had enough activity so that they can reach out to you with some encouragement.



Make sure that you configure the Accountability Settings to meet your needs along with the Strava and Send Email credentials.

## Template JSON

```
{
  "id": "14",
  "name": "Activity Encouragement",
  "nodes": [
    {
      "name": "Strava",
      "type": "n8n-nodes-base.strava",
      "position": [
        640,
        300
      ],
      "parameters": {
        "operation": "getAll",
        "returnAll": true
      },
      "credentials": {
        "stravaOAuth2Api": "Strava OAuth2 Creds"
      },
      "typeVersion": 1
    },
    {
      "name": "Accountability Settings",
      "type": "n8n-nodes-base.set",
      "position": [
        450,
        300
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "moveTime",
              "value": 1800
            }
          ],
          "string": [
            {
              "name": "actPartner1",
              "value": "john.doe@example.com"
            },
            {
              "name": "actPartner2",
              "value": "jane.doe@example.com"
            },
            {
              "name": "actPartner3",
              "value": "jill.doe@example.com"
            },
            {
              "name": "yourName",
              "value": "Jim"
            },
            {
              "name": "yourEmail",
              "value": "jim.doe@example.com"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "Check Activity Level",
      "type": "n8n-nodes-base.if",
      "position": [
        840,
        300
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$node[\"Strava\"].json[\"moving_time\"]}}",
              "value2": "={{$node[\"Accountability Settings\"].parameter[\"values\"][\"number\"][0][\"value\"]}}",
              "operation": "largerEqual"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Enough Activity",
      "type": "n8n-nodes-base.noOp",
      "position": [
        1050,
        220
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Send Email",
      "type": "n8n-nodes-base.emailSend",
      "position": [
        1050,
        390
      ],
      "parameters": {
        "text": "=Hey Accountability Team,\n\nLooks like {{$node[\"Accountability Settings\"].json[\"yourName\"]}} has been spending a bit too much time inactive! How about sending them a quick word of encouragement?\n\nThanks!\n{{$node[\"Accountability Settings\"].json[\"yourName\"]}}'s Heart",
        "options": {},
        "toEmail": "={{$node[\"Accountability Settings\"].parameter[\"values\"][\"string\"][0][\"value\"]}}; {{$node[\"Accountability Settings\"].parameter[\"values\"][\"string\"][1][\"value\"]}}; {{$node[\"Accountability Settings\"].parameter[\"values\"][\"string\"][2][\"value\"]}}",
        "fromEmail": "={{$node[\"Accountability Settings\"].json[\"yourEmail\"]}}"
      },
      "credentials": {
        "smtp": "Email Creds"
      },
      "typeVersion": 1
    },
    {
      "name": "Check Daily at 11:AM",
      "type": "n8n-nodes-base.cron",
      "position": [
        260,
        300
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 11
            }
          ]
        }
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Strava": {
      "main": [
        [
          {
            "node": "Check Activity Level",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check Activity Level": {
      "main": [
        [
          {
            "node": "Enough Activity",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Send Email",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check Daily at 11:AM": {
      "main": [
        [
          {
            "node": "Accountability Settings",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Accountability Settings": {
      "main": [
        [
          {
            "node": "Strava",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
