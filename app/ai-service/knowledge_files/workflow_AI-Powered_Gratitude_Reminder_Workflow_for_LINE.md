# AI-Powered Gratitude Reminder Workflow for LINE

**[View Template](https://n8n.io/workflows/3040-/)**  **Published Date:** 02/28/2025  **Created By:** lin@davoy.tech  **Categories:** `Development` `Core Nodes` `AI` `Langchain`  

## Template Description

This workflow template, "Daily Gratitude Reminder Bot for LINE," is designed to help users cultivate a habit of gratitude by sending personalized, AI-generated reminders every evening at 9:00 PM. Using Azure OpenAI , the bot generates varied and engaging messages to prompt users to reflect on the positive aspects of their day. The reminders are then sent directly to users via the LINE messaging platform , ensuring a seamless and impactful experience.

Whether you're a developer, counselor, or business owner, this template offers a customizable and scalable solution for promoting mental wellness and fostering a culture of gratitude.

profile
Qwen2.5-Max
2:56 pm
Here’s a polished and detailed description for your "Daily Gratitude Reminder Bot for LINE" template, following the submission guidelines provided. This description is structured to meet all the requirements, including SEO optimization, clarity, and user convenience.

Daily Gratitude Reminder Bot for LINE
This workflow template, "Daily Gratitude Reminder Bot for LINE," is designed to help users cultivate a habit of gratitude by sending personalized, AI-generated reminders every evening at 9:00 PM. Using Azure OpenAI , the bot generates varied and engaging messages to prompt users to reflect on the positive aspects of their day. The reminders are then sent directly to users via the LINE messaging platform , ensuring a seamless and impactful experience.

Whether you're a developer, counselor, or business owner, this template offers a customizable and scalable solution for promoting mental wellness and fostering a culture of gratitude.

Who Is This Template For?
Developers who want to integrate AI-powered workflows into messaging platforms like LINE.
Counselors & Therapists looking to encourage mindfulness and emotional well-being among their clients.
Businesses & Organizations focused on employee wellness or customer engagement through positive reinforcement.
Educators & Nonprofits seeking tools to promote mental health awareness and self-care practices.

What Problem Does This Workflow Solve?
Gratitude journaling has been proven to improve mental health, reduce stress, and increase overall happiness. However, many people struggle to maintain the habit due to busy schedules or forgetfulness. This workflow solves that problem by automating daily reminders to reflect on positive experiences, making it easier for users to build and sustain a gratitude practice.

What This Workflow Does
Scheduled Trigger:
The workflow is triggered every evening at 9:00 PM using a schedule node.
AI-Powered Message Generation:
An Azure OpenAI Chat Model generates a unique and engaging reminder message with a temperature setting of 0.9 to ensure variety and creativity.
Message Formatting:
The generated message is reformatted to comply with the LINE Push API requirements, ensuring smooth delivery.
Push Notification via LINE:
The formatted message is sent to the user via the LINE Push API , delivering the reminder directly to their chat.

Setup Guide
Pre-Requisites
Access to an Azure OpenAI account with credentials.
A LINE Developers Console account with access to the Push API.
Basic knowledge of n8n workflows and JSON formatting.

How to Customize This Workflow to Your Needs
Change the Time: Adjust the schedule trigger to send reminders at a different time.
Modify the Prompt: Edit the AI model's input prompt to generate messages tailored to your audience (e.g., focus on work achievements or personal growth).
Expand Recipients: Update the LINE Push API node to send reminders to multiple users or groups.
Integrate Additional Features: Add nodes to log user responses or track engagement metrics.
Why Use This Template?
Promotes Mental Wellness: Encourages users to reflect on positive experiences, improving emotional well-being.
Highly Customizable: Easily adapt the workflow to suit different audiences and use cases.
Scalable: Send reminders to one user or thousands, making it suitable for both personal and organizational use.
AI-Powered Creativity: Avoid repetitive messages by leveraging AI to generate fresh and engaging content.

## Template JSON

```
{
  "id": "Sebvr1R2t4zkAg1V",
  "meta": {
    "instanceId": "558d88703fb65b2d0e44613bc35916258b0f0bf983c5d4730c00c424b77ca36a",
    "templateCredsSetupCompleted": true
  },
  "name": "Gratitude Jar Reminder",
  "tags": [],
  "nodes": [
    {
      "id": "ac48becc-e207-489b-a8e4-a8f69780c626",
      "name": "Trigger 2100 Bear Gratitude Jar Notice",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -80,
        -100
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "triggerAtHour": 21
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "37f46ac1-5c0b-4cdf-aa33-67fad80dafdd",
      "name": "WriteReminder",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        180,
        -100
      ],
      "parameters": {
        "text": "=Today is a wonderful day! \ud83c\udf1f What or who brought a smile to your face today? \ud83d\ude0a\n",
        "messages": {
          "messageValues": [
            {
              "message": "You'll rewrite this message to send reminder to user to record good thing today."
            }
          ]
        },
        "promptType": "define"
      },
      "typeVersion": 1.5
    },
    {
      "id": "816f8089-a54f-4860-a658-448ab53a08fd",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -180,
        -240
      ],
      "parameters": {
        "width": 300,
        "height": 360,
        "content": "## Trigger \nWe schedule the trigger at 9.00 pm before going to bed. This flow is to reflect what is the great thing that happened today."
      },
      "typeVersion": 1
    },
    {
      "id": "c7a620fe-2a50-4cfb-af91-8a4b4ca58adb",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        160,
        -240
      ],
      "parameters": {
        "color": 5,
        "width": 300,
        "height": 360,
        "content": "## Write Reminder\nAfter getting the same reminder, we tend to ignore it. This is to generate variations of reminder by setting the temperature of the model at 0.9"
      },
      "typeVersion": 1
    },
    {
      "id": "66b865a1-0a6c-4a3c-abb3-024ec7ff8b40",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        500,
        -240
      ],
      "parameters": {
        "color": 6,
        "width": 300,
        "height": 360,
        "content": "## Reformatted \nThis is to reformat text to be able to send in Line Push API properly."
      },
      "typeVersion": 1
    },
    {
      "id": "adb8cf4e-de77-4490-a8da-b32122c3a730",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        840,
        -240
      ],
      "parameters": {
        "color": 4,
        "width": 300,
        "height": 360,
        "content": "## Push Message\nSend push message via LINE"
      },
      "typeVersion": 1
    },
    {
      "id": "6562967a-fae7-400a-913a-4cf68e70b40a",
      "name": "Reformat Output from Chat Model",
      "type": "n8n-nodes-base.set",
      "position": [
        600,
        -100
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "90abc5a6-c9b9-4b0d-b433-c6f90816dba3",
              "name": "posestoday",
              "type": "string",
              "value": "={{ $json.text.replaceAll(\"\\n\",\"\\\\n\").replaceAll(\"\\n\",\"\").removeMarkdown().removeTags().replaceAll('\"',\"\") }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "d2ab000a-6f3a-494f-807f-829cbb124685",
      "name": "Azure OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatAzureOpenAi",
      "position": [
        280,
        -20
      ],
      "parameters": {
        "model": "4o",
        "options": {
          "temperature": 0.9
        }
      },
      "credentials": {
        "azureOpenAiApi": {
          "id": "5AjoWhww5SQi2VXd",
          "name": "Azure Open AI account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "c548df75-dc6c-472f-8992-77f0f57d4732",
      "name": "Line Push Message",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        940,
        -100
      ],
      "parameters": {
        "url": "https://api.line.me/v2/bot/message/push",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n    \"to\": \"YOUR ID HERE\",\n    \"messages\":[\n        {\n            \"type\":\"text\",\n            \"text\":\"{{ $json.posestoday }}\"\n        }\n    ]\n} ",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "yiPG7xPwvDzsY0Qd",
          "name": "Line @511dizji"
        }
      },
      "typeVersion": 4.2
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "timezone": "Asia/Bangkok",
    "callerPolicy": "workflowsFromSameOwner",
    "executionOrder": "v1"
  },
  "versionId": "19321d28-e96d-4f97-94a9-604b59b5b651",
  "connections": {
    "WriteReminder": {
      "main": [
        [
          {
            "node": "Reformat Output from Chat Model",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Azure OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "WriteReminder",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Reformat Output from Chat Model": {
      "main": [
        [
          {
            "node": "Line Push Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Trigger 2100 Bear Gratitude Jar Notice": {
      "main": [
        [
          {
            "node": "WriteReminder",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
