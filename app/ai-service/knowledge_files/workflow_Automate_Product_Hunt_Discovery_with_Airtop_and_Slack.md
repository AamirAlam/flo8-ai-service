# Automate Product Hunt Discovery with Airtop and Slack

**[View Template](https://n8n.io/workflows/3481-/)**  **Published Date:** 04/08/2025  **Created By:** Cesar @ Airtop AI  **Categories:** `Communication` `HITL` `Productivity` `Development`  

## Template Description

About The Product Hunt Automation

Staying up-to-date with specific topics and launches on Product Hunt can be time-consuming. Manually checking the site multiple times a day interrupts your workflow and risks missing important launches. What if you could automatically get relevant launches delivered to your Slack workspace?

How to Monitor Product Hunt

In this guide, you'll learn how to create a Product Hunt monitoring system using Airtop's built-in node in n8n. This automation will scan Product Hunt for your chosen topics and deliver the most relevant launches directly to Slack.

What You'll Need

A free Airtop API key
A Slack workspace with permissions to add incoming webhooks
Estimated setup time: 5 minutes

Understanding the Process

The Monitor Product Hunt automation uses Airtop's cloud browser capabilities to access Product Hunt and extract launch information. Here's what happens:

Airtop visits Product Hunt and navigates the page
It searches for and extracts up to 5 launches related to your chosen topic
The information is formatted and sent to your specified Slack channel

This process can run on your preferred schedule, ensuring you never miss relevant launches.

Setting Up Your Automation

We've created a ready-to-use template that handles all the complex parts. Here's how to get started:

Connect your Airtop account by adding the API key you created
Connect your Slack account
Set your prompt in the Airtop node. For this example, we’ve set it to be “Extract up to 5 launches related to AI products”
Choose your preferred monitoring schedule.

Customization Options

While our template works immediately, you might want to customize it for your specific needs:

Adjust the prompt and the maximum number of launches to monitor
Customize the Slack message format
Change the monitoring frequency
Add filters for particular keywords or companies

Real-World Applications

Here's how teams can use this automation:

A startup's engineering team could track trends in other product’s tech stack, helping them stay informed about potential issues and improvements.

A product manager can track launches of competitor products, enabling them to gather valuable market insights and user feedback directly from the tech community on that launch.

Best Practices

To get the most out of this automation:

Choose Specific Search Terms**: For more relevant results, instead of broad terms like "AI," use specific phrases like "machine learning for healthcare"
Optimize Scheduling**: When setting the monitoring frequency, consider your team's workflow. Running the scenario every 4 hours during working hours often provides a good balance between staying updated and avoiding notification fatigue.
Set Up Error Handling**: Enable n8n's error output to alert you if the automation encounters any issues with accessing Product Hunt or sending messages to Slack.
Regular Topic Review**: Schedule a monthly review of your monitored topics to ensure they're still relevant to your needs and adjust as necessary.

What's Next?

Now that you've set up your Product Hunt monitor automation, you might be interested in:

Creating a similar monitor for other tech websites
Setting up automated content curation for your team's newsletter
Building a competitive intelligence dashboard using web monitoring

Happy Automating!

## Template JSON

```
{
  "id": "fvYgcG9s1pqP5cQ6",
  "meta": {
    "instanceId": "660cf2c29eb19fa42319afac3bd2a4a74c6354b7c006403f6cba388968b63f5d",
    "templateCredsSetupCompleted": true
  },
  "name": "Monitor ProductHunt",
  "tags": [
    {
      "id": "a8B9vqj0vNLXcKVQ",
      "name": "template",
      "createdAt": "2025-04-04T15:38:37.785Z",
      "updatedAt": "2025-04-04T15:38:37.785Z"
    }
  ],
  "nodes": [
    {
      "id": "3cf0b7e0-ec9f-4173-bc85-1b4daef5aa22",
      "name": "Define relevant products",
      "type": "n8n-nodes-base.set",
      "position": [
        220,
        -100
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "a83156e0-1782-4d0a-a15c-1ff889ff915d",
              "name": "Relevant Products",
              "type": "string",
              "value": "AI Agents"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "a316f080-0fd8-4723-a65c-bce2c2a13cf8",
      "name": "Found products?",
      "type": "n8n-nodes-base.if",
      "position": [
        660,
        -100
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
              "id": "552c61c2-1ec0-40b5-b473-2423b646418b",
              "operator": {
                "type": "string",
                "operation": "notContains"
              },
              "leftValue": "={{ $json.data.modelResponse }}",
              "rightValue": "[NA]"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "ffb0289e-9341-4641-bfcd-41b25f0b1379",
      "name": "Look up products",
      "type": "n8n-nodes-base.airtop",
      "position": [
        440,
        -100
      ],
      "parameters": {
        "url": "https://www.producthunt.com/",
        "prompt": "=Extract up to 5 product launches that are {{ $json[\"Relevant Products\"] }} for each product extract the title and URL (if exists).\n\nReturn format:\nToday's [{{ $json[\"Relevant Products\"] }}] on Producthunt\n1. Title 1 (URL 1)\n2. Title 2 (URL 2)\nand so on\n\nIf you cannot find any relevant products, return [NA]",
        "resource": "extraction",
        "operation": "query",
        "sessionMode": "new",
        "additionalFields": {}
      },
      "credentials": {
        "airtopApi": {
          "id": "byhouJF8RLH5DkmY",
          "name": "[PROD] Airtop"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "4d1f0668-d5d5-4440-8608-3cfe3d61d0c0",
      "name": "Send slack message",
      "type": "n8n-nodes-base.slack",
      "position": [
        880,
        -100
      ],
      "webhookId": "9887477b-9680-4701-a2a1-583d47f1fb5d",
      "parameters": {
        "text": "={{ $json.data.modelResponse }}",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "list",
          "value": "C087FK3J0MC",
          "cachedResultName": "make-debug"
        },
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": {
          "id": "NgjAmOgS9xRg1RlU",
          "name": "Slack account"
        }
      },
      "typeVersion": 2.3
    },
    {
      "id": "921d283e-6d67-4aaa-a344-687bb23b8710",
      "name": "Trigger daily",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        0,
        -100
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "triggerAtHour": 6
            }
          ]
        }
      },
      "typeVersion": 1.2
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "e51e2bd0-43f0-4601-a0ad-f553f419a827",
  "connections": {
    "Trigger daily": {
      "main": [
        [
          {
            "node": "Define relevant products",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Found products?": {
      "main": [
        [
          {
            "node": "Send slack message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Look up products": {
      "main": [
        [
          {
            "node": "Found products?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Define relevant products": {
      "main": [
        [
          {
            "node": "Look up products",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
