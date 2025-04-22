# Create a document in outline for each new GitLab release

**[View Template](https://n8n.io/workflows/1375-/)**  **Published Date:** 12/22/2021  **Created By:** Manu  **Categories:** `Development` `Core Nodes`  

## Template Description

Create a document in Outline for each new GitLab release.

Depends on this PR being merged.

Copy workflow
Set credentials for GitLab and Outline
Inside HTTP Request node, set the following:
   collectionId
   parentDocumentId (or remove if unwanted)

Example result


## Template JSON

```
{
  "nodes": [
    {
      "name": "Gitlab Trigger",
      "type": "n8n-nodes-base.gitlabTrigger",
      "position": [
        240,
        140
      ],
      "parameters": {
        "owner": "tennox",
        "events": [
          "tag_push"
        ],
        "repository": "ci-test"
      },
      "typeVersion": 1
    },
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        820,
        40
      ],
      "parameters": {
        "url": "https://app.getoutline.com/api/documents.create",
        "options": {},
        "requestMethod": "POST",
        "authentication": "headerAuth",
        "jsonParameters": true,
        "bodyParametersJson": "={ \n\"collectionId\": \"PLACEHOLDER\",\n\"parentDocumentId\": \"PLACEHOLDER\",\n\"publish\": true, \n\"title\": {{JSON.stringify(\"Release \" + $json.body.name)}},\n\"text\": {{JSON.stringify($json.body.description + '\\n\\n\\\\\\n[More info](' + $json.body.url + ')')}}\n}"
      },
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        540,
        140
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json.body.object_kind}}",
              "value2": "release"
            }
          ]
        }
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Gitlab Trigger": {
      "main": [
        [
          {
            "node": "IF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
