# Extract and Clean YouTube Video Transcripts with RapidAPI

**[View Template](https://n8n.io/workflows/3417-/)**  **Published Date:** 04/03/2025  **Created By:** Joseph  **Categories:** `Development` `Core Nodes`  

## Template Description

Here is your refined template description with detailed step-by-step instructions, markdown formatting, and customization guidance.  

YouTube Transcript Extraction Workflow  

This n8n workflow extracts and processes transcripts from YouTube videos using the YouTube Transcript API on RapidAPI. It allows users to retrieve subtitles from YouTube videos, clean them up, and return structured transcript data for further processing.  

Table of Contents  
Problem Statement & Target Audience  
Pre-conditions & API Requirements  
Step-by-Step Workflow Explanation  
Customization Guide  
How to Set Up This Workflow  

Problem Statement & Target Audience  

Who is this for?  
This workflow is ideal for content creators, researchers, and developers who need to:  
Extract subtitles from YouTube videos automatically.  
Format and clean** transcript data for readability.  
Use transcripts for summarization, content repurposing, or language analysis.  

Pre-conditions & API Requirements  

API Required  
YouTube Transcript API** (RapidAPI)  

n8n Setup Prerequisites  
A running n8n instance (Installation Guide)  
A RapidAPI account to access the YouTube Transcript API  
An API key from RapidAPI to authenticate requests  

Step-by-Step Workflow Explanation  

1. Input YouTube Video URL (Trigger)  
This step provides a simple input form where users enter a YouTube video URL.  

2. HTTP Request Node (Retrieve Transcript Data)  
Makes a POST request to the YouTube Transcript API via RapidAPI.  
Passes the video URL received from the input form.  
Uses an environment variable to store the API key securely.  

3. Function Node (Process Transcript)  
Receives* the API response containing the *raw transcript**.  
Processes and cleans** the transcript:  
  Removes unwanted characters.  
  Formats text for readability.  
Handles errors** when no transcript is available.  
Outputs* both the *raw and cleaned transcript** for further use.  

4. Set Field Node (Response Formatting)  
Structures** the processed transcript data into a user-friendly format.  
Returns** the final transcript data to the client.  

Customization Guide  

1. Modify Transcript Cleaning Rules  
Update the Function Node to apply custom text processing, such as:  
  Removing timestamps.  
  Changing the output format (e.g., JSON, plain text).  

2. Store Transcripts in a Database  
Add a Database Node (e.g., MySQL, PostgreSQL, or Firebase) to save transcripts.  

3. Generate Summaries from Transcripts  
Integrate AI services (e.g., OpenAI, Google Gemini) to summarize transcripts.  

4. Convert Transcripts into Speech  
Use ElevenLabs API to generate an AI-powered voiceover from transcripts.  

How to Set Up This Workflow  

Step 1: Import the Workflow into n8n  
Download or copy the workflow JSON file.  
Import it into your n8n instance.  

Step 2: Set Up the API Key  
Sign up for the YouTube Transcript API.  
Subscribe to the api.  
Copy and paste your api key where the "your_api_key" is.

Step 3: Activate the Workflow  
Start the workflow in n8n.  
Enter a YouTube video URL in the input form.  
The workflow will return a cleaned transcript.  

This workflow ensures seamless YouTube transcript extraction and processing with minimal manual effort. 🚀

## Template JSON

```
{
  "id": "XxkmcgZC4OtIOVoD",
  "meta": {
    "instanceId": "b3c467df4053d13fe31cc98f3c66fa1d16300ba750506bfd019a0913cec71ea3"
  },
  "name": "Youtube Video Transcript Extraction",
  "tags": [],
  "nodes": [
    {
      "id": "686e639a-650d-480d-9887-11bd4140f1fe",
      "name": "YoutubeVideoURL",
      "type": "n8n-nodes-base.formTrigger",
      "position": [
        -20,
        0
      ],
      "webhookId": "156a04c8-917d-4624-a46e-8fbcab89d16b",
      "parameters": {
        "options": {},
        "formTitle": "Youtube Video Transcriber",
        "formFields": {
          "values": [
            {
              "fieldLabel": "Youtube Video Url",
              "requiredField": true
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "5384c4ed-a726-4253-8a88-d413124f80be",
      "name": "cleanedTranscript",
      "type": "n8n-nodes-base.set",
      "position": [
        740,
        0
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "7653a859-556d-4e00-bafa-6f70f90de0d7",
              "name": "transcript",
              "type": "string",
              "value": "={{ $json.cleanedTranscript }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "83b6567f-c931-429c-8d7c-0b2549820ca1",
      "name": "processTranscript",
      "type": "n8n-nodes-base.function",
      "position": [
        500,
        0
      ],
      "parameters": {
        "functionCode": "// Extract and process the transcript\nconst data = $input.first().json;\n\nif (!data.transcript && !data.text) {\n  return {\n    json: {\n      success: false,\n      message: 'No transcript available for this video',\n      videoUrl: $input.first().json.body?.videoUrl || 'Unknown'\n    }\n  };\n}\n\n// Process the transcript text\nlet transcriptText = '';\n\n// Handle different API response formats\nif (data.transcript) {\n  // Format for array of transcript segments\n  if (Array.isArray(data.transcript)) {\n    data.transcript.forEach(segment => {\n      if (segment.text) {\n        transcriptText += segment.text + ' ';\n      }\n    });\n  } else if (typeof data.transcript === 'string') {\n    transcriptText = data.transcript;\n  }\n} else if (data.text) {\n  // Format for single transcript object with text property\n  transcriptText = data.text;\n}\n\n// Clean up the transcript (remove extra spaces, normalize punctuation)\nconst cleanedTranscript = transcriptText\n  .replace(/\\s+/g, ' ')\n  .replace(/\\s([.,!?])/g, '$1')\n  .trim();\n\nreturn {\n  json: {\n    success: true,\n    videoUrl: $input.first().json.body?.videoUrl || 'From transcript',\n    rawTranscript: data.text || data.transcript,\n    cleanedTranscript,\n    duration: data.duration,\n    offset: data.offset,\n    language: data.lang\n  }\n};"
      },
      "typeVersion": 1
    },
    {
      "id": "cebf0fd7-6b66-4287-bede-fab53061bed2",
      "name": "extractTranscript",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        240,
        0
      ],
      "parameters": {
        "url": "https://youtube-transcript3.p.rapidapi.com/api/transcript",
        "options": {},
        "sendBody": true,
        "sendQuery": true,
        "sendHeaders": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "url",
              "value": "={{ $json['Youtube Video Url'] }}"
            }
          ]
        },
        "queryParameters": {
          "parameters": [
            {
              "name": "videoId",
              "value": "ZacjOVVgoLY"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "x-rapidapi-host",
              "value": "youtube-transcript3.p.rapidapi.com"
            },
            {
              "name": "x-rapidapi-key",
              "value": "\"your_api_key\""
            },
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        }
      },
      "typeVersion": 3
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "084b006b-36f9-46a7-8a0b-7656126b29cd",
  "connections": {
    "YoutubeVideoURL": {
      "main": [
        [
          {
            "node": "extractTranscript",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "extractTranscript": {
      "main": [
        [
          {
            "node": "processTranscript",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "processTranscript": {
      "main": [
        [
          {
            "node": "cleanedTranscript",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
