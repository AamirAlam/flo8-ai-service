# Automated LinkedIn Profile Discovery with Airtop and Google Search

**[View Template](https://n8n.io/workflows/3477-/)**  **Published Date:** 04/08/2025  **Created By:** Cesar @ Airtop AI  **Categories:** `Data & Storage` `Productivity` `Development` `Core Nodes`  

## Template Description

About The LinkedIn Profile Discovery Automation

Are you tired of manually searching for LinkedIn profiles or paying expensive data providers for often outdated information? If you spend countless hours trying to find accurate LinkedIn URLs for your prospects or candidates, this automation will change your workflow forever. Just give this workflow the information you have about a contact, and it will automatically augment it with a LinkedIn profile.

How to find a LinkedIn Profile Link

In this guide, you'll learn how to automate LinkedIn profile link discovery using Airtop's built-in node in n8n. Using this automation, you'll have a fully automated workflow that saves you hours of manual searching while providing accurate, validated LinkedIn URLs.

What You'll Need

A free Airtop API key
A Google Workspace account. If you have a Gmail account, you’re all set
Estimated setup time: 10 minutes

Understanding the Process

This automation leverages the power of intelligent search algorithms combined with LinkedIn validation to ensure accuracy. Here's how it works:

Takes your input data (name, company, etc.) and constructs intelligent search queries
Utilizes Google search to identify potential LinkedIn profile URLs
Validates the discovered URLs directly against LinkedIn to ensure accuracy
Returns confirmed, accurate LinkedIn profile URLs

Setting Up Your Automation

Getting started with this automation is straightforward:

Prepare Your Google Sheet

Create a new Google Sheet with columns for input data (name, company, domain, etc.)
Add columns for the output LinkedIn URL and validation status (see this example)

Configure the Automation

Connect your Google Workspace account to n8n if you haven't already
Add your Airtop API credentials
(Optionally) Configure your Airtop Profile and sign-in to LinkedIn in order to validate profile URL's

Run Your First Test

Add a few test entries to your Google Sheet
Run the workflow
Check the results in your output columns

Customization Options

While the default setup uses Google Sheets, this automation is highly flexible:

Webhook Integration**: Perfect for integrating with tools like Clay, Instantly, or your custom applications
Alternatives**: Replace Google Sheets with Airtable, Notion, or any other tools you already use for more robust database capabilities
Custom Output Formatting**: Modify the output structure to match your existing systems
Batch Processing**: Configure for bulk processing of multiple profiles

Real-World Applications

This automation has the potential to transform how we organizations handle profile enrichment.

Recruiting Firm Success Story

With this automation, a recruiting firm could save hundreds of dollars a month in data enrichment fees, achieve better accuracy, and eliminate subscription costs. They would also be able to process thousands of profiles weekly with near-perfect accuracy.

Sales Team Integration

A B2B sales team could integrate this automation with their CRM, automatically enriching new leads with validated LinkedIn profiles and saving their SDRs hours per week on manual research.

Best Practices

To maximize the accuracy of your results:

Always include company information (domain or company name) with your search queries
Use full names rather than nicknames or initials when possible
Consider including location data for more accurate results with common names
Implement rate limiting to respect LinkedIn's usage guidelines
Keep your input data clean and standardized for best results
Use the integrated proxy to navigate more effectively through Google and LinkedIn

What's Next?

Now that you've automated LinkedIn profile discovery, consider exploring related automations:

Automated lead scoring based on LinkedIn profile data
Email finder automation using validated LinkedIn profiles
Integration with your CRM for automated contact enrichment


## Template JSON

```
{
  "id": "lifB7iUXlDzr5dmI",
  "meta": {
    "instanceId": "660cf2c29eb19fa42319afac3bd2a4a74c6354b7c006403f6cba388968b63f5d",
    "templateCredsSetupCompleted": true
  },
  "name": "LinkedIn Profile Discovery",
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
      "id": "9ae64a3a-c7e7-45ca-88ee-ebf6144f3197",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        0,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "a22416bb-ef9e-422f-b480-cd52d8c93bfa",
      "name": "Person info",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        220,
        0
      ],
      "parameters": {
        "options": {},
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1rjlKzphEbknNh_ToS9pR_dP_Tw93FsxDte5AI4LH5_E/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1rjlKzphEbknNh_ToS9pR_dP_Tw93FsxDte5AI4LH5_E",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1rjlKzphEbknNh_ToS9pR_dP_Tw93FsxDte5AI4LH5_E/edit?usp=drivesdk",
          "cachedResultName": "Linkedin Profile URLs"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "CwpCAR1HwgHZpRtJ",
          "name": "Google Drive"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "a4699dd8-54ef-478e-9ff8-2c2046ad6ea8",
      "name": "Search profile",
      "type": "n8n-nodes-base.airtop",
      "notes": "This could take a few minutes depending on the number of rows",
      "position": [
        440,
        0
      ],
      "parameters": {
        "url": "=https://www.google.com/search?q={{ encodeURI($json['Person Info']) }}",
        "prompt": "=This is Google Search results. the first results should be the Linkedin Page of {{ $json['Person Info'] }} \nReturn the Linkedin URL and nothing else.\nIf you cannot find the Linkedin URL, return an empty string. \nA valid Linkedin profile URL starts with \"https://www.linkedin.com/in/\"",
        "resource": "extraction",
        "operation": "query",
        "sessionMode": "new",
        "additionalFields": {}
      },
      "credentials": {
        "airtopApi": {
          "id": "byhouJF8RLH5DkmY",
          "name": "Airtop"
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "2dd4d350-743e-48a7-ab69-d0996bc46f49",
      "name": "Parse response",
      "type": "n8n-nodes-base.code",
      "position": [
        660,
        0
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "const linkedInProfile = $json.data.modelResponse\nconst rowData = $('Person info').item.json\n\nreturn { json: {\n  ...rowData,\n  'LinkedIn URL': linkedInProfile\n}};"
      },
      "typeVersion": 2
    },
    {
      "id": "3efc182a-8707-4c8d-8263-a2aebe62b0a7",
      "name": "Update row",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        880,
        0
      ],
      "parameters": {
        "columns": {
          "value": {},
          "schema": [
            {
              "id": "Person Info",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Person Info",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Linkedin URL",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Linkedin URL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Validated",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Validated",
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
          "mappingMode": "autoMapInputData",
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
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1rjlKzphEbknNh_ToS9pR_dP_Tw93FsxDte5AI4LH5_E/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1rjlKzphEbknNh_ToS9pR_dP_Tw93FsxDte5AI4LH5_E",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1rjlKzphEbknNh_ToS9pR_dP_Tw93FsxDte5AI4LH5_E/edit?usp=drivesdk",
          "cachedResultName": "Linkedin Profile URLs"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "CwpCAR1HwgHZpRtJ",
          "name": "Google Drive"
        }
      },
      "typeVersion": 4.5
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "97cd5141-63d5-4ece-83eb-e544455097d3",
  "connections": {
    "Person info": {
      "main": [
        [
          {
            "node": "Search profile",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parse response": {
      "main": [
        [
          {
            "node": "Update row",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Search profile": {
      "main": [
        [
          {
            "node": "Parse response",
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
            "node": "Person info",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
