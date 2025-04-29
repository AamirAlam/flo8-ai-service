# Sync Squarespace Newsletter Signups to Mailchimp via Google Sheets

**[View Template](https://n8n.io/workflows/3251-/)**  **Published Date:** 03/21/2025  **Created By:** bangank36  **Categories:** `Data & Storage` `Productivity` `Communication` `Marketing`  

## Template Description

This workflow captures Squarespace newsletter signups in a Google Sheet and automatically creates new Mailchimp contacts in the selected audience.  

It overcomes the limitation in Squarespace’s native Mailchimp integration, which only supports new, empty audiences.  

You can trigger the workflow manually or schedule it for continuous synchronization.  

Step-by-step tutorial
First, you need to connect Squarespace newsletter block submission to Google Drive
In Mailchimp node, choose your targeted audience in List Name or ID
Connect a Squarespace Form to Google Drive  
To connect a form to Google Drive:  

In the form's storage options, click Connect on Google Drive.  
Log into your Google account.  
Click Allow to permit Squarespace to connect to Google Drive.  
Enter a Spreadsheet Name. This creates a new spreadsheet for your form submissions.  

Columns in my sheet:  
Submitted On  
Email Address  
Name  

This structure is inspired by Squarespace’s newsletter block connection, but you can modify it based on your preferred data format.  

👉 Clone my Google Sheets template  

Requirements  

Credentials  

To use this workflow, you need:  

Mailchimp API Key** – Required to add contacts to Mailchimp.  
Google Sheets API credentials** – Required to retrieve signups from the spreadsheet.  

📌 Mailchimp API Authentication Guide  

Explore More Templates  

👉 Check out my other n8n templates


## Template JSON

```
{
  "meta": {
    "instanceId": "e634e668fe1fc93a75c4f2a7fc0dad807ca318b79654157eadb9578496acbc76",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "a5f5621a-bd4c-45b8-be09-ebdda13ebb3e",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -280,
        120
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "9447f0d4-1be3-4b8c-b172-3ff856f2197b",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -280,
        -160
      ],
      "parameters": {
        "rule": {
          "interval": [
            {}
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "4ffd30f6-6f56-42cd-9f1c-07b58adbe312",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -740,
        -260
      ],
      "parameters": {
        "color": 4,
        "width": 371.1995072042308,
        "height": 600.88409546716,
        "content": "## Create Mailchimp contact based on Squarespace newsletter\nThis workflow will get Squarespace newsletter signups and create new Mailchimp contact in the given Audience on Mailchimp\n\nThis overcome the limitation between Squarespace forms and Mailchimp connection where only new, empty audience can be used\n\nYou can run the workflow on demand or by schedule\n\n## Spreadsheet template\n\nThe sheet columns are inspire from Squarespace newsletter block connection, but you can change the node to adapt new columns format\n\nClone the [sample sheet here](https://docs.google.com/spreadsheets/d/1wi2Ucb4b35e0-fuf-96sMnyzTft0ADz3MwdE_cG_WnQ/edit?usp=sharing)\n- Submitted On\t\n- Email Address\t\n- Name"
      },
      "typeVersion": 1
    },
    {
      "id": "7af3d027-ffb8-4ca0-84d4-06dbf3902e80",
      "name": "Squarespace newsletter submissions",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        0,
        0
      ],
      "parameters": {
        "options": {},
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/15A3ZWzIBfONL4U_1XGJvtsS8HtMQ69qrpxd5C5L6Akg/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "15A3ZWzIBfONL4U_1XGJvtsS8HtMQ69qrpxd5C5L6Akg",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/15A3ZWzIBfONL4U_1XGJvtsS8HtMQ69qrpxd5C5L6Akg/edit?usp=drivesdk",
          "cachedResultName": "n8n-submission"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "JgI9maibw5DnBXRP",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "f0fe2c40-2971-4068-b5b0-57e70f65ff72",
      "name": "Loop Over each item",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        260,
        0
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 3
    },
    {
      "id": "ebad2d00-56b3-4dec-9e3b-d9cb6cc4aaf1",
      "name": "Add new member to Mailchimp",
      "type": "n8n-nodes-base.mailchimp",
      "onError": "continueErrorOutput",
      "position": [
        540,
        20
      ],
      "parameters": {
        "email": "={{ $json['Email Address'] }}{{ $json.row_number }}",
        "status": "subscribed",
        "options": {
          "timestampSignup": "={{ $json['Submitted On'] }}"
        },
        "mergeFieldsUi": {
          "mergeFieldsValues": [
            {
              "name": "FNAME",
              "value": "={{ $json.Name }}"
            }
          ]
        }
      },
      "credentials": {
        "mailchimpApi": {
          "id": "E6kRZLAOwvNxFpNz",
          "name": "Mailchimp account"
        }
      },
      "typeVersion": 1,
      "alwaysOutputData": false
    }
  ],
  "pinData": {},
  "connections": {
    "Schedule Trigger": {
      "main": [
        [
          {
            "node": "Squarespace newsletter submissions",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Loop Over each item": {
      "main": [
        [],
        [
          {
            "node": "Add new member to Mailchimp",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Add new member to Mailchimp": {
      "main": [
        [
          {
            "node": "Loop Over each item",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    },
    "When clicking \u2018Test workflow\u2019": {
      "main": [
        [
          {
            "node": "Squarespace newsletter submissions",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Squarespace newsletter submissions": {
      "main": [
        [
          {
            "node": "Loop Over each item",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
