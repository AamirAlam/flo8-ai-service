# Scrape Latest Github Trending Repositories

**[View Template](https://n8n.io/workflows/2866-/)**  **Published Date:** 02/08/2025  **Created By:** Teddy  **Categories:** `Development` `Core Nodes`  

## Template Description

Scrape Latest 20 TechCrunch Articles

Who is this for?
This workflow is designed for developers, researchers, and data analysts who need to track the latest trending repositories on GitHub. It is useful for anyone who wants to stay updated on popular open-source projects without manually browsing GitHub’s trending page.

What problem is this workflow solving?
Manually checking GitHub’s trending repositories daily can be time-consuming and inefficient. This workflow automates the extraction of trending repositories, providing structured data including repository name, author, description, programming language, and direct repository links. 

What this workflow does
This workflow scrapes the trending repositories from GitHub’s trending page and extracts essential metadata such as repository names, languages, descriptions, and URLs. It processes the extracted data and structures it into an easy-to-use format.

Setup
Ensure you have n8n installed and configured.
Import this workflow into your n8n instance.
Run the workflow manually or schedule it to execute at regular intervals.
(Optional) Customize the extracted data or integrate it with other systems.

How to customize this workflow to your needs
Modify the HTTP request node to target different GitHub trending categories (e.g., specific programming languages).
Add further processing steps such as filtering repositories by stars, forks, or specific keywords.
Integrate this workflow with Slack, email, or a database to store or notify about trending repositories.

Workflow Steps
Trigger execution manually using the "When clicking ‘Test workflow’" node.
Send an HTTP request to fetch GitHub’s trending page using "Request to Github Trend".
Extract the trending repositories box from the HTML response using "Extract Box".
Extract all repository data including names, authors, descriptions, and languages using "Extract all repositories".
Convert extracted data into a structured list for easier processing using "Turn to a list".
Extract detailed repository information using "Extract repository data".
Format and set variables to ensure clean and structured data output using "Set Result Variables".

Note: Since GitHub’s trending page updates dynamically, ensure you run this workflow periodically to capture the latest trends.


## Template JSON

```
{
  "id": "BXfxO6faULfsy2JN",
  "meta": {
    "instanceId": "0b0f5302e78710cf1b1457ee15a129d8e5d83d4e366bd96d14cc37da6693e692"
  },
  "name": "Scrape Today's Github Trend 13 Top Repositories",
  "tags": [],
  "nodes": [
    {
      "id": "e2981cad-c09b-46ee-b2db-cb007a95c4a1",
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
      "id": "990de0c9-f540-4a10-8a1a-63a0526444ff",
      "name": "Extract Box",
      "type": "n8n-nodes-base.html",
      "position": [
        440,
        0
      ],
      "parameters": {
        "options": {},
        "operation": "extractHtmlContent",
        "extractionValues": {
          "values": [
            {
              "key": "box",
              "cssSelector": "div.Box",
              "returnValue": "html"
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "7f7968ce-3935-488e-98f9-7ddd270d14b0",
      "name": "Request to Github Trend",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        220,
        0
      ],
      "parameters": {
        "url": "https://github.com/trending",
        "options": {}
      },
      "typeVersion": 4.2
    },
    {
      "id": "87cd7fa1-d896-49a3-9336-17663ca522aa",
      "name": "Turn to a list",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        880,
        0
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "repositories"
      },
      "typeVersion": 1
    },
    {
      "id": "bed61dad-0066-45de-bcf2-79fd143e360c",
      "name": "Set Result Variables",
      "type": "n8n-nodes-base.set",
      "position": [
        1320,
        0
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "a0e76646-60d7-44a6-af77-33f27fb465cb",
              "name": "author",
              "type": "string",
              "value": "={{ $json.repository.split('/')[0].trim() }}"
            },
            {
              "id": "a2bd790a-784e-4d72-9a4e-92be22edea8f",
              "name": "title",
              "type": "string",
              "value": "={{ $json.repository.split('/')[1].trim() }}"
            },
            {
              "id": "22f1518a-7081-4417-ab9d-88f26a7b5cfe",
              "name": "repository",
              "type": "string",
              "value": "={{ $json.repository }}"
            },
            {
              "id": "baff9a9f-020a-4968-bb80-a4a91a94144a",
              "name": "url",
              "type": "string",
              "value": "=https://github.com/{{ $json.repository.replaceAll(' ','') }}"
            },
            {
              "id": "f5c48a02-b55d-4167-a823-53ac1d851ee5",
              "name": "created_at",
              "type": "string",
              "value": "={{$now}}"
            },
            {
              "id": "27a44ce9-4b5b-44b2-94d9-eb5b2ae81dcd",
              "name": "description",
              "type": "string",
              "value": "={{ $json.description }}"
            }
          ]
        },
        "includeOtherFields": "="
      },
      "typeVersion": 3.4
    },
    {
      "id": "d7b39e99-38df-4025-9afd-a602c4bd01cf",
      "name": "Extract repository data",
      "type": "n8n-nodes-base.html",
      "position": [
        1100,
        0
      ],
      "parameters": {
        "options": {},
        "operation": "extractHtmlContent",
        "dataPropertyName": "repositories",
        "extractionValues": {
          "values": [
            {
              "key": "repository",
              "cssSelector": "a.Link"
            },
            {
              "key": "language",
              "cssSelector": "span.d-inline-block"
            },
            {
              "key": "description",
              "cssSelector": "p"
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "382e7a3b-f65f-4a79-a69f-2818f09f5daa",
      "name": "Extract all repositories",
      "type": "n8n-nodes-base.html",
      "position": [
        660,
        0
      ],
      "parameters": {
        "options": {
          "trimValues": true,
          "cleanUpText": true
        },
        "operation": "extractHtmlContent",
        "dataPropertyName": "box",
        "extractionValues": {
          "values": [
            {
              "key": "repositories",
              "cssSelector": "article.Box-row",
              "returnArray": true,
              "returnValue": "html"
            }
          ]
        }
      },
      "typeVersion": 1.2
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "33ada4c0-b6ad-4ad6-bee8-51b630908c04",
  "connections": {
    "Extract Box": {
      "main": [
        [
          {
            "node": "Extract all repositories",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Turn to a list": {
      "main": [
        [
          {
            "node": "Extract repository data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract repository data": {
      "main": [
        [
          {
            "node": "Set Result Variables",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Request to Github Trend": {
      "main": [
        [
          {
            "node": "Extract Box",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract all repositories": {
      "main": [
        [
          {
            "node": "Turn to a list",
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
            "node": "Request to Github Trend",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
