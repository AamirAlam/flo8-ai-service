# Simple Google indexing Workflow in N8N

**[View Template](https://n8n.io/workflows/2123-/)**  **Published Date:** 02/23/2024  **Created By:** Joachim Brindeau  **Categories:** `Development` `Core Nodes`  

## Template Description

What it does
The workflow is a simple yet efficient way to automate the process of indexing your website on Google using the Google Indexing API.

How it works

It works by extracting information from your sitemap, converting it into a JSON file, and looping through each URL to submit it for indexing. 


Here's a brief rundown of the workflow:

The workflow can be triggered manually via the "Execute Workflow" button or scheduled to run at a specific time using the "Schedule Trigger" node.

The sitemap of your website is fetched using the "sitemap_set" node with a HTTP Request to the sitemap URL. 

This XML sitemap is then converted into a JSON file using the "sitemap_convert" node.

The "sitemap_parse" node splits the JSON file into individual URLs.

The "url_set" node then prepares each URL to be sent to the Google Indexing API.

A loop is created using the "loop" node to process each URL individually and make a POST request to Google Indexing API indicating that the URL has been updated.

If the POST request is successful and the URL has been updated, the workflow waits for 2 seconds before moving to the next URL.

In case the daily limit for the Google Indexing API is reached (200/day by default), an error message is triggered using the "Stop and Error" node.
Before you use the workflow
Activate the indexing API
Create an account with Google Cloud Platform &gt; Console and then create a new project
Search for the Indexing API in the Library
Activate the API

Create a Service Account and get credentials
Open the Service accounts page. If prompted, select a project.
Click add Create Service Account, enter a name and description for the service account. You can use the default service account ID, or choose a different, unique one. 
When done click Create.
On the Grant users access to this service account screen, scroll down to the Create key section. Click add Create key.
In the side panel that appears, select the JSON format
Click Create. Your new public/private key pair is generated and downloaded to your machine.
Open the file and copy the private key.
Add the credentials in the url_index node

Add the user as owner of the site
Beware, for each site you need to add the user as a owner like this:

Set your sitemap

Open the sitemap_set node and add the url to your sitemap.

Now you should be able to ensure that Google is always up-to-date with the latest content on your website, improving your website's visibility and SEO rankings, have fun!

## Template JSON

```
{
  "meta": {
    "instanceId": "2edac0e72822bb0462c05ce3b5a939f685ded652d02e9a767d1afa775988460e"
  },
  "nodes": [
    {
      "id": "0788a3db-20c3-43b6-956a-394f688f7763",
      "name": "When clicking \"Execute Workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        360,
        440
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "51460fab-a53c-46cd-a484-d2c038cd102d",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        360,
        600
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "triggerAtHour": 1
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "5326416c-5715-4cc7-acfd-38a32f864bfb",
      "name": "loop",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        1360,
        600
      ],
      "parameters": {
        "options": {},
        "batchSize": 1
      },
      "typeVersion": 2
    },
    {
      "id": "fb0ca9f7-ff49-4a4b-9575-42b80594737e",
      "name": "sitemap_set",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        540,
        600
      ],
      "parameters": {
        "url": "https://bushidogym.fr/sitemap.xml",
        "options": {}
      },
      "typeVersion": 4.1
    },
    {
      "id": "150b47fe-f1c8-4dcb-b187-b459ee50c316",
      "name": "sitemap_convert",
      "type": "n8n-nodes-base.xml",
      "position": [
        700,
        600
      ],
      "parameters": {
        "options": {
          "trim": true,
          "normalize": true,
          "mergeAttrs": true,
          "ignoreAttrs": true,
          "normalizeTags": true
        }
      },
      "typeVersion": 1
    },
    {
      "id": "83cd19d6-81e7-46af-83a3-090cdd66b420",
      "name": "sitemap_parse",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        920,
        600
      ],
      "parameters": {
        "options": {
          "destinationFieldName": "url"
        },
        "fieldToSplitOut": "urlset.url"
      },
      "typeVersion": 1
    },
    {
      "id": "95c784d1-5756-4bf0-b2e5-e25a84c01b72",
      "name": "url_set",
      "type": "n8n-nodes-base.set",
      "position": [
        1140,
        600
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "url",
              "value": "={{ $json.url.loc }}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 2
    },
    {
      "id": "43b62667-a37e-4bd1-bbb9-7a20a0914c97",
      "name": "url_index",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1560,
        580
      ],
      "parameters": {
        "url": "https://indexing.googleapis.com/v3/urlNotifications:publish",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "authentication": "predefinedCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "url",
              "value": "={{ $json.url }}"
            },
            {
              "name": "type",
              "value": "URL_UPDATED"
            }
          ]
        },
        "nodeCredentialType": "googleApi"
      },
      "credentials": {
        "googleApi": {
          "id": "RywvL8c7V2ZtBvdK",
          "name": "850737154850-compute@developer.gserviceaccount.com"
        }
      },
      "typeVersion": 4,
      "continueOnFail": true,
      "alwaysOutputData": true
    },
    {
      "id": "39ae8c01-64e4-44f5-be43-d5c402b00739",
      "name": "index_check",
      "type": "n8n-nodes-base.if",
      "position": [
        1780,
        580
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.urlNotificationMetadata.latestUpdate.type }}",
              "value2": "URL_UPDATED"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "c4bf483b-af4b-451e-974b-d4abeb2c70f6",
      "name": "wait",
      "type": "n8n-nodes-base.wait",
      "position": [
        2040,
        560
      ],
      "webhookId": "b0df1fe8-e509-4d0c-a486-f523226621e2",
      "parameters": {
        "unit": "seconds",
        "amount": 2
      },
      "typeVersion": 1
    },
    {
      "id": "455955a8-c767-453b-805c-77c5b7d2e9bc",
      "name": "Stop and Error",
      "type": "n8n-nodes-base.stopAndError",
      "position": [
        2040,
        840
      ],
      "parameters": {
        "errorMessage": "You have reached the Google Indexing API limit (200/day by default)"
      },
      "typeVersion": 1
    },
    {
      "id": "275abdd5-be5d-458f-bc75-d9f72824c49f",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        340,
        180
      ],
      "parameters": {
        "width": 482.7089688834655,
        "height": 221.39109212934721,
        "content": "## Simple indexing workflow using the Google Indexing API\n\nThis workflow is the simplest indexing workflow. It simply extracts a sitemap, converts it to a JSON, and loops through each URL. It will output an error if your quota is reached.\n\n*Joachim*"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "loop": {
      "main": [
        [
          {
            "node": "url_index",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "wait": {
      "main": [
        [
          {
            "node": "loop",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "url_set": {
      "main": [
        [
          {
            "node": "loop",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "url_index": {
      "main": [
        [
          {
            "node": "index_check",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "index_check": {
      "main": [
        [
          {
            "node": "wait",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Stop and Error",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "sitemap_set": {
      "main": [
        [
          {
            "node": "sitemap_convert",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "sitemap_parse": {
      "main": [
        [
          {
            "node": "url_set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "sitemap_convert": {
      "main": [
        [
          {
            "node": "sitemap_parse",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Schedule Trigger": {
      "main": [
        [
          {
            "node": "sitemap_set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When clicking \"Execute Workflow\"": {
      "main": [
        [
          {
            "node": "sitemap_set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
