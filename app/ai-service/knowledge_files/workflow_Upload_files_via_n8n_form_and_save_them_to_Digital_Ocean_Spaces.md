# Upload files via n8n form and save them to Digital Ocean Spaces

**[View Template](https://n8n.io/workflows/2660-/)**  **Published Date:** 12/19/2024  **Created By:** Alfred Nutile  **Categories:** `Data & Storage` `Development`  

## Template Description

How it works
This workflow provides a streamlined process for uploading files to Digital Ocean Spaces, making them publicly accessible. The process happens in three main steps:

User submits the form with file, in this case I needed it to upload images I use in my seo tags.
File is automatically uploaded to Digital Ocean Spaces using S3-compatible storage
Form completion confirmation is provided

Setup steps
Initial setup typically takes 5-10 minutes
Configure your Digital Ocean Spaces credentials and bucket settings
Test the upload functionality with a small sample file
Verify public access permissions are working as expected

Important notes
Credentials are tricky check the screenshot above for how I set the url, bucket etc.
I am just using the S3 Node
Set the ACL as seen below

Troubleshooting
Bucket name might be incorrect
Region Wrong
Check Space permissions if uploads fail
Verify API credentials are correctly configured


You can see a video here. (live in 24 hours)
https://youtu.be/pYOpy3Ntt1o

## Template JSON

```
{
  "id": "CYv2u2izrgZWk5bK",
  "meta": {
    "instanceId": "b77b374d91a001765a8bf2832badc1f8fcc5407c99c4c6f3f68d6413d663ef83",
    "templateCredsSetupCompleted": true
  },
  "name": "DigialOceanUpload",
  "tags": [
    {
      "id": "6YbZxCb4ODJ2Rmva",
      "name": "admin",
      "createdAt": "2024-12-01T14:18:53.184Z",
      "updatedAt": "2024-12-01T14:18:53.184Z"
    }
  ],
  "nodes": [
    {
      "id": "dedd8475-1f90-4c6e-a7b3-d4246648fcec",
      "name": "On form submission",
      "type": "n8n-nodes-base.formTrigger",
      "position": [
        200,
        340
      ],
      "webhookId": "f506f7cd-dded-491a-b56e-fb4e0eade910",
      "parameters": {
        "options": {},
        "formTitle": "Upload File",
        "formFields": {
          "values": [
            {
              "fieldType": "file",
              "fieldLabel": "File to Upload",
              "requiredField": true
            }
          ]
        },
        "formDescription": "Upload the file to the public storage area"
      },
      "typeVersion": 2.2
    },
    {
      "id": "bbaed371-3860-4370-8103-16b7b955cd7e",
      "name": "S3",
      "type": "n8n-nodes-base.s3",
      "position": [
        360,
        340
      ],
      "parameters": {
        "fileName": "={{ $json['File to Upload'][0].filename }}",
        "operation": "upload",
        "bucketName": "dailyai",
        "additionalFields": {
          "acl": "publicRead"
        },
        "binaryPropertyName": "File_to_Upload"
      },
      "credentials": {
        "s3": {
          "id": "FHy0lHKFlTe0nVPv",
          "name": "Digital Ocean Spaces"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "da21e508-a62f-49dd-ac1c-6ed4b9a307a6",
      "name": "Form",
      "type": "n8n-nodes-base.form",
      "position": [
        540,
        340
      ],
      "webhookId": "cea10f93-617e-4762-9c40-582a8d159240",
      "parameters": {
        "options": {},
        "operation": "completion",
        "completionTitle": "Your file path is below!",
        "completionMessage": "=https://dailyai.nyc3.cdn.digitaloceanspaces.com/{{ $('On form submission').first().json['File to Upload'][0].filename }}"
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "pinData": {
    "On form submission": [
      {
        "json": {
          "formMode": "production",
          "submittedAt": "2024-12-19T13:00:27.445-05:00",
          "File to Upload": [
            {
              "size": 986986,
              "filename": "prompt_booster.png",
              "mimetype": "image/png"
            }
          ]
        }
      }
    ]
  },
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "e7f5d777-36c3-4601-8eef-dc1ab68cf67e",
  "connections": {
    "S3": {
      "main": [
        [
          {
            "node": "Form",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On form submission": {
      "main": [
        [
          {
            "node": "S3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
