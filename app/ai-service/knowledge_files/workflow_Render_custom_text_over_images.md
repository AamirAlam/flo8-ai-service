# Render custom text over images

**[View Template](https://n8n.io/workflows/365-/)**  **Published Date:** 05/12/2020  **Created By:** tanaypant  **Categories:** `Development` `Core Nodes` `Communication` `Marketing`  

## Template Description

This workflow gets triggered every Friday at 6 PM with the help of a Cron node. It pulls in data about a random cocktail via the HTTP Request Node and sends the data to a Bannerbear node to create an image based on a template. The image is then finally shared on a specified Rocket.Chat channel.

## Template JSON

```
{
  "id": "46",
  "name": "Cocktail Recipe Sharing",
  "nodes": [
    {
      "name": "Bannerbear",
      "type": "n8n-nodes-base.bannerbear",
      "position": [
        650,
        300
      ],
      "parameters": {
        "templateId": "",
        "modificationsUi": {
          "modificationsValues": [
            {
              "name": "cocktail-image",
              "imageUrl": "={{$node[\"HTTP Request\"].json[\"drinks\"][0][\"strDrinkThumb\"]}}"
            },
            {
              "name": "title",
              "text": "={{$node[\"HTTP Request\"].json[\"drinks\"][0][\"strDrink\"]}}"
            },
            {
              "name": "recipe",
              "text": "={{$node[\"HTTP Request\"].json[\"drinks\"][0][\"strInstructions\"]}}"
            }
          ]
        },
        "additionalFields": {
          "waitForImage": true
        }
      },
      "credentials": {
        "bannerbearApi": "Bannerbear"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        450,
        300
      ],
      "parameters": {
        "url": "https://www.thecocktaildb.com/api/json/v1/1/random.php",
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        250,
        300
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 18,
              "mode": "everyWeek",
              "weekday": "5"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Rocketchat",
      "type": "n8n-nodes-base.rocketchat",
      "position": [
        850,
        300
      ],
      "parameters": {
        "channel": "",
        "options": {},
        "attachments": [
          {
            "imageUrl": "={{$node[\"Bannerbear\"].json[\"image_url\"]}}"
          }
        ]
      },
      "credentials": {
        "rocketchatApi": "Rocket"
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
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Bannerbear": {
      "main": [
        [
          {
            "node": "Rocketchat",
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
            "node": "Bannerbear",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
