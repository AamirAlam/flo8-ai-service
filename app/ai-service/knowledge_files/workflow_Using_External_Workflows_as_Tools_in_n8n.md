# Using External Workflows as Tools in n8n

**[View Template](https://n8n.io/workflows/2713-/)**  **Published Date:** 01/09/2025  **Created By:** Alfred Nutile  **Categories:** `Development` `Core Nodes`  

## Template Description

This guide will show you how to use a workflow as a reusable tool in n8n, such as integrating an AI Agent or other specialized processes into your workflows.

By the end of this example, you'll have a simple, reusable workflow that can be easily plugged into larger projects, making your automations more efficient and scalable.



With this approach, you can create reusable workflows like "Scrape a Page," "Search Brave," or "Generate an Image," which you can then call whenever needed.

While n8n makes it easy to build these workflows from scratch, setting them up as reusable components saves time as your automations grow in complexity.

Setup

Add the "Execute Workflow Trigger" node

Add the node(s) to perform the desired tasks in the workflow

Add a final "Set" or "Edit Fields" node at the end to ensure all external workflows return a consistent output format

Details

In this example, the "Execute Workflow Trigger" expects input in the following JSON format:

[
  {
    "query": {
      "url": "https://en.wikipedia.org/wiki/some_info"
    }
  }
]

Once your external workflow is ready, you can instruct the AI Agent to use this tool by connecting it to the external workflow. Set up the schema type to "Generate from JSON Example" using this structure:

{
  "url": "URL_TO_GET"
}


Finally, ensure your external workflow includes a "Set" or "Edit Fields" node at the end to define the response format. This helps keep the outputs of your reusable workflows consistent and predictable.



## Template JSON

```
{
  "id": "7DPLpEkww5Uctcml",
  "meta": {
    "instanceId": "75d76ac1fb686d403c2294ca007b62282f34c3e15dc3528cc1dbe36a827c0c6e"
  },
  "name": "get_a_web_page",
  "tags": [
    {
      "id": "7v5QbLiQYkQ7zGTK",
      "name": "tools",
      "createdAt": "2025-01-08T16:33:21.887Z",
      "updatedAt": "2025-01-08T16:33:21.887Z"
    }
  ],
  "nodes": [
    {
      "id": "290cc9b8-e4b1-4124-ab0e-afbb02a9072b",
      "name": "Execute Workflow Trigger",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        -460,
        -100
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "f256ed59-ba61-4912-9a75-4e7703547de5",
      "name": "FireCrawl",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -220,
        -100
      ],
      "parameters": {
        "url": "https://api.firecrawl.dev/v1/scrape",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"url\": \"{{ $json.query.url }}\",\n  \"formats\": [\n    \"markdown\"\n  ]\n} ",
        "sendBody": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "headerParameters": {
          "parameters": [
            {}
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "RoJ6k6pWBzSVp9JK",
          "name": "Firecrawl"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "a28bdbe6-fa59-4bf1-b0ab-c34ebb10cf0f",
      "name": "Edit Fields",
      "type": "n8n-nodes-base.set",
      "position": [
        -20,
        -100
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "1af62ef9-7385-411a-8aba-e4087f09c3a9",
              "name": "response",
              "type": "string",
              "value": "={{ $json.data.markdown }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "fcd26213-038a-453f-80e5-a3936e4c2d06",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -480,
        -340
      ],
      "parameters": {
        "width": 620,
        "height": 200,
        "content": "## Send URL got Crawl\nThis can be reused by Ai Agents and any Workspace to crawl a site. All that Workspace has to do is send a request:\n\n```json\n {\n    \"url\": \"Some URL to Get\"\n  }\n```"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {
    "Execute Workflow Trigger": [
      {
        "json": {
          "query": {
            "url": "https://en.wikipedia.org/wiki/Linux"
          }
        }
      }
    ]
  },
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "396f46a7-3120-42f9-b3d5-2021e6e995b8",
  "connections": {
    "FireCrawl": {
      "main": [
        [
          {
            "node": "Edit Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Execute Workflow Trigger": {
      "main": [
        [
          {
            "node": "FireCrawl",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
