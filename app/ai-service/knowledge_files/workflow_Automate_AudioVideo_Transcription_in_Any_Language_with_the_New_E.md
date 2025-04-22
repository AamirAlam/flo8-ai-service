# Automate Audio/Video Transcription in Any Language with the New ElevenLabs Model

**[View Template](https://n8n.io/workflows/3105-/)**  **Published Date:** 03/07/2025  **Created By:** phil  **Categories:** `Development` `Core Nodes`  

## Template Description

How it works  🗣️&gt; 📖

I set up this workflow to convert any audio or video file into structured text using the new ElevenLabs Scribe model, one of the best Speech-to-Text AIs, available in 99+ languages. This workflow integrates seamlessly with n8n and leverages the ElevenLabs Scribe API to:

This workflow seamlessly integrates with n8n to:
✅ Upload audio/video files automatically
✅ Transcribe them with industry-leading accuracy in any language
✅ Export the text for further processing (summaries, subtitles, SEO content, etc.)

👉 Try the new ElevenLabs Scribe model now: Convert speech to text instantly

Business Cases

🔹 Podcast Transcriptions – Convert podcast episodes into blog posts for SEO and accessibility
🔹 YouTube Subtitles – Generate captions automatically for increased engagement
🔹 Legal & Compliance – Accurately transcribe meetings, interviews, or customer calls
🔹 E-learning – Turn lectures and webinars into structured course notes
🔹 SEO & Content Marketing – Repurpose videos into articles, quotes, and social media content

💡 Boost your productivity with the new Scribe model → Start with ElevenLabs Scribe

Set up steps

🚀 Quick & simple setup in n8n – Upload your file, select the model (scribe_v1), and let the AI handle the rest via the ElevenLabs API.

⸻

📢 Why I Chose the New ElevenLabs Scribe Model?
I wanted the most accurate and reliable transcription tool for my workflow. After testing different options, Scribe outperformed Google Gemini & OpenAI Whisper in independent benchmarks. It delivers high-quality transcriptions, even in underserved languages like Serbian, Mongolian, and many more.

✅ Transcribes in 99+ languages
✅ Fast, accurate, and easy to integrate
✅ Suitable for content creators, businesses, and professionals


🔗 Get started now and revolutionize your workflow with the new Scribe model →  Try Scribe AI today 🚀

Phil | Inforeole

## Template JSON

```
{
  "meta": {
    "instanceId": "c911aed9995230b93fd0d9bc41c258d697c2fe97a3bab8c02baf85963eeda618"
  },
  "nodes": [
    {
      "id": "fe599878-c955-4354-bbd0-a24fc1e3e933",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -340,
        -40
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "e03c7cef-4897-4234-b285-7be69e3c970d",
      "name": "Create Transcript1",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        100,
        -40
      ],
      "parameters": {
        "url": "https://api.elevenlabs.io/v1/speech-to-text",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "contentType": "multipart-form-data",
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "file",
              "parameterType": "formBinaryData",
              "inputDataFieldName": "data"
            },
            {
              "name": "model_id",
              "value": "scribe_v1"
            }
          ]
        },
        "genericAuthType": "httpCustomAuth",
        "headerParameters": {
          "parameters": [
            {
              "name": "Content-Type",
              "value": "multipart/form-data"
            }
          ]
        }
      },
      "credentials": {
        "httpCustomAuth": {
          "id": "rDkSKjIA0mjmEv5k",
          "name": "Eleven Labs"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "ea48aabf-1d93-41b4-84a0-53115aba53b4",
      "name": "Read/Write Files from Disk",
      "type": "n8n-nodes-base.readWriteFile",
      "position": [
        -120,
        -40
      ],
      "parameters": {
        "options": {},
        "fileSelector": "/files/tmp/tst1.mp4"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Read/Write Files from Disk": {
      "main": [
        [
          {
            "node": "Create Transcript1",
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
            "node": "Read/Write Files from Disk",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
