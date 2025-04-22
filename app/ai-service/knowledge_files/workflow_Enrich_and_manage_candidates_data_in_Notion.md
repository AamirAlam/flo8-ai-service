# Enrich and manage candidates data in Notion

**[View Template](https://n8n.io/workflows/1107-/)**  **Published Date:** 06/03/2021  **Created By:** ghagrawal17  **Categories:** `Analytics` `Productivity`  

## Template Description

This workflow allows you to add candidates’ profile assessments to Notion before an interview.

Prerequisites
Add an input field on your Calendly Invite page where the candidate can enter their LinkedIn URL.
Create credentials for your Calendly account. Follow the steps mentioned in the documentation to learn how to do that.
Create credentials for Humantic AI following the steps mentioned here.
Create a page on Notion similar to this page.
Create credentials for the Notion node by following the steps in the documentation.



Calendly Trigger node: This node will trigger the workflow when an interview gets scheduled. Make sure to add a field to collect the candidates' LinkedIn URL on your invite page.

Humantic AI: This node uses the LinkedIn URL received by the previous node to create a candidate profile in Humantic AI.

Humantic AI1: This node will analyze the candidates' profile.


Notion node: This node will create a new page in Notion using the information from the previous node.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Notion",
      "type": "n8n-nodes-base.notion",
      "position": [
        1050,
        300
      ],
      "parameters": {
        "blockUi": {
          "blockValues": [
            {
              "textContent": "=Name: {{$json[\"display_name\"]}}\nPersonality: {{$json[\"personality_analysis\"][\"summary\"][\"ocean\"][\"description\"].join(', ')}}, {{$json[\"personality_analysis\"][\"summary\"][\"disc\"][\"description\"].join(', ')}}\nOpenness: {{$json[\"personality_analysis\"][\"ocean_assessment\"][\"openness\"][\"level\"]}} {{$json[\"personality_analysis\"][\"ocean_assessment\"][\"openness\"][\"score\"]}}\nCalculativeness: {{$json[\"personality_analysis\"][\"disc_assessment\"][\"calculativeness\"][\"level\"]}} {{$json[\"personality_analysis\"][\"disc_assessment\"][\"calculativeness\"][\"score\"]}}"
            }
          ]
        },
        "resource": "databasePage",
        "databaseId": "",
        "propertiesUi": {
          "propertyValues": [
            {
              "key": "Name|title",
              "title": "={{$json[\"display_name\"]}}"
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
      "name": "Humantic AI",
      "type": "n8n-nodes-base.humanticAi",
      "position": [
        650,
        300
      ],
      "parameters": {
        "userId": "={{$json[\"payload\"][\"questions_and_responses\"][\"1_response\"]}}"
      },
      "credentials": {
        "humanticAiApi": "humantic"
      },
      "typeVersion": 1
    },
    {
      "name": "Calendly Trigger",
      "type": "n8n-nodes-base.calendlyTrigger",
      "position": [
        450,
        300
      ],
      "webhookId": "6d38c1f6-42ee-4f44-b424-20943075087b",
      "parameters": {
        "events": [
          "invitee.created"
        ]
      },
      "credentials": {
        "calendlyApi": ""
      },
      "typeVersion": 1
    },
    {
      "name": "Humantic AI1",
      "type": "n8n-nodes-base.humanticAi",
      "position": [
        850,
        300
      ],
      "parameters": {
        "userId": "={{$json[\"results\"][\"userid\"]}}",
        "options": {},
        "operation": "get"
      },
      "credentials": {
        "humanticAiApi": ""
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Humantic AI": {
      "main": [
        [
          {
            "node": "Humantic AI1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Humantic AI1": {
      "main": [
        [
          {
            "node": "Notion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Calendly Trigger": {
      "main": [
        [
          {
            "node": "Humantic AI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
