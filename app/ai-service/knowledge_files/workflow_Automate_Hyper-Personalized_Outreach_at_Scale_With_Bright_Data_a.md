# Automate Hyper-Personalized Outreach at Scale With Bright Data and LLMs

**[View Template](https://n8n.io/workflows/3561-/)**  **Published Date:** 04/15/2025  **Created By:** Yaron Been  **Categories:** `Data & Storage` `Productivity` `Development` `Core Nodes` `AI` `Langchain`  

## Template Description

LinkedIn Enrichment & Ice Breaker Generator

For SDRs, growth marketers, and founders looking to scale personalized outreach.  
This workflow enriches LinkedIn profile data using Bright Data and generates AI-powered ice breakers using Claude (Anthropic).  
It automates research and messaging to help you connect smarter and faster — without manual effort.

🧩 How It Works

This workflow combines Google Sheets, Brigt Data, and Claude (Anthropic) to fully automate your outreach research:

Trigger  
   Manually trigger the workflow or run it on a schedule (via Manual Trigger or Schedule Trigger).

Read Input Sheet  
   Fetches rows from a Google Sheet. Each row must contain at least a Linkedin_URL_Person and row_number.

Prepare Input  
   Formats each row for Bright Data’s API using Set and SplitInBatches nodes.

Enrich Profile (Bright Data API)  
   Sends LinkedIn URLs to Bright Data’s Dataset API via HTTP Request.
   Waits for snapshot to be ready using polling logic with Wait, If, and Snapshot Progress nodes.
   Once ready, retrieves the enriched profile data including:
     Name
     City
     Current company
     About section
     Recent posts

Update Sheet with Profile Data  
   Writes the retrieved enrichment data into the corresponding row in Google Sheets (via row_number).

Generate Ice Breaker (Claude AI)  
   Sends enriched profile content to Claude (Anthropic) using a custom prompt.
   Focuses on recent posts for crafting relevant, respectful, 1–4-line ice breakers.

Update Sheet with Ice Breaker  
   Writes the generated ice breaker to the Ice Breaker 1 column in the original row.

✅ Requirements

To use this workflow, you must have the following:

Google Sheets
A Google account
A Google Sheet with at least one sheet/tab containing:
  Column: Linkedin_URL_Person
  Column: row_number (used for mapping input and output rows)

Bright Data
A Bright Data account with access to the Dataset API
An active dataset that accepts LinkedIn URLs
API key with Dataset API access

Anthropic Claude
An Anthropic API key (for Claude 3.5 Haiku or other Claude models)

n8n Environment
Access to HTTP Request, Set, Wait, SplitInBatches, If, and Google Sheets nodes
Access to Claude integration (via LangChain nodes: @n8n/n8n-nodes-langchain)
Credential manager properly configured with:
  Google Sheets OAuth2 credentials
  Bright Data API key
  Anthropic API key

⚙️ Setup Instructions

Step 1: Copy the Google Sheets Template

&gt; 📄 Click here to make a copy

Fill the Linkedin_URL_Person column with LinkedIn profile URLs you want to enrich
Do not modify headers or add filters to the sheet
Leave other columns (name, city, about, posts, ice breaker) blank — the workflow fills them

Step 2: Connect Your Accounts in n8n

Google Sheets: Create a credential under Google Sheets OAuth2 API
Bright Data: Add your API key as a credential under HTTP Request (Authorization header)
Anthropic: Create a credential for Anthropic API with your Claude key

Step 3: Import and Configure the Workflow

Import the workflow into your n8n instance.
In each Google Sheets node:
   Select the copied Google Sheet
   Select the correct tab (usually input or Sheet1)
In the HTTP Request node to Bright Data:
   Paste your Bright Data dataset ID
In the Claude prompt node:
   Optionally adjust the tone and length of the ice breaker prompt

Step 4: Run the Workflow

Test it using the Manual Trigger node
For daily automation, enable the Schedule Trigger and configure interval settings
Watch your Google Sheet populate with enriched data and tailored ice breakers

🧠 Tips & Best Practices

Bright Data Delay**: Snapshots may take time. The workflow polls the status until complete.
Retry Protection**: If and Wait nodes avoid infinite loops by checking snapshot status.
Mapping via row_number**: Critical to ensure data is updated in the right row.
Prompt Engineering**: You can fine-tune Claude's behavior by editing the text prompt.

🧾 Output Example

Once complete, each row in your Google Sheet will contain:

| Linkedin_URL_Person | Name | City | Company | Recent Post | Ice Breaker |
|---------------------|------|------|---------|-------------|--------------|
| linkedin.com/... | Jane Doe | NYC | ACME Corp | “Why AI should replace meetings” | "Loved your post about AI and meetings — finally someone said it!" |

💬 Support & Feedback

Questions? Want to tweak the prompt or expand the enrichment?

📧 Email: Yaron@nofluff.online  
📺 YouTube: @YaronBeen  
🔗 LinkedIn: linkedin.com/in/yaronbeen



## Template JSON

```
{
  "meta": {
    "instanceId": "5aaf4236c70e34e423fbdb2c7b754d19253a933bb1476d548f75848a01e473cf"
  },
  "nodes": [
    {
      "id": "f3641141-a880-4400-bad7-909558848c20",
      "name": "When clicking \"Test workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        1880,
        580
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "7b1ddbd1-f918-4ef9-a05e-2c02e6de75df",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        340
      ],
      "parameters": {
        "color": 4,
        "width": 1289,
        "height": 2698,
        "content": "=======================================\n         WORKFLOW DETAILS & GUIDELINES\n=======================================\nName:\n    LinkedIn Enrichment & Ice Breaker Generator\n\nPurpose:\n    Automate the process of enriching LinkedIn profiles using Bright Data,\n    generate personalized ice breakers with an LLM, and update Google Sheets.\n\nTools Needed:\n    - n8n Nodes:\n        \u2022 Manual Trigger or Schedule Trigger\n        \u2022 Set\n        \u2022 SplitInBatches\n        \u2022 HTTP Request\n        \u2022 If\n        \u2022 Wait\n        \u2022 Google Sheets\n        \u2022 LangChain LLM (Claude via Anthropic)\n    - External Services:\n        \u2022 Bright Data (Dataset API)\n        \u2022 Anthropic Claude (Haiku)\n        \u2022 Google Sheets API\n\nAPI Keys & Authentication Required:\n    \u2022 Bright Data API Key\n        \u2192 Used in HTTP Request headers as:\n           `Authorization: Bearer YOUR_BRIGHTDATA_API_KEY`\n    \u2022 Google Sheets OAuth2 Credentials\n        \u2192 Connects n8n to your Google account for reading/writing to Sheets.\n    \u2022 Anthropic API Key\n        \u2192 Used for generating ice breakers via Claude models.\n        \u2192 Must be set in the Anthropic credential section in n8n.\n\nGeneral Guidelines:\n    \u2022 Use descriptive and consistent naming for all nodes.\n    \u2022 Add retry limits to polling loops to avoid infinite cycles.\n    \u2022 Ensure each LinkedIn URL maps to a unique `row_number`.\n    \u2022 Obfuscate any keys before sharing the workflow publicly.\n\nThings to be Aware Of:\n    \u2022 Bright Data may require some delay (via Wait node) before snapshot is ready.\n    \u2022 Retry logic should not exceed API rate limits.\n    \u2022 If snapshot fails or times out, ensure fallback logging is in place.\n    \u2022 Claude model IDs and prompt formats may change \u2014 validate before updates.\n\nAdditional Notes:\n    \u2022 Make a copy of the Google Sheet template before use.\n    \u2022 Replace placeholders in `Authorization` headers and credentials section.\n    \u2022 Use test data first to avoid exhausting API quotas during setup.\n\n=======================================\n\nThis workflow allows you to enrich LinkedIn profiles using Bright Data,\ngenerate AI-written ice breakers with Claude, and log everything into Google Sheets.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "215cd515-149b-41b1-adbe-fa203cbc9b5d",
      "name": "Get rows to enrich",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        2160,
        580
      ],
      "parameters": {
        "options": {},
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4/edit#gid=0",
          "cachedResultName": "input"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4/edit?usp=drivesdk",
          "cachedResultName": "NoFluff-N8N-Sheet-Template"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "5YFG2MAT8opHAtTt",
          "name": "Google Sheets account 2"
        }
      },
      "typeVersion": 4.3
    },
    {
      "id": "f140e851-6409-4169-b5af-28ab6f16d99c",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2840,
        440
      ],
      "parameters": {
        "width": 1420,
        "height": 460,
        "content": "Personal Data"
      },
      "typeVersion": 1
    },
    {
      "id": "8878ae56-0772-498a-b153-b628222f6688",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1840,
        440
      ],
      "parameters": {
        "width": 266.12865147126786,
        "height": 627.5654650079845,
        "content": "Run the workflow manually or activate it to run on schedule\n"
      },
      "typeVersion": 1
    },
    {
      "id": "df3f1f83-1092-40fe-bc5d-301e9a118601",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2120,
        220
      ],
      "parameters": {
        "width": 194.6864335083109,
        "height": 525.6560478822986,
        "content": "In this workflow, I use Google Sheets to store the results. \n\nYou can use my template to get started faster:\n\n1. [Click on this link to get the template](https://docs.google.com/spreadsheets/d/1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4/edit?usp=sharing)\n2. Make a copy of the Sheets\n3. Add the URL to this node and the node **\"Google Sheets - Update Row with data\"**\n\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "1c294196-206a-4add-8d47-8558ba99515d",
      "name": "Sticky Note9",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        0
      ],
      "parameters": {
        "color": 4,
        "width": 1280,
        "height": 320,
        "content": "=======================================\n            WORKFLOW ASSISTANCE\n=======================================\nFor any questions or support, please contact:\n    Yaron@nofluff.online\n\nExplore more tips and tutorials here:\n   - YouTube: https://www.youtube.com/@YaronBeen/videos\n   - LinkedIn: https://www.linkedin.com/in/yaronbeen/\n=======================================\n"
      },
      "typeVersion": 1
    },
    {
      "id": "3491b2bf-83a0-4966-9ff5-9c7c55f316e0",
      "name": "Anthropic Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatAnthropic",
      "position": [
        4420,
        1000
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "claude-3-5-haiku-20241022",
          "cachedResultName": "Claude 3.5 Haiku"
        },
        "options": {}
      },
      "credentials": {
        "anthropicApi": {
          "id": "FxW7H7jK9lF8qbdv",
          "name": "Anthropic account 2"
        }
      },
      "typeVersion": 1.3
    },
    {
      "id": "66b79bfc-3447-4b42-9617-308e490079bb",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        4340,
        640
      ],
      "parameters": {
        "width": 1120,
        "height": 580,
        "content": "ICE BREAKER\n"
      },
      "typeVersion": 1
    },
    {
      "id": "7557e53f-b898-4831-a52e-be9eeb0f4964",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2560,
        320
      ],
      "parameters": {
        "color": 4,
        "width": 2980,
        "height": 1000,
        "content": "LOOP"
      },
      "typeVersion": 1
    },
    {
      "id": "0119ee4c-bc70-4aef-84e0-881cdea57aa9",
      "name": "Basic LLM Chain- Ice Breaker",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        4540,
        660
      ],
      "parameters": {
        "text": "=Help me with writing a witty Ice breaker to try to persuade  {{ $json.name }} from{{ $('BrightData_Get_Linkedin').item.json.city }}. His About section in his Linkedin profile says:{{ $('BrightData_Get_Linkedin').item.json.about }}. \nHe also had a recent post about:{{ $('BrightData_Get_Linkedin').item.json.posts[0].title }}\n\nMake it 4 lines maximum. Focus more on his recent post, not the about. Just to make it feel personalized yet respectful and not creepy.\n\nWRITE THE ICE BREAKER Straight away. Dont write \"here's a draft\" or any other text before your actual response.",
        "promptType": "define"
      },
      "retryOnFail": true,
      "typeVersion": 1.6
    },
    {
      "id": "e3965132-4d21-4252-ab26-525128d79d29",
      "name": "BrightData_Get_Linkedin",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        3740,
        500
      ],
      "parameters": {
        "url": "=https://api.brightdata.com/datasets/v3/snapshot/{{ $json.snapshot_id }}",
        "options": {},
        "sendQuery": true,
        "sendHeaders": true,
        "queryParameters": {
          "parameters": [
            {
              "name": "format",
              "value": "json"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "Bearer <BRIGHT_DATA_API_KEY>"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "0e55b67e-7ddb-4431-8250-59be59c6c557",
      "name": "Adjust_input_for_loop",
      "type": "n8n-nodes-base.set",
      "position": [
        2360,
        580
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "fcc97354-b9f6-4459-a004-46e87902c77c",
              "name": "person_input",
              "type": "string",
              "value": "={{ $json.Linkedin_URL_Person }}"
            },
            {
              "id": "e5415c49-5204-45b1-a0e9-814157127b12",
              "name": "row_number",
              "type": "number",
              "value": "={{ $json.row_number }}"
            }
          ]
        }
      },
      "typeVersion": 3.3
    },
    {
      "id": "0cc85426-64f7-41f8-bd9a-215aaaad3299",
      "name": "HTTP_Request_Post_Request_BrightData",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        2920,
        500
      ],
      "parameters": {
        "url": "https://api.brightdata.com/datasets/v3/trigger",
        "method": "POST",
        "options": {},
        "jsonBody": "=[\n  {\n    \"url\": \"{{ $json.person_input }}\"\n  }\n]",
        "sendBody": true,
        "sendQuery": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "queryParameters": {
          "parameters": [
            {
              "name": "dataset_id",
              "value": "gd_l1viktl72bvl7bjuj0"
            },
            {
              "name": "include_errors",
              "value": "true"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "Bearer <BRIGHT_DATA_API_KEY>"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "851b23e0-6a1b-4a47-95e9-d2f769243a57",
      "name": "Wait_For_API_Call_Results",
      "type": "n8n-nodes-base.wait",
      "position": [
        3120,
        500
      ],
      "webhookId": "8005a2b3-2195-479e-badb-d90e4240e699",
      "parameters": {
        "amount": 10
      },
      "executeOnce": false,
      "typeVersion": 1.1
    },
    {
      "id": "294a7c03-2268-4d7a-b4e7-a52faa78d929",
      "name": "API_Call_Snapshot_Progress",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        3280,
        600
      ],
      "parameters": {
        "url": "=https://api.brightdata.com/datasets/v3/progress/{{ $json.snapshot_id }}",
        "options": {},
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "Bearer <Bright_Data_API_KEY>"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "d568403b-c323-4798-b7e5-e4a89dfe7830",
      "name": "IF-Checking_Status_API_Call",
      "type": "n8n-nodes-base.if",
      "position": [
        3480,
        660
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
              "id": "7932282b-71bb-4bbb-ab73-4978e554de7e",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $json.status }}",
              "rightValue": "running"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "b44b5f4b-8aef-4ea3-bbd7-1e72548dda64",
      "name": "Google Sheets - Update Row with data From API",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        4120,
        700
      ],
      "parameters": {
        "columns": {
          "value": {
            "city": "={{ $json.city }}",
            "name": "={{ $json.name }}",
            "about": "={{ $json.about }}",
            "row_number": "={{ $('Loop Over Items- All Prospects').item.json.row_number }}",
            "country_code": "={{ $json.country_code }}",
            "Linkedin_URL_Person": "={{ $json.input.url }}",
            "current_company.name": "={{ $json.current_company.name }}"
          },
          "schema": [
            {
              "id": "Linkedin_URL_Person",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Linkedin_URL_Person",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "name",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "city",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "city",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "country_code",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "country_code",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Position",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Position",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "about",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "about",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "current_company.name",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "current_company.name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Post 1",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Post 1",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Post 2",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Post 2",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Post 3",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Post 3",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Ice Breaker 1",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Ice Breaker 1",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Ice Breaker 2",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Ice Breaker 2",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "row_number",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": true,
              "required": false,
              "displayName": "row_number",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "row_number"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "update",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4/edit#gid=0",
          "cachedResultName": "input"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4/edit?usp=drivesdk",
          "cachedResultName": "NoFluff-N8N-Sheet-Template"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "5YFG2MAT8opHAtTt",
          "name": "Google Sheets account 2"
        }
      },
      "typeVersion": 4.3,
      "alwaysOutputData": true
    },
    {
      "id": "081f9e1d-6325-4645-bb0c-368a8ac3be99",
      "name": "Google Sheets - Update Row with Ice Breaker",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        5020,
        1000
      ],
      "parameters": {
        "columns": {
          "value": {
            "row_number": "={{ $('Loop Over Items- All Prospects').item.json.row_number }}",
            "Ice Breaker 1": "={{ $json.text }}"
          },
          "schema": [
            {
              "id": "Linkedin_URL_Person",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Linkedin_URL_Person",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "name",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "city",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "city",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "country_code",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "country_code",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Position",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Position",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "about",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "about",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "current_company.name",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "current_company.name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Post 1",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Post 1",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Post 2",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Post 2",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Post 3",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Post 3",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Ice Breaker 1",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "Ice Breaker 1",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Ice Breaker 2",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Ice Breaker 2",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "row_number",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": true,
              "required": false,
              "displayName": "row_number",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "row_number"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "update",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4/edit#gid=0",
          "cachedResultName": "input"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1_jbr5zBllTy_pGbogfGSvyv1_0a77I8tU-Ai7BjTAw4/edit?usp=drivesdk",
          "cachedResultName": "NoFluff-N8N-Sheet-Template"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "5YFG2MAT8opHAtTt",
          "name": "Google Sheets account 2"
        }
      },
      "typeVersion": 4.3,
      "alwaysOutputData": true
    },
    {
      "id": "7709c869-5283-4760-b929-fde27167f040",
      "name": "Run Workflow on a certain Schedule",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        1880,
        760
      ],
      "parameters": {
        "rule": {
          "interval": [
            {}
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "84e08531-b548-43f2-a17a-b2809f833d32",
      "name": "Loop Over Items- All Prospects",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        2600,
        480
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 3
    }
  ],
  "pinData": {},
  "connections": {
    "Get rows to enrich": {
      "main": [
        [
          {
            "node": "Adjust_input_for_loop",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Anthropic Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Basic LLM Chain- Ice Breaker",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Adjust_input_for_loop": {
      "main": [
        [
          {
            "node": "Loop Over Items- All Prospects",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "BrightData_Get_Linkedin": {
      "main": [
        [
          {
            "node": "Google Sheets - Update Row with data From API",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wait_For_API_Call_Results": {
      "main": [
        [
          {
            "node": "API_Call_Snapshot_Progress",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "API_Call_Snapshot_Progress": {
      "main": [
        [
          {
            "node": "IF-Checking_Status_API_Call",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF-Checking_Status_API_Call": {
      "main": [
        [
          {
            "node": "Wait_For_API_Call_Results",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "BrightData_Get_Linkedin",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Basic LLM Chain- Ice Breaker": {
      "main": [
        [
          {
            "node": "Google Sheets - Update Row with Ice Breaker",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When clicking \"Test workflow\"": {
      "main": [
        [
          {
            "node": "Get rows to enrich",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Loop Over Items- All Prospects": {
      "main": [
        [],
        [
          {
            "node": "HTTP_Request_Post_Request_BrightData",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Run Workflow on a certain Schedule": {
      "main": [
        [
          {
            "node": "Get rows to enrich",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP_Request_Post_Request_BrightData": {
      "main": [
        [
          {
            "node": "Wait_For_API_Call_Results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets - Update Row with Ice Breaker": {
      "main": [
        [
          {
            "node": "Loop Over Items- All Prospects",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets - Update Row with data From API": {
      "main": [
        [
          {
            "node": "Basic LLM Chain- Ice Breaker",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
