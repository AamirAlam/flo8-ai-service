# Post on X using Airtop and automate content pipelines

**[View Template](https://n8n.io/workflows/3482-/)**  **Published Date:** 04/08/2025  **Created By:** Cesar @ Airtop AI  **Categories:** `Productivity` `Development`  

## Template Description

About The Post to X Automation

Seamlessly automate posting to X using Airtop and Make.

How to Automate Posting to X with Airtop

Consistently engaging your audience on X (formerly Twitter) can be a challenge, particularly when done manually. Developers and automation engineers often struggle with repetitive tasks like scheduling tweets, maintaining consistent posting cycles, and integrating content from various sources or AI-generated feeds. Manually managing content updates increases fatigue, human error, and decreases scalability.

This n8n automation, powered by Airtop, simplifies automated content publishing onto X. Whether you're sharing daily updates, integrating dynamically generated AI content, or streamlining your marketing content pipeline, Airtop’s automation helps eliminate manual labor and reduces potential execution errors.

Who is this Automation for?

Social Media Managers scheduling recurring or automated posts on X
Content Marketers integrating AI-generated content into their publishing process
Developers implementing automated social media pipelines
Automation Engineers minimizing errors and manual posting efforts

Key Benefits

Real-time, authenticated API postings via X
Reliable structured workflows minimize manual errors
Seamless integration with AI content pipelines

Use Cases

Automatically publish scheduled daily content updates
Seamlessly post AI-generated insights, news summaries or industry updates
Distribute alerts and event announcements reliably at set intervals
Maintain active audience engagement by automating regular, high-frequency posts

How the Post to X Automation Works

This Airtop automation works by using your Airtop Profile signed-in into X via Airtop. Once authenticated securely with your X credentials, n8n handles the structured data flow, which can come from manual inputs, AI-generated sources, databases, or RSS feeds. Airtop then securely publishes the posts, providing reliable scheduled updates directly on X, removing manual oversight and streamlining your social media workflows.

What You’ll Need

An Airtop API key
Your X (Twitter) account
An Airtop Profile signed into X

Setting Up the Automation

Connect your Airtop account using your free Airtop API key
Create an Airtop Profile and connect it to your X account
Activate and schedule your scenario to automate regular posting

Customize the Automation

Customize your posting workflow extensively using Airtop's built-in node in n8n:

Integrate diverse sources like RSS feeds and AI tools to dynamically customize automated posts
Schedule precise posting intervals or diversify times for maximum audience engagement
Set conditional logic to automate content posting based on predefined triggers and events
Utilize Airtop’s structured data flows to manage categories, hashtags, or mentions in your posts

Automation Best Practices

Consistently update security credentials for uninterrupted access
Clearly structure your workflow to simplify troubleshooting and logic updates
Monitor posting frequency to ensure optimal audience reach and engagement
Regularly review content sources to maintain quality control of automated postings

Happy Automating!


## Template JSON

```
{
  "id": "plzObaqgoEvV4UU0",
  "meta": {
    "instanceId": "28a947b92b197fc2524eaba16e57560338657b2b0b5796300b2f1cedc1d0d355",
    "templateCredsSetupCompleted": true
  },
  "name": "Post on X",
  "tags": [
    {
      "id": "gNiDOCnjqCXR7phD",
      "name": "Marketing",
      "createdAt": "2025-04-15T01:08:25.516Z",
      "updatedAt": "2025-04-15T01:08:25.516Z"
    },
    {
      "id": "zKNO4Omjzfu6J25M",
      "name": "Demo",
      "createdAt": "2025-04-15T18:59:57.364Z",
      "updatedAt": "2025-04-15T18:59:57.364Z"
    }
  ],
  "nodes": [
    {
      "id": "203a06a1-2e25-46df-9465-4d5740177249",
      "name": "Create session",
      "type": "n8n-nodes-base.airtop",
      "position": [
        60,
        180
      ],
      "parameters": {
        "profileName": "={{ $json.airtop_profile }}",
        "timeoutMinutes": 5,
        "saveProfileOnTermination": true
      },
      "credentials": {
        "airtopApi": {
          "id": "Yi4YPNnovLVUjFn5",
          "name": "Airtop API"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "18c8ade3-8492-4e75-8310-3be4d7815ab6",
      "name": "Create window",
      "type": "n8n-nodes-base.airtop",
      "position": [
        280,
        180
      ],
      "parameters": {
        "url": "https://x.com/",
        "resource": "window",
        "additionalFields": {}
      },
      "credentials": {
        "airtopApi": {
          "id": "Yi4YPNnovLVUjFn5",
          "name": "Airtop API"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "c46baeac-5d91-4656-a30f-0ca932e8042c",
      "name": "Type text",
      "type": "n8n-nodes-base.airtop",
      "position": [
        500,
        180
      ],
      "parameters": {
        "text": "={{ $('Parameters').item.json.post_text }}",
        "resource": "interaction",
        "operation": "type",
        "pressEnterKey": true,
        "additionalFields": {},
        "elementDescription": "\"What's happening?\" text box on top"
      },
      "credentials": {
        "airtopApi": {
          "id": "Yi4YPNnovLVUjFn5",
          "name": "Airtop API"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "cfc19d89-8fb2-49c5-97a3-38ad03dffe31",
      "name": "Click on Post",
      "type": "n8n-nodes-base.airtop",
      "position": [
        720,
        180
      ],
      "parameters": {
        "resource": "interaction",
        "additionalFields": {
          "visualScope": "viewport"
        },
        "elementDescription": "Click on the Post button "
      },
      "credentials": {
        "airtopApi": {
          "id": "Yi4YPNnovLVUjFn5",
          "name": "Airtop API"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "1b2a4d37-1fcd-4b6a-8db7-a7056c569ad4",
      "name": "End session",
      "type": "n8n-nodes-base.airtop",
      "position": [
        940,
        180
      ],
      "parameters": {
        "operation": "terminate"
      },
      "credentials": {
        "airtopApi": {
          "id": "Yi4YPNnovLVUjFn5",
          "name": "Airtop API"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "2fdae018-aaca-4101-acdc-42d799463880",
      "name": "When Executed by Another Workflow",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        -380,
        280
      ],
      "parameters": {
        "workflowInputs": {
          "values": [
            {
              "name": "airtop_profile"
            },
            {
              "name": "post_text"
            }
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "2a2125ff-6acd-4aca-bc69-d148b6cbb678",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        20
      ],
      "parameters": {
        "color": 5,
        "width": 220,
        "height": 320,
        "content": "### Heads up!\nTo make sure everything works smoothly, use an [Airtop Profile](https://docs.airtop.ai/guides/how-to/saving-a-profile) signed into x.com for the \"Create session\" node"
      },
      "typeVersion": 1
    },
    {
      "id": "ca75bf36-55c4-4496-9a77-3870d078bec2",
      "name": "On form submission",
      "type": "n8n-nodes-base.formTrigger",
      "position": [
        -380,
        80
      ],
      "webhookId": "bf22d894-7313-40b1-aefa-98bc518473bf",
      "parameters": {
        "options": {
          "buttonLabel": "Post on X",
          "appendAttribution": false,
          "respondWithOptions": {
            "values": {
              "formSubmittedText": "\u2705 Your post has been published!"
            }
          }
        },
        "formTitle": "Post on X",
        "formFields": {
          "values": [
            {
              "fieldLabel": "Airtop profile name",
              "placeholder": "e.g. my-x-profile",
              "requiredField": true
            },
            {
              "fieldLabel": "Text to post",
              "placeholder": "e.g. This X post was made with Airtop and n8n",
              "requiredField": true
            }
          ]
        },
        "responseMode": "lastNode",
        "formDescription": "Enter the <a href=\"https://docs.airtop.ai/guides/how-to/saving-a-profile\" target=\"_blank\">Airtop Profile</a> and the content you would like to post on x.com"
      },
      "typeVersion": 2.2
    },
    {
      "id": "d56e067b-9825-4a81-88a4-c65dac5a919c",
      "name": "Parameters",
      "type": "n8n-nodes-base.set",
      "position": [
        -160,
        180
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "e612bf63-72bd-4b61-82c9-786a90b58b7b",
              "name": "airtop_profile",
              "type": "string",
              "value": "={{ $json[\"Airtop profile name\"] || $json.airtop_profile }}"
            },
            {
              "id": "567e5e7d-4efd-4d0a-a93c-6c7aed02c305",
              "name": "post_text",
              "type": "string",
              "value": "={{ $json[\"Text to post\"] || $json.post_text }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "9129144f-d078-48f8-825a-7f8bbda4570b",
  "connections": {
    "Type text": {
      "main": [
        [
          {
            "node": "Click on Post",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parameters": {
      "main": [
        [
          {
            "node": "Create session",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Click on Post": {
      "main": [
        [
          {
            "node": "End session",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create window": {
      "main": [
        [
          {
            "node": "Type text",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create session": {
      "main": [
        [
          {
            "node": "Create window",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On form submission": {
      "main": [
        [
          {
            "node": "Parameters",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When Executed by Another Workflow": {
      "main": [
        [
          {
            "node": "Parameters",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
