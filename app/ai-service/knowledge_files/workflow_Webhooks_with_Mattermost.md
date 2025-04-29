# Webhooks with Mattermost

**[View Template](https://n8n.io/workflows/351-/)**  **Published Date:** 04/25/2020  **Created By:** tanaypant  **Categories:** `Development` `Core Nodes` `Communication`  

## Template Description

Does pretty much what this workflow does but is triggered by a slash command using a Webhook node.



## Template JSON

```
{
  "id": "13",
  "name": "Mattermost Webhook",
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        340,
        200
      ],
      "parameters": {
        "path": "webhook",
        "options": {},
        "httpMethod": "POST"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        570,
        200
      ],
      "parameters": {
        "url": "https://www.thecocktaildb.com/api/json/v1/1/random.php",
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "Mattermost",
      "type": "n8n-nodes-base.mattermost",
      "position": [
        770,
        200
      ],
      "parameters": {
        "message": "=Why not try {{$node[\"HTTP Request\"].json[\"drinks\"][0][\"strDrink\"]}}?\n{{$node[\"HTTP Request\"].json[\"drinks\"][0][\"strInstructions\"]}} Serve in {{$node[\"HTTP Request\"].json[\"drinks\"][0][\"strGlass\"]}}.",
        "channelId": "={{$node[\"Webhook\"].json[\"body\"][\"channel_id\"]}}",
        "attachments": [
          {
            "image_url": "={{$node[\"HTTP Request\"].json[\"drinks\"][0][\"strDrinkThumb\"]}}"
          }
        ],
        "otherOptions": {}
      },
      "credentials": {
        "mattermostApi": "Mattermost"
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "Webhook": {
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
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Mattermost",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
