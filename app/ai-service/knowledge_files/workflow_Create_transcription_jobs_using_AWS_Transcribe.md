# Create transcription jobs using AWS Transcribe

**[View Template](https://n8n.io/workflows/1111-/)**  **Published Date:** 06/03/2021  **Created By:** ghagrawal17  **Categories:** `Data & Storage` `Development`  

## Template Description

This workflow allows you to create transcription jobs for all your audio and video files stored in AWS S3.



AWS S3: This node will retrieve all the files from an S3 bucket you specify.

AWS Transcribe: This node will create a transcription job for the files that get returned by the previous node.

## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        190,
        160
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "AWS Transcribe",
      "type": "n8n-nodes-base.awsTranscribe",
      "position": [
        590,
        160
      ],
      "parameters": {
        "options": {},
        "mediaFileUri": "=s3://{{$node[\"AWS S3\"].parameter[\"bucketName\"]}}/{{$json[\"Key\"]}}",
        "detectLanguage": true,
        "transcriptionJobName": "={{$json[\"Key\"].replace(/\\s/g,'-')}}"
      },
      "credentials": {
        "aws": "AWS Transcribe Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "AWS S3",
      "type": "n8n-nodes-base.awsS3",
      "position": [
        390,
        160
      ],
      "parameters": {
        "options": {},
        "operation": "getAll",
        "returnAll": true,
        "bucketName": "n8n-docs"
      },
      "credentials": {
        "aws": "AWS S3 Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "AWS S3": {
      "main": [
        [
          {
            "node": "AWS Transcribe",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "AWS S3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
