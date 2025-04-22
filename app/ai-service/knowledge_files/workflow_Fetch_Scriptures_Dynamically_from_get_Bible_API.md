# Fetch Scriptures Dynamically from get Bible API

**[View Template](https://n8n.io/workflows/2818-/)**  **Published Date:** 01/29/2025  **Created By:** getBible  **Categories:** `Development` `Core Nodes`  

## Template Description

Overview
The Get Bible Query Workflow is a modular and self-standing workflow designed to retrieve scriptures dynamically based on structured input. It serves as an intermediary layer that extracts references, queries the GetBible API, and returns scriptures in a standardized JSON format.

This workflow is fully prepared for integration—simply call it from another workflow with the required JSON input, and it will return the requested scripture data.

Who Is This For?
This workflow is ideal for developers, Bible study apps, research tools, and dynamic scripture-based projects that need seamless access to scriptural content without direct API interaction.

✅ Use Cases:
Bible Study Apps** → Embed scripture retrieval functionality.
Research & Theology Tools** → Fetch structured verse data.
Dynamic Content Generation** → Integrate real-time scripture references.
Sermon Preparation** → Automate scripture lookups.

How It Works
Trigger Workflow → This workflow is designed to be called from another workflow with a structured JSON input.
Receive Input → Accepts a JSON object containing references, translation, and API version.
Extract References → Parses single verses, comma-separated lists, and ranged passages.
Query API → Sends structured requests to the GetBible API.
Format Response → Returns structured JSON output, maintaining API response consistency.

JSON Input Structure
References** → Should include the book name, chapter, and verse(s).
Multiple Verses** → Separated by commas (e.g., John 3:16,18).
Verse Ranges** → Defined with a dash (e.g., John 3:16-18).
Translation** → Choose from the supported translations.
API Version** → Currently supports v2.

Example JSON Input
{
  "references": [
    "1 John 3:16",
    "Jn 3:16",
    "James 3:16",
    "Rom 3:16"
  ],
  "translation": "kjv",
  "version": "v2"
}

Example API Response
{
  "result": {
    "kjv_62_3": {
      "translation": "King James Version",
      "abbreviation": "kjv",
      "book_name": "1 John",
      "chapter": 3,
      "ref": ["1 John 3:16"],
      "verses": [
        {
          "chapter": 3,
          "verse": 16,
          "name": "1 John 3:16",
          "text": "Hereby perceive we the love of God, because he laid down his life for us: and we ought to lay down our lives for the brethren."
        }
      ]
    }
  }
}

💡 Fully structured and formatted response – ready for seamless integration.

Integration and Usage
The GetBible Query Workflow is designed for immediate use. Simply call it from another workflow and pass the appropriate JSON object as input, and it will return the requested scripture passages.

✔️ No additional configuration is required.
✔️ Designed for fast, reliable, and structured scripture retrieval.
✔️ Fully compatible with GetBible API responses.

Why Use This Workflow?
✔️ Fast & Reliable → Direct API integration for efficient queries.
✔️ Flexible Queries → Supports single, multi-verse, and ranged requests.
✔️ Agent-Compatible → Easily integrates into automated workflows.
✔️ No Code Needed → Just configure the JSON input and run the workflow.

Next Steps
🔗 API Support
📖 API Documentation
💬 Need help? Join the community for support! 🚀

## Template JSON

```
{
  "id": "gqwYlZvL1dwy9W3T",
  "meta": {
    "templateCredsSetupCompleted": true
  },
  "name": "getBible Query v1.0",
  "tags": [],
  "nodes": [
    {
      "id": "37e21e75-6f18-45fc-9b74-860c1e095b83",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -880,
        -320
      ],
      "parameters": {
        "width": 780,
        "height": 1720,
        "content": "# GetBible Query Workflow Documentation\n\n## Overview\n\nThe **GetBibleQuery** workflow is a modular and self-standing workflow designed to retrieve scriptures based on provided references. It serves as an intermediary layer that takes in a structured JSON object, extracts the references, and returns the corresponding scriptures in the same format as if they were retrieved directly from the API.\n\nThis workflow is highly adaptable and can be integrated into various projects where scriptural references need to be dynamically fetched.\n\n## JSON Input Structure\n\nThe workflow expects a JSON object with the following parameters:\n\n - References should include the book name, chapter, and verse(s). \n - Multiple verses can be separated by commas (e.g., `John 3:16,18`).\n - Ranges can be specified using a dash (e.g., `John 3:16-18`).\n - The Bible [translation](https://api.getbible.net/v2/translations.json) to be used.\n - Specifies the API version (v2)\n\n### Example JSON Input:\n\n```json\n{\n  \"references\": [\n      \"1 John 3:16\",\n      \"Jn 3:16\",\n      \"James 3:16\",\n      \"Rom 3:16\"\n  ],\n  \"translation\": \"kjv\",\n  \"version\": \"v2\"\n}\n```\n\n### API Response Format\n\nThe response returned by this workflow follows the same API format as if the request were made directly to the source API. This ensures compatibility with projects that rely on standard API responses.\n\nExample JSON Response (in this workflow):\n```json\n{\n  \"result\": {\n    \"kjv_62_3\": {\n      \"translation\": \"King James Version\",\n      \"abbreviation\": \"kjv\",\n      \"lang\": \"en\",\n      \"language\": \"English\",\n      \"direction\": \"LTR\",\n      \"encoding\": \"UTF-8\",\n      \"book_nr\": 62,\n      \"book_name\": \"1 John\",\n      \"chapter\": 3,\n      \"name\": \"1 John 3\",\n      \"ref\": [\n        \"1 John 3:16\"\n      ],\n      \"verses\": [\n        {\n          \"chapter\": 3,\n          \"verse\": 16,\n          \"name\": \"1 John 3:16\",\n          \"text\": \"Hereby perceive we the love of God, because he laid down his life for us: and we ought to lay down our lives for the brethren.\"\n        }\n      ]\n    }\n  }\n}\n```\n\n## Integration and Usage\n\nThe GetBible Query workflow is designed for easy integration into any project that requires scripture retrieval. Simply pass the appropriate JSON object as input, and it will return the requested scripture passages.\n\n## Support\n\nFor any questions or additional assistance, please visit our [Support desk](https://git.vdm.dev/getBible/support) or [API documentation](https://getbible.net/docs)"
      },
      "typeVersion": 1
    },
    {
      "id": "8d5da846-fd1b-48f6-8199-2f9a3a4c99b5",
      "name": "Entry",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        0,
        0
      ],
      "parameters": {
        "inputSource": "jsonExample",
        "jsonExample": "{\n  \"references\": [\n      \"1 John 3:16\",\n      \"Jn 3:16\",\n      \"James 3:16\",\n      \"Rom 3:16\"\n  ],\n  \"translation\": \"kjv\",\n  \"version\": \"v2\"\n}"
      },
      "typeVersion": 1.1
    },
    {
      "id": "17444cd4-4ec3-4d8f-9f9d-29369632c420",
      "name": "ModelJson",
      "type": "n8n-nodes-base.code",
      "position": [
        220,
        0
      ],
      "parameters": {
        "jsCode": "// Loop over input items and process the 'references' field\nfor (let item of $input.all()) {\n  // Check if 'references' exists and is an array\n  if (Array.isArray(item.json.references)) {\n    item.json.references = item.json.references.join('; ');\n  } else {\n    // Handle cases where 'references' is missing or not an array\n    item.json.references = 'John 3:16';\n  }\n}\n\n// Return the modified items\nreturn $input.all();"
      },
      "executeOnce": true,
      "retryOnFail": false,
      "typeVersion": 2,
      "alwaysOutputData": true
    },
    {
      "id": "b392423f-22d7-4b3f-8e25-9c703c33c78d",
      "name": "API Query to GetBible",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        460,
        0
      ],
      "parameters": {
        "url": "=https://query.getbible.net/{{ $json.version || 'v2' }}/{{ $json.translation || 'kjv' }}/{{ $json.references }}",
        "options": {}
      },
      "executeOnce": false,
      "typeVersion": 4.2,
      "alwaysOutputData": false
    },
    {
      "id": "e55d8b82-a30a-4ed9-a28f-ae2d9808422c",
      "name": "Map API Respons to Result",
      "type": "n8n-nodes-base.set",
      "position": [
        680,
        0
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "360a59c4-5e4c-43b8-8b0b-bb121054a709",
              "name": "result",
              "type": "object",
              "value": "={{ $json }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    }
  ],
  "pinData": {
    "Entry": [
      {
        "json": {
          "version": "v2",
          "references": [
            "1 John 3:16",
            "Jn 3:16",
            "James 3:16",
            "Rom 3:16"
          ],
          "translation": "kjv"
        }
      }
    ]
  },
  "settings": {
    "callerPolicy": "workflowsFromSameOwner",
    "executionOrder": "v1",
    "saveExecutionProgress": false
  },
  "versionId": "c8a37d01-c65f-4975-878a-20ed73c42b6b",
  "staticData": null,
  "connections": {
    "Entry": {
      "main": [
        [
          {
            "node": "ModelJson",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "ModelJson": {
      "main": [
        [
          {
            "node": "API Query to GetBible",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "API Query to GetBible": {
      "main": [
        [
          {
            "node": "Map API Respons to Result",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "triggerCount": 0
}
```
