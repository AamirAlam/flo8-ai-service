# Auto-Notify on New Major n8n Releases via RSS, Email & Telegram

**[View Template](https://n8n.io/workflows/736-/)**  **Published Date:** 10/26/2020  **Created By:** Miquel Colomer  **Categories:** `Communication` `HITL` `Development`  

## Template Description



This n8n workflow template checks for new major releases (tagged with .0) of the n8n project using its official GitHub releases feed. It runs multiple times a day and sends notifications via email and Telegram if a new release is found.

&gt; ⚠️ Note: You must *activate the workflow* to start receiving release notifications.

🚀 What It Does

Monitors the n8n GitHub releases feed
Detects major versions (e.g., 1.0.0, 2.0.0)
Sends alert messages via Telegram and email (SES) when a release is published

⏰ Scheduling Details

The Cron node checks for new releases three times per day:  
  10:00, 14:00, and 18:00 server time.

🛠️ Step-by-Step Setup

Configure Telegram Bot  
   Connect your Telegram bot and specify the chat ID where you want to receive notifications.

Set up AWS SES Credentials  
   Use a verified sender email and set up AWS SES credentials in your n8n instance.

Activate the Workflow  
   Enable the workflow in your instance to start receiving notifications.

Customize Notification Messages (Optional)  
   You can modify the email subject, Telegram format, or filter logic.

🧠 How It Works: Workflow Overview

Cron Trigger  
   Runs the workflow at 10:00, 14:00, and 18:00 daily.

Read RSS Feed  
   Pulls data from https://github.com/n8n-io/n8n/releases.atom.

Filter by Current Day  
   Filters the feed to match:
   Releases published in the last 4 hours
   Titles starting with n8n@ and ending with .0

Condition Check  
   Uses a regex to check if the filter result contains any release data.

Notifications  
   If a new major release is found, sends:
     Telegram message to a specified chat
     Email via AWS SES with release info

📨 Final Output

You'll receive a Telegram message and email when a new major n8n version is released.

🔐 Credentials Used

Telegram API** – For sending chat notifications
AWS SES** – To send email alerts

✨ Customization Tips

Change Notification Channels**: Add Slack, Discord, or other preferred channels.
Adjust Cron Schedule**: Modify the Cron node to fit your check frequency.
Modify Filters**: Detect patch or beta versions by changing the .0 condition.
Send Release Notes**: Extend the feed parsing to include release content.

❓Questions?

Template created by Miquel Colomer and n8nhackers.com.  

Need help customizing or deploying? Contact us for consulting and support.




## Template JSON

```
{
  "id": "33",
  "name": "n8n_check",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -520,
        250
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "RSS Feed Read",
      "type": "n8n-nodes-base.rssFeedRead",
      "position": [
        -320,
        260
      ],
      "parameters": {
        "url": "https://github.com/n8n-io/n8n/releases.atom"
      },
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        70,
        260
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Filter by current day\"].json[\"data\"]}}",
              "value2": "/.+/",
              "operation": "regex"
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
        -520,
        421
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "mode": "custom",
              "cronExpression": "0 0 10,14,18 * * *"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Filter by current day",
      "type": "n8n-nodes-base.function",
      "position": [
        -120,
        260
      ],
      "parameters": {
        "functionCode": "var d = new Date();\nvar year = d.getFullYear();\nvar month = d.getMonth() + 1;\nvar day = d.getDate();\nvar hour = d.getHours() - 4;//Publication in last 4 hours\n\nmonth = month < 10 ? \"0\" + month : month;\nday = day < 10 ? \"0\" + day : day;\nhour = hour < 10 ? \"0\" + hour : hour;\n\nvar lines = items.filter(function(item) {\n  //var str = year + \"-\" + month + \"-\" + day + \"T\" + hour;\n  var str = year + \"-\" + month + \"-\" + day + \"T\" + hour;\n  //return true;//item.json.pubDate.indexOf(str) !== -1 && item.json.title.indexOf(\"n8n@\") !== -1;\n  return item.json.pubDate.indexOf(str) !== -1 && item.json.title.indexOf(\"n8n@\") !== -1 && item.json.title.indexOf(\".0\") !== -1;\n}).map(function(item) {\n  return item.json.title;\n}).join(\"\\n\");\n\n\nreturn [\n  {\n  json: {\n    date: year + \"-\" + month + \"-\" + day + \" \" + hour,\n    data: lines && lines.length ? \"New release on n8n:\\n\" + lines : \"\"\n   }\n  }\n]"
      },
      "typeVersion": 1
    },
    {
      "name": "Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        300,
        280
      ],
      "parameters": {
        "text": "={{$node[\"Filter by current day\"].json[\"data\"]}}",
        "chatId": "-1001235337538",
        "additionalFields": {
          "parse_mode": "HTML"
        }
      },
      "credentials": {
        "telegramApi": "it-killia-bot"
      },
      "typeVersion": 1
    },
    {
      "name": "AWS SES",
      "type": "n8n-nodes-base.awsSes",
      "position": [
        300,
        110
      ],
      "parameters": {
        "body": "={{$node[\"Filter by current day\"].json[\"data\"]}}",
        "subject": "New n8n version",
        "fromEmail": "myemail@mydomain.com",
        "isBodyHtml": true,
        "toAddresses": [
          "myemail@mydomain.com"
        ],
        "additionalFields": {}
      },
      "credentials": {
        "aws": "ses"
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "Telegram",
            "type": "main",
            "index": 0
          },
          {
            "node": "AWS SES",
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
            "node": "RSS Feed Read",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "RSS Feed Read": {
      "main": [
        [
          {
            "node": "Filter by current day",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter by current day": {
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
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "RSS Feed Read",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
