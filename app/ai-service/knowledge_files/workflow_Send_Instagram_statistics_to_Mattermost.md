# Send Instagram statistics to Mattermost

**[View Template](https://n8n.io/workflows/812-/)**  **Published Date:** 12/07/2020  **Created By:** damien  **Categories:** `Data & Storage` `Productivity` `Communication`  

## Template Description


This worflow let us know main stat on our Instagram : this is the first i share with community as i am a beginner :)

Every morning i know how many follower we have, how many posts have been made.

I use a fantastic tool which is : 
https://socialblade.com

and also :
 https://martechwithme.com/monitoring-youtube-channels-subscribers-with-google-sheets/

to send them to Google Sheets

Hope this could help :)
This can be improved for sure, so i will be very pleased to have your comments
thanks


French version : :) *

Ce schéma permet d'avoir les statistiques de notre Instagram : combien de followers et combien de posts ont été réalisés.
Ces données sont publiées sur MAttermost.

J'utilise un outil génial pour récupérer les données de instagram : https://socialblade.com
puis https://martechwithme.com/monitoring-youtube-channels-subscribers-with-google-sheets/
pour les récupérer sur Google Sheets

## Template JSON

```
{
  "id": "3",
  "name": "StatsInstagram",
  "nodes": [
    {
      "name": "Mattermost",
      "type": "n8n-nodes-base.mattermost",
      "position": [
        1030,
        290
      ],
      "parameters": {
        "message": "=Bonjour ! Voici les stats de notre Instagram {{$json[\"Compte\"]}} en ce beau matin du {{$node[\"Date & Time\"].json[\"day_today\"]}} {{$node[\"Date & Time\"].json[\"data\"]}}\nLe nombre de Followers est de : {{$json[\"Followers\"]}}\nNous avons r\u00e9alis\u00e9 : {{$json[\"Posts\"]}} posts, \nBravo !",
        "channelId": "xxxxxxx",
        "attachments": [],
        "otherOptions": {}
      },
      "credentials": {
        "mattermostApi": "API"
      },
      "typeVersion": 1
    },
    {
      "name": "Date & Time",
      "type": "n8n-nodes-base.dateTime",
      "position": [
        640,
        290
      ],
      "parameters": {
        "value": "={{$json[\"date_today\"]}}",
        "custom": true,
        "options": {},
        "toFormat": "DD-MM-YYYY"
      },
      "typeVersion": 1
    },
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        310,
        290
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 8
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Get the date today",
      "type": "n8n-nodes-base.function",
      "position": [
        470,
        290
      ],
      "parameters": {
        "functionCode": "var date = new Date().toISOString();\nvar day = new Date().getDay();\nconst weekday = [\"Dimanche\", \"Lundi\", \"Mardi\", \"Mercredi\", \"Jeudi\", \"Vendredi\", \"Samedi\"];\n\nitems[0].json.date_today = date;\nitems[0].json.day_today = weekday[day];\n\nreturn items;\n"
      },
      "typeVersion": 1
    },
    {
      "name": "Read data on Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        850,
        290
      ],
      "parameters": {
        "range": "cells",
        "options": {},
        "sheetId": "sheetID",
        "authentication": "oAuth2"
      },
      "credentials": {
        "googleSheetsOAuth2Api": "GoogleAPI"
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
            "node": "Get the date today",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Date & Time": {
      "main": [
        [
          {
            "node": "Read data on Google Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get the date today": {
      "main": [
        [
          {
            "node": "Date & Time",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Read data on Google Sheets": {
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
