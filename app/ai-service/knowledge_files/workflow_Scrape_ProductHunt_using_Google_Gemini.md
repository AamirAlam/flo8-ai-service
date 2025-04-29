# Scrape ProductHunt using Google Gemini

**[View Template](https://n8n.io/workflows/2698-/)**  **Published Date:** 01/05/2025  **Created By:** Mauricio Perera  **Categories:** `Development` `Core Nodes` `AI` `Langchain`  

## Template Description

Workflow Description: Product Data Extractor

This workflow automates the extraction of product data from Product Hunt by combining webhook interactions, HTML processing, AI-based data analysis, and structured output formatting. It is designed to handle incoming requests dynamically and return detailed JSON responses for further usage.

Overview

The workflow processes a product name submitted through a webhook. It fetches the corresponding Product Hunt page, extracts and analyzes inline scripts, and structures the data into a well-defined JSON format using AI tools. The final JSON response is returned to the client through the webhook.

Workflow Steps

1. Webhook Listener

Node:** Receive Product Request
Function:** Captures incoming requests containing the product name to process.
Details:** Accepts HTTP requests and extracts the product parameter from the query string, such as &lt;custom_webhook_url&gt;/?product=epigram.

2. Fetch Product HTML

Node:** Fetch Product HTML
Function:** Sends an HTTP request to retrieve the HTML content of the specified Product Hunt page.
Details:** Constructs a dynamic URL using the product name and fetches the page data.

3. Extract Inline Scripts

Node:** Extract Inline Scripts
Function:** Parses the HTML content to extract inline scripts located within the &lt;head&gt; section.
Details:** Excludes scripts containing src attributes and validates the presence of inline scripts.

4. Process Data with LLM

Node:** Process Script with LLM
Function:** Analyzes the extracted scripts using a language model to identify key product data.
Details:** Processes the script to derive structured and meaningful insights.

5. Refine Data with Google Gemini

Node:** Analyze Script with Google Gemini
Function:** Leverages Google Gemini AI for enhanced analysis of script data.
Details:** Ensures the extracted data is precise and enriched.

6. Format Product Data to JSON

Node:** Format Product Data to JSON
Function:** Structures the processed data into a clean JSON format.
Details:** Defines a schema to ensure all relevant fields are included in the output.

7. Send JSON Response to Client

Node:** Send JSON Response to Client
Function:** Returns the final structured JSON response to the client.
Details:** Sends the response back via the same webhook that initiated the request. For example, &lt;custom_webhook_url&gt;.

Key Features

Versatile Use Cases:** This workflow can be used to gather Product Hunt data for creating blog posts or as a tool for AI agents to research products efficiently.
Dynamic Processing:** Adapts to various product names through dynamic URL construction.
AI Integration:** Utilizes the Gemini 1.5 8B AI model, offering reduced latency and minimal or no cost depending on the use case.
Selector Independence:** Functions even if Product Hunt's DOM structure changes, as it does not rely on direct DOM selectors.
Reliable Data Output:** A low temperature setting (0) and a precisely defined JSON schema ensure accurate and real data extraction.
Dynamic Processing:** Adapts to various product names through dynamic URL construction.
AI Integration:** Utilizes advanced language models for data extraction and refinement.
Structured Output:** Ensures the output JSON adheres to a predefined schema for consistency.
Error Handling:** Includes validations to handle missing or malformed data gracefully.

Customization Options

Limitations
Dependency on Product Hunt:** Significant changes to the way Product Hunt loads data on its pages might require modifications to the workflow.
Adaptability:** Even if changes occur, the workflow can be updated to maintain functionality due to its reliance on AI and not direct DOM selectors.


Modify the webhook path to suit your application.
Adjust the prompt for the language model to include additional fields.
Extend the JSON schema to capture more data fields as needed.

Expected Output

Performance Metrics
Response Time:** Typically ~6 seconds per product.
Accuracy:** Data extracted with &gt;95% precision due to the pre-defined JSON schema.


A JSON object containing detailed information about the specified product. Below is an example of a complete response for the product Epigram:

{
  "id": "861675",
  "slug": "epigram",
  "followersCount": 181,
  "name": "Epigram",
  "tagline": "Open-Source, Free, and AI-Powered News in Short",
  "reviewsRating": 0,
  "logoUuid": "735c2528-554c-467c-9dcf-745ee4b8bbdd.png",
  "postsCount": 1,
  "websiteUrl": "https://epigram.news",
  "websiteDomain": "epigram.news",
  "metaTitle": "Epigram - Open-source, free, and ai-powered news in short",
  "postName": "Epigram",
  "postTagline": "Open-source, free, and ai-powered news in short",
  "dailyRank": "3",
  "description": "An open-source, AI-powered news app for busy people. Stay updated with bite-sized news, real-time updates, and in-depth analysis. Experience balanced, trustworthy reporting tailored for fast-paced lifestyles in a sleek, user-friendly interface.",
  "pricingType": "free",
  "userName": "Fazle Rahman",
  "userHeadline": "Co-founder & CEO, Hashnode",
  "userUsername": "fazlerocks",
  "userAvatarUrl": "https://ph-avatars.imgix.net/129147/f84e1796-548b-4d6f-9dcf-745ee4b8bbdd.jpeg",
  "makerName1": "Fazle Rahman",
  "makerHeadline1": "Co-founder & CEO, Hashnode",
  "makerUsername1": "fazlerocks",
  "makerAvatarUrl1": "https://ph-avatars.imgix.net/129147/f84e1796-548b-4d6f-9dcf-745ee4b8bbdd.jpeg",
  "makerName2": "Sandeep Panda",
  "makerHeadline2": "Co-Founder @ Hashnode",
  "makerUsername2": "sandeepg33k",
  "makerAvatarUrl2": "https://ph-avatars.imgix.net/101872/80b0b618-a540-4110-a6d1-74df39675ad0.jpeg",
  "primaryLinkUrl": "https://epigram.news/",
  "media1OriginalHeight": 1080,
  "media1OriginalWidth": 1440,
  "media1ImageUuid": "ac426fd1-3854-4734-b43d-34a5e06347ea.gif",
  "media1MediaType": "video",
  "media1MetadataUrl": "https://www.loom.com/share/b1a48a9b3cac4ba89ce772a3fbcc2847?sid=75efc771-25fa-4ac0-bb1b-5e38fc447deb",
  "media1VideoId": "b1a48a9b3cac4ba89ce772a3fbcc2847",
  "media2OriginalHeight": 630,
  "media2OriginalWidth": 1200,
  "media2ImageUuid": "8521a6bd-7640-487b-abd6-29b9f65fee32",
  "media2MediaType": "image",
  "media2MetadataUrl": null,
  "launchState": "featured",
  "thumbnailImageUuid": "735c2528-554c-467c-9dcf-745ee4b8bbdd.png",
  "link1StoreName": "Website",
  "link1WebsiteName": "epigram.news",
  "link2StoreName": "Github",
  "link2WebsiteName": "github.com",
  "latestScore": 233,
  "launchDayScore": 233,
  "userId": "129147",
  "topic1": "News",
  "topic2": "Open Source",
  "topic3": "Artificial Intelligence",
  "weeklyRank": "24",
  "commentsCount": 20,
  "postUrl": "https://www.producthunt.com/posts/epigram"
}

Target Audience

This workflow is ideal for developers, marketers, and data analysts seeking to automate the extraction and structuring of product data from Product Hunt for analytics, reporting, or integration with other tools.



## Template JSON

```
{
  "id": "PjmORR4QITmw1TSm",
  "meta": {
    "instanceId": "57d3ba707284c18c36b0508d0a86fd8cd64b5e08ec224bc67c06b6dcc4799603"
  },
  "name": "My workflow",
  "tags": [],
  "nodes": [
    {
      "id": "267d0887-c2ce-4302-9040-a3c5b6fea051",
      "name": "Receive Product Request",
      "type": "n8n-nodes-base.webhook",
      "position": [
        1700,
        -180
      ],
      "webhookId": "a6d424b5-41ab-4eb1-96c5-ea7c3f6b4c60",
      "parameters": {},
      "typeVersion": 2
    },
    {
      "id": "d13a1845-ee24-4007-9acb-3a414bddadf5",
      "name": "Fetch Product HTML",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        2160,
        -180
      ],
      "parameters": {},
      "typeVersion": 4.2
    },
    {
      "id": "a3714478-636b-49b5-a5c5-b7f51df13f22",
      "name": "Extract Inline Scripts",
      "type": "n8n-nodes-base.code",
      "position": [
        2580,
        -180
      ],
      "parameters": {},
      "typeVersion": 2
    },
    {
      "id": "6fa0c53a-c4bb-4867-b0ca-077367012186",
      "name": "Process Script with LLM",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        3000,
        -180
      ],
      "parameters": {},
      "typeVersion": 1.5
    },
    {
      "id": "f7503b98-698c-4bb7-bffb-b17974e19ee4",
      "name": "Analyze Script with Google Gemini",
      "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
      "position": [
        2800,
        240
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "58e1ef40-b62e-4cec-b396-25edab562993",
      "name": "Format Product Data to JSON",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        3360,
        240
      ],
      "parameters": {},
      "typeVersion": 1.2
    },
    {
      "id": "a7c09c95-2927-4a93-9384-78ddcacc6ca7",
      "name": "Send JSON Response to Client",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        3620,
        -180
      ],
      "parameters": {},
      "typeVersion": 1.1
    },
    {
      "id": "a2ccfa5e-1aed-45ac-add6-871ef837efcb",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1600,
        -360
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "a672d2cd-7cf6-43fc-8eb8-6049f73d652e",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2060,
        -360
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "55a0a3bd-c10a-47ab-9ad7-d6be98261de5",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2480,
        -360
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "7a413f72-247c-41fe-94ea-d3f934b382d2",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2980,
        -360
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "55f657cb-a1aa-490d-99bf-51337b2f5e5f",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2700,
        40
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "fb9effbd-e8c4-4373-a547-9646a9596703",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        3240,
        40
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "effc8669-3f88-40a7-a4e5-b2439d699e85",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        3520,
        -380
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "active": true,
  "pinData": {
    "Receive Product Request": [
      {
        "json": {
          "body": {},
          "query": {
            "product": "epigram"
          },
          "params": {},
          "headers": {
            "host": "n8n-latest-relk.onrender.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "cf-ray": "8fd0c49934462c8d-DFW",
            "cookie": "rl_session=RudderEncrypt%3AU2FsdGVkX19e%2B7qMt4i3Ys4JYvbiUSZzs3kfatMTxfXlHcY2jq0R%2FlAkeFucX11ECA0%2BJK291YI7SwsdUqDdXsFhm2EcWoZQTYDN6xrDixBlWinQXhtgDRByRQoOduoIz1KisUo7kltVadbY67EVzQ%3D%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2BnfZPwuqv64YjXtcgD5g9QKBmx4Ed82o6o6EV%2BFVIZ6Bg%2F2uYfVH63qSKXHvCwAD5KLZ1iI350WA%3D%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2BcYyRPr4iLz7Qco%2F00vcUkm49RXcBE%2B98%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX18ytsjeLZPyGfwEvHwx6KQEuWAQwaP0dWk%3D; n8n-auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImQ4ODNhZDg1LWI4YzktNGE2Ni1hYjk1LTE0NzBlNTc1OGJlMiIsImhhc2giOiJuNVBZTklQVUZJIiwiYnJvd3NlcklkIjoiei9IQ3RlUlBUbFYrU3pnOWVEVWdzNWh3ZzdWb2VONWZ3OXVwcC9mcHVybz0iLCJpYXQiOjE3MzYwMjUwMjEsImV4cCI6MTczNjYyOTgyMX0.8v7TNTB9HcZLzfUzljRHn_iPFd5uN9EL2bMiT_XkjXw; rl_user_id=RudderEncrypt%3AU2FsdGVkX19dnySkXTyiYf7TzD74z2btLpIegLXThFjqWAShe2NInMjDvKyI2DlmihteoasBtDnNg0I83P6j1N0WF16d4pP7qCNu75PmlDTOvmGlrcEbEndhgHl%2FKyX6KqpNqOT1A9u9JDgpqfCLBMiZl6ZTVQuS9tGAUxSOOIc%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2FTaQJzTQ0vinRDH%2FaIP%2FkqXVTpuXOFRWP63Qd911tZH4a3YeLYGWOeZlO30qwdaf7YDcixieTy9klJKxY%2BT2cr3efxgB%2BuXCKxlKroxuZc%2FUSIm1mMasUbhXSiUSu9MU%2F7TgoT8bBB2g%3D%3D; ph_phc_4URIAm1uYfJO7j8kWSe0J8lc8IqnstRLS7Jx8NcakHo_posthog=%7B%22distinct_id%22%3A%2257d3ba707284c18c36b0508d0a86fd8cd64b5e08ec224bc67c06b6dcc4799603%23d883ad85-b8c9-4a66-ab95-1470e5758be2%22%2C%22%24sesid%22%3A%5Bnull%2Cnull%2Cnull%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fn8n-latest-relk.onrender.com%2Fsignin%3Fredirect%3D%25252Fsettings%25252Fusage%25253Fkey%25253D4da2272c-b404-49f5-ae7b-90285457f9bb%22%7D%7D",
            "rndr-id": "2f3929bc-7cfb-4d52",
            "cdn-loop": "cloudflare; loops=1; subreqs=1",
            "priority": "u=0, i",
            "cf-ew-via": "15",
            "cf-worker": "onrender.com",
            "cf-visitor": "{\"scheme\":\"https\"}",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
            "cf-ipcountry": "MX",
            "if-none-match": "W/\"8ef-YlXbmqYipwLEtdHARcVNMvja5S8\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "true-client-ip": "177.232.86.248",
            "accept-encoding": "gzip, br",
            "accept-language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
            "x-forwarded-for": "177.232.86.248, 108.162.246.57, 10.223.123.4",
            "x-request-start": "1736051792891982",
            "cf-connecting-ip": "177.232.86.248",
            "render-proxy-ttl": "4",
            "x-forwarded-proto": "https",
            "upgrade-insecure-requests": "1"
          },
          "webhookUrl": "https://n8n-latest-relk.onrender.com/webhook/a6d424b5-41ab-4eb1-96c5-ea7c3f6b4c60",
          "executionMode": "production"
        }
      }
    ]
  },
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "bcbebb70-59e4-4e80-ac6e-6f13f1fa9cf1",
  "connections": {
    "Fetch Product HTML": {
      "main": [
        [
          {
            "node": "Extract Inline Scripts",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Inline Scripts": {
      "main": [
        [
          {
            "node": "Process Script with LLM",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Process Script with LLM": {
      "main": [
        [
          {
            "node": "Send JSON Response to Client",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Receive Product Request": {
      "main": [
        [
          {
            "node": "Fetch Product HTML",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format Product Data to JSON": {
      "ai_outputParser": [
        [
          {
            "node": "Process Script with LLM",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Analyze Script with Google Gemini": {
      "ai_languageModel": [
        [
          {
            "node": "Process Script with LLM",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
