# Capture Website Screenshots via Google Sheets to Google Drive with CustomJS

**[View Template](https://n8n.io/workflows/3332-/)**  **Published Date:** 03/26/2025  **Created By:** CustomJS  **Categories:** `Data & Storage`  

## Template Description


n8n Workflow: Automating Website Screenshots from Google Sheets

This n8n workflow captures screenshots of websites listed in a Google Sheet and saves them to Google Drive using the CustomJS PDF Toolkit.

@custom-js/n8n-nodes-pdf-toolkit

Features

Monitors** a Google Sheet for new rows with website URLs.
Captures** screenshots of the websites using the CustomJS PDF Toolkit.
Uploads** the screenshots to a specified Google Drive folder.

Notice 
Community nodes can only be installed on self-hosted instances of n8n.

Requirements

Self-hosted** n8n instance
A Google Sheets document containing website URLs and Titles.
A Google Drive folder to store the screenshots.
A CustomJS API key for website screenshots.
n8n credentials** for Google Sheets and Google Drive.

Workflow Steps

Google Sheets Trigger

   Monitors a specified sheet for new rows.
   Extracts the URL and Title from the row.

Website Screenshot Node

   Uses CustomJS PDF Toolkit to take a screenshot of the given URL.

Google Drive Upload
   Saves the screenshot to a specific Google Drive folder.
   Uses the Title column as the filename.

Setup Guide

1. Connect Google Sheets

Ensure your Google Sheet has a column named Url for website URLs and Name for website names.
Set up Google Sheets credentials in n8n.

2. Configure CustomJS API

Sign up at CustomJS.
Retrieve your API key from the profile page.

Add your API key as n8n credentials.

3. Set Up Google Drive

Create a folder in Google Drive to store screenshots.
Copy the folder ID and set it in the Google Drive node in n8n.

Perfect for:

Website monitoring**
Generating visual archives of web pages**
Automating content curation**

This workflow streamlines the process of capturing and organizing website screenshots efficiently.


## Template JSON

```
{
  "meta": {
    "instanceId": "b503899dfd9ae32bbf8e1f446a1f2c9b3c59f80c79b274c49b1606b7ae9579e1"
  },
  "nodes": [
    {
      "id": "21da7bb6-6544-4756-9d0a-ab8ae21650d4",
      "name": "Google Sheets Trigger",
      "type": "n8n-nodes-base.googleSheetsTrigger",
      "position": [
        -120,
        -20
      ],
      "parameters": {
        "event": "rowAdded",
        "options": {},
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        },
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1SP8Y-qffC96ZV3ueVUYWP5pjqtaycaM7Kbv5L-ztw5g/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1SP8Y-qffC96ZV3ueVUYWP5pjqtaycaM7Kbv5L-ztw5g",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1SP8Y-qffC96ZV3ueVUYWP5pjqtaycaM7Kbv5L-ztw5g/edit?usp=drivesdk",
          "cachedResultName": "URL list"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "39a9a0a3-13c7-4271-bca4-31848201e48b",
      "name": "Take a screenshot of a website",
      "type": "@custom-js/n8n-nodes-pdf-toolkit.websiteScreenshot",
      "position": [
        160,
        -20
      ],
      "parameters": {
        "urlInput": "={{ $json.Url }}"
      },
      "typeVersion": 1
    },
    {
      "id": "1dc3cb1a-99ee-4e85-b628-0f4a77149728",
      "name": "Store Screenshots",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        400,
        -20
      ],
      "parameters": {
        "name": "={{ $json.Title }}.png",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "list",
          "value": "1oFbmzgG2fsRix45r5JtowYjAdwskJ0P6",
          "cachedResultUrl": "https://drive.google.com/drive/folders/1oFbmzgG2fsRix45r5JtowYjAdwskJ0P6",
          "cachedResultName": "screenshots"
        }
      },
      "typeVersion": 3
    }
  ],
  "pinData": {},
  "connections": {
    "Google Sheets Trigger": {
      "main": [
        [
          {
            "node": "Take a screenshot of a website",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Take a screenshot of a website": {
      "main": [
        [
          {
            "node": "Store Screenshots",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
