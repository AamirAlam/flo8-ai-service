# Convert Text to Speech with Local KOKORO TTS

**[View Template](https://n8n.io/workflows/3547-/)**  **Published Date:** 04/14/2025  **Created By:** bswlife  **Categories:**   

## Template Description

Disclaimer
The Execute Command node is only supported on self-hosted (local) instances of n8n.

Introduction


KOKORO TTS - Kokoro TTS is a compact yet powerful text-to-speech model, currently available on Hugging Face and GitHub. Despite its modest size—trained on less than 100 hours of audio—it delivers impressive results, consistently topping the TTS leaderboard on Hugging Face. Unlike larger systems, Kokoro TTS offers the advantage of running locally, even on devices without GPUs, making it accessible for a wide range of users.

Who will benefit from this integration?

This will be useful for video bloggers, TikTokers, and it will also enable the creation of a free voice chat bot. Currently, TTS models are mostly paid, but this integration will allow for fully free voice generation. The possibilities are limited only by your imagination.

Note
Unfortunately, we can't interact with the KOKORO API via browser URL (GET/POST), 
but we can run a Python script through n8n and pass any variables to it.

In the tutorial, the D drive is used, but you can rewrite this for any paths, including the C drive.

Step 1 

You need to have Python installed. link
Also, download and extract the portable version of KOKORO from GitHub.

Create a file named voicegen.py with the following code in the KOKORO folder: (C:\KOKORO). As you can see, the output path is: (D:\output.mp3).

import sys
import shutil
from gradio_client import Client

Set UTF-8 encoding for stdout
sys.stdout.reconfigure(encoding='utf-8')

Get arguments from command line
text = sys.argv[1] # First argument: input text
voice = sys.argv[2] # Second argument: voice
speed = float(sys.argv[3]) # Third argument: speed (converted to float)

print(f"Received text: {text}")
print(f"Voice: {voice}")
print(f"Speed: {speed}")

Connect to local Gradio server
client = Client("http://localhost:7860/")

Generate speech using the API
result = client.predict(
text=text,
voice=voice,
speed=speed,
api_name="/generate_speech"
)

Define output path
output_path = r"D:\output.mp3"

Move the generated file
shutil.move(result[1], output_path)

Print output path
print(output_path)

Step 2
Go to n8n and create the following workflow.

Step 3
Edit Field Module.
{
  "voice": "af_sarah",
  "text": "Hello world!"
}
Step 4 
We’ll need an Execute Command module with the command: python 
C:\KOKORO\voicegen.py “{{ $json.text }}” “{{ $json.voice }}” 1

Step 5 
The script is already working, but to listen to it, you can connect a Binary module with the path to the generated MP3 file 
D:/output.mp3

Step 6
Click “Text workflow” and enjoy the result.

There are more voices and accents than in ChatGPT, plus it’s free.

P.S.
If you want, there is a detailed tutorial on my blog.



## Template JSON

```
{
  "meta": {
    "instanceId": "a6d5191e58fd6be87222f47435e6f9df8f98ec0d945d3e7b7f6373c59a6c3f37",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "fcf1064e-557f-4514-9109-bb10ac837f8b",
      "name": "Run python script",
      "type": "n8n-nodes-base.executeCommand",
      "position": [
        -100,
        20
      ],
      "parameters": {
        "command": "=python C:\\KOKORO\\voicegen.py \"{{ $json.text }}\" \"{{ $json.voice }}\" 1\n"
      },
      "typeVersion": 1
    },
    {
      "id": "199a3212-69c0-4314-92c8-783573f165d7",
      "name": "Passing variables",
      "type": "n8n-nodes-base.set",
      "position": [
        -320,
        20
      ],
      "parameters": {
        "mode": "raw",
        "options": {},
        "jsonOutput": "{\n  \"voice\": \"af_sarah\",\n  \"text\": \"Hello world!\"\n}\n"
      },
      "typeVersion": 3.4
    },
    {
      "id": "deb008d0-53ae-4348-a555-9e54b6e0efd4",
      "name": "Start",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -540,
        20
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "ffa1b2bf-abc3-45d8-8b7b-de4c0780a609",
      "name": "Play sound",
      "type": "n8n-nodes-base.readBinaryFiles",
      "position": [
        120,
        20
      ],
      "parameters": {
        "fileSelector": "D:/output.mp3"
      },
      "typeVersion": 1,
      "alwaysOutputData": false
    }
  ],
  "pinData": {},
  "connections": {
    "Start": {
      "main": [
        [
          {
            "node": "Passing variables",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Passing variables": {
      "main": [
        [
          {
            "node": "Run python script",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Run python script": {
      "main": [
        [
          {
            "node": "Play sound",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
