# Analyze feedback and send a message on Mattermost

**[View Template](https://n8n.io/workflows/786-/)**  **Published Date:** 11/20/2020  **Created By:** ghagrawal17  **Categories:** `Communication` `Analytics`  

## Template Description

This workflow analyzes the sentiments of the feedback provided by users and sends them to a Mattermost channel.



Typeform Trigger node: Whenever a user submits a response to the Typeform, the Typeform Trigger node will trigger the workflow. The node returns the response that the user has submitted in the form.

Google Cloud Natural Language node: This node analyses the sentiment of the response the user has provided and gives a score.

IF node: The IF node uses the score provided by the Google Cloud Natural Language node and checks if the score is negative (smaller than 0). If the score is negative we get the result as True, otherwise False.

Mattermost node: If the score is negative, the IF node returns true and the true branch of the IF node is executed. We connect the Mattermost node with the true branch of the IF node. Whenever the score of the sentiment analysis is negative, the node gets executed and a message is posted on a channel in Mattermost.

NoOp: This node here is optional, as the absence of this node won't make a difference to the functioning of the workflow.

This workflow can be used by Product Managers to analyze the feedback of the product. The workflow can also be used by HR to analyze employee feedback. You can even use this node for sentiment analysis of Tweets.

To perform a sentiment analysis of Tweets, replace the Typeform Trigger node with the Twitter node.

Note:* You will need a Trigger node or Start node to start the workflow.

Instead of posting a message on Mattermost, you can save the results in a database or a Google Sheet, or Airtable. Replace the Mattermost node with (or add after the Mattermost node) the node of your choice to add the result to your database. 

You can learn to build this workflow on the documentation page of the Google Cloud Natural Language node.

## Template JSON

```
{
  "id": "133",
  "name": "Analyze the sentiment of feedback and send a message on Mattermost",
  "nodes": [
    {
      "name": "Typeform Trigger",
      "type": "n8n-nodes-base.typeformTrigger",
      "position": [
        510,
        260
      ],
      "webhookId": "ad8a87ef-d293-4e48-8d36-838d69ebce0f",
      "parameters": {
        "formId": ""
      },
      "credentials": {
        "typeformApi": "typeform"
      },
      "typeVersion": 1
    },
    {
      "name": "Google Cloud Natural Language",
      "type": "n8n-nodes-base.googleCloudNaturalLanguage",
      "position": [
        710,
        260
      ],
      "parameters": {
        "content": "={{$node[\"Typeform Trigger\"].json[\"What did you think about the event?\"]}}",
        "options": {}
      },
      "credentials": {
        "googleCloudNaturalLanguageOAuth2Api": "cloud"
      },
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        910,
        260
      ],
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$node[\"Google Cloud Natural Language\"].json[\"documentSentiment\"][\"score\"]}}"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Mattermost",
      "type": "n8n-nodes-base.mattermost",
      "position": [
        1110,
        160
      ],
      "parameters": {
        "message": "=You got a new feedback with a score of {{$node[\"Google Cloud Natural Language\"].json[\"documentSentiment\"][\"score\"]}}. Here is what it says:{{$node[\"Typeform Trigger\"].json[\"What did you think about the event?\"]}}",
        "channelId": "4h1bz64cyifwxnzojkzh8hxh4a",
        "attachments": [],
        "otherOptions": {}
      },
      "credentials": {
        "mattermostApi": "mattermost"
      },
      "typeVersion": 1
    },
    {
      "name": "NoOp",
      "type": "n8n-nodes-base.noOp",
      "position": [
        1110,
        360
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "IF": {
      "main": [
        [
          {
            "node": "Mattermost",
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
