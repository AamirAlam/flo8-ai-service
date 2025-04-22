# 🚀 Process YouTube Transcripts with Apify, OpenAI & Pinecone Database

**[View Template](https://n8n.io/workflows/3184-/)**  **Published Date:** 03/16/2025  **Created By:** Adyl Itto   **Categories:** `Data & Storage` `Development` `Core Nodes` `AI` `Langchain`  

## Template Description

🚀 YouTube Transcript Indexing Backend for Pinecone 🎥💾

This tutorial explains how to build the backend workflow in n8n that indexes YouTube video transcripts into a Pinecone vector database. Note: This workflow handles the processing and indexing of transcripts only—the retrieval agent (which searches these embeddings) is implemented separately.

📋 Workflow Overview

This backend workflow performs the following tasks:

Fetch Video Records from Airtable 📥  
   Retrieves video URLs and related metadata.

Scrape YouTube Transcripts Using Apify 🎬  
   Triggers an Apify actor to scrape transcripts with timestamps from each video.

Update Airtable with Transcript Data 🔄  
   Stores the fetched transcript JSON back in Airtable linked via video ID.

Process & Chunk Transcripts ✂️  
   Parses the transcript JSON, converts "mm:ss" timestamps to seconds, and groups entries into meaningful chunks. Each chunk is enriched with metadata—such as video title, description, start/end timestamps, and a direct URL linking to that video moment.

Generate Embeddings & Index in Pinecone 💾  
   Uses OpenAI to create vector embeddings for each transcript chunk and indexes them in Pinecone. This enables efficient semantic searches later by a separate retrieval agent.

🔧 Step-by-Step Guide

Step 1: Retrieve Video Records from Airtable 📥

Airtable Search Node:**  
  Setup: Configure the node to fetch video records (with essential fields like url and metadata) from your Airtable base.
  
Loop Over Items:**  
  Use a SplitInBatches node to process each video record individually.

Step 2: Scrape YouTube Transcripts Using Apify 🎬

Trigger Apify Actor:**  
  HTTP Request Node ("Apify NinjaPost"):  
    Method: POST  
    Endpoint: https://api.apify.com/v2/acts/topaz_sharingan~youtube-transcript-scraper-1/runs?token=&lt;YOUR_TOKEN&gt;  
    Payload Example:
            {
        "includeTimestamps": "Yes",
        "startUrls": ["{{ $json.url }}"]
      }
        Purpose: Initiates transcript scraping for each video URL.

Wait for Processing:**  
  Wait Node:  
    Duration: Approximately 1 minute to allow Apify to generate the transcript.

Retrieve Transcript Data:**  
  HTTP Request Node ("Get JSON TS"):  
    Method: GET  
    Endpoint: https://api.apify.com/v2/acts/topaz_sharingan~youtube-transcript-scraper-1/runs/last/dataset/items?token=&lt;YOUR_TOKEN&gt;

Step 3: Update Airtable with Transcript Data 🔄

Format Transcript Data:**  
  Code Node ("Code"):  
    Task: Convert the fetched transcript JSON into a formatted string.
            const jsonObject = items[0].json;
      const jsonString = JSON.stringify(jsonObject, null, 2);
      return { json: { stringifiedJson: jsonString } };
            
Extract the Video ID:**  
  Set Node ("Edit Fields"):  
    Expression:  
            {{$json.url.split('v=')[1].split('&')[0]}}
            
Update Airtable Record:**  
  Airtable Update Node ("Airtable1"):  
    Updates:  
      ts: Stores the transcript string.  
      videoid: Uses the extracted video ID to match the record.

Step 4: Process Transcripts into Semantic Chunks ✂️

Retrieve Updated Records:**  
  Airtable Search Node ("Airtable2"):  
    Purpose: Fetch records that now contain transcript data.

Parse and Chunk Transcripts:**  
  Code Node ("Code4"):  
    Functionality:  
      Parses transcript JSON.
      Converts "mm:ss" timestamps to seconds.
      Groups transcript entries into chunks based on a 3-second gap.
      Creates an object for each chunk that includes:
        Text: The transcript segment.
        Video Metadata: Video ID, title, description, published date, thumbnail.
        Chunk Details: Start and end timestamps.
        Direct URL: A link to the exact moment in the video (e.g., https://youtube.com/watch?v=VIDEOID&t=XXs).

Enrich & Split Text:**  
  Default Data Loader Node:  
    Attaches additional metadata (e.g., video title, description) to each chunk.
  Recursive Character Text Splitter Node:  
    Settings: Typically set to 500-character chunks with a 50-character overlap.
    Purpose: Ensures long transcript texts are broken into manageable segments for embedding.

Step 5: Generate Embeddings & Index in Pinecone 💾

Generate Embeddings:**  
  Embeddings OpenAI Node:  
    Task: Convert each transcript chunk into a vector embedding.
    Tip: Adjust the batch size (e.g., 512) based on your data volume.

Index in Pinecone:**  
  Pinecone Vector Store Node:  
    Configuration:  
      Index: Specify your Pinecone index (e.g., "videos").  
      Namespace: Use a dedicated namespace (e.g., "transcripts").
    Outcome: Each enriched transcript chunk is stored in Pinecone, ready for semantic retrieval by a separate retrieval agent.

🎉 Final Thoughts

This backend workflow is dedicated to processing and indexing YouTube video transcripts so that a separate retrieval agent can perform efficient semantic searches. With this setup:

Transcripts Are Indexed:**  
  Chunks of transcripts are enriched with metadata and stored as vector embeddings.

Instant Topic Retrieval:**  
  A retrieval agent (implemented separately) can later query Pinecone to find the exact moment in a video where a topic is discussed, thanks to the direct URL and metadata stored with each chunk.

Scalable & Modular:**  
  The separation between indexing and retrieval allows for easy updates and scalability.

Happy automating and enjoy building powerful search capabilities with your YouTube content! 🎉

## Template JSON

```
{
  "id": "Vlyhg8yXcCMMVq7k",
  "meta": {
    "instanceId": "7e4a2ed9435505e7ac8a1705caf648bc7288d77cc54adb476b4bec35afce8dbd"
  },
  "name": "YT RAG Agent Backend Transcript-format-pineconeUpsert",
  "tags": [],
  "nodes": [
    {
      "id": "308ee339-14ae-4920-8830-0756440f06b3",
      "name": "Airtable",
      "type": "n8n-nodes-base.airtable",
      "position": [
        40,
        260
      ],
      "parameters": {},
      "typeVersion": 2.1
    },
    {
      "id": "4a0324d8-27a0-468b-9a37-d7297c419cc0",
      "name": "Loop Over Items",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        240,
        260
      ],
      "parameters": {},
      "typeVersion": 3
    },
    {
      "id": "14e43ff8-16fd-45f6-b7d9-5ac7e4f10dfe",
      "name": "Airtable1",
      "type": "n8n-nodes-base.airtable",
      "onError": "continueErrorOutput",
      "position": [
        1180,
        340
      ],
      "parameters": {},
      "typeVersion": 2.1,
      "alwaysOutputData": true
    },
    {
      "id": "f1e16621-7642-42df-baff-fa943f5ec7f9",
      "name": "Wait",
      "type": "n8n-nodes-base.wait",
      "position": [
        540,
        340
      ],
      "webhookId": "bb544bfb-251a-497a-8a17-1b70e2a014c9",
      "parameters": {},
      "typeVersion": 1.1
    },
    {
      "id": "2a17f4a3-91be-465d-9318-f889b87b47ca",
      "name": "Apify NinjaPost",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        400,
        340
      ],
      "parameters": {},
      "typeVersion": 4.2
    },
    {
      "id": "a3071928-a592-4f26-a548-ac52cfb18ca6",
      "name": "Get JSON TS",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        680,
        340
      ],
      "parameters": {},
      "typeVersion": 4.2,
      "alwaysOutputData": true
    },
    {
      "id": "9216991d-e5de-4681-bab0-c20ddd00c77c",
      "name": "JSON Stringifier",
      "type": "n8n-nodes-base.code",
      "position": [
        820,
        340
      ],
      "parameters": {},
      "typeVersion": 2
    },
    {
      "id": "90db5c4e-e23e-4101-8465-10bbb686b658",
      "name": "Edit Fields",
      "type": "n8n-nodes-base.set",
      "position": [
        980,
        340
      ],
      "parameters": {},
      "typeVersion": 3.4
    },
    {
      "id": "c04e0167-8104-4149-8b81-09ebe7957e91",
      "name": "Airtable2",
      "type": "n8n-nodes-base.airtable",
      "position": [
        100,
        740
      ],
      "parameters": {},
      "typeVersion": 2.1
    },
    {
      "id": "b5132329-2385-4fb9-8d8a-ce838974c189",
      "name": "Pinecone Vector Store",
      "type": "@n8n/n8n-nodes-langchain.vectorStorePinecone",
      "position": [
        420,
        740
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "4c68d784-d86e-4f87-ad72-b2085cb998a1",
      "name": "Embeddings OpenAI",
      "type": "@n8n/n8n-nodes-langchain.embeddingsOpenAi",
      "position": [
        420,
        920
      ],
      "parameters": {},
      "typeVersion": 1.2
    },
    {
      "id": "6f641b5d-5716-4283-bd09-2bb746e41939",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -40,
        740
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "6ed623e3-0256-44ba-b3d2-c74ea7f38399",
      "name": "Transcript Processor",
      "type": "n8n-nodes-base.code",
      "position": [
        260,
        740
      ],
      "parameters": {},
      "typeVersion": 2
    },
    {
      "id": "5f77e165-4288-4e40-a381-23d2ef409752",
      "name": "Default Data Loader",
      "type": "@n8n/n8n-nodes-langchain.documentDefaultDataLoader",
      "position": [
        540,
        900
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "50495550-405a-4ab5-aa1c-dbd5731fa3f1",
      "name": "Recursive Character Text Splitter1",
      "type": "@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter",
      "position": [
        540,
        1060
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "aafb300a-7311-43a2-8bbe-67dfabfec313",
      "name": "Installation Tutorial",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -260,
        -760
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "89526f4d-4135-4cc1-87bc-4fcbf0bc213e",
  "connections": {
    "Wait": {
      "main": [
        [
          {
            "node": "Get JSON TS",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Airtable": {
      "main": [
        [
          {
            "node": "Loop Over Items",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Airtable1": {
      "main": [
        [
          {
            "node": "Loop Over Items",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Loop Over Items",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Airtable2": {
      "main": [
        [
          {
            "node": "Transcript Processor",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Edit Fields": {
      "main": [
        [
          {
            "node": "Airtable1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get JSON TS": {
      "main": [
        [
          {
            "node": "JSON Stringifier",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Apify NinjaPost": {
      "main": [
        [
          {
            "node": "Wait",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Loop Over Items": {
      "main": [
        [],
        [
          {
            "node": "Apify NinjaPost",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "JSON Stringifier": {
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
    "Embeddings OpenAI": {
      "ai_embedding": [
        [
          {
            "node": "Pinecone Vector Store",
            "type": "ai_embedding",
            "index": 0
          }
        ]
      ]
    },
    "Default Data Loader": {
      "ai_document": [
        [
          {
            "node": "Pinecone Vector Store",
            "type": "ai_document",
            "index": 0
          }
        ]
      ]
    },
    "Transcript Processor": {
      "main": [
        [
          {
            "node": "Pinecone Vector Store",
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
            "node": "Airtable2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Recursive Character Text Splitter1": {
      "ai_textSplitter": [
        [
          {
            "node": "Default Data Loader",
            "type": "ai_textSplitter",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
