# Sync data between Google Drive and AWS S3

**[View Template](https://n8n.io/workflows/1396-/)**  **Published Date:** 01/11/2022  **Created By:** Lorena  **Categories:** `Data & Storage` `Development`  

## Template Description

This workflow synchronizes files one-way from Google Drive to AWS S3.



Google Drive Trigger node** triggers the workflow when a new file is added to the drive.
AWS S3 node** gets all files stored in an S3 bucket.
Merge node** merges the files from Google Drive and AWS S3 by key (file name) and keeps only the new file.
AWS S3 node** uploads the new file in the S3 bucket.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Google Drive Trigger",
      "type": "n8n-nodes-base.googleDriveTrigger",
      "position": [
        480,
        1480
      ],
      "parameters": {
        "event": "fileUpdated",
        "options": {},
        "triggerOn": "specificFolder",
        "folderToWatch": "https://drive.google.com/drive/folders/[your_id]"
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "12",
          "name": "Google Drive account"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Merge",
      "type": "n8n-nodes-base.merge",
      "position": [
        680,
        1560
      ],
      "parameters": {
        "mode": "removeKeyMatches",
        "propertyName1": "name.value",
        "propertyName2": "Key.value"
      },
      "typeVersion": 1
    },
    {
      "name": "AWS S3  - get",
      "type": "n8n-nodes-base.awsS3",
      "position": [
        480,
        1660
      ],
      "parameters": {
        "options": {},
        "operation": "getAll",
        "bucketName": "mybucket"
      },
      "credentials": {
        "aws": {
          "id": "9",
          "name": "aws"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "AWS S3 - upload",
      "type": "n8n-nodes-base.awsS3",
      "position": [
        860,
        1560
      ],
      "parameters": {
        "tagsUi": {
          "tagsValues": [
            {
              "key": "source",
              "value": "gdrive"
            }
          ]
        },
        "fileName": "={{$json[\"name\"]}}",
        "operation": "upload",
        "binaryData": false,
        "bucketName": "mybucket",
        "additionalFields": {
          "serverSideEncryption": "AES256"
        }
      },
      "credentials": {
        "aws": {
          "id": "9",
          "name": "aws"
        }
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Merge": {
      "main": [
        [
          {
            "node": "AWS S3 - upload",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AWS S3  - get": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Google Drive Trigger": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
