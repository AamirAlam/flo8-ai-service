# Generate and Content From Google Sheets to X with GPT-4

**[View Template](https://n8n.io/workflows/3161-generate-and-content-from-google-sheets-to-x-with-gpt-4/)**  
**Published Date:** 03/14/2025  
**Created By:** Subham Singh  
**Categories:** `AI`, `Marketing`  

## Template Description

### 🧑‍💻 Who is this for?
This workflow is perfect for social media managers, content creators, and digital marketers who want to save time by automating social media post generation and publishing across platforms.

### 📌 What problem does this solve?
Manually generating and scheduling social media content is time-consuming and repetitive. This workflow automates content creation and publishing, allowing you to:

* Streamline content generation using AI  
* Ensure consistent posting across social media platforms  
* Track published posts in Google Sheets  

### 🔍 What this workflow does:
1. **Fetches content ideas** from a Google Sheet.  
2. **Generates social media posts** using OpenAI's GPT-4.  
3. **Checks the target platform** (e.g., Twitter/X, LinkedIn).  
4. **Posts the content** to the chosen social media platform.  
5. **Updates the Google Sheet** with the generated post and timestamp.  

### 🛠️ Setup Guide:
1. **Connect Google Sheets**: Ensure you have a Google Sheet with content ideas (columns: `Idea`, `Status`, `Generated Post`).  
2. **Set up OpenAI API Key**: Provide your OpenAI API key for GPT-4.  
3. **Configure Social Media Accounts**: Link your Twitter/X or other social media accounts using n8n's built-in nodes.  
4. **Test the Workflow**: Run the workflow to verify automation.  
5. **Schedule Automation**: Set a recurring trigger (e.g., daily) to automate posting.  

### 🔧 Customization Tips:
* Adjust prompt inputs in the OpenAI node to tailor the tone and style.  
* Add more platforms (e.g., Instagram, Facebook) by duplicating the social media node.  
* Include analytics tracking for engagement insights.  

### 📊 Example Use Cases:
* Automatically generate and share daily motivational quotes.  
* Post product updates and announcements.  
* Share curated industry news and insights.  

This workflow saves time and keeps your social media presence active and engaging effortlessly. 🚀


## Template JSON

```
{
  "nodes": [
    {
      "name": "Get Content Ideas",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        200,
        300
      ],
      "parameters": {
        "range": "Sheet1!A:C",
        "sheetId": "YOUR_GOOGLE_SHEET_ID"
      },
      "credentials": {
        "googleSheetsOAuth2Api": "YOUR_GOOGLE_SHEETS_CREDENTIALS"
      },
      "typeVersion": 1
    },
    {
      "name": "Generate Post with OpenAI",
      "type": "n8n-nodes-base.openAi",
      "position": [
        500,
        300
      ],
      "parameters": {
        "model": "gpt-4",
        "prompt": "Create a social media post for {{$node[\"Get Content Ideas\"].json[\"Platform\"]}} based on this idea: {{$node[\"Get Content Ideas\"].json[\"Idea\"]}}. Keep it engaging and concise."
      },
      "credentials": {
        "openAIApi": "YOUR_OPENAI_CREDENTIALS"
      },
      "typeVersion": 1
    },
    {
      "name": "Check Platform",
      "type": "n8n-nodes-base.if",
      "position": [
        800,
        300
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "{{$node[\"Get Content Ideas\"].json[\"Platform\"]}}",
              "value2": "Twitter",
              "operation": "equal"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Post to Twitter",
      "type": "n8n-nodes-base.twitter",
      "position": [
        1000,
        200
      ],
      "parameters": {
        "text": "{{$node[\"Generate Post with OpenAI\"].json[\"text\"]}}"
      },
      "credentials": {
        "twitterOAuth1Api": "YOUR_TWITTER_CREDENTIALS"
      },
      "typeVersion": 1
    },
    {
      "name": "Update Google Sheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1200,
        300
      ],
      "parameters": {
        "range": "Sheet1!D:F",
        "values": "Posted,{{$node[\"Generate Post with OpenAI\"].json[\"text\"]}},{{Date.now()}}",
        "sheetId": "YOUR_GOOGLE_SHEET_ID",
        "updateOperation": "append"
      },
      "credentials": {
        "googleSheetsOAuth2Api": "YOUR_GOOGLE_SHEETS_CREDENTIALS"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Check Platform": {
      "main": [
        [
          {
            "node": "Post to Twitter",
            "type": "main"
          }
        ]
      ]
    },
    "Post to Twitter": {
      "main": [
        [
          {
            "node": "Update Google Sheet",
            "type": "main"
          }
        ]
      ]
    },
    "Get Content Ideas": {
      "main": [
        [
          {
            "node": "Generate Post with OpenAI",
            "type": "main"
          }
        ]
      ]
    },
    "Generate Post with OpenAI": {
      "main": [
        [
          {
            "node": "Check Platform",
            "type": "main"
          }
        ]
      ]
    }
  }
}
```