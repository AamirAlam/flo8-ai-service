# Social Media Content Generator And Publisher | X, Linkedin

**[View Template](https://n8n.io/workflows/3082-/)**  **Published Date:** 03/04/2025  **Created By:** ömer  **Categories:** `Marketing` `Communication` `AI` `Langchain`  

## Template Description

Generate and Publish AI Content to LinkedIn and X (Twitter) with n8n

Overview
This n8n workflow automates the generation and publishing of AI-powered social media content across LinkedIn and X (formerly Twitter). By leveraging AI, this workflow helps social media managers, marketers, and content creators streamline their posting process.

Who is this for?
Social media managers
Content creators
Digital marketers
Businesses looking to automate content generation

Features
AI-powered content creation** tailored for LinkedIn and X (Twitter)
Automated publishing** to both platforms
Structured output parsing** to ensure consistency
OAuth2 authentication** for secure posting
Merge and confirmation steps** to track successful postings

Setup Instructions
Prerequisites
Before using this workflow, ensure you have:
An n8n instance set up
API credentials for:
  Google Gemini AI (for content generation)
  X Developer Account with OAuth2 authentication
  LinkedIn Developer Account with OAuth2 authentication
A form submission service integrated with n8n

Workflow Breakdown

1. Trigger: Form Submission
A user submits a form containing the post title.
The form is secured with Basic Authentication.
The submitted title is passed to the AI Agent.

2. AI Content Generation
The Google Gemini Chat Model processes the title and generates:
  LinkedIn post content
  Twitter (X) post content
  Hashtags
  Call-to-action (LinkedIn)
  Character limit check (Twitter)

3. Parsing AI Output
A structured output parser converts the AI-generated content into a JSON format.
Ensures correct formatting for LinkedIn and Twitter (X).

4. Publishing to Social Media
X (Twitter) Posting
Extracts the Twitter post from the AI output.
Publishes it via an OAuth2-authenticated X (Twitter) account.

LinkedIn Posting
Extracts the LinkedIn post from the AI output.
Publishes it via an OAuth2-authenticated LinkedIn account.

5. Merging Post Results
Merges the response data from both LinkedIn and Twitter after publishing.

6. Confirmation Step
Displays a final confirmation form once the posts are successfully published.

Benefits
Save time** by automating content creation and publishing.
Ensure consistency** across platforms with structured AI-generated posts.
Secure authentication** using OAuth2 for LinkedIn and Twitter.
Increase engagement** with AI-optimized hashtags and CTAs.

This workflow enables seamless social media automation, helping professionals post engaging AI-powered content effortlessly. 🚀



## Template JSON

```
{
  "id": "wyzRJoRGTlwmZ0JJ",
  "meta": {
    "instanceId": "38c7fb933498a5028d938adeb8c37dbb3117d7ec2d546d718be8f13730816a0d",
    "templateCredsSetupCompleted": true
  },
  "name": "Social Media Content Generator And Publisher | X, Linkedin",
  "tags": [],
  "nodes": [
    {
      "id": "7095690e-4f33-4ad0-8276-f5f91768bc42",
      "name": "Google Gemini Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
      "position": [
        200,
        220
      ],
      "parameters": {
        "options": {},
        "modelName": "models/gemini-2.0-flash"
      },
      "credentials": {
        "googlePalmApi": {
          "id": "Td5xMGwy3MYAYRjH",
          "name": "Google Gemini(PaLM) Api account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "2858290a-82be-4f2f-9f20-a1147d1feb32",
      "name": "Receive Post Title",
      "type": "n8n-nodes-base.formTrigger",
      "position": [
        0,
        0
      ],
      "webhookId": "4d921ee9-7668-4133-8750-4e35f9fc2353",
      "parameters": {
        "options": {},
        "formTitle": "post",
        "formFields": {
          "values": [
            {
              "fieldLabel": "post title"
            }
          ]
        },
        "authentication": "basicAuth",
        "formDescription": "post"
      },
      "credentials": {
        "httpBasicAuth": {
          "id": "YoS57iMdTC3pnXR6",
          "name": "Unnamed credential 2"
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "b1540464-46ca-42d3-9e53-c3b7bd006d55",
      "name": "Generate AI Content",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        200,
        0
      ],
      "parameters": {
        "text": "=\nwrite min 50 word about this topic '{{ $json[\"post title\"] }}'\nfor Linkedin and X platform separately",
        "options": {},
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.7
    },
    {
      "id": "ac86de4e-49a2-4efc-9067-bbb0008a218c",
      "name": "Format AI Output",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        360,
        260
      ],
      "parameters": {
        "schemaType": "manual",
        "inputSchema": "{\n  \"type\": \"object\",\n  \"properties\": {\n    \"event_name\": {\n      \"type\": \"string\"\n    },\n    \"event_description\": {\n      \"type\": \"string\"\n    },\n    \"platform_posts\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"LinkedIn\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"post\": {\n              \"type\": \"string\"\n            },\n            \"hashtags\": {\n              \"type\": \"array\",\n              \"items\": {\n                \"type\": \"string\"\n              }\n            },\n            \"call_to_action\": {\n              \"type\": \"string\"\n            }\n          }\n        },\n        \"Twitter\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"post\": {\n              \"type\": \"string\"\n            },\n            \"hashtags\": {\n              \"type\": \"array\",\n              \"items\": {\n                \"type\": \"string\"\n              }\n            },\n            \"character_limit\": {\n              \"type\": \"integer\"\n            }\n          }\n        }\n      }\n    },\n    \"additional_notes\": {\n      \"type\": \"string\"\n    }\n  }\n}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "5a4cbb6f-4efc-4fd1-85ea-9022d6415811",
      "name": "Post to X",
      "type": "n8n-nodes-base.twitter",
      "position": [
        580,
        -100
      ],
      "parameters": {
        "text": "={{ $json.output.platform_posts.Twitter.post }}",
        "additionalFields": {}
      },
      "credentials": {
        "twitterOAuth2Api": {
          "id": "tFoAD5zVouFXHqHV",
          "name": "X account 4"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "6be0a393-1ef8-4e2e-b58e-e7dd90bf5295",
      "name": "Post to LinkedIn",
      "type": "n8n-nodes-base.linkedIn",
      "position": [
        580,
        120
      ],
      "parameters": {
        "text": "={{ $json.output.platform_posts.LinkedIn.post }}",
        "person": "-HtNhNKSsE",
        "additionalFields": {}
      },
      "credentials": {
        "linkedInOAuth2Api": {
          "id": "wssjQBMipjgQPG10",
          "name": "LinkedIn account 3"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "10336b6e-b093-473c-b8d1-90d6b7b043b3",
      "name": "Append Linkedin And X Publishing Responses",
      "type": "n8n-nodes-base.merge",
      "position": [
        860,
        20
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combineBy": "combineAll"
      },
      "typeVersion": 3
    },
    {
      "id": "a236d6ba-0ded-4d42-99a3-0b53069faec5",
      "name": "Show Confirmation",
      "type": "n8n-nodes-base.form",
      "position": [
        1080,
        20
      ],
      "webhookId": "9c0b2419-aff6-40dd-95f7-5dfd0a88d46c",
      "parameters": {
        "options": {},
        "operation": "completion",
        "completionTitle": "Your post has been successfully shared",
        "completionMessage": "=\ud83d\udd17 View your posts:\n\nX (Twitter): \n[https://x.com/x/status/{{ $json.id }}]\n\nLinkedIn:\n[https://www.linkedin.com/feed/update/{{ $json.urn }}]"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "7b92c25a-8617-44c8-b3b6-c038f01d6bfa",
  "connections": {
    "Post to X": {
      "main": [
        [
          {
            "node": "Append Linkedin And X Publishing Responses",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format AI Output": {
      "ai_outputParser": [
        [
          {
            "node": "Generate AI Content",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Post to LinkedIn": {
      "main": [
        [
          {
            "node": "Append Linkedin And X Publishing Responses",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Receive Post Title": {
      "main": [
        [
          {
            "node": "Generate AI Content",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate AI Content": {
      "main": [
        [
          {
            "node": "Post to X",
            "type": "main",
            "index": 0
          },
          {
            "node": "Post to LinkedIn",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Gemini Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Generate AI Content",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Append Linkedin And X Publishing Responses": {
      "main": [
        [
          {
            "node": "Show Confirmation",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
