# Automated Upwork Job Alerts with MongoDB & Slack

**[View Template](https://n8n.io/workflows/2834-/)**  **Published Date:** 02/01/2025  **Created By:** Artur  **Categories:** `Development` `Core Nodes` `Communication` `HITL` `Data & Storage`  

## Template Description

Overview  
This automated workflow fetches Upwork job postings using Apify, removes duplicate job listings via MongoDB, and sends new job opportunities to Slack.  

Key Features:  
Automated job retrieval** from Upwork via Apify API  
Duplicate filtering** using MongoDB to store only unique jobs  
Slack notifications** for new job postings  
Runs every 20 minutes** during working hours (9 AM - 5 PM)  

This workflow requires an active Apify subscription to function, as it uses the Apify Upwork API to fetch job listings. 

Who is This For?  
This workflow is ideal for:  
Freelancers looking to track Upwork jobs in real time  
Recruiters automating job collection for analytics  
Developers who want to integrate Upwork job data into their applications  

What Problem Does This Solve?  
Manually checking Upwork for jobs is time-consuming and inefficient. This workflow:  
Automates job discovery based on your keywords  
Filters out duplicate listings, ensuring only new jobs are stored  
Notifies you on Slack when new jobs appear  

How the Workflow Works  

1. Schedule Trigger (Every 20 Minutes)  
Triggers the workflow at 20-minute intervals  
Ensures job searches are only executed during working hours (9 AM - 5 PM)  

2. Query Upwork for Jobs  
Uses Apify API to scrape Upwork job posts for specific keywords (e.g., "n8n", "Python")  

3. Find Existing Jobs in MongoDB  
Searches MongoDB to check if a job (based on title and budget) already exists  

4. Filter Out Duplicate Jobs  
The Merge Node compares Upwork jobs with MongoDB data  
The IF Node filters out jobs that are already stored in the database  

5. Save Only New Jobs in MongoDB  
The Insert Node adds only new job listings to the MongoDB collection  

6. Send a Slack Notification  
If a new job is found, a Slack message is sent with job details  

Setup Guide  

Required API Keys  
Upwork Scraper (Apify Token) – Get your token from Apify
MongoDB Credentials – Set up MongoDB in n8n using your connection string  
Slack API Token – Connect Slack to n8n and set the channel ID (default: #general)  

Configuration Steps  
Modify search keywords in the 'Assign Parameters' node (startUrls)  
Adjust the Working Hours in the 'If Working Hours' node  
Set your Slack channel in the Slack node  
Ensure MongoDB is connected properly  
Adjust the 'If Working Hours' node to match your timezone and hours, or remove it altogether to receive notifications and updates constantly.

How to Customize the Workflow  
Change keywords: update the startUrls in the 'Assign Parameters' node to track different job categories  
Change 'If Working Hours': Modify conditions in the IF Node to filter times based on your needs  
Modify Slack Notifications: Adjust the Slack message format to include additional job details  

Why Use This Workflow?  
Automated job tracking without manual searches  
Prevents duplicate entries in MongoDB  
Instant Slack notifications for new job opportunities  
Customizable – adapt the workflow to different job categories  

Next Steps  
Run the workflow and test with a small set of keywords  
Expand job categories for better coverage  
Enhance notifications by integrating Telegram, Email, or a dashboard  

This workflow ensures real-time job tracking, prevents duplicates, and keeps you updated effortlessly.

## Template JSON

```
{
  "meta": {
    "instanceId": "2f9460831fcdb0e9a4494f0630367cfe2968282072e2d27c6ee6ab0a4c165a36",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "140f236c-8946-4ca8-b18f-0af99107b15c",
      "name": "Assign parameters",
      "type": "n8n-nodes-base.set",
      "position": [
        300,
        80
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "b836ba12-262a-4fed-a31d-9e2f6514137a",
              "name": "startUrls",
              "type": "array",
              "value": "=[\n    {\n      \"url\": \"https://www.upwork.com/nx/search/jobs/?nbs=1&q=python\",\n      \"method\": \"GET\"\n    },\n{\n            \"url\": \"https://www.upwork.com/nx/search/jobs/?nbs=1&q=java\",\n            \"method\": \"GET\"\n        }\n  ]"
            },
            {
              "id": "5f7ba5cc-a8fc-4f67-9feb-6243d08462f9",
              "name": "proxyCountryCode",
              "type": "string",
              "value": "FR"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "d1863b34-d35f-477c-bb94-8a77ff08b51d",
      "name": "Query For Upwork Job Posts",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        520,
        80
      ],
      "parameters": {
        "url": "=https://api.apify.com/v2/acts/arlusm~upwork-scraper-with-fresh-job-posts/run-sync-get-dataset-items",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "authentication": "genericCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "startUrls",
              "value": "={{ $json.startUrls }}"
            },
            {
              "name": "proxyCountryCode",
              "value": "={{ $json.proxyCountryCode }}"
            }
          ]
        },
        "genericAuthType": "httpQueryAuth"
      },
      "credentials": {
        "httpQueryAuth": {
          "id": "WajVMGJs8zYL5VdP",
          "name": "Query Auth account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "a923af43-f417-470c-af97-2a50dc0c0d79",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -100,
        80
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "minutes",
              "minutesInterval": 10
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "26322972-4ecd-4f8e-a1fc-81607a911c22",
      "name": "If Working Hours",
      "type": "n8n-nodes-base.if",
      "position": [
        80,
        80
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "loose"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "795a6d51-0ea0-4493-bc1e-a1807a2cbd77",
              "operator": {
                "type": "number",
                "operation": "gt"
              },
              "leftValue": "={{ $json.Hour }}",
              "rightValue": 2
            },
            {
              "id": "f9ba101d-226d-4d6a-aab8-62229762a046",
              "operator": {
                "type": "number",
                "operation": "lt"
              },
              "leftValue": "={{ $json.Hour }}",
              "rightValue": 15
            }
          ]
        },
        "looseTypeValidation": true
      },
      "typeVersion": 2.2
    },
    {
      "id": "d68cb363-df1f-4601-b194-c1dc044b0c6a",
      "name": "Find Existing Entries",
      "type": "n8n-nodes-base.mongoDb",
      "position": [
        720,
        -40
      ],
      "parameters": {
        "query": "={\n  \"title\": \"{{ $json.title }}\",\n  \"budget\": \"{{ $json.budget }}\"\n}\n",
        "options": {},
        "collection": "n8n"
      },
      "credentials": {
        "mongoDb": {
          "id": "aXU1Q0utjxwEpfEk",
          "name": "MongoDB account"
        }
      },
      "typeVersion": 1.1,
      "alwaysOutputData": false
    },
    {
      "id": "82a6a26a-9fd5-4ce5-986f-e0aeb0c43fcc",
      "name": "Output New Entries",
      "type": "n8n-nodes-base.merge",
      "position": [
        940,
        80
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "joinMode": "keepNonMatches",
        "fieldsToMatchString": "title, budget"
      },
      "typeVersion": 3
    },
    {
      "id": "361603e9-d173-42e2-a170-de08725ffd24",
      "name": "Add New Entries To MongoDB",
      "type": "n8n-nodes-base.mongoDb",
      "position": [
        1160,
        -40
      ],
      "parameters": {
        "fields": "title,link,paymentType,budget,projectLength,shortBio,skills,publishedDate,normalizedDate,searchUrl",
        "options": {},
        "operation": "insert",
        "collection": "n8n"
      },
      "credentials": {
        "mongoDb": {
          "id": "aXU1Q0utjxwEpfEk",
          "name": "MongoDB account"
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "e13787c6-f3e5-4bad-afcc-b1c3387a866c",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        220,
        -240
      ],
      "parameters": {
        "height": 260,
        "content": "## Setup\n1. Add MongoDB, Slack credentials\n2. Add a query auth credential where the key='token' and the value being your apify token\n3. Modify the 'Assign parameters' node to include the Upwork URLs you want to query for"
      },
      "typeVersion": 1
    },
    {
      "id": "bc83acf0-b28b-48ff-bcb1-695404f30282",
      "name": "Send message in #general",
      "type": "n8n-nodes-base.slack",
      "position": [
        1160,
        200
      ],
      "webhookId": "7b8d0119-c115-4ed3-9d2d-ea8d58edfae6",
      "parameters": {
        "text": "=Job Title : {{ $json.title }}\nPublished : {{ $json.publishedDate }}\nLink : {{ $json.link }}\nPayment Type: {{ $json.paymentType }}\nBudget: {{ $json.budget }}\nSkills: {{ $json.skills }}\nBio: {{ $json.shortBio }}",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "name",
          "value": "#general"
        },
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": {
          "id": "nilit1oFWL3xhyvx",
          "name": "Slack account"
        }
      },
      "typeVersion": 2.3
    }
  ],
  "pinData": {},
  "connections": {
    "If Working Hours": {
      "main": [
        [
          {
            "node": "Assign parameters",
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
            "node": "If Working Hours",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Assign parameters": {
      "main": [
        [
          {
            "node": "Query For Upwork Job Posts",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Output New Entries": {
      "main": [
        [
          {
            "node": "Add New Entries To MongoDB",
            "type": "main",
            "index": 0
          },
          {
            "node": "Send message in #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Find Existing Entries": {
      "main": [
        [
          {
            "node": "Output New Entries",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Query For Upwork Job Posts": {
      "main": [
        [
          {
            "node": "Find Existing Entries",
            "type": "main",
            "index": 0
          },
          {
            "node": "Output New Entries",
            "type": "main",
            "index": 1
          }
        ]
      ]
    }
  }
}
```
