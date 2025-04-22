# Analyze feedback using AWS Comprehend and send it to a Mattermost channel

**[View Template](https://n8n.io/workflows/965-/)**  **Published Date:** 03/03/2021  **Created By:** ghagrawal17  **Categories:** `Communication` `Development`  

## Template Description

This workflow analyzes the sentiments of the feedback provided by users and sends them to a Mattermost channel.



Typeform Trigger node: Whenever a user submits a response to the Typeform, the Typeform Trigger node will trigger the workflow. The node returns the response that the user has submitted in the form.

AWS Comprehend node: This node analyses the sentiment of the response the user has provided and gives a score.

IF node: The IF node uses the data provided by the AWS Comprehend node and checks if the sentiment is negative. If the sentiment is negative we get the result as true, otherwise false.

Mattermost node: If the score is negative, the IF node returns true and the true branch of the IF node is executed. We connect the Mattermost node with the true branch of the IF node. Whenever the score of the sentiment analysis is negative, the node gets executed and a message is posted on a channel in Mattermost.

NoOp: This node here is optional, as the absence of this node won't make a difference to the functioning of the workflow.

This workflow can be used by Product Managers to analyze the feedback of the product. The workflow can also be used by HR to analyze employee feedback. You can even use this node for sentiment analysis of Tweets.

To perform a sentiment analysis of Tweets, replace the Typeform Trigger node with the Twitter node.

Note: You will need a Trigger node or Start node to start the workflow.

Instead of posting a message on Mattermost, you can save the results in a database or a Google Sheet, or Airtable. Replace the Mattermost node with (or add after the Mattermost node) the node of your choice to add the result to your database. 

## Template JSON

```
{
  "nodes": [
    {
      "name": "Mattermost",
      "type": "n8n-nodes-base.mattermost",
      "position": [
        810,
        300
      ],
      "parameters": {
        "message": "=You got new feedback with a score of {{$json[\"SentimentScore\"][\"Negative\"]}}. Here is what it says:{{$node[\"Typeform Trigger\"].json[\"What did you think about the event?\"]}}",
        "channelId": "h7cxrd1cefr13x689enzyw7xhc",
        "attachments": [],
        "otherOptions": {}
      },
      "credentials": {
        "mattermostApi": "Mattermost Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "NoOp",
      "type": "n8n-nodes-base.noOp",
      "position": [
        800,
        500
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "position": [
        600,
        400
      ],
      "parameters": {
        "conditions": {
          "number": [],
          "string": [
            {
              "value1": "={{$json[\"Sentiment\"]}}",
              "value2": "NEGATIVE"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "AWS Comprehend",
      "type": "n8n-nodes-base.awsComprehend",
      "position": [
        400,
        400
      ],
      "parameters": {
        "text": "={{$json[\"What did you think about the event?\"]}}",
        "operation": "detectSentiment"
      },
      "credentials": {
        "aws": "AWS Comprehend Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Typeform Trigger",
      "type": "n8n-nodes-base.typeformTrigger",
      "position": [
        200,
        400
      ],
      "webhookId": "ad8a87ef-d293-4e48-8d36-838d69ebce0f",
      "parameters": {
        "formId": "DuJHEGW5"
      },
      "credentials": {
        "typeformApi": "typeform"
      },
      "typeVersion": 1
    }
  ],
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
    "AWS Comprehend": {
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
    "Typeform Trigger": {
      "main": [
        [
          {
            "node": "AWS Comprehend",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
