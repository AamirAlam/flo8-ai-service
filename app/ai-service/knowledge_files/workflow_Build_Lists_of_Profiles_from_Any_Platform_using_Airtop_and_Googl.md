# Build Lists of Profiles from Any Platform using Airtop and Google Sheets

**[View Template](https://n8n.io/workflows/3479-/)**  **Published Date:** 04/08/2025  **Created By:** Cesar @ Airtop AI  **Categories:** `Data & Storage` `Productivity` `Development` `Core Nodes`  

## Template Description

About The List Building Automation

This automation will guide you on how to automate list building using Airtop. You’ll have a streamlined workflow that can reduce your research time by up to 90% while improving the accuracy of your target lists.

How to automate list building

It can be challenging to spend too much time on tasks like compiling lists of potential investors, customers, job candidates, industry influencers, or key decision-makers. Verifying contact details often requires significant effort, whether building an outreach list, tracking thought leaders, or researching potential customers. Not anymore. With Airtop's List Building Automation, turn hours of tedious research into clean, reliable and accurate lists, built in just minutes. 

Check this out:

What You'll Need

A free Airtop API Key
Target audience parameters (persona and which network. i.e. "AI Influencers on LinkedIn)
Make a copy of this template to start

Understanding the Process

This automation leverages Airtop's advanced data processing capabilities powered by AI to scan multiple unstructured sources and compile accurate, targeted lists based on your specific requirements. The magic lies in its ability to understand context and verify information across different platforms.

This workflow:
 Handles multi-source data collection and consolidation
 Manages automatic verification of social profiles and domains
 Automates the filtering and ranking of results based on relevance

Setting Up Your Automation

Enter your search criteria in the "Parameters" node:
    Who: Your target audience (e.g., "Angel investors in Europe," "Top AI influencers")
    Where: The platform or domain to focus on (e.g., "LinkedIn," "TikTok") 
Configure your Airtop API Key
    Create one for free at the Airtop Portal
 In the last node, select the spreadsheet that you copied earlier
 Run the workflow

Customization Options

While our template works out of the box, you might want to customize it for your specific needs:

Add custom filtering criteria for more targeted results
Implement automatic data enrichment from additional sources
Set up automatic exports to your preferred CRM or database

Real-World Applications

Here's how businesses can use this automation:

A VC firm could use this automation to build a comprehensive EU angel investors database. What previously required their analysts to work 15 hours per week now runs automatically in the background, providing fresh leads daily.

A PR agency could automate its influencer discovery process across multiple platforms, reducing its research time from 10 hours to 30 minutes per client while increasing the relevance of its outreach lists.

Best Practices

To get the most out of this automation:

Start with specific, well-defined parameters to ensure relevant results
Regularly update your parameters to keep your lists fresh and relevant
Combine multiple runs with different parameters for comprehensive coverage

What's Next?

Now that you've automated your list building, you might be interested in:

Setting up automated outreach sequences
Creating dynamic lead scoring systems
Implementing automatic list updating and maintenance

Happy automating!


## Template JSON

```
{
  "id": "VwU1zMhcgzgPS9ak",
  "meta": {
    "instanceId": "660cf2c29eb19fa42319afac3bd2a4a74c6354b7c006403f6cba388968b63f5d",
    "templateCredsSetupCompleted": true
  },
  "name": "List Builder",
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
      "id": "1a6aa574-467d-40b0-a9a5-a5537bede3de",
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
      "id": "62db9366-7e6f-4346-9de8-9fa730d059ed",
      "name": "Format results",
      "type": "n8n-nodes-base.code",
      "position": [
        660,
        0
      ],
      "parameters": {
        "jsCode": "// Get first input item\nconst input = $input.first().json.data.modelResponse\n// Parse list of links\nconst listOfLinks = JSON.parse(input).results\n// Format node's output\nconst output = listOfLinks.map((item) => ({\n  json: { url: item.url }\n}))\n\nreturn output;"
      },
      "typeVersion": 2
    },
    {
      "id": "fa960de3-8dd6-40a3-aa59-634ad250f5d1",
      "name": "Get urls",
      "type": "n8n-nodes-base.airtop",
      "position": [
        440,
        0
      ],
      "parameters": {
        "url": "=https://www.google.com/search?q={{ encodeURI($json.who+' on ' + $json.where) }}",
        "prompt": "=Those are search results, return up to 10 non-sponsored results that lead to a web page with a list of {{$json.who}} on {{$json.where}}. For each return the title and URL.",
        "resource": "extraction",
        "operation": "query",
        "sessionMode": "new",
        "additionalFields": {
          "outputSchema": "{  \"type\": \"object\",  \"properties\": {    \"results\": {      \"type\": \"array\",      \"items\": {        \"type\": \"object\",        \"properties\": {          \"title\": {            \"type\": \"string\",            \"description\": \"The title of the search result.\"          },          \"url\": {            \"type\": \"string\",            \"description\": \"The URL of the webpage.\"          }        },        \"required\": [          \"title\",          \"url\"        ],        \"additionalProperties\": false      },      \"description\": \"A list of up to 10 non-sponsored search results.\"    }  },  \"required\": [    \"results\"  ],  \"additionalProperties\": false,  \"$schema\": \"http://json-schema.org/draft-07/schema#\"}"
        }
      },
      "credentials": {
        "airtopApi": {
          "id": "byhouJF8RLH5DkmY",
          "name": "Airtop"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "d75dbdce-7a7e-4a30-81b0-6e8fa5221f55",
      "name": "Get people",
      "type": "n8n-nodes-base.airtop",
      "position": [
        880,
        0
      ],
      "parameters": {
        "url": "={{ $json.url }}",
        "prompt": "=This is a list of {{ $('Parameters').item.json.who }} on {{ $('Parameters').item.json.where }}.\nExtract up to 20 items. For each person extract: \n- name \n- handle or ID \n- URL",
        "resource": "extraction",
        "operation": "query",
        "sessionMode": "new",
        "additionalFields": {
          "outputSchema": "{\n  \"$schema\": \"http://json-schema.org/draft-07/schema#\",\n  \"type\": \"object\",\n  \"properties\": {\n    \"items\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the item.\"\n          },\n          \"identifier\": {\n            \"type\": \"string\",\n            \"description\": \"The unique identifier or handle for the item.\"\n          },\n          \"url\": {\n            \"type\": \"string\",\n            \"description\": \"The URL to access the item or its related resource.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"identifier\",\n          \"url\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"items\"\n  ],\n  \"additionalProperties\": false\n}"
        }
      },
      "credentials": {
        "airtopApi": {
          "id": "byhouJF8RLH5DkmY",
          "name": "Airtop"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "285ce6af-bda8-4025-872e-f5f8c4a56b3c",
      "name": "Dedupe results",
      "type": "n8n-nodes-base.code",
      "position": [
        1100,
        0
      ],
      "parameters": {
        "jsCode": "const allResults = []\n\nfor (const inputItem of $input.all()) {\n  // Parse input to JSON\n  const input = inputItem.json.data.modelResponse\n  const results = JSON.parse(input).items\n  // clean results\n  const cleanedResults = results\n    .filter((res) => res.name) // only those with name\n    .map((res) => ({\n      ...res,\n      url: res.url.split('?')[0] // clean url\n    }))\n  // add results to list\n  allResults.push(...cleanedResults)\n}\n\n// Dedupe urls\nconst uniqueList = allResults.filter((item, index, self) =>\n  index === self.findIndex((t) => (t.url === item.url))\n);\n\nreturn uniqueList.map((item) => ({\n  json: {...item}\n}));"
      },
      "typeVersion": 2
    },
    {
      "id": "fdc86d5c-4df3-48b9-9cf6-a5ddc3b45c90",
      "name": "Add to spreadsheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1320,
        0
      ],
      "parameters": {
        "columns": {
          "value": {
            "URL": "={{ $json.url }}",
            "Name": "={{ $json.name }}",
            "Who?": "={{ $('Parameters').first().json.who }}",
            "Where?": "={{ $('Parameters').first().json.where }}",
            "Added on": "={{ $now }}",
            "ID or Handle": "={{ $json.identifier }}"
          },
          "schema": [
            {
              "id": "Who?",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Who?",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Where?",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Where?",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Name",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Name",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "ID or Handle",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "ID or Handle",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "URL",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "URL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Added on",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Added on",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "append",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/150eh4t5GyEBN_TcO5TDeNWpE2GzHR4hQWoNRbUpw7A0/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "150eh4t5GyEBN_TcO5TDeNWpE2GzHR4hQWoNRbUpw7A0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/150eh4t5GyEBN_TcO5TDeNWpE2GzHR4hQWoNRbUpw7A0/edit?usp=drivesdk",
          "cachedResultName": "List Builder"
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
      "id": "44c54497-741c-4c48-b4f9-0c5c836d10ad",
      "name": "Parameters",
      "type": "n8n-nodes-base.set",
      "position": [
        220,
        0
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "bc2d3cb9-b7d0-4c3f-b392-53262d60441e",
              "name": "who",
              "type": "string",
              "value": "Top \"Build in Public\" influencers"
            },
            {
              "id": "b2cfa361-c80a-4945-bc0e-23eac5edebd6",
              "name": "where",
              "type": "string",
              "value": "X"
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
  "versionId": "a2572aec-54cb-4bbb-b503-09d1d0beb64f",
  "connections": {
    "Get urls": {
      "main": [
        [
          {
            "node": "Format results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get people": {
      "main": [
        [
          {
            "node": "Dedupe results",
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
            "node": "Get urls",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Dedupe results": {
      "main": [
        [
          {
            "node": "Add to spreadsheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format results": {
      "main": [
        [
          {
            "node": "Get people",
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
