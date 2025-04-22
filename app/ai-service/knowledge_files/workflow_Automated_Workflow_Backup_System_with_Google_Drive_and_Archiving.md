# Automated Workflow Backup System with Google Drive and Archiving

**[View Template](https://n8n.io/workflows/3559-/)**  **Published Date:** 04/15/2025  **Created By:** Niten Musa  **Categories:** `Data & Storage`  

## Template Description


If you have any question, or difficulty, feel free to come discuss about it on my Telegram (you might find something there 🎁)



This workflow provides a fully automated system for backing up your n8n workflows to Google Drive. It runs on a schedule (which you can customize) and saves each workflow as a .json file, named after the workflow itself. All active workflows are backed up by default and stored in a specified Google Drive folder of your choice.

A special feature of this workflow is its ability to archive and clean up old workflows. If you tag a workflow with ARCHIVE (case-sensitive), the workflow will be backed up into a designated Archive subfolder inside your main Google Drive folder — and then automatically deleted from your n8n instance. This keeps your workspace clean and reduces clutter while ensuring everything is safely stored.

Requirements

A Google Drive account connected to n8n (via OAuth2 or preferred method)
An n8n instance with access to your workflows
A folder in Google Drive for storing backups
  Inside this folder, create a subfolder named Archive
Folder IDs for both the main and archive folders* (Find it in folder's URL e.g. https://drive.google.com/drive/u/0/folders/1F7Exr2xkZQFvmHmjdFD43K0jfd*)

Setup

In your Google Drive, create a main folder for storing backups.
Inside it, create a subfolder called Archive.
Retrieve the folder IDs for both folders
In n8n, connect your Google Drive credentials.
Open the workflow and insert the folder IDs in the appropriate nodes.
Optionally, edit the schedule trigger to set your preferred backup frequency.

Usage

Once configured, the workflow will:
Run automatically on the defined schedule
Back up all existing workflows into your Drive
For workflows tagged with ARCHIVE:
  Save them into the Archive subfolder
  Delete them from your n8n instance

The workflow ensures your automation logic is safely versioned, with optional cleanup for outdated or unused flows.

Customization

You can modify the schedule to run daily, weekly, or at any custom interval using the built-in Cron node.

You can also change the folder structure or naming conventions in the Google Drive nodes to match your personal or team preferences.

Workflows are archived only if they are explicitly tagged with ARCHIVE — this tag is case-sensitive.

## Template JSON

```
{
  "meta": {
    "instanceId": "82646634f490cb8ae2f5cc5a0c85aabc71a170fd92ff0cf9f1844efe09613228"
  },
  "name": "Automated Workflow Backup System with Google Drive and Archiving",
  "tags": [],
  "nodes": [
    {
      "id": "137736a9-1806-49a0-916f-5f9d42374af6",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -40,
        840
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "weeks",
              "triggerAtDay": [
                5
              ],
              "triggerAtHour": 18
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "be319541-c52e-49c6-87c8-fefbf4e7fd3e",
      "name": "If",
      "type": "n8n-nodes-base.if",
      "position": [
        1060,
        840
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "793ada07-2a98-4399-8780-c931fec040b7",
              "operator": {
                "type": "array",
                "operation": "notEmpty",
                "singleValue": true
              },
              "leftValue": "={{ $json.tags.filter(tags => tags.name === 'ARCHIVE') }}",
              "rightValue": ""
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "91bb5679-ba91-482e-a20a-f8323b395259",
      "name": "Sticky Note9",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -140,
        680
      ],
      "parameters": {
        "color": 5,
        "width": 320,
        "height": 440,
        "content": "## SET HERE\n### The schedule for update\n\n# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\u2b07\ufe0f"
      },
      "typeVersion": 1
    },
    {
      "id": "f3d17ceb-8ade-4803-892c-b614e292a9af",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        580,
        680
      ],
      "parameters": {
        "width": 380,
        "height": 440,
        "content": "## IF NEEDED\n### You can filter with tags, or exclude inactives\n\n# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\u2b07\ufe0f"
      },
      "typeVersion": 1
    },
    {
      "id": "9dd1aa23-fbee-42a9-a5e8-93309db351ee",
      "name": "Create to date folder",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        340,
        840
      ],
      "parameters": {
        "name": "=Save {{ $now.format('MM-dd-yyyy') }}",
        "driveId": {
          "__rl": true,
          "mode": "id",
          "value": "="
        },
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "id",
          "value": "="
        },
        "resource": "folder"
      },
      "typeVersion": 3
    },
    {
      "id": "5778496b-fbbd-4949-8bec-118346eee19a",
      "name": "GET Workflows",
      "type": "n8n-nodes-base.n8n",
      "position": [
        720,
        840
      ],
      "parameters": {
        "filters": {},
        "requestOptions": {}
      },
      "typeVersion": 1
    },
    {
      "id": "0b512c8b-6601-42f3-a787-fbbcbdce5089",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        980,
        420
      ],
      "parameters": {
        "width": 1160,
        "height": 700,
        "content": "&nbsp;\n## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This will sort Workflows tagged 'ARCHIVE' to save them separatly \n## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; and then delete them from your n8n instance\n\n\n\n\n\n\n\n\n\n\n### And also save all other workflows in your drive \n### in the dated folder"
      },
      "typeVersion": 1
    },
    {
      "id": "651ac297-2bc1-4966-9ed9-a4995537ac29",
      "name": "Convert to JSON",
      "type": "n8n-nodes-base.convertToFile",
      "position": [
        1280,
        960
      ],
      "parameters": {
        "mode": "each",
        "options": {
          "fileName": "={{ $json.name }}"
        },
        "operation": "toJson"
      },
      "typeVersion": 1.1
    },
    {
      "id": "fc69f86d-eeac-43cc-901a-3fd7d14ba726",
      "name": "Convert to JSON'",
      "type": "n8n-nodes-base.convertToFile",
      "position": [
        1280,
        720
      ],
      "parameters": {
        "mode": "each",
        "options": {
          "fileName": "={{ $json.name }}"
        },
        "operation": "toJson"
      },
      "typeVersion": 1.1
    },
    {
      "id": "f23e6e7f-60be-4436-815b-3ba03146e414",
      "name": "Save 'ARCHIVE' Workflows",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        1600,
        720
      ],
      "parameters": {
        "name": "=",
        "driveId": {
          "__rl": true,
          "mode": "id",
          "value": "="
        },
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "id",
          "value": "="
        }
      },
      "typeVersion": 3
    },
    {
      "id": "fcab95c4-a0e0-4c9f-b754-14ae2a81c532",
      "name": "Save all other Workflows",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        1600,
        960
      ],
      "parameters": {
        "driveId": {
          "__rl": true,
          "mode": "id",
          "value": "="
        },
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $('Create to date folder').item.json.id }}"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "fca8442a-7ef5-47a1-b217-3c2cf571caf0",
      "name": "Delete 'ARCHIVE' Workflows",
      "type": "n8n-nodes-base.n8n",
      "position": [
        1920,
        720
      ],
      "parameters": {
        "operation": "delete",
        "workflowId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $('If').item.json.id }}"
        },
        "requestOptions": {}
      },
      "typeVersion": 1
    },
    {
      "id": "8a32345b-bc4e-48da-b215-9a2beac8a06d",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        0
      ],
      "parameters": {
        "color": 6,
        "width": 2040,
        "height": 380,
        "content": "&nbsp;\n&nbsp;\n&nbsp;\n&nbsp;\n# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Hey bro, if you see any mistake, misspell, or any unclear thing [\u27a1\ufe0f Telegram \u2b05\ufe0f](https://t.me/+ZeFskaPyp_Q2N2Vk)\n## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ==> *feel free to come talk about it in my Telegram group, I try my best to answer fast everyday*\n## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `I want my explanation to be the clearest possible for everyone`\n\n\n## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Your loyal servant\n# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Niten"
      },
      "typeVersion": 1
    },
    {
      "id": "afd14921-ce70-44e0-9798-b8d94851eb2e",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -160,
        400
      ],
      "parameters": {
        "color": 7,
        "width": 2320,
        "height": 740,
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "21adbbea-b46a-4046-a959-82395f13cbe9",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -120,
        440
      ],
      "parameters": {
        "color": 3,
        "width": 1060,
        "height": 220,
        "content": "# &nbsp;&nbsp;&nbsp;&nbsp; Workflow : Automated n8n BackUp\n## Schedule an automated backup for all your workflows\n### Clear your n8n instance from outdated workflows that you still want to keep by applying them the tag 'ARCHIVE'"
      },
      "typeVersion": 1
    },
    {
      "id": "8c59561d-3d4c-47ca-93ba-c4e6a8b4991c",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1480,
        560
      ],
      "parameters": {
        "color": 5,
        "width": 340,
        "height": 360,
        "content": "## SET HERE\n### Create an 'Archive' folder in the parent backup folder and set the id here\n# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\u2b07\ufe0f\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n### You could also replace Google Drive with any drive"
      },
      "typeVersion": 1
    },
    {
      "id": "920d81cb-87ef-499d-b9ea-00f2fb92a8ab",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        200,
        680
      ],
      "parameters": {
        "color": 5,
        "width": 360,
        "height": 440,
        "content": "## SET HERE\n### The folder ID from your Google Drive\n\n# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\u2b07\ufe0f\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n### You could also replace Google Drive with any drive"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "If": {
      "main": [
        [
          {
            "node": "Convert to JSON'",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Convert to JSON",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "GET Workflows": {
      "main": [
        [
          {
            "node": "If",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Convert to JSON": {
      "main": [
        [
          {
            "node": "Save all other Workflows",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Convert to JSON'": {
      "main": [
        [
          {
            "node": "Save 'ARCHIVE' Workflows",
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
            "node": "Create to date folder",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create to date folder": {
      "main": [
        [
          {
            "node": "GET Workflows",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Save 'ARCHIVE' Workflows": {
      "main": [
        [
          {
            "node": "Delete 'ARCHIVE' Workflows",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
