# Send new YouTube channel videos to Telegram

**[View Template](https://n8n.io/workflows/1599-/)**  **Published Date:** 04/17/2022  **Created By:** Alessio  **Categories:** `Communication` `HITL` `Marketing`  

## Template Description


A simple node to send new YouTube videos from a channel to a Telegram chat (private, group or channel).
CheckTime: set how often videos should be fetched from YouTube. Default is 30 minutes.
GetVideosYT: this node will fetch the list of videos from a given channel. Here you need to specify on "Limit" the number of videos to fetch, and on "Channel ID" the ID of the desired channel (it should be the ending part of the URL). You need Google OAuth2 credentials to make it work. A guide is available here. (If you use n8n's tunneling, you may need to adjust the OAuth callback URL on Google Cloud Platform)
Set: this node will set some variables to work easily with the next nodes. You shouldn't edit this.
Function: this node checks if the video was seen previously by the workflow, so that it won't be published a second time on Telegram. You shouldn't edit this.
SendVideo: this node sends the message to Telegram. You need to set your bot's credentials (guide here), specify the Chat ID to send the message (how to get) and personalize the Text of your message.

This workflow works correctly only when it's activated. If you manually execute the workflow, it will send every time the latest videos.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        500,
        510
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "id",
              "value": "={{$node[\"GetVideosYT\"].json[\"id\"][\"videoId\"]}}"
            },
            {
              "name": "url",
              "value": "=https://youtu.be/{{$node[\"GetVideosYT\"].json[\"id\"][\"videoId\"]}}"
            },
            {
              "name": "title",
              "value": "={{$node[\"GetVideosYT\"].json[\"snippet\"][\"title\"]}}"
            }
          ],
          "boolean": []
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "Function",
      "type": "n8n-nodes-base.function",
      "position": [
        640,
        510
      ],
      "parameters": {
        "functionCode": "const new_items = [];\nconst data = this.getWorkflowStaticData('node');\n\ndata.ids = data.ids || [];\n\nfor (var i=0; i<items.length; i++) {\n  if (data.ids.includes(items[i].json.id)) {\n    break;\n  } else {\n    new_items.push({json: {id: items[i].json.id, url: items[i].json.url, title: items[i].json.title}});\n  }\n}\n\ndata.ids = items.map(item => item.json.id)\nreturn new_items;\n"
      },
      "typeVersion": 1
    },
    {
      "name": "CheckTime",
      "type": "n8n-nodes-base.interval",
      "position": [
        210,
        510
      ],
      "parameters": {
        "unit": "minutes",
        "interval": 30
      },
      "typeVersion": 1
    },
    {
      "name": "GetVideosYT",
      "type": "n8n-nodes-base.youTube",
      "position": [
        370,
        510
      ],
      "parameters": {
        "limit": 4,
        "filters": {
          "channelId": "UCTe5YtigJdZZ3i-za6IkbGQ"
        },
        "options": {
          "order": "date"
        },
        "resource": "video"
      },
      "credentials": {
        "youTubeOAuth2Api": "tubo"
      },
      "typeVersion": 1
    },
    {
      "name": "SendVideo",
      "type": "n8n-nodes-base.telegram",
      "position": [
        790,
        510
      ],
      "parameters": {
        "text": "=Nuovo video di almi su YouTube!\n<b>{{$node[\"Function\"].json[\"title\"]}}</b>\n\n{{$node[\"Function\"].json[\"url\"]}}",
        "chatId": "-1001178002763",
        "additionalFields": {
          "parse_mode": "HTML"
        }
      },
      "credentials": {
        "telegramApi": "bot raspino"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Set": {
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
            "node": "SendVideo",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "CheckTime": {
      "main": [
        [
          {
            "node": "GetVideosYT",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "GetVideosYT": {
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
