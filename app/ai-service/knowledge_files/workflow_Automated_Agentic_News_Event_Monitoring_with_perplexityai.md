# Automated Agentic News Event Monitoring with perplexity.ai

**[View Template](https://n8n.io/workflows/2458-/)**  **Published Date:** 10/10/2024  **Created By:** Derek Cheung  **Categories:** `Communication` `HITL` `AI` `Langchain`  

## Template Description

Purpose of workflow:
The purpose of this workflow is to create a news reporter AI agent that automatically monitors specific news events and sends summary emails to the user. 

This tool aims to keep users up-to-date with the latest happenings on topics of interest without the need to constantly check multiple news sources manually. It's particularly useful for investors or researchers who must stay informed about specific events that may impact their work or investments.

How it works:
It leverages the power of large language models, specifically Perplexity's (perplexity.ai) online models accessed through Open Router (openrouter.ai), to understand and summarize up-to-date news. 

The workflow is scheduled to run at predetermined intervals (e.g., daily at 7 AM), automatically scanning for news on the specified topic, generating a summary, and sending it via email to the user.

Setup:
Sign up and generate an API key from Openrouter.ai This provides access to Perplexity's online language models
Update Perplexity node with Openrouter.ai API key
Specify the event/topic to monitor in the News Reporter node
Activate workflow to turn on scheduling feature 

## Template JSON

```
{
  "meta": {
    "instanceId": "2723a3a635131edfcb16103f3d4dbaadf3658e386b4762989cbf49528dccbdbd"
  },
  "nodes": [
    {
      "id": "f78605f4-cddb-481c-82c2-8d6cf768530b",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        840,
        380
      ],
      "parameters": {},
      "typeVersion": 1.2
    },
    {
      "id": "601bbd26-d1a0-4c1a-87a7-bb48b3d6ec6e",
      "name": "Gmail",
      "type": "n8n-nodes-base.gmail",
      "position": [
        2020,
        380
      ],
      "parameters": {},
      "typeVersion": 2.1
    },
    {
      "id": "361c74e4-7c15-4884-babd-173b795eca0e",
      "name": "Markdown",
      "type": "n8n-nodes-base.markdown",
      "position": [
        1420,
        380
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "d0af0361-6e41-4c9e-89bc-bfbad41f1a7e",
      "name": "Perplexity",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        1120,
        600
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "352defa0-f354-491c-a35d-dd2a94f38553",
      "name": "Title",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        1640,
        380
      ],
      "parameters": {},
      "typeVersion": 1.4
    },
    {
      "id": "3bab5737-7f9b-4b2e-b0fd-49b3e744b932",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        420,
        320
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "c19ff26f-8cb6-41d9-b110-46214323eca1",
      "name": "News Reporter",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        1040,
        380
      ],
      "parameters": {},
      "retryOnFail": true,
      "typeVersion": 1.6
    }
  ],
  "pinData": {},
  "connections": {
    "Title": {
      "main": [
        [
          {
            "node": "Gmail",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Markdown": {
      "main": [
        [
          {
            "node": "Title",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Perplexity": {
      "ai_languageModel": [
        [
          {
            "node": "Title",
            "type": "ai_languageModel",
            "index": 0
          },
          {
            "node": "News Reporter",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "News Reporter": {
      "main": [
        [
          {
            "node": "Markdown",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Schedule Trigger": {
      "main": [
        [
          {
            "node": "News Reporter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
