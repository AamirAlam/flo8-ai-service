# Add positive feedback messages to a table in Notion

**[View Template](https://n8n.io/workflows/1109-/)**  **Published Date:** 06/03/2021  **Created By:** ghagrawal17  **Categories:** `Communication` `HITL` `Productivity` `Analytics`  

## Template Description

This workflow allows you to add positive feedback messages to a table in Notion.

Prerequisites
Create a Typeform that contains Long Text filed question type to accepts feedback from users.
Get your Typeform credentials by following the steps mentioned in the documentation.
Follow the steps mentioned in the documentation to create credentials for Google Cloud Natural Language.
Create a page on Notion similar to this page.
Create credentials for the Notion node by following the steps in the documentation.
Follow the steps mentioned in the documentation to create credentials for Slack.
Follow the steps mentioned in the documentation to create credentials for Trello.




Typeform Trigger node: Whenever a user submits a response to the Typeform, the Typeform Trigger node will trigger the workflow. The node returns the response that the user has submitted in the form.

Google Cloud Natural Language node: This node analyses the sentiment of the response the user has provided and gives a score.

IF node: The IF node uses the score provided by the Google Cloud Natural Language node and checks if the score is positive (larger than 0). If the score is positive we get the result as True, otherwise False.

Notion node: This node gets connected to the true branch of the IF node. It adds the positive feedback shared by the user in a table in Notion.

Slack node: This node will share the positive feedback along with the score and username to a channel in Slack.

Trello node: If the score is negative, the Trello node is executed. This node will create a card on Trello with the feedback from the user.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Typeform Trigger",
      "type": "n8n-nodes-base.typeformTrigger",
      "position": [
        0,
        400
      ],
      "webhookId": "ad8a87ef-d293-4e48-8d36-838d69ebce0f",
      "parameters": {
        "formId": "fBYjtY5e"
      },
      "credentials": {
        "typeformApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Google Cloud Natural Language",
      "type": "n8n-nodes-base.googleCloudNaturalLanguage",
      "position": [
        200,
        400
      ],
      "parameters": {
        "content": "={{$json[\"Any suggestions for us? \"]}}",
        "options": {}
      },
      "credentials": {
        "googleCloudNaturalLanguageOAuth2Api": ""
      },
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        400,
        400
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$node[\"Google Cloud Natural Language\"].json[\"documentSentiment\"][\"score\"]}}",
              "operation": "larger"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Notion",
      "type": "n8n-nodes-base.notion",
      "position": [
        600,
        300
      ],
      "parameters": {
        "resource": "databasePage",
        "databaseId": "b7d1130a-3756-4bb3-aa56-0c77bf416437",
        "propertiesUi": {
          "propertyValues": [
            {
              "key": "Name|title",
              "title": "={{$node[\"Typeform Trigger\"].json[\"Name\"]}}"
            },
            {
              "key": "Feedback|rich_text",
              "textContent": "={{$node[\"Typeform Trigger\"].json[\"Any suggestions for us? \"]}}"
            }
          ]
        }
      },
      "credentials": {
        "notionApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "position": [
        800,
        300
      ],
      "parameters": {
        "channel": "general",
        "blocksUi": {
          "blocksValues": []
        },
        "attachments": [
          {
            "text": "={{$node[\"Typeform Trigger\"].json[\"Any suggestions for us? \"]}}",
            "title": "={{$node[\"Typeform Trigger\"].json[\"Name\"]}} {{$node[\"Google Cloud Natural Language\"].json[\"documentSentiment\"][\"score\"]}}"
          }
        ],
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Trello",
      "type": "n8n-nodes-base.trello",
      "position": [
        600,
        500
      ],
      "parameters": {
        "name": "=Score: {{$json[\"documentSentiment\"][\"score\"]}}",
        "listId": "5fbb9e2eb1d5cc0a8a7ab8ac",
        "description": "=Score: {{$json[\"documentSentiment\"][\"score\"]}}\nFeedback: {{$node[\"Typeform Trigger\"].json[\"Any suggestions for us? \"]}}\nUser: {{$node[\"Typeform Trigger\"].json[\"Name\"]}}",
        "additionalFields": {}
      },
      "credentials": {
        "trelloApi": ""
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "Notion",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Trello",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Notion": {
      "main": [
        [
          {
            "node": "Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Typeform Trigger": {
      "main": [
        [
          {
            "node": "Google Cloud Natural Language",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Cloud Natural Language": {
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
