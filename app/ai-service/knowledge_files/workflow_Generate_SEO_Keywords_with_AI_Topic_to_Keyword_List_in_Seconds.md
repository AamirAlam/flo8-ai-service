# Generate SEO Keywords with AI: Topic to Keyword List in Seconds

**[View Template](https://n8n.io/workflows/3544-/)**  **Published Date:** 04/13/2025  **Created By:** Gegenfeld  **Categories:** `Communication` `HITL` `Development` `Core Nodes` `AI` `Langchain`  

## Template Description

Who is this template for?
This AI Keyword Generator workflow template is designed for marketers, SEO specialists, and content creators who need to quickly generate high-quality keyword lists for their content strategy. Instead of spending hours researching keywords manually, this AI-powered tool delivers targeted keyword suggestions based on your specific criteria.

What problem does this workflow solve?
Keyword research is a time-consuming but essential part of SEO and content marketing. Many professionals struggle with:
Finding relevant keywords that match specific search intents
Balancing between short-tail and long-tail keywords
Generating comprehensive keyword lists that cover different aspects of a topic
Consistently identifying high-potential keywords for content creation

What this workflow does
This n8n workflow leverages AI to automatically generate a customized list of 15-20 high-potential keywords based on three simple inputs:
Topic** - The main subject area you want keywords for
Search Intent** - Choose between Navigational, Informational, Commercial, or Transactional
Keyword Type** - Select Short-Tail or Long-Tail keywords

The workflow processes your input through an AI language model that follows SEO best practices to generate relevant keywords. It then formats the results and delivers them directly to your email inbox, ready for use in your SEO strategy.

Setup
Setting up this workflow is straightforward:

Add your credentials for the AI language model in the "Select your Chat Model" node
   Click on the node and connect your Groq account (and choose any LLM you want, like: OpenAI, Claude AI or Llama)  or replace with another LLM provider
   
Configure email delivery in the "Send Result" node
   Update the "sendTo" parameter with your email address
   Add your Gmail credentials or replace with your preferred email service

Test your workflow by clicking the "Test Workflow" button
   Use the form to enter your topic, search intent, and keyword type
   Check your email for the generated keyword report

Activate the workflow once testing is complete

How to customize this workflow
The template is highly adaptable to fit your specific needs:

Replace the email node** with a database or spreadsheet node to store keywords
Modify the AI prompts** in the "AI Keyword Agent" to adjust the keyword generation strategy
Add additional filtering nodes** to further refine keywords based on custom criteria
Integrate with other SEO tools** to analyze competition or search volume for generated keywords

This workflow serves as a powerful starting point for automating your keyword research process, saving you valuable time while delivering consistent, high-quality results.

## Template JSON

```
{
  "id": "fdmFbwuFWRNIrUOq",
  "meta": {
    "instanceId": "acd8d3f9e3e1f54a0f1e8891386f8d39713d521c50bf0fc51addf59415c709de",
    "templateCredsSetupCompleted": true
  },
  "name": "AI Keyword Generator by Gegenfeld",
  "tags": [],
  "nodes": [
    {
      "id": "4e8229b4-22f4-4132-bc83-a3f880aa10e9",
      "name": "Set Data from Form",
      "type": "n8n-nodes-base.set",
      "position": [
        -160,
        -20
      ],
      "parameters": {},
      "notesInFlow": true,
      "typeVersion": 3.4
    },
    {
      "id": "6a28dc8f-aeef-4580-82b8-296facbde163",
      "name": "Select your Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatGroq",
      "position": [
        240,
        180
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "a25518ef-ee3f-43df-b66f-d363d46dcbcb",
      "name": "AI Keyword Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        240,
        -20
      ],
      "parameters": {},
      "typeVersion": 1.8
    },
    {
      "id": "9fb9bdc2-b43c-47fc-8a20-9b02a7b0faa6",
      "name": "Aggregate Data Points for AI Keyword Agent",
      "type": "n8n-nodes-base.aggregate",
      "position": [
        40,
        -20
      ],
      "parameters": {},
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "858e51e3-0b67-4502-993c-cda3f6456465",
      "name": "Extract and Format",
      "type": "n8n-nodes-base.code",
      "position": [
        600,
        -20
      ],
      "parameters": {},
      "typeVersion": 2
    },
    {
      "id": "7da899dd-cf03-4a85-b51c-eceb943afb93",
      "name": "Send Result",
      "type": "n8n-nodes-base.gmail",
      "position": [
        800,
        -20
      ],
      "webhookId": "5a22af29-3b72-4e75-8a60-624f93b88b4f",
      "parameters": {},
      "typeVersion": 2.1
    },
    {
      "id": "d66d2fd2-ec89-4b17-9c28-cf95c57ab023",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        800,
        160
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "1eb09baf-6105-4aee-aa8d-103b4a6ef8dc",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -500,
        140
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "bd97ef37-b8de-47f6-a9a5-1c19b9f1a393",
      "name": "Input Form",
      "type": "n8n-nodes-base.formTrigger",
      "position": [
        -360,
        -20
      ],
      "webhookId": "46703448-dd28-468a-8e76-b55d844bf76b",
      "parameters": {},
      "typeVersion": 2.2
    },
    {
      "id": "5148e29e-6e62-4c99-8413-c9c6918db5bd",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        160,
        340
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "42c87b85-ed7b-4b25-a46b-420819329b33",
  "connections": {
    "Input Form": {
      "main": [
        [
          {
            "node": "Set Data from Form",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Keyword Agent": {
      "main": [
        [
          {
            "node": "Extract and Format",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract and Format": {
      "main": [
        [
          {
            "node": "Send Result",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Data from Form": {
      "main": [
        [
          {
            "node": "Aggregate Data Points for AI Keyword Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Select your Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "AI Keyword Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Aggregate Data Points for AI Keyword Agent": {
      "main": [
        [
          {
            "node": "AI Keyword Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
