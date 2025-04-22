# Automate Figma Versioning and Jira Updates with n8n Webhook Integration

**[View Template](https://n8n.io/workflows/2991-/)**  **Published Date:** 02/24/2025  **Created By:** omid dev  **Categories:** `Productivity` `Development`  

## Template Description

How It Works:
This n8n template automates the process of tracking design changes in Figma and updating relevant Jira issues. The template is triggered when a new version is created in Figma via a custom plugin. Once the version is committed, the plugin sends the design details to an n8n workflow using a webhook.

The workflow then performs the following actions:
Fetches the Jira issue based on the provided issue link from Figma.
Adds the design changes as a comment to the Jira issue.
Updates the status of the Jira issue based on the provided task status (e.g., "In Progress", "Done").
This streamlines the workflow, reducing the need for manual updates and ensuring that both the design team and developers have the latest design changes and task statuses in sync.

How to Use It:
Set up the Figma Plugin:

Install the Figma Commit Plugin from GitHub.
In the plugin, fill out the version name, design link, Jira issue link, and the task status.
Commit the changes in Figma, which will trigger the webhook.

Set Up the n8n Workflow:
Import this template into your n8n instance.
Connect the Figma Trigger node to capture version updates from Figma.
Configure the Jira nodes to retrieve the issue and update the status/comment based on the data sent from the plugin.

Automate:
Once the version is committed in Figma, the workflow will automatically update the Jira issue and keep both your Figma design and Jira tasks in sync!
By integrating Figma, Jira, and n8n through this template, you’ll eliminate manual steps, making collaboration between design and development teams more efficient.

## Template JSON

```
{
  "id": "5kYHogzDGeo21MxE",
  "meta": {
    "instanceId": "e7bcfb7f83803b3561455f2e97f622835eda64ae4467d4f2b8a5cf915b534600",
    "templateCredsSetupCompleted": true
  },
  "name": "Automate Figma Versioning and Jira Updates with n8n Webhook Integration",
  "tags": [],
  "nodes": [
    {
      "id": "a3853962-36ce-4a2f-b9d6-c2807652d7ff",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -20,
        -260
      ],
      "parameters": {
        "width": 700,
        "height": 200,
        "content": "## Note\nTo use this automation, you will need the Figma Commit Plugin installed and configured. The plugin sends the design version details via a webhook to trigger this n8n workflow.\n\nYou can find the Figma Commit Plugin on GitHub here:\n\ud83d\udd17 [Figma Commit Plugin on GitHub](https://github.com/omid-d3v/Figma-Commit-plugin-with-webhook/)\n\nMake sure to follow the setup instructions in the plugin\u2019s documentation to get started."
      },
      "typeVersion": 1
    },
    {
      "id": "843f1e0b-4c8b-4744-a9b7-8ce5725768bc",
      "name": "Find Jira Issue",
      "type": "n8n-nodes-base.jira",
      "position": [
        220,
        0
      ],
      "parameters": {
        "issueKey": "={{ $json.issueLink }}",
        "operation": "get",
        "additionalFields": {}
      },
      "credentials": {
        "jiraSoftwareCloudApi": {
          "id": "CBgXAIn2agwnaJ1Y",
          "name": "Jira SW Cloud account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "59101813-9625-4d1f-b2b6-7ff442c1fe0f",
      "name": "Add Comment in Issue",
      "type": "n8n-nodes-base.jira",
      "position": [
        440,
        0
      ],
      "parameters": {
        "comment": "={{ $('Figma Trigger').item.json.pageName }}{{ '\\n' }}{{ $('Figma Trigger').item.json.versionName }}{{ '\\n' }}{{ $('Figma Trigger').item.json.designLink }}{{ '\\n' }} {{ $now }}",
        "options": {},
        "issueKey": "={{ $json.key }}",
        "resource": "issueComment"
      },
      "credentials": {
        "jiraSoftwareCloudApi": {
          "id": "CBgXAIn2agwnaJ1Y",
          "name": "Jira SW Cloud account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "378150c5-b640-477a-861f-216e8b15c0e4",
      "name": "Figma Trigger",
      "type": "n8n-nodes-base.figmaTrigger",
      "position": [
        0,
        0
      ],
      "webhookId": "b9fcde90-3e53-4958-b352-933891f95220",
      "parameters": {
        "teamId": "940915773877350235",
        "triggerOn": "fileVersionUpdate"
      },
      "credentials": {
        "figmaApi": {
          "id": "DjRDveAKp5VxZRE8",
          "name": "Figma account"
        }
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "pinData": {
    "Figma Trigger": [
      {
        "json": {
          "status": "IN PROGRESS",
          "pageName": "page: Favorait",
          "issueLink": "JAJ-368",
          "designLink": "test url ",
          "versionName": "Changes: \n -nothing"
        }
      }
    ]
  },
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "9525049e-7fca-4f83-bf6a-069d477f669e",
  "connections": {
    "Figma Trigger": {
      "main": [
        [
          {
            "node": "Find Jira Issue",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Find Jira Issue": {
      "main": [
        [
          {
            "node": "Add Comment in Issue",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Add Comment in Issue": {
      "main": [
        []
      ]
    }
  }
}
```
