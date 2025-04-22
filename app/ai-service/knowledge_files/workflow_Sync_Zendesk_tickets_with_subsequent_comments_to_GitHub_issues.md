# Sync Zendesk tickets with subsequent comments to GitHub issues

**[View Template](https://n8n.io/workflows/1832-/)**  **Published Date:** 12/02/2022  **Created By:** n8n Team  **Categories:** `Development` `Communication`  

## Template Description

This workflow creates a GitHub issue when a new ticket is created in Zendesk. Subsequent comments on the ticket in Zendesk are added as comments to the issue in GitHub.

Prerequisites

Zendesk account and Zendesk credentials.
GitHub account and GitHub credentials.
GitHub repository to create issues in.

How it works

The workflow listens for new tickets in Zendesk.
When a new ticket is created, the workflow creates a new issue in GitHub.
The GitHub issue number is then saved in one of the ticket's fields (in setup we call this "GitHub Issue Number").
The next time a comment is added to the ticket, the workflow retrieves the GitHub issue number from the ticket's field and adds the comment to the issue in GitHub.

Setup

This workflow requires that you set up a webhook in Zendesk. To do so, follow the steps below:

In the workflow, open the On new Zendesk ticket node and copy the webhook URL.
In Zendesk, navigate to Admin Center &gt; Apps and integrations &gt; Webhooks &gt; Actions &gt; Create Webhook.
Add all the required details which can be retrieved from the On new Zendesk ticket node. The webhook URL gets added to the “Endpoint URL” field, and the “Request method” should match what is shown in n8n.
Save the webhook.
In Zendesk, navigate to Admin Center &gt; Objects and rules &gt; Business rules &gt; Triggers &gt; Add trigger.
Give trigger a name such as “New tickets”.
Under “Conditions” in “Meet ALL of the following conditions”, add “Status is New”.
Under “Actions”, select “Notify active webhook” and select the webhook you created previously.
In the JSON body, add the following:
    
        {
    	"id": "{{ticket.id}}",
    	"comment": "{{ticket.latest_comment_html}}"
    }
        
Save the Zendesk trigger.

You will also need to set up a field in Zendesk to store the GitHub issue number. To do so, follow the steps below:

In Zendesk, navigate to Admin Center &gt; Objects and rules &gt; Tickets &gt; Fields &gt; Add field.
Use the number field option and give the field a name such as “GitHub Issue Number”.
Save the field.
In n8n, open the Update ticket node and select the field you created in Zendesk.

## Template JSON

```
{
  "meta": {
    "instanceId": "237600ca44303ce91fa31ee72babcdc8493f55ee2c0e8aa2b78b3b4ce6f70bd9"
  },
  "nodes": [
    {
      "id": "f0913aa6-4e78-4808-b828-7e9953e71764",
      "name": "Get ticket",
      "type": "n8n-nodes-base.zendesk",
      "position": [
        380,
        480
      ],
      "parameters": {
        "id": "={{$node[\"On new Zendesk ticket\"].json[\"body\"][\"id\"]}}",
        "operation": "get"
      },
      "credentials": {
        "zendeskApi": {
          "id": "24",
          "name": "[UPDATE ME]"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "f8774217-bc05-4b02-8632-154654f79d5f",
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        780,
        480
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Determine\"].json[\"GitHub Issue Number\"]}}",
              "operation": "isNotEmpty"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "6ae7e40b-b75c-41e2-9ba7-bb299f12911a",
      "name": "Update ticket",
      "type": "n8n-nodes-base.zendesk",
      "notes": "Update the Zendesk ticket by adding the Jira issue key to the \"Jira Issue Key\" field.",
      "position": [
        1180,
        580
      ],
      "parameters": {
        "id": "={{$node[\"On new Zendesk ticket\"].json[\"body\"][\"id\"]}}",
        "operation": "update",
        "updateFields": {
          "customFieldsUi": {
            "customFieldsValues": [
              {
                "id": 6721726848029,
                "value": "={{$node[\"Create issue\"].json[\"number\"]}}"
              }
            ]
          }
        }
      },
      "credentials": {
        "zendeskApi": {
          "id": "24",
          "name": "[UPDATE ME]"
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "7959986c-cfbf-4ba2-a968-95b62d2aa819",
      "name": "Determine",
      "type": "n8n-nodes-base.function",
      "notes": "if issue was created already in Jira",
      "position": [
        580,
        480
      ],
      "parameters": {
        "functionCode": "/* configure here =========================================================== */\n/*  Zendesk field ID which represents the \"GitHub Issue Number\" field.\n*/\nconst ISSUE_KEY_FIELD_ID = 6721726848029;\n\n/* ========================================================================== */\nnew_items = [];\n\nfor (item of $items(\"Get ticket\")) {\n    \n    // instantiate a new variable for status\n    var custom_fields = item.json[\"custom_fields\"];\n    var github_issue_number = \"\";\n    for (var i = 0; i < custom_fields.length; i++) {\n        if (custom_fields[i].id == ISSUE_KEY_FIELD_ID) {\n            github_issue_number = custom_fields[i].value;\n            break;\n        }\n    }\n\n    // push the new item to the new_items array\n    new_items.push({\n        \"GitHub Issue Number\": github_issue_number\n    });\n}\n\nreturn new_items;"
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "a1ca21d3-958f-498c-a896-05d4ecbc286d",
      "name": "Create issue",
      "type": "n8n-nodes-base.github",
      "position": [
        980,
        580
      ],
      "parameters": {
        "owner": "John-n8n",
        "title": "={{$node[\"Get ticket\"].json[\"subject\"]}}",
        "labels": [],
        "assignees": [],
        "repository": "DemoRepo"
      },
      "credentials": {
        "githubApi": {
          "id": "20",
          "name": "[UPDATE ME]"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "1ad6f536-2cdb-4ecc-85b4-2e960fb84498",
      "name": "Create comment on existing issue",
      "type": "n8n-nodes-base.github",
      "position": [
        980,
        380
      ],
      "parameters": {
        "body": "={{$node[\"On new Zendesk ticket\"].json[\"body\"][\"comment\"]}}",
        "owner": "John-n8n",
        "operation": "createComment",
        "repository": "DemoRepo",
        "issueNumber": "={{$node[\"Determine\"].json[\"GitHub Issue Number\"]}}"
      },
      "credentials": {
        "githubApi": {
          "id": "20",
          "name": "[UPDATE ME]"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "73e8c380-63de-4e5a-8e57-a17956174869",
      "name": "On new Zendesk ticket",
      "type": "n8n-nodes-base.webhook",
      "position": [
        180,
        480
      ],
      "webhookId": "b4253880-b5e2-4d61-bb2a-b0ea335bee14",
      "parameters": {
        "path": "b4253880-b5e2-4d61-bb2a-b0ea335bee14",
        "options": {},
        "httpMethod": "POST"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "Create comment on existing issue",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Create issue",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Determine": {
      "main": [
        [
          {
            "node": "IF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get ticket": {
      "main": [
        [
          {
            "node": "Determine",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create issue": {
      "main": [
        [
          {
            "node": "Update ticket",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On new Zendesk ticket": {
      "main": [
        [
          {
            "node": "Get ticket",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
