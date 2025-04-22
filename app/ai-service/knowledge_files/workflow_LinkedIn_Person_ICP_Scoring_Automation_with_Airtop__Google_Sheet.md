# LinkedIn Person ICP Scoring Automation with Airtop & Google Sheets

**[View Template](https://n8n.io/workflows/3476-/)**  **Published Date:** 04/08/2025  **Created By:** Cesar @ Airtop AI  **Categories:** `Data & Storage` `Productivity` `Development` `Core Nodes`  

## Template Description

About The ICP Person Scoring Automation

Sorting through lists of potential leads manually to determine who's truly worth your sales team's time isn't just tedious, it's incredibly inefficient. Without proper qualification, your team might spend hours pursuing prospects who aren't the right fit for your product, while ideal customers slip through the cracks.

How to Automate Identifying Your Ideal Customers

With this automation, you'll learn how to automatically score and prioritize leads using data extracted directly from LinkedIn profiles via Airtop's built-in integration with n8n. By the end, you'll have a fully automated workflow that analyzes prospects and calculates an Ideal Customer Profile (ICP) score, helping your sales team focus on high-potential opportunities.

What You'll Need

A free Airtop API key
A copy of this Google Sheets

Understanding the Process

This automation transforms how you qualify and prioritize leads by extracting real-time, accurate information directly from LinkedIn profiles. Unlike static databases that quickly become outdated, this workflow taps into the most current professional information available.

The workflow in this template:

Uses Airtop to extract comprehensive LinkedIn profile data
Analyzes the data to calculate an ICP score based on AI interest, technical depth, and seniority
Updates your Google Sheet with the enriched data and the ICP score

Person ICP Scoring Workflow

Our person-focused workflow evaluates individual LinkedIn profiles to determine how well they match your ideal customer profile by:

Extracting data for each individual
Analyzing  their profile to determine seniority and technical depth

The system then automatically calculates an ICP score based on the following criteria:

AI Interest: beginner-5 pts, intermediate-10 pts, advanced-25 pts, expert-35 pts
Technical Depth: basic-5 pts, intermediate-15 pts, advanced-25 pts, expert-35 pts
Seniority Level: junior-5 pts, mid-level-15 pts, senior-25 pts, executive-30 pts

Setting Up Your Automation

Here's how to get started:

Configure your connections

Connect your Google Sheets account
Add your Airtop API key (obtain from the Airtop dashboard)

Set up your Google Sheet

Ensure your Google Sheet has the necessary columns for input data and result fields
Ensure that columns Linkedin_URL_Person and ICP_Score_Person exist at least

Configure the Airtop module

Set up the Airtop module to use the appropriate LinkedIn extraction prompt
Use our provided prompt that extracts individual profile data

Customization Options

While our templates work out of the box, you might want to customize them for your specific needs:

Modify the ICP scoring criteria: Adjust the point values or add additional criteria specific to your business
Add notification triggers: Set up Slack or email notifications for high-value leads that exceed a certain ICP threshold
Implement batch processing: Modify the workflow to process leads in batches to optimize performance
Add conditional logic: Create different scoring models for different industries or product lines
Integrate with your CRM: Integrate this automation with your preferred CRM to get the details added automatically for you

Real-World Applications

Here's how businesses are using this automation:

AI Sales Platform: A B2B AI company could implement this workflow to process their trade show lead list of contacts. Within hours, they can identify the top 50 prospects based on ICP score.

SaaS Analytics Tool: A SaaS company could implement LinkedIn enrichment to identify which companies fit best. The automation processes weekly leads and categorizes them into high, medium, and low priority tiers, allowing their sales team to focus on the most promising opportunities first.

Best Practices

To get the most out of this automation:

Review and refine your ICP criteria quarterly: What constitutes an ideal customer may evolve as your product and market develop
Create tiered follow-up processes: Develop different outreach strategies based on ICP score ranges
Perform regular data validation: Periodically check the accuracy of the automated scoring against your actual sales results

What's Next?

Now that you've automated your ICP scoring with LinkedIn data, you might be interested in:

Setting up automated outreach sequences based on ICP score thresholds
Creating custom reporting dashboards to track conversion rates by ICP segment
Expanding your scoring model to include additional data sources
Implementing lead assignment automation based on ICP scores


Happy automating!

## Template JSON

```
{
  "meta": {
    "instanceId": "257476b1ef58bf3cb6a46e65fac7ee34a53a5e1a8492d5c6e4da5f87c9b82833"
  },
  "nodes": [
    {
      "id": "45ae6e88-3fda-4e95-84db-085a895cc564",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        260,
        -100
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "09f71a7c-1219-426d-8563-fa05654cab44",
      "name": "Calculate ICP PersonScoring",
      "type": "n8n-nodes-base.airtop",
      "position": [
        700,
        -100
      ],
      "parameters": {
        "url": "={{ $json['Linkedin_URL_Person'] }}",
        "prompt": "Please extract the following information from the LinkedIn profile page:\n\n1. **Full Name**: Extract the full name of the individual.\n2. **Current or Most Recent Job Title**: Identify the job title next to the logo of the current or last employer.\n3a. **Current or Most Recent Employer**: Extract the name of the first company in the employment experience block. \n3b. Linkedin Company URL of the Current or Most Recent Employer: Extract the link of the first company in the employment experience block\n4. **Location**: Extract the location of the individual.\n5. **Number of Connections**: Extract the number of connections the individual has.\n6. **Number of Followers**: Extract the number of followers the individual has.\n7. **About Section Text**: Extract the text from the 'About' section.\n8. **Interest Level in AI**: Determine the person's interest level in AI (e.g., beginner, intermediate, advanced, expert).\n9. **Seniority Level**: Determine the seniority level of the person (e.g., junior, mid-level, senior, executive).\n10. **Technical Depth**: Determine the technical depth of the person (e.g., basic, intermediate, advanced, expert).\n11. **ICP Score**: Calculate the ICP Score based on the following criteria:\n    - AI Interest: beginner-5 pts, intermediate-10 pts, advanced-25 pts, expert-35 pts\n    - Technical Depth: basic-5 pts, intermediate-15 pts, advanced-25 pts, expert-35 pts\n    - Seniority Level: junior-5 pts, mid-level-15 pts, senior-25 pts, executive-30 pts\n    - Sum the points to get the ICP Score.\n\nEnsure that the extracted information is accurate and formatted according to the specified output schema.\n\nFor example, if the LinkedIn profile is of a senior software engineer with a strong interest in AI, return the following output:\n{\n  \"full_name\": \"Jane Doe\",\n  \"current_or_last_employer\": \"Tech Innovations Inc.\",\n  \"current_or_last_title\": \"Senior Software Engineer\",\n  \"location\": \"San Francisco, CA\",\n  \"number_of_connections\": 500,\n  \"number_of_followers\": 300,\n  \"about_section_text\": \"Experienced software engineer with a passion for developing innovative programs that expedite the efficiency and effectiveness of organizational success.\",\n  \"ai_interest_level\": \"advanced\",\n  \"seniority_level\": \"senior\",\n  \"technical_depth\": \"advanced\",\n  \"icp_score\": 85\n}\n",
        "resource": "extraction",
        "operation": "query",
        "sessionMode": "new",
        "additionalFields": {
          "outputSchema": "{\n  \"type\": \"object\",\n  \"properties\": {\n    \"full_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the individual.\"\n    },\n    \"current_or_last_title\": {\n      \"type\": \"string\",\n      \"description\": \"The job title next to the logo of the current or last employer.\"\n    },\n    \"current_or_last_employer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first company in the employment experience block.\"\n    },\n    \"linkedin_company_url\": {\n      \"type\": \"string\",\n      \"description\": \"The LinkedIn URL of the first company in the employment experience block.\"\n    },\n    \"location\": {\n      \"type\": \"string\",\n      \"description\": \"The location of the individual.\"\n    },\n    \"number_of_connections\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of connections the individual has.\"\n    },\n    \"number_of_followers\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of followers the individual has.\"\n    },\n    \"about_section_text\": {\n      \"type\": \"string\",\n      \"description\": \"The text from the 'About' section.\"\n    },\n    \"ai_interest_level\": {\n      \"type\": \"string\",\n      \"description\": \"The person's interest level in AI.\"\n    },\n    \"seniority_level\": {\n      \"type\": \"string\",\n      \"description\": \"The seniority level of the person.\"\n    },\n    \"technical_depth\": {\n      \"type\": \"string\",\n      \"description\": \"The technical depth of the person.\"\n    },\n    \"icp_score\": {\n      \"type\": \"integer\",\n      \"description\": \"The ICP Score calculated based on AI interest, technical depth, and seniority level.\"\n    }\n  },\n  \"required\": [\n    \"full_name\",\n    \"current_or_last_title\",\n    \"current_or_last_employer\",\n    \"linkedin_company_url\",\n    \"location\",\n    \"number_of_connections\",\n    \"number_of_followers\",\n    \"about_section_text\",\n    \"ai_interest_level\",\n    \"seniority_level\",\n    \"technical_depth\",\n    \"icp_score\"\n  ],\n  \"additionalProperties\": false,\n  \"$schema\": \"http://json-schema.org/draft-07/schema#\"\n}\n"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "28c2c1d4-f43f-46c6-b21d-fbaf5fed4efa",
      "name": "Format response",
      "type": "n8n-nodes-base.code",
      "position": [
        900,
        -100
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "const row_number = $('Get person').item.json.row_number\nconst Linkedin_URL_Person = $('Get person').item.json.Linkedin_URL_Person\nconst ICP_Score_Person = JSON.parse($input.item.json.data.modelResponse).icp_score\n\nreturn { json: {\n  row_number,\n  Linkedin_URL_Person,\n  ICP_Score_Person\n}};"
      },
      "typeVersion": 2
    },
    {
      "id": "1646b60c-21f2-4222-bc4c-8660184fa46a",
      "name": "Update row",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1120,
        -100
      ],
      "parameters": {
        "columns": {
          "value": {},
          "schema": [
            {
              "id": "Linkedin_URL_Person",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Linkedin_URL_Person",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ICP_Score_Person",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "ICP_Score_Person",
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
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1WC_awgb-Ohtb0f4o_OJgRcvunTLuS8kFQgk6l8fkR2Q/edit#gid=0",
          "cachedResultName": "Person"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1WC_awgb-Ohtb0f4o_OJgRcvunTLuS8kFQgk6l8fkR2Q",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1WC_awgb-Ohtb0f4o_OJgRcvunTLuS8kFQgk6l8fkR2Q/edit?usp=drivesdk",
          "cachedResultName": "ICP Score for Template"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "5a151773-1075-4a9f-9637-6241e7137638",
      "name": "Get person",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        480,
        -100
      ],
      "parameters": {
        "options": {},
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1WC_awgb-Ohtb0f4o_OJgRcvunTLuS8kFQgk6l8fkR2Q/edit#gid=0",
          "cachedResultName": "Person"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1WC_awgb-Ohtb0f4o_OJgRcvunTLuS8kFQgk6l8fkR2Q",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1WC_awgb-Ohtb0f4o_OJgRcvunTLuS8kFQgk6l8fkR2Q/edit?usp=drivesdk",
          "cachedResultName": "ICP Score for Template"
        }
      },
      "typeVersion": 4.5
    }
  ],
  "pinData": {},
  "connections": {
    "Get person": {
      "main": [
        [
          {
            "node": "Calculate ICP PersonScoring",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format response": {
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
    "Calculate ICP PersonScoring": {
      "main": [
        [
          {
            "node": "Format response",
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
            "node": "Get person",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
