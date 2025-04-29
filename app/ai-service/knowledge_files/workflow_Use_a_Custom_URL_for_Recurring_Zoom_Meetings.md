# Use a Custom URL for Recurring Zoom Meetings

**[View Template](https://n8n.io/workflows/2543-/)**  **Published Date:** 11/13/2024  **Created By:** Eric  **Categories:** `Communication` `HITL` `Marketing`  

## Template Description

Use case

Instead of this:
https://us06web.zoom.us/j/83456429326?pwd=1hVesbyHCsOfstyVU3z4CR6D46A8K.1

share this:
mydomain.com/meet-me

Do you ever wish you had one, simple URL that you can share with people to hop on a Zoom meeting? 😃

You could waste time: 👎👎

creating a recurring Zoom meeting 😫
saving the link somewhere 😵‍💫
finding it, copying it each time you need it 😭
sharing an ugly long link with everyone 🤢

Or...

You could create a 🌹 beautiful link using your own domain/website that redirects to your Zoom meeting, and share that beautified URL with everyone. 😌 And it will be easy for you to remember 💡

&gt; NOTE
Zoom now forces a one-year max lifetime on recurring videos. 😐 So I created this simple workflow to solve a few headaches. ☺️

What this workflow does

Triggers once, annually (360 days)
Creates a new, recurring meeting in Zoom
Updates a redirect script with the new Zoom URL on a Wordpress Page
Notifies you in a Slack channel

What this workflow lacks in breakthrough innovation, it makes up for with usefulness and peace of mind.

Have fun and make it your own!

Setup
Add your credentials in each node
	this pre-requires you have a Zoom, Wordpress and Slack account, and have gotten API access on those accounts
Create a Page in Wordpress, and get its ID.
(Or create a new Page in WP.)
Configure node parameters according to your needs.
TEST!!!! Don't ever skip this step. Ever.
Set it and forget it.

&gt; NOTE
You can replace the Wordpress node with another website CMS node, or generic HTTP request for a non-wordpress site.
You can also remove or replace the Slack node with other notification functionality (eg. sms, whatsapp, email...)

Template was created in n8n v1.58.2


## Template JSON

```
{
  "nodes": [
    {
      "name": "Zoom",
      "type": "n8n-nodes-base.zoom",
      "position": [
        1340,
        580
      ],
      "parameters": {
        "topic": "New Meeting",
        "authentication": "oAuth2",
        "additionalFields": {
          "type": 3,
          "settings": {
            "muteUponEntry": true,
            "joinBeforeHost": true,
            "participantVideo": true
          },
          "timeZone": "America/New_York"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "notes": "Cron trigger to reset zoom meeting on the auto-redirect link",
      "position": [
        1120,
        580
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "daysInterval": 360,
              "triggerAtHour": 3
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "name": "Wordpress",
      "type": "n8n-nodes-base.wordpress",
      "position": [
        1560,
        580
      ],
      "parameters": {
        "pageId": "123 (Create a page in WP, copy the ID of the page, paste it here)",
        "resource": "page",
        "operation": "update",
        "updateFields": {
          "content": "=\n<meta http-equiv=\"refresh\" content=\"0;{{ $json.join_url }}\">\n<p>Redirecting, please wait a moment. Meeting will begin shortly&#8230;</p>"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "position": [
        1780,
        580
      ],
      "parameters": {
        "text": "=Zoom recurring meeting updated!\n{{ $('Zoom').item.json.join_url }}",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "list",
          "value": "abc123",
          "cachedResultName": "my-slack-channel"
        },
        "otherOptions": {
          "includeLinkToWorkflow": true
        }
      },
      "typeVersion": 2.2
    }
  ],
  "pinData": {},
  "connections": {
    "Zoom": {
      "main": [
        [
          {
            "node": "Wordpress",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wordpress": {
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
    "Schedule Trigger": {
      "main": [
        [
          {
            "node": "Zoom",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
