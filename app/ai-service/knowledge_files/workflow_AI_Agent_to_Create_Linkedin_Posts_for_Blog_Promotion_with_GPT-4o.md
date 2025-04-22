# ✍️ AI Agent to Create Linkedin Posts for Blog Promotion with GPT-4o

**[View Template](https://n8n.io/workflows/3500-/)**  **Published Date:** 04/09/2025  **Created By:** Samir Saci  **Categories:** `Data & Storage` `Productivity` `Marketing` `Development` `Core Nodes` `AI` `Langchain`  

## Template Description

Tags: Automation, AI, Marketing, Content Creation

Note: it seems that there is an issue with the publication of the template, Ghost node is missing. I am investigating to understand the reason.

Context
I’m a Supply Chain Data Scientist and content creator who writes regularly about data-driven optimization, logistics, and sustainability. Promoting blog articles on LinkedIn used to be a manual task — until I decided to automate it with N8N and GPT-4o.

This workflow lets you automatically extract blog posts, clean the content, and generate a professional LinkedIn post using an AI Agent powered by GPT-4o — all in one seamless automation.

&gt;Save hours of repetitive work and boost your reach with AI.

📬 For business inquiries, you can add me on LinkedIn

Who is this template for?
This template is perfect for:
Bloggers and writers** who want to promote their content on LinkedIn
Marketing teams** looking to automate professional post-generation
Content creators** using Ghost platforms

It generates polished LinkedIn posts with:
A hook
A quick summary
A call-to-action
A signature to drive readers to your contact page

How does it work?
This workflow runs in N8N and performs the following steps:

🚀 Triggers manually or you can add a scheduler
📰 Pulls recent blog posts from your Ghost site (via API)
🧼 Cleans the HTML content for AI input
🤖 Sends content to GPT-4o with a tailored prompt to create a LinkedIn post
📄 Records all data (post content + LinkedIn output) in a Google Sheet

What do I need to start?
You don’t need to write a single line of code.
Prerequisites:
A Ghost CMS account with blog content
A Google Sheet to store generated posts
An OpenAI API Key
Google Sheets API** connected via OAuth2

Next Steps
Use the sticky notes in the workflow to understand how to:
Add your Ghost API credentials
Link your Google Sheet
Customize the AI prompt (e.g., change the author name or tone)
Optionally add auto-posting to LinkedIn using tools like Buffer or Make



🎥 Watch My Tutorial

🚀 Want to explore how automation can scale your brand or business?
📬 Let’s connect on LinkedIn

Notes
You can adapt this template for Twitter, Facebook, or even email newsletters by adjusting the prompt and output channel.
This workflow was built using n8n 1.85.4

Submitted: April 9th, 2025


## Template JSON

```
{
  "meta": {
    "instanceId": "=",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "c6fd43cc-35ae-48cf-8d3a-60fce2d5c293",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -1080,
        -420
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "39b0ce07-f7b6-4cb8-a228-7ec5c51fca0c",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        280,
        -280
      ],
      "parameters": {
        "text": "=Article Title: {{ $json.title }}\nArticle Link: {{ $json.link }}\nArticle Content: {{ $json.clean_content }}",
        "options": {
          "systemMessage": "=You are a content marketing assistant. Based on the article metadata (ID, title) and cleaned content, generate a short LinkedIn promotional message for a professional audience.\n\nFollow this structure:\n\nStart with a hook that grabs attention (a bold insight, surprising fact, or thought-provoking question).\n\nBriefly summarize the article\u2019s value \u2014 what readers will learn or gain from it.\n\nInclude a clear call-to-action encouraging readers to read the article.\n\nEnd with this author signature and invitation:\n\u201c\u2014\nSamir Saci\nSupply Chain Data Scientist & Founder of LogiGreen\n\ud83d\udce9 Contact me: https://logi-green.com/contactus\u201d\n\nUse a professional and engaging tone. Do not include hashtags or Markdown formatting."
        },
        "promptType": "define"
      },
      "typeVersion": 1.8
    },
    {
      "id": "=",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        220,
        -120
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "=",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "44db3b7f-03cd-4942-b1d2-e0136fad29fe",
      "name": "Clean HTML",
      "type": "n8n-nodes-base.code",
      "position": [
        -160,
        -320
      ],
      "parameters": {
        "jsCode": "const htmlContent = $input.first().json.content;\n\nconst cleanText = htmlContent\n  .replace(/<[^>]*>/g, '') // remove  tags\n  .replace(/\\s+/g, ' ')    // normalize spaces\n  .replace(/&nbsp;/g, ' ') // decode common entity\n  .trim();\n\nreturn [\n  {\n    json: {\n      clean_content: cleanText\n    }\n  }\n];\n"
      },
      "typeVersion": 2
    },
    {
      "id": "=",
      "name": "Extract Blog Posts",
      "type": "n8n-nodes-base.ghost",
      "position": [
        -860,
        -420
      ],
      "parameters": {
        "limit": 3,
        "options": {},
        "operation": "getAll"
      },
      "credentials": {
        "ghostContentApi": {
          "id": "=",
          "name": "Ghost Content account"
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "402db85f-4a3f-4df4-986e-b27a4ebabda9",
      "name": "Extract Post Content",
      "type": "n8n-nodes-base.set",
      "position": [
        -640,
        -420
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "00b337cd-1c61-4f19-8c51-b76f3a8dece1",
              "name": "id",
              "type": "string",
              "value": "={{ $json.id }}"
            },
            {
              "id": "8d38f4bc-bca6-4343-8c5e-5d9fd9cbe178",
              "name": "title",
              "type": "string",
              "value": "={{ $json.title }}"
            },
            {
              "id": "c34ddd76-0db6-4225-82fa-04d5542f9c7c",
              "name": "featured_image",
              "type": "string",
              "value": "={{ $json.feature_image }}"
            },
            {
              "id": "c0f9593c-0d5a-4659-9e25-91b098318bd6",
              "name": "excerpt",
              "type": "string",
              "value": "={{ $json.excerpt }}"
            },
            {
              "id": "0d11d3d5-49f8-473a-8602-b49769f88005",
              "name": "content",
              "type": "string",
              "value": "={{ $json.html }}"
            },
            {
              "id": "ec89a00d-9d76-4594-a8ce-98aa177e6737",
              "name": "link",
              "type": "string",
              "value": "={{ $json.url }}"
            }
          ]
        }
      },
      "notesInFlow": true,
      "typeVersion": 3.4
    },
    {
      "id": "0154183e-aaab-4efe-b72f-7a0626390528",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1120,
        -780
      ],
      "parameters": {
        "color": 7,
        "width": 200,
        "height": 520,
        "content": "### 1. Workflow Trigger\nThis workflow uses simple trigger.\n\n#### How to setup?\n*Nothing to do.*\n"
      },
      "typeVersion": 1
    },
    {
      "id": "2641b9c3-bb34-4f4d-9bb6-8b9fcc68d2a5",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -900,
        -780
      ],
      "parameters": {
        "color": 7,
        "width": 400,
        "height": 520,
        "content": "### 2. Extract Blog Posts Content\nThe Ghost node extracts all the posts of your blog with content and metadata. In the second node, we extract description, URL, content and features image url.\n\n#### How to setup?\n- **Ghost Account API**:\n   1. Add your Ghost Blog Account Credentials\n   2. Select the number of Blog Posts you want to collect\n  [Learn more about the Ghost Node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.ghost)\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "3f7609d8-e8f8-404b-a5d5-a7f7bf7cf5a8",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -460,
        -780
      ],
      "parameters": {
        "color": 7,
        "width": 1520,
        "height": 800,
        "content": "### 3. Generate a Linkedin Post for each Post with an AI Agent\nThis block loops through all the posts pulled by the Ghost Node, send the content to the AI agent that generates a Linkedin post. The results are combined and pulled in a Google Sheet.\n\n#### How to setup?\n- **AI Agent with the Chat Model**:\n   1. Add a **chat model** with the required credentials *(Example: Open AI 4o-mini)*\n   2. Adapt the system prompt with your **post signature** and additional points you want to add in your posts\n  [Learn more about the AI Agent Node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)\n- **Record Long Break in the Google Sheet Node**:\n   1. Add your Google Sheet API credentials to access the Google Sheet file\n   2. Select the file using the list, an URL or an ID\n   3. Select the sheet in which you want to record your working sessions\n   4. Map the fields\n  [Learn more about the Google Sheet Node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets)\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "=",
      "name": "Record the posts",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        900,
        -180
      ],
      "parameters": {
        "columns": {
          "value": {
            "id": "={{ $json.id }}",
            "title": "={{ $json.title }}",
            "content": "={{ $json.content }}",
            "excerpt": "={{ $json.excerpt }}",
            "clean_content": "={{ $json.clean_content }}",
            "linkedin_post": "={{ $json.output }}",
            "featured_image": "={{ $json.featured_image }}"
          },
          "schema": [
            {
              "id": "id",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "id",
              "defaultMatch": true,
              "canBeUsedToMatch": true
            },
            {
              "id": "title",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "title",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "featured_image",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "featured_image",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "excerpt",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "excerpt",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "content",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "content",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "clean_content",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "clean_content",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "linkedin_post",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "linkedin_post",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "id"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "append",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "=",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "=",
          "cachedResultUrl": "=",
          "cachedResultName": "Blog Post"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "=",
          "name": "="
        }
      },
      "notesInFlow": true,
      "typeVersion": 4.5
    },
    {
      "id": "a61fedfd-c1ff-4c3a-9440-fa5bf7bd6df7",
      "name": "Merge Linkedin",
      "type": "n8n-nodes-base.merge",
      "position": [
        660,
        -420
      ],
      "parameters": {
        "mode": "combineBySql"
      },
      "notesInFlow": true,
      "typeVersion": 3
    },
    {
      "id": "8c767967-759b-44e5-aeeb-186a83e1b210",
      "name": "Add Clean HTML",
      "type": "n8n-nodes-base.merge",
      "position": [
        80,
        -420
      ],
      "parameters": {
        "mode": "combineBySql"
      },
      "typeVersion": 3
    },
    {
      "id": "65fc196a-4137-4440-a092-9b27eb40b822",
      "name": "Loop Over Posts",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        -360,
        -420
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 3
    }
  ],
  "pinData": {},
  "connections": {
    "AI Agent": {
      "main": [
        [
          {
            "node": "Merge Linkedin",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Clean HTML": {
      "main": [
        [
          {
            "node": "Add Clean HTML",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Add Clean HTML": {
      "main": [
        [
          {
            "node": "AI Agent",
            "type": "main",
            "index": 0
          },
          {
            "node": "Merge Linkedin",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Merge Linkedin": {
      "main": [
        [
          {
            "node": "Record the posts",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Loop Over Posts": {
      "main": [
        [],
        [
          {
            "node": "Clean HTML",
            "type": "main",
            "index": 0
          },
          {
            "node": "Add Clean HTML",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Record the posts": {
      "main": [
        [
          {
            "node": "Loop Over Posts",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Extract Blog Posts": {
      "main": [
        [
          {
            "node": "Extract Post Content",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Post Content": {
      "main": [
        [
          {
            "node": "Loop Over Posts",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When clicking \u2018Test workflow\u2019": {
      "main": [
        [
          {
            "node": "Extract Blog Posts",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
