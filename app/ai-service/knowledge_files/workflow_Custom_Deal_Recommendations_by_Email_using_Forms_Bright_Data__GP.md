# Custom Deal Recommendations by Email using Forms, Bright Data & GPT-4o-mini

**[View Template](https://n8n.io/workflows/3304-/)**  **Published Date:** 03/24/2025  **Created By:** Miquel Colomer  **Categories:** `Communication` `Core Nodes` `HITL` `AI` `Langchain`  

## Template Description



This n8n workflow template automates the process of collecting and delivering the "Top Deals of the Day" from MediaMarkt, tailored to user preferences. By combining user-submitted forms, Bright Data web scraping, GPT-4o-mini deal generation, and email delivery, this workflow sends personalized product recommendations straight to a user’s inbox.

&gt; ⚠️ Note: This workflow uses community nodes (Bright Data and Document Generator) which only work on *self-hosted n8n instances*.

🚀 What It Does

Collects user preferences via a form (categories + email)
Scrapes MediaMarkt’s deals page using Bright Data
Uses GPT-4o-mini (OpenAI) to recommend top deals
Generates a structured HTML email using a template
Sends the personalized deals directly via email

🧩 Community Node Integration
We created and used the following community nodes:

Bright Data** – To scrape MediaMarkt deals using proxy-based scraping
Document Generator** – To generate a templated HTML document from deal data

These nodes are not available in n8n Cloud and require self-hosted n8n.

🛠️ Step-by-Step Setup

Install Community Nodes  
   Make sure you're on a self-hosted n8n instance. Install:
   n8n-nodes-brightdata
   n8n-nodes-document-generator

Configure Credentials  
   Bright Data API Key (Proxy + Scraping setup)
   OpenAI API Key (GPT-4o-mini access)
   SMTP Credentials for sending emails

Customize the Form  
   Adapt the form node to collect desired categories and email addresses. Typical categories include appliances, phones, laptops, etc.

Design Your HTML Template  
   In the Document Generator node, you can tweak the HTML/CSS to change how deals appear in the final email.

Test the Workflow  
   Submit the form with test data and check that the entire flow—from scraping to email—executes as expected.

🧠 How It Works: Workflow Overview

User Interaction via Form  
   Users select product categories and enter their email. This triggers the workflow.

Data Extraction via Bright Data  
   Bright Data scrapes the MediaMarkt offers page and returns HTML content.

HTML Parsing  
   Key elements like product names, prices, and links are extracted for processing.

GPT-4o-mini Recommendation Generation  
   The extracted data is sent to OpenAI (GPT-4o-mini), which filters, ranks, and enhances deals based on the user’s preferences.

Data Structuring & Split  
   The result is split into individual deal items to be formatted.

HTML Document Creation  
   Document Generator populates a clean HTML template with the top recommended deals.

Email Delivery  
   The final document is emailed via SMTP to the user with a friendly message.

📨 Final Output

Users receive a custom HTML email featuring a curated list of top MediaMarkt deals based on their selected categories.

🔐 Credentials Used

Bright Data API** – Web scraping with proxy support  
OpenAI API** – Generating personalized recommendations  
SMTP** – Sending personalized deal emails

✨ Customization Tips

Change the Data Source**: You can adapt this to scrape other e-commerce sites.
Update the Email Template**: Make it match your branding or include images.
Extend the Form**: Add preferences like price range or specific brands.
Add Scheduling**: Use Cron to run the workflow daily or weekly.

❓Questions?

Template and node created by Miquel Colomer and n8nhackers.com.  

Need help customizing or deploying? Contact us for consulting and support.


## Template JSON

```
{
  "meta": {
    "instanceId": "b1f85eae352fde76d801a1a612661df6824cc2e68bfd6741e31305160a737e6e",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "a85eff80-4330-4bd8-acd9-9bf6e0b67c59",
      "name": "Get MediaMarkt Offers Website",
      "type": "n8n-nodes-brightdata.brightData",
      "position": [
        40,
        -160
      ],
      "parameters": {
        "url": "https://www.mediamarkt.es/es/campaign/campanas-y-ofertas",
        "zone": {
          "__rl": true,
          "mode": "list",
          "value": "web_unlocker1",
          "cachedResultName": "web_unlocker1"
        },
        "format": "json",
        "country": {
          "__rl": true,
          "mode": "list",
          "value": "es",
          "cachedResultName": "es"
        },
        "requestOptions": {}
      },
      "credentials": {
        "brightdataApi": {
          "id": "jk945kIuAFAo9bcg",
          "name": "BrightData account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "d27b03e0-b0f1-4c76-b68e-d716391c71da",
      "name": "Create HTML for Email",
      "type": "n8n-nodes-document-generator.documentGenerator",
      "position": [
        60,
        100
      ],
      "parameters": {
        "template": "<br>\nThese are our recommended deals today:<br>\n<ul>\n{{#each items}}\n<li>{{category}}: <a href=\"https://www.bestbuy.com{{link}}\">{{name}}</a> for {{price}}\u20ac</li>\n{{/each}}\n</ul>\n<br>",
        "oneTemplate": true
      },
      "typeVersion": 1
    },
    {
      "id": "d47ee04f-c1c5-4aac-a615-aa68f5a2d6cd",
      "name": "Extract items from results",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        -140,
        100
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "message.content.results"
      },
      "typeVersion": 1
    },
    {
      "id": "34df63de-9b0d-4245-8f87-3654cab0c17e",
      "name": "Notify End User by Email",
      "type": "n8n-nodes-base.emailSend",
      "position": [
        280,
        100
      ],
      "webhookId": "626001db-5451-4225-bf98-cd74c3952754",
      "parameters": {
        "html": "=Hi!\n<br>\n{{ $json.text }}\n\nBest,\n<br>\nThe n8nhackers team!",
        "options": {},
        "subject": "Your last deals!",
        "toEmail": "={{ $('When User Completes Form').first().json.Email}}",
        "fromEmail": "deals@n8nhackers.com"
      },
      "credentials": {
        "smtp": {
          "id": "z3kiLWNZTH4wQaGy",
          "name": "SMTP account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "fbbd7e95-d972-401a-9aca-8015a1acf553",
      "name": "Show Form Results Page",
      "type": "n8n-nodes-base.form",
      "position": [
        480,
        100
      ],
      "webhookId": "a67843b4-3ab9-427b-8e52-dfc42831065d",
      "parameters": {
        "options": {},
        "operation": "completion",
        "completionTitle": "Our recommended deals!",
        "completionMessage": "=We have sent {{ $('Extract items from results').all().length }} recommended deals to your email!"
      },
      "typeVersion": 1
    },
    {
      "id": "e03ebc2b-db42-4a8d-8758-b3d988c4b943",
      "name": "Extract Body and Title from Website",
      "type": "n8n-nodes-base.html",
      "position": [
        240,
        -160
      ],
      "parameters": {
        "options": {
          "trimValues": true
        },
        "operation": "extractHtmlContent",
        "dataPropertyName": "body",
        "extractionValues": {
          "values": [
            {
              "key": "title",
              "cssSelector": "title"
            },
            {
              "key": "body",
              "cssSelector": "body"
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "74b0dcd7-d833-452c-82fe-98a21bd39d12",
      "name": "Generate List of Deals by Category",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        -520,
        100
      ],
      "parameters": {
        "modelId": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini",
          "cachedResultName": "GPT-4O-MINI"
        },
        "options": {},
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Generate a list of recommended deals in json list. Classify items by category. Generate the next properties: name, description, price, link and category. All properties will be in a property called: results. Translate texts to english if required."
            },
            {
              "content": "=The input text is:\n{{ $json.body }}"
            },
            {
              "content": "=Categories to filter: {{ $('When User Completes Form').item.json.Category.join(',') }}"
            }
          ]
        },
        "jsonOutput": true
      },
      "credentials": {
        "openAiApi": {
          "id": "oKzfvOwieOm4upQ2",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.8
    },
    {
      "id": "a1095cea-6adc-4cf9-93fe-3a67dc061276",
      "name": "When User Completes Form",
      "type": "n8n-nodes-base.formTrigger",
      "position": [
        -180,
        -160
      ],
      "webhookId": "33e8f7c3-82fb-4339-9c91-4b19aa6c14ba",
      "parameters": {
        "options": {
          "path": "get-top-deals",
          "ignoreBots": true,
          "buttonLabel": "Get Deals"
        },
        "formTitle": "Top deals",
        "formFields": {
          "values": [
            {
              "fieldType": "dropdown",
              "fieldLabel": "Category",
              "multiselect": true,
              "fieldOptions": {
                "values": [
                  {
                    "option": "Appliances"
                  },
                  {
                    "option": "Cameras, CamCorders & Drones"
                  },
                  {
                    "option": "Car Electronics "
                  },
                  {
                    "option": "Cell Phones"
                  },
                  {
                    "option": "Computers & Tablets"
                  },
                  {
                    "option": "TV & Home Theater"
                  },
                  {
                    "option": "Video Games"
                  }
                ]
              },
              "requiredField": true
            },
            {
              "fieldType": "email",
              "fieldLabel": "Email",
              "placeholder": "Complete your email",
              "requiredField": true
            }
          ]
        },
        "responseMode": "lastNode",
        "formDescription": "This form returns top deals by your preferences in the same page.\n\nYou can schedule your future deals once per day at the end of this test."
      },
      "typeVersion": 2.2
    }
  ],
  "pinData": {},
  "connections": {
    "Create HTML for Email": {
      "main": [
        [
          {
            "node": "Notify End User by Email",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Notify End User by Email": {
      "main": [
        [
          {
            "node": "Show Form Results Page",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When User Completes Form": {
      "main": [
        [
          {
            "node": "Get MediaMarkt Offers Website",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract items from results": {
      "main": [
        [
          {
            "node": "Create HTML for Email",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get MediaMarkt Offers Website": {
      "main": [
        [
          {
            "node": "Extract Body and Title from Website",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Generate List of Deals by Category": {
      "main": [
        [
          {
            "node": "Extract items from results",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Body and Title from Website": {
      "main": [
        [
          {
            "node": "Generate List of Deals by Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
