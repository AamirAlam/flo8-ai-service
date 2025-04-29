# Get GitHub Issue Updates and Send Notifications to Telegram

**[View Template](https://n8n.io/workflows/3021-/)**  **Published Date:** 02/26/2025  **Created By:** Prakash  **Categories:** `Development` `Communication` `HITL`  

## Template Description

Who is this for?  
This workflow is ideal for:  
Developers** who want to stay updated on issues without constantly checking GitHub.
Managers** tracking issue progress in a Telegram group.   
 DevOps teams that need automated notification alerts for new or updated issues.

What problem does this workflow solve?  
Keeping track of GitHub issues manually can be tedious. Teams often miss critical updates because notifications are buried in emails or dashboards. This workflow automates the process by fetching new or open GitHub issues and instantly sending notifications to a specified Telegram chat.  

What this workflow does  
This workflow connects GitHub and Telegram to provide real-time issue notifications:  
Fetch GitHub Issues – Retrieves new or open issues from a selected GitHub repository.  
Format the Issue Details – Extracts key information like issue title, number, status, and URL.  
Send to Telegram – Posts the formatted issue details to a Telegram group or private chat.  

Setup Guide  

Prerequisites  
Before setting up the workflow, ensure you have:  
GitHub Personal Access Token**: Required to fetch issue details. Generate it under Developer Settings with repo or public_repo permissions.  
Telegram Bot Token**: Create a bot via BotFather on Telegram and obtain the token.  
Telegram Chat ID**: Find the chat ID where the bot should send messages using this method.  

Step-by-Step Setup  

Set Up GitHub Node  
   Authenticate using your GitHub token.  
   Choose the repository you want to track.  
   Configure filters (e.g., fetch only open issues).  

Format Issue Details  
   Extract key details like title, issue number, assignee, and status.  
   Customize the message structure for better readability.  

Send Message to Telegram  
   Add the Telegram node and enter your bot token.  
   Use the Chat ID to define the recipient.  
   Format the message to include issue details and links.  

Schedule the Workflow (Optional)  
   Use the Cron node to run this workflow periodically (e.g., every hour).  

How to Customize This Workflow  
Filter Issues by Labels**: Modify the GitHub node to fetch only issues with specific labels.  
Include Additional Fields**: Add issue comments, priority, or assignee details in the message.  
Send Alerts Based on Priority**: Use conditional logic to send high-priority issues to a different chat.  
Trigger on Issue Events**: Instead of fetching periodically, use GitHub webhooks (if permitted in the repo) to trigger the workflow on issue creation or updates.  

Why Use This Workflow?  
Automates GitHub issue tracking** without manually checking repositories.  
Instant notifications in Telegram** ensure quick response times.  
Fully customizable** to fit different team workflows.  


## Template JSON

```
{
  "id": "okjjim5PVb2dZUgg",
  "meta": {
    "instanceId": "b229c9a129a49cc78e21e7f6e65be625850967828e8c77a8f82738e7c8461afc",
    "templateCredsSetupCompleted": true
  },
  "name": "FetchGithubIssues",
  "tags": [],
  "nodes": [
    {
      "id": "2f3cac64-7326-471d-8f6a-1677a4ff5a6d",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -540,
        -560
      ],
      "parameters": {
        "color": 5,
        "content": "### Get Github Issues HTTP Request \n- Edit the OWNER and REPO NAME in the respective fields\n- The request is configured with query parameters of *state*, *since* and *labels*"
      },
      "typeVersion": 1
    },
    {
      "id": "13809408-63f3-4161-87f2-c5d950274aa9",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -260,
        -560
      ],
      "parameters": {
        "color": 3,
        "width": 180,
        "content": "### Extract Fields\nExtract fields like title, comments, created_at, etc from the github api response"
      },
      "typeVersion": 1
    },
    {
      "id": "3df26230-c2b0-44d5-98da-cccbca493c8f",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -40,
        -560
      ],
      "parameters": {
        "color": 3,
        "width": 180,
        "content": "### Filter on Fields\nFilter issues based on number of comments"
      },
      "typeVersion": 1
    },
    {
      "id": "819bd3f8-8d23-4299-ac1d-ae9762f944dd",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        220,
        -680
      ],
      "parameters": {
        "color": 5,
        "width": 200,
        "height": 280,
        "content": "### Send message to Telegram User\n- This node is configured to send *issue title* and *url* to your user id\n- Create a new telegram bot using the instructions [here](https://core.telegram.org/bots/tutorial#obtain-your-bot-token) and configure bot token in the telegram credential\n- Chat ID can be your username or your username ID"
      },
      "typeVersion": 1
    },
    {
      "id": "9e08036f-e082-424d-b536-349d236a40ec",
      "name": "Send Message to @user",
      "type": "n8n-nodes-base.telegram",
      "position": [
        280,
        -380
      ],
      "webhookId": "d0c6ee9e-ed0b-49fa-95cd-e483fc29ffbc",
      "parameters": {
        "text": "=New Issue:  {{ $json.title }} [Link]({{ $json.html_url }})",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": {
          "id": "MEwozHKykMH3flb4",
          "name": "Telegram account 2"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "9cf3bf31-12a6-4f3b-a1e7-69f575f801f0",
      "name": "Check for comments",
      "type": "n8n-nodes-base.filter",
      "position": [
        0,
        -380
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "88ae0b8f-c586-4f01-8389-bc0e2c0473bc",
              "operator": {
                "type": "number",
                "operation": "lt"
              },
              "leftValue": "={{ $json.comments }}",
              "rightValue": 5
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "0cfd2924-64c0-4f8b-a15b-7e619d5b21bf",
      "name": "Map title, url, created, comments",
      "type": "n8n-nodes-base.set",
      "position": [
        -220,
        -380
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "ebad3986-8804-428f-acbb-7c1953dbbc47",
              "name": "title",
              "type": "string",
              "value": "={{ $json.title }}"
            },
            {
              "id": "2daabd16-f1af-4d24-8409-51e7ba242bbb",
              "name": "html_url",
              "type": "string",
              "value": "={{ $json.html_url }}"
            },
            {
              "id": "7ea20a16-794c-4701-81e0-4b99fb1a9fc7",
              "name": "created_at",
              "type": "string",
              "value": "={{ $json.created_at }}"
            },
            {
              "id": "0a4985f9-5d80-420b-ae57-15329bf19634",
              "name": "comments",
              "type": "number",
              "value": "={{ $json.comments }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "eacbb029-03b9-46d6-9f2e-edaab70cce10",
      "name": "Run every 10 minutes",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -780,
        -380
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "minutes",
              "minutesInterval": 10
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "d87f01e3-8277-4dbb-bcc0-4ca2e1c794d4",
      "name": "Get Github Issues",
      "type": "n8n-nodes-base.github",
      "position": [
        -480,
        -380
      ],
      "parameters": {
        "owner": {
          "__rl": true,
          "mode": "name",
          "value": ""
        },
        "resource": "repository",
        "repository": {
          "__rl": true,
          "mode": "name",
          "value": ""
        },
        "getRepositoryIssuesFilters": {
          "since": "={{ new Date(Date.now() - 30 * 60 * 1000).toISOString() }}",
          "state": "open",
          "labels": "Bug"
        }
      },
      "credentials": {
        "githubApi": {
          "id": "2yRBqav2uahP1pas",
          "name": "GitHub account"
        }
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "5bc6fb0e-face-48c3-aba4-0c53ad1e9b35",
  "connections": {
    "Get Github Issues": {
      "main": [
        [
          {
            "node": "Map title, url, created, comments",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check for comments": {
      "main": [
        [
          {
            "node": "Send Message to @user",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Run every 10 minutes": {
      "main": [
        [
          {
            "node": "Get Github Issues",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Map title, url, created, comments": {
      "main": [
        [
          {
            "node": "Check for comments",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
