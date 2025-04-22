# Trigger a build in Travis CI when code changes are push to a GitHub repo

**[View Template](https://n8n.io/workflows/1132-/)**  **Published Date:** 06/18/2021  **Created By:** ghagrawal17  **Categories:** `Development`  

## Template Description

This workflow allows you to trigger a build in Travis CI when code changes are pushed to a GitHub repo or a pull request gets opened.



GitHub Trigger node: This node will trigger the workflow when changes are pushed or when a pull request is created, updated, or deleted.

IF node: This node checks for the action type. We want to trigger a build when code changes are pushed or when a pull request is opened. We don't want to build the project when a PR is closed or updated.

TravisCI node: This node will trigger the build in Travis CI. If you're using CircleCI in your pipeline, replace the node with the CircleCI node.

NoOp node: Adding this node is optional.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Github Trigger",
      "type": "n8n-nodes-base.githubTrigger",
      "position": [
        450,
        300
      ],
      "webhookId": "01518289-14b1-4a45-9d33-39be08f7a544",
      "parameters": {
        "owner": "n8n-io",
        "events": [
          "push",
          "pull_request"
        ],
        "repository": "n8n",
        "authentication": "oAuth2"
      },
      "credentials": {
        "githubOAuth2Api": "GitHub Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        650,
        300
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"headers\"][\"x-github-event\"]}}",
              "value2": "push"
            },
            {
              "value1": "={{$json[\"body\"][\"action\"]}}",
              "value2": "opened"
            }
          ]
        },
        "combineOperation": "any"
      },
      "typeVersion": 1
    },
    {
      "name": "TravisCI",
      "type": "n8n-nodes-base.travisCi",
      "position": [
        850,
        200
      ],
      "parameters": {
        "slug": "={{$json[\"body\"][\"repository\"][\"full_name\"]}}",
        "branch": "=",
        "operation": "trigger",
        "additionalFields": {}
      },
      "credentials": {
        "travisCiApi": "Travis API"
      },
      "typeVersion": 1
    },
    {
      "name": "NoOp",
      "type": "n8n-nodes-base.noOp",
      "position": [
        850,
        400
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "TravisCI",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "NoOp",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Github Trigger": {
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
