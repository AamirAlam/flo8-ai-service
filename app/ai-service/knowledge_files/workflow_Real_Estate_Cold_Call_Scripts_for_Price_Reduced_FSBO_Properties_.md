# Real Estate Cold Call Scripts for Price Reduced FSBO Properties (Zillow Data)

**[View Template](https://n8n.io/workflows/3143-/)**  **Published Date:** 03/12/2025  **Created By:** T Zero  **Categories:** `Data & Storage` `Development` `Core Nodes` `AI` `Langchain`  

## Template Description

Real Estate Price-Reduced Property Opportunity Guide

Overview
This comprehensive automation solution targets FSBO properties listed on Zillow that have recently had their price reduced, providing both investment analysis and tailored outreach scripts. The workflow gathers comprehensive market data to analyze local trends for each specific city and incorporates this intelligence into personalized communication strategies (more aggressive in buyers' markets, more value-focused in sellers' markets).

Key benefits:
Identify motivated homeowners who have recently reduced their property prices
Prepare data-driven offer strategies based on detailed market conditions
Develop effective, personalized communication approaches
Create a consistent, automated workflow to find and capitalize on opportunities

Requirements
Airtable account (free tier works)
n8n automation platform
OpenAI API key 
Zillow Rapid API access
Basic understanding of automation workflows

Step 1: Set Up Airtable Database
Create a new Airtable base
Set up a table with the following fields:
  Property ID (primary field)
  Address
  Price
  Status (single select field with options: "Contacted" and "Uncontacted")
  Phone Number
  Communication Template
  Market Analysis
  Offer Price
  Investment Metrics (Long text field for detailed financial analysis)
  Expected Cash Flow (Currency field)
  Expected ROI (Percentage field)
  Follow-up Date
Set the default Status to "Uncontacted"
Generate a Personal Access Token from Airtable settings for API connections

Step 2: Configure Zillow API Connection
Set up an HTTP request node in n8n to connect to Zillow's Rapid API
Configure the search parameters:
  Listing type: "For Sale By Owner"
  Location: Your target market
  Price reduction: true
  Auction properties: false
Add filters to:
  Exclude properties without contact information
  Only include listings with recent price reductions
  Filter by minimum square footage or bedrooms if desired
  Set maximum days since price reduction (e.g., last 14 days)

Step 3: Market Analysis Workflow
Our market analysis engine processes Zillow market data to provide strategic insights for each location:

Comprehensive Market Indicators**:
  Current inventory levels and new listing rates
  Median list price and sale price comparison
  Days-to-pending metrics (current and historical)
  Sale-to-list price ratios
  Percentage of properties selling above/below list price

Market Trend Analysis**:
  6-month and year-over-year comparative trends
  Market trend scoring system (-10 to +10 scale)
  Market cycle position identification (Early, Mid, Late)
  Seasonal market pattern recognition

Strategic Investment Guidance**:
  Market type classification (Buyer's, Balanced, Seller's)
  Negotiation power assessment
  Market timing recommendations
  Risk evaluation (Low to High scale)
  Actionable investment strategies based on current conditions

This analysis is transformed into actionable advice that directs your negotiation approach and helps you calibrate offers appropriately for market conditions.

Step 4: Calculate Investment Metrics
Our investment calculator analyzes each Zillow property and its RentZestimate to provide comprehensive financial projections:

Purchase & Financing Analysis**:
  Purchase price and standard acquisition costs (20% down payment, 3% closing costs)
  Loan amount and monthly mortgage payment (30-year term)
  Total initial investment calculation

Monthly Expense Projections**:
  Property tax (2% of property value annually)
  Insurance (0.5% of property value annually)
  Maintenance reserves (1% of property value annually)
  Vacancy allowance (8% of rental income)
  Total monthly expense calculation

Rental Income & Returns**:
  RentZestimate integration (with 1% rule fallback when unavailable)
  Monthly and annual cash flow projections
  Cash-on-cash ROI calculation
  Break-even timeline analysis

Investment Quality Filtering**:
  Automatic filtering to show only positive cash flow properties
  Property identification with complete details (address, beds, baths, sqft)
  Full investment metrics breakdown for investor decision-making

This calculator ensures you focus only on properties with profit potential, saving you countless hours of manual analysis.

Step 5: Generate Communication Templates
Create templates that combine:
  Property details (address, price, features)
  Market intelligence from your analysis
  Investment metrics showing the property's potential
Configures your templates to include:
  A professional introduction
  Reference to the specific property address
  Mention of the price reduction
  A strategic cash offer (typically 5-15% below asking)
  Local market statistics to build credibility
  A clear call to action (request to visit the property)

Step 6: Automated Workflow
Set up the complete n8n workflow to:
  Check for new listings with price reductions daily
  Run market analysis on each new property
  Calculate potential investment returns
  Generate personalized communication templates
  Upload data to Airtable
  Flag properties ready for contact
  Update status to "Contacted" after outreach

Troubleshooting
If outreach isn't being tracked: Check API connections to Airtable
If market data seems incorrect: Verify Zillow API parameters and location settings
If offers are too low/high: Adjust your calculation parameters

Step by Step tutorial: 
https://youtu.be/IqVw9CIL254?si=MKE5UY4rD0TOMLPg

By following this guide, you'll have a functional system that can identify opportunities, analyze market conditions, and help you create personalized offers to potential sellers—all while minimizing the manual effort required so you can focus on closing deals.

## Template JSON

```
{
  "id": "WQVw13itknVWzCSq",
  "meta": {
    "instanceId": "a5367fea70861552a827c021d90623f5760fca08d12ceabff8df03a6d277df78",
    "templateCredsSetupCompleted": true
  },
  "name": "FSBO Main",
  "tags": [
    {
      "id": "NXQKNEbkDQ6A37lY",
      "name": "real estate",
      "createdAt": "2025-02-24T04:27:54.728Z",
      "updatedAt": "2025-02-24T04:27:54.728Z"
    }
  ],
  "nodes": [
    {
      "id": "6c846e47-b8c1-442c-8277-d3afafe30b1f",
      "name": "On form submission",
      "type": "n8n-nodes-base.formTrigger",
      "position": [
        -2160,
        -740
      ],
      "webhookId": "e7395354-db56-41d4-b11f-e8148d3f9d18",
      "parameters": {},
      "typeVersion": 2.2
    },
    {
      "id": "6bed3f74-9595-465c-8ec2-2916de396325",
      "name": "Zillow Search",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -1540,
        -740
      ],
      "parameters": {},
      "typeVersion": 4.2
    },
    {
      "id": "11eae8e4-04ba-4c0d-8db6-bd21b49d6e36",
      "name": "RentZestimate",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -1220,
        -740
      ],
      "parameters": {},
      "typeVersion": 4.2
    },
    {
      "id": "c7b95a10-3802-45a2-8bf7-2c6c7268c1e7",
      "name": "Split Out",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        -1380,
        -740
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "8fc30382-fab2-4b10-b255-ca2bf3319ee6",
      "name": "market_overview",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -1680,
        -480
      ],
      "parameters": {},
      "typeVersion": 4.2
    },
    {
      "id": "8c741d5f-f7a8-43dc-a72d-2072eac9e216",
      "name": "Edit Fields1",
      "type": "n8n-nodes-base.set",
      "position": [
        -1500,
        -480
      ],
      "parameters": {},
      "typeVersion": 3.4
    },
    {
      "id": "d69538e4-994c-4e36-866c-765a0d2501f0",
      "name": "FSBO",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        -1880,
        -480
      ],
      "parameters": {},
      "typeVersion": 1.1
    },
    {
      "id": "140c76e1-1e23-4399-8695-3e13a689e096",
      "name": "OpenAI Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        -1120,
        -300
      ],
      "parameters": {},
      "typeVersion": 1.2
    },
    {
      "id": "f00c212b-749a-4b84-a5d1-139a3f6c79ab",
      "name": "Execute Workflow",
      "type": "n8n-nodes-base.executeWorkflow",
      "position": [
        -1940,
        -740
      ],
      "parameters": {},
      "typeVersion": 1.2
    },
    {
      "id": "2cb0714f-3581-49fe-a772-9cfb164c1da0",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -2260,
        -1300
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "97b48507-3390-425c-a3f9-b2def2c91730",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -3200,
        -1300
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "6dfe04b0-b2b5-4cee-b3dc-bfc84c51c428",
      "name": "Investment Calculator",
      "type": "n8n-nodes-base.code",
      "position": [
        -1040,
        -740
      ],
      "parameters": {},
      "typeVersion": 2
    },
    {
      "id": "0822ef45-d231-4fb9-bd67-f88e354aba29",
      "name": "FSBO Property Criteria Set",
      "type": "n8n-nodes-base.set",
      "position": [
        -1740,
        -740
      ],
      "parameters": {},
      "typeVersion": 3.4
    },
    {
      "id": "1ed17726-588b-4a3c-913b-480c21c689b3",
      "name": "Call Script Database Airtable",
      "type": "n8n-nodes-base.airtable",
      "position": [
        -460,
        -740
      ],
      "parameters": {},
      "typeVersion": 2.1
    },
    {
      "id": "75032c75-40bf-448e-8ecb-0a4774c08fa8",
      "name": "Call Script Generator",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        -860,
        -740
      ],
      "parameters": {},
      "typeVersion": 1.8
    },
    {
      "id": "4d34acbf-9614-4d0c-a519-52bab9955350",
      "name": "Historical Market Summary",
      "type": "@n8n/n8n-nodes-langchain.chainSummarization",
      "position": [
        -1100,
        -480
      ],
      "parameters": {},
      "typeVersion": 2
    },
    {
      "id": "9669cf77-fa18-482d-8447-6ba5035a0f5f",
      "name": "Historical Market Results Indicator",
      "type": "n8n-nodes-base.code",
      "position": [
        -1320,
        -480
      ],
      "parameters": {},
      "typeVersion": 2
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "2206d527-dd02-4cd0-b5ce-2fbaf3c7f4cc",
  "connections": {
    "FSBO": {
      "main": [
        [
          {
            "node": "market_overview",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split Out": {
      "main": [
        [
          {
            "node": "RentZestimate",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Edit Fields1": {
      "main": [
        [
          {
            "node": "Historical Market Results Indicator",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "RentZestimate": {
      "main": [
        [
          {
            "node": "Investment Calculator",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Zillow Search": {
      "main": [
        [
          {
            "node": "Split Out",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "market_overview": {
      "main": [
        [
          {
            "node": "Edit Fields1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Execute Workflow": {
      "main": [
        [
          {
            "node": "FSBO Property Criteria Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On form submission": {
      "main": [
        [
          {
            "node": "Execute Workflow",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model1": {
      "ai_languageModel": [
        [
          {
            "node": "Historical Market Summary",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Call Script Generator": {
      "main": [
        [
          {
            "node": "Call Script Database Airtable",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Investment Calculator": {
      "main": [
        [
          {
            "node": "Call Script Generator",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Historical Market Summary": {
      "main": [
        []
      ]
    },
    "FSBO Property Criteria Set": {
      "main": [
        [
          {
            "node": "Zillow Search",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Historical Market Results Indicator": {
      "main": [
        [
          {
            "node": "Historical Market Summary",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
