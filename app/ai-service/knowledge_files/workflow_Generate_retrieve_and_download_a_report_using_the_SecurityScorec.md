# Generate, retrieve and download a report using the SecurityScorecard

**[View Template](https://n8n.io/workflows/920-/)**  **Published Date:** 02/04/2021  **Created By:** ghagrawal17  **Categories:** `Analytics`  

## Template Description

This workflow allows you to generate, retrieve and download a report using the SecurityScorecard node.



SecurityScorecard node: This node generates a full scorecard report. Based on your use-case, you can generate other type of report.

SecurityScorecard1 node: This node fetches the latest report from SecurirtScoredcard. Toggle Return All to true to return all the reports.

SecurityScorecard2 node: This node downloads the report that got fetched from the previous node. 

Based on your use-case, you can either store this report in Dropbox, Google Drive etc. or email it using the Gmail node, Send Email node or the Microsoft Outlook node.

You can replace the Strat node with the Cron node to trigger the workflow on a regurlar interval.


## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "SecurityScorecard",
      "type": "n8n-nodes-base.securityScorecard",
      "position": [
        450,
        300
      ],
      "parameters": {
        "report": "full-scorecard-json",
        "resource": "report",
        "operation": "generate",
        "scorecardIdentifier": "n8n.io"
      },
      "credentials": {
        "securityScorecardApi": "SecurityScorecard Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "SecurityScorecard1",
      "type": "n8n-nodes-base.securityScorecard",
      "position": [
        650,
        300
      ],
      "parameters": {
        "limit": 1,
        "resource": "report"
      },
      "credentials": {
        "securityScorecardApi": "SecurityScorecard Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "SecurityScorecard2",
      "type": "n8n-nodes-base.securityScorecard",
      "position": [
        850,
        300
      ],
      "parameters": {
        "url": "={{$json[\"download_url\"]}}",
        "resource": "report",
        "operation": "download"
      },
      "credentials": {
        "securityScorecardApi": "SecurityScorecard Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "SecurityScorecard": {
      "main": [
        [
          {
            "node": "SecurityScorecard1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "SecurityScorecard1": {
      "main": [
        [
          {
            "node": "SecurityScorecard2",
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
            "node": "SecurityScorecard",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
