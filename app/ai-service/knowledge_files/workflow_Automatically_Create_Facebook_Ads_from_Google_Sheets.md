# Automatically Create Facebook Ads from Google Sheets

**[View Template](https://n8n.io/workflows/3406-/)**  **Published Date:** 04/02/2025  **Created By:** Artur  **Categories:** `Data & Storage` `Productivity` `Development` `Core Nodes`  

## Template Description


Who is this for?

This template is designed for Marketing Managers, Performance Marketers, and Ad Ops professionals who want to automate Facebook ad creation using structured data in Google Sheets. It’s ideal for teams running multiple creatives or testing ad variations without having to manually use Meta Ads Manager.

&gt; ⚠️ Important Note:  
This is not a plug-and-play workflow. It requires:
A configured Facebook Business account
A valid Facebook App, Page, and Ad Account
Access tokens** and the correct Facebook Graph API credentials
A basic understanding of the Meta API and JSON to tweak ad set parameters like demographics, optimization goals, or sales objectives

Additionally, launching Facebook ads will incur real advertising costs, so this template is best suited for users willing to make a time investment to set things up properly and test responsibly. Expect to spend time customizing targeting and budget strategies based on your campaign needs.

What problem does this solve?

Manually uploading creatives, setting up ad sets, and creating ads in Meta’s Ad Manager is time-consuming, repetitive, and error-prone—especially at scale. This workflow eliminates the manual work by pulling data from Google Sheets and using it to automatically:

Generate Facebook Ad Sets
Upload creative images
Build and launch Ad Creatives and Ads
Update your source spreadsheet with generated Ad IDs

What this workflow does

Using a trigger from a Google Sheets row update, this workflow:

Reads ad parameters (like message, render URL, and campaign info) from a Google Sheet  
Generates ad set configuration dynamically using variables in an “Edit Fields” node  
Creates a Facebook Ad Set via the Graph API  
Fetches the ad image from a render URL  
Uploads the image to Facebook Ads Library  
Creates the Ad Creative using the uploaded image and dynamic text  
Launches the Ad using the generated Ad Set and Creative  
Updates the same Google Sheet with the generated Ad ID and status

All configuration fields like campaign_id, act_id, pixel_id, age ranges, interest targeting, and call-to-action links are defined up front in a single Edit Fields node, making the template easy to maintain or extend.

Google Sheet Structure
| Hooks | Render URL | Generate Ad | Ad ID |
|-------|------------|-------------|-------|
| Static ad text (e.g., “Visit us at...”) | Link to the creative asset (image) | Status: generate, generated, or error | Populated by the workflow with the created Facebook Ad ID |

Hooks**: This is the primary ad copy. It will be used as the main text for the static ad.
Render URL**: Direct link to the media asset (image or video) for the ad.
Generate Ad**: Dropdown or text value that controls workflow execution:
  generate — workflow will attempt to create the ad
  generated — already processed
  error — error occurred during generation
Ad ID**: The Meta Ad ID will be written here once the ad is successfully created.

Setup

Copy this Google Sheet template and populate it with your data
Create a Facebook App and retrieve the access credentials for the Facebook Graph API
In n8n:
   Connect your Google Sheets and Facebook Graph API accounts
   Update the Edit Fields node with your actual ad account ID, page ID, campaign ID, pixel ID, and destination link
   Deploy the workflow

This workflow runs every time the generate ad column in your sheet is updated.

How to customize this workflow to your needs

Modify the Edit Fields node to adjust ad set parameters like targeting, budget strategy, CTA type, and more
Expand interest-based targeting using more interest objects in the array
Add extra Google Sheet columns and map them to Facebook ad fields (e.g. different messages, URLs, creative assets)
Add logic to pause or duplicate ads based on performance

## Template JSON

```
{
  "meta": {
    "instanceId": "2718e70d3927cc6f222cd0fca1f41929053688eb8b4504451ee7746fdfef7be1"
  },
  "nodes": [
    {
      "id": "d82a3afd-4d22-4886-b175-d2f78ec54f94",
      "name": "Get image",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        480,
        20
      ],
      "parameters": {},
      "typeVersion": 4.2
    },
    {
      "id": "9aaf29e7-17f9-453f-88fb-cd9f90611706",
      "name": "Upload Ad image",
      "type": "n8n-nodes-base.facebookGraphApi",
      "position": [
        700,
        20
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "d1539410-3b66-4790-a20d-ec48276bc61d",
      "name": "Facebook Ad Creative",
      "type": "n8n-nodes-base.facebookGraphApi",
      "position": [
        920,
        20
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "0481e563-bffb-4c97-addc-74ff3620270f",
      "name": "Create an Ad",
      "type": "n8n-nodes-base.facebookGraphApi",
      "position": [
        1140,
        20
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "762da443-fcc0-4dc7-b024-b90b9ec563ba",
      "name": "Google Sheets Trigger",
      "type": "n8n-nodes-base.googleSheetsTrigger",
      "position": [
        -180,
        20
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "42c1cf13-b87d-4700-bee6-655fcc7afe8c",
      "name": "Create an Ad Set",
      "type": "n8n-nodes-base.facebookGraphApi",
      "position": [
        260,
        20
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "7f42f413-b004-4ee3-9f1e-8bcb943e8088",
      "name": "Update Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1360,
        20
      ],
      "parameters": {},
      "typeVersion": 4.5
    },
    {
      "id": "1bbafbf9-5848-4009-b6b5-49e1ea6a2471",
      "name": "Specify variables",
      "type": "n8n-nodes-base.set",
      "position": [
        40,
        20
      ],
      "parameters": {},
      "typeVersion": 3.4
    }
  ],
  "pinData": {
    "Google Sheets Trigger": [
      {
        "Hooks": "\"Ever wish you could sprinkle a little magic into their day, even with your busy schedule?\"",
        "ad id": "120219801541720760",
        "Render URL": "https://templated-assets.s3.amazonaws.com/render/d8785acf-a6f4-4f25-bb17-46abe7376cd4.jpg",
        "generate ad": "generated"
      }
    ]
  },
  "connections": {
    "Get image": {
      "main": [
        [
          {
            "node": "Upload Ad image",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create an Ad": {
      "main": [
        [
          {
            "node": "Update Google Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Upload Ad image": {
      "main": [
        [
          {
            "node": "Facebook Ad Creative",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create an Ad Set": {
      "main": [
        [
          {
            "node": "Get image",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Specify variables": {
      "main": [
        [
          {
            "node": "Create an Ad Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Facebook Ad Creative": {
      "main": [
        [
          {
            "node": "Create an Ad",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets Trigger": {
      "main": [
        [
          {
            "node": "Specify variables",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
