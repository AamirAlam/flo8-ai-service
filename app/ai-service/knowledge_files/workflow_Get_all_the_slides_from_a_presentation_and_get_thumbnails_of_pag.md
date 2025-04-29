# Get all the slides from a presentation and get thumbnails of pages

**[View Template](https://n8n.io/workflows/1035-/)**  **Published Date:** 04/13/2021  **Created By:** ghagrawal17  **Categories:** `Marketing`  

## Template Description

This workflow allows you to get all the slides from a presentation and get thumbnails of pages.



Google Slides node: This Google Slides node will get all the slides from a presentation.

Google Slides1 node: This node will return thumbnails of the pages that were returned by the previous node.

Based on your use case, to upload the thumbnails to Dropbox, Google Drive, etc, you can use the respective nodes.

## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        270,
        280
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Google Slides",
      "type": "n8n-nodes-base.googleSlides",
      "position": [
        470,
        280
      ],
      "parameters": {
        "operation": "getSlides",
        "returnAll": true,
        "authentication": "oAuth2",
        "presentationId": "11myCBTn3IT-Iww01WMz43L7HUmQdL6cCR6NCtpsZer0"
      },
      "credentials": {
        "googleSlidesOAuth2Api": "Google Slides Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Google Slides1",
      "type": "n8n-nodes-base.googleSlides",
      "position": [
        670,
        280
      ],
      "parameters": {
        "download": true,
        "resource": "page",
        "operation": "getThumbnail",
        "pageObjectId": "={{$json[\"objectId\"]}}",
        "authentication": "oAuth2",
        "presentationId": "={{$node[\"Google Slides\"].parameter[\"presentationId\"]}}"
      },
      "credentials": {
        "googleSlidesOAuth2Api": "Google Slides Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Google Slides": {
      "main": [
        [
          {
            "node": "Google Slides1",
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
            "node": "Google Slides",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
