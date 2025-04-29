# Notify a team channel about new software releases via Slack and GitHub

**[View Template](https://n8n.io/workflows/371-/)**  **Published Date:** 05/18/2020  **Created By:** q  **Categories:** `Communication` `HITL`  

## Template Description

This workflow automatically notifies the team in a Slack channel when code in a GitHub repository gets a new release.

Prerequisites

A GitHub account and credentials
A Slack account and credentials

Nodes

GitHub Trigger node triggers the workflow when a release event takes place in the specified repository.
Slack node posts a message in a specified channel with the text "New release is available in {repository name}", along with further details and a link to the release.

## Template JSON

```
{
  "id": "5ec2322573f7590007802e1f",
  "name": "Extranet Releases",
  "nodes": [
    {
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "position": [
        560,
        550
      ],
      "parameters": {
        "text": "=New release is available in {{$node[\"Github Trigger\"].json[\"body\"][\"repository\"][\"full_name\"]}} !\n{{$node[\"Github Trigger\"].json[\"body\"][\"release\"][\"tag_name\"]}} Details:\n{{$node[\"Github Trigger\"].json[\"body\"][\"release\"][\"body\"]}}\n\nLink: {{$node[\"Github Trigger\"].json[\"body\"][\"release\"][\"html_url\"]}}",
        "as_user": true,
        "channel": "extranet-md",
        "attachments": [],
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": "Extranet-md"
      },
      "typeVersion": 1
    },
    {
      "name": "Github Trigger",
      "type": "n8n-nodes-base.githubTrigger",
      "position": [
        350,
        550
      ],
      "parameters": {
        "owner": "Mesdocteurs",
        "events": [
          "release"
        ],
        "repository": "mda-admin-partner-api"
      },
      "credentials": {
        "githubApi": "Github API"
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "Github Trigger": {
      "main": [
        [
          {
            "node": "Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
