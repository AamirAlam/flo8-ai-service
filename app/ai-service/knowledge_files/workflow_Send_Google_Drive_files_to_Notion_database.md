# Send Google Drive files to Notion database

**[View Template](https://n8n.io/workflows/1819-/)**  **Published Date:** 11/01/2022  **Created By:** n8n Team  **Categories:** `Productivity`  

## Template Description

This workflow sends a file to a Notion database of your choosing when a new file is created in a specific Google Drive folder.

Prerequisites

Notion account and Notion credentials.
Google account and Google credentials.
Google Drive folder to monitor for new files.

How it works

When a Google Drive file is created in the folder you specified, the workflow sends the file to the Notion database you created. The workflow uses the On file upload node to trigger the workflow when a new file is created in the folder. The Create database page node creates a new page in the Notion database you created.

Setup

Create a Notion database called "My Google Drive Files" with the following columns:
    Filename
    Google Drive File
Share the database to n8n.
In the n8n workflow, click on the Create database page node and select the database you created in step 1.
In Google Drive, create a folder and navigate to it.
Copy the URL of the Google Drive folder you are currently in.
In the n8n workflow, add the folder URL to On file upload node.

## Template JSON

```
{
  "meta": {
    "instanceId": "237600ca44303ce91fa31ee72babcdc8493f55ee2c0e8aa2b78b3b4ce6f70bd9"
  },
  "nodes": [
    {
      "id": "fa143713-0a54-465b-bfeb-cfb180871ab4",
      "name": "On file upload",
      "type": "n8n-nodes-base.googleDriveTrigger",
      "position": [
        240,
        480
      ],
      "parameters": {
        "event": "fileCreated",
        "options": {},
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        },
        "triggerOn": "specificFolder",
        "folderToWatch": "1_vYi00lSdzU2p6wGrnW_IqsOblOL-3zG"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "16",
          "name": "[UPDATE ME]"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "78fe0319-e8bf-4c37-8d49-2cd1d6d084e6",
      "name": "Create database page",
      "type": "n8n-nodes-base.notion",
      "position": [
        440,
        480
      ],
      "parameters": {
        "title": "={{$node[\"On file upload\"].json[\"name\"]}}",
        "resource": "databasePage",
        "databaseId": "d637c796-d33b-4768-b955-55c66a0966b7",
        "propertiesUi": {
          "propertyValues": [
            {
              "key": "File|files",
              "fileUrls": {
                "fileUrl": [
                  {
                    "url": "={{ $json[\"webViewLink\"] }}",
                    "name": "={{ $node[\"On file upload\"].json[\"name\"] }}"
                  }
                ]
              }
            }
          ]
        }
      },
      "credentials": {
        "notionApi": {
          "id": "9",
          "name": "[UPDATE ME]"
        }
      },
      "typeVersion": 2
    }
  ],
  "connections": {
    "On file upload": {
      "main": [
        [
          {
            "node": "Create database page",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
