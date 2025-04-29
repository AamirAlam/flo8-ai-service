# Bulk Automated Google Drive Files Sharing and Direct Download Link Generation

**[View Template](https://n8n.io/workflows/2042-/)**  **Published Date:** 01/08/2024  **Created By:** Nskha  **Categories:** `Data & Storage` `Development` `Core Nodes`  

## Template Description

This N8N workflow automates the process of sharing files from Google Drive. It includes OAuth2 authentication, batch processing, public link generation, and access status modification for efficient file handling. Suitable for users seeking to streamline their Google Drive file sharing process. sutiable for bulk actions, tested on 4.2K files folder working like charm.

How It Works

Initialize Workflow: The process begins with a Manual Trigger, allowing the user to start the workflow at their convenience.
Folder ID Specification: A 'Set Folder ID' node where the user can enter the desired Google Drive Folder ID.
List Files from Google Drive: The 'Google Drive' node lists all files within the specified folder using OAuth2 authentication.
Batch Processing: The 'Loop Over Items' node processes the files in batches for efficiency.
Generate Public Links: The 'Generate Download Links' node creates downloadable links for each file.
Change File Access: The 'Change Status' node alters the file status to make them publicly accessible.
Merge and Output: A 'Merge' node consolidates the data, preparing it for further actions or output.

Set Up Steps

Estimated Time**: The setup should take approximately 10-15 minutes.
Initial Setup**: You'll need to provide OAuth2 credentials for Google Drive and specify a folder ID.
Customization**: Adjust the batch size and file access permissions according to your needs.
Detailed Descriptions**: For specific configuration details, refer to the sticky notes within the workflow.

Example Item output
{
"link": "https://drive.google.com/u/3/uc?id=1hojqPfXchNTY8YRTNkxSo-8txK9re-V4&export=download&confirm=t&authuser=0",
"name": "firefox_rNjA0ybKu7.png",
"kind": "drive#permission",
"id": "anyoneWithLink",
"type": "anyone",
"role": "reader",
"allowFileDiscovery": false
}
You can store the output data with any data store node you want, for example save them into Excel Sheet or Airtable etc...
Keywords: n8n workflow, Google Drive integration, file sharing automation, batch file processing, public link generation, OAuth2 authentication, workflow automation


## Template JSON

```
{
  "meta": {
    "instanceId": "c59a6b1daf09a846754bc2cf0a94db3299bd5a69fb14687c3a5e692704c548dd"
  },
  "nodes": [
    {
      "id": "2165cd37-10ff-46bd-88a5-c8377bf4bef7",
      "name": "Google Drive",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        1280,
        1100
      ],
      "parameters": {
        "limit": 100,
        "options": {
          "spaces": [
            "*"
          ],
          "corpora": "allDrives"
        },
        "operation": "list",
        "queryString": "='{{ $json[\"Folder ID\"] }}' in parents",
        "authentication": "oAuth2",
        "useQueryString": true
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "KJE0ZORR1Q1fJCd5",
          "name": "Google Drive account 2"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "5061db5e-2137-4c50-8902-a24cd53a6bdf",
      "name": "Loop Over Items",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        1480,
        1160
      ],
      "parameters": {
        "options": {},
        "batchSize": 50
      },
      "typeVersion": 3
    },
    {
      "id": "62a16fb8-9bfc-46db-a556-23fac7f403f5",
      "name": "Merge",
      "type": "n8n-nodes-base.merge",
      "position": [
        1720,
        1020
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combinationMode": "multiplex"
      },
      "typeVersion": 2.1
    },
    {
      "id": "bd410148-e745-43a2-960b-128bbb49828f",
      "name": "Set Folder ID",
      "type": "n8n-nodes-base.set",
      "notes": "Enter desired Folder",
      "position": [
        1120,
        1100
      ],
      "parameters": {
        "fields": {
          "values": [
            {
              "name": "Folder ID",
              "stringValue": "Enter Your Folder ID here"
            }
          ]
        },
        "options": {}
      },
      "notesInFlow": true,
      "typeVersion": 3.2
    },
    {
      "id": "16def9df-5c8b-4359-a879-11e66f191f92",
      "name": "Manual Execute Workflow",
      "type": "n8n-nodes-base.manualTrigger",
      "notes": "Optional",
      "position": [
        940,
        1100
      ],
      "parameters": {},
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "e7d54620-e5e6-470e-add5-ccefdfb2a979",
      "name": "Generate Download Links",
      "type": "n8n-nodes-base.code",
      "position": [
        1480,
        980
      ],
      "parameters": {
        "jsCode": "// This function will create an array of file links from the given Google Drive folder\nreturn items.map(file => {\n  return { json: { 'link': `https://drive.google.com/u/3/uc?id=${file.json.id}&export=download&confirm=t&authuser=0`, 'name': file.json.name } };\n});"
      },
      "typeVersion": 2
    },
    {
      "id": "04e71edf-c40f-4c80-961c-f511e145232c",
      "name": "Change Status",
      "type": "n8n-nodes-base.googleDrive",
      "notes": "Make Files Public to anyone with a link",
      "position": [
        1660,
        1180
      ],
      "parameters": {
        "fileId": {
          "__rl": true,
          "mode": "id",
          "value": "={{ $json.id }}"
        },
        "options": {
          "supportsAllDrives": true
        },
        "operation": "share",
        "permissionsUi": {
          "permissionsValues": {
            "role": "reader",
            "type": "anyone"
          }
        },
        "authentication": "oAuth2"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "KJE0ZORR1Q1fJCd5",
          "name": "Google Drive account 2"
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "4452cd81-e94a-465e-987b-5acf46e25428",
      "name": "Replace Me",
      "type": "n8n-nodes-base.noOp",
      "position": [
        1880,
        1020
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "dab69e10-d9af-4ece-a6c6-cb35468e3bf0",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        880,
        820
      ],
      "parameters": {
        "width": 1235.0111197082438,
        "height": 545.6382804772701,
        "content": "## Example Output:\n```JSON\n{\n\"link\": \"https://drive.google.com/u/3/uc?id=1hojqPfXchNTY8YRTNkxSo-8txK9re-V4&export=download&confirm=t&authuser=0\",\n\"name\": \"firefox_rNjA0ybKu7.png\",\n\"kind\": \"drive#permission\",\n\"id\": \"anyoneWithLink\",\n\"type\": \"anyone\",\n\"role\": \"reader\",\n\"allowFileDiscovery\": false\n}\n```\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n### You can store the output data with any data store node you want\n### for example save them into Excel Sheet or Airtable etc..."
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Merge": {
      "main": [
        [
          {
            "node": "Replace Me",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Drive": {
      "main": [
        [
          {
            "node": "Loop Over Items",
            "type": "main",
            "index": 0
          },
          {
            "node": "Generate Download Links",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Change Status": {
      "main": [
        [
          {
            "node": "Loop Over Items",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Folder ID": {
      "main": [
        [
          {
            "node": "Google Drive",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Loop Over Items": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 1
          }
        ],
        [
          {
            "node": "Change Status",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate Download Links": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Manual Execute Workflow": {
      "main": [
        [
          {
            "node": "Set Folder ID",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
