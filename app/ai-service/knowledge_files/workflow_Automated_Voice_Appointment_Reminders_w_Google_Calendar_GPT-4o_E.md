# Automated Voice Appointment Reminders w/ Google Calendar, GPT-4o, ElevenLabs, Gmail

**[View Template](https://n8n.io/workflows/3194-/)**  **Published Date:** 03/17/2025  **Created By:** phil  **Categories:** `Development` `Core Nodes` `Productivity` `Communication` `HITL` `AI` `Langchain`  

## Template Description

This workflow automates voice reminders for upcoming appointments by generating a professional audio message and sending it to clients via email with the voice file attached.

It integrates Google Calendar to track appointments, ElevenLabs to generate high-quality voice messages, and Gmail to deliver them efficiently.

Who Needs Automated Voice Appointment Reminders?

This automated voice appointment reminder system is ideal for businesses that rely on scheduled appointments. It helps reduce no-shows, improve client engagement, and streamline communication.

Medical Offices & Clinics – Ensure patients receive timely appointment reminders.
Real Estate Agencies – Keep potential buyers and renters informed about property visits.
Service-Based Businesses – Perfect for salons, consultants, therapists, and coaches.
Legal & Financial Services – Help clients remember important meetings and consultations.

If your business depends on scheduled appointments, this workflow saves time and enhances client satisfaction. 🚀

Why Use This Workflow?

Ensures clients receive timely reminders.
Reduces appointment no-shows and scheduling issues.
Automates the process with a personalized voice message.

Step-by-Step: How This Workflow Automates Voice Reminders

Trigger the Workflow – The system runs manually or on a schedule to check upcoming appointments in Google Calendar.
Retrieve Appointment Data – It fetches event details (client name, time, and location) from Google Calendar.
Generate a Voice Reminder – Using ElevenLabs, the workflow converts the appointment details into a natural-sounding voice message.
Send via Email – The generated audio file is attached to an email and sent to the client as a reminder.

Customization: Tailor the Workflow to Your Business Needs

Adjust Trigger Frequency – Modify the scheduling to run daily, hourly, or at specific intervals.
Customize Voice Message Format – Change the script structure and voice tone to match your business needs.
Change Notification Method – Instead of email, integrate SMS or WhatsApp for delivery.

🔑 Prerequisites

Google Calendar Access** – Ensure you have access to the calendar with scheduled appointments.
ElevenLabs API Key – Required for generating voice messages (you can start for free).
Gmail API Access** – Needed for sending reminder emails.
n8n Setup** – The workflow runs on an n8n instance (self-hosted or cloud).

🚀 Step-by-Step Installation & Setup

Set Up Google Calendar API**
	Go to Google Cloud Console.
	Create a new project and enable Google Calendar API.
	Generate OAuth 2.0 credentials and save them for n8n.

Get an ElevenLabs API Key**
	Sign up at ElevenLabs.
	Retrieve your API key from the dashboard.

Configure Gmail API**
	Enable Gmail API in Google Cloud Console.
	Create OAuth credentials and authorize your email address for sending.

Deploy n8n & Install the Workflow**
	Install n8n (Installation Guide).
	Add the required Google Calendar, ElevenLabs, and Gmail nodes.
	Import or build the workflow with the correct credentials.
	Test and fine-tune as needed.

⚠ Important:
The LangChain Community node used in this workflow only works on self-hosted n8n instances. It is not compatible with n8n Cloud. Please ensure you are running a self-hosted instance before using this workflow.

─── ◇ ❖ ◇ ───

This workflow ensures a professional and seamless experience for your clients, keeping them informed and engaged. 🚀🔊

Phil | Inforeole 

## Template JSON

```
{
  "meta": {
    "instanceId": "c911aed9995230b93fd0d9bc41c258d697c2fe97a3bab8c02baf85963eeda618"
  },
  "nodes": [
    {
      "id": "4b970a76-2629-4b57-80ab-0bef20c7d2fe",
      "name": "When clicking 'Test workflow'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -160,
        280
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "e1f81dc4-1399-42f8-8817-4952d7db0e47",
      "name": "Basic LLM Chain",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "position": [
        280,
        180
      ],
      "parameters": {
        "text": "=name: {{ $json.summary }}\ntime: {{ $json.start.dateTime }}\naddress: {{ $json.location }}\nToday's date: {{ $now }}",
        "messages": {
          "messageValues": [
            {
              "message": "=You are an assistant. You will create a structured message in JSON.\n\n**\nmessage:\nGenerate a voice script reminder for a real estate appointment. The message should be clear, professional, and engaging.\n\nIt must include:\n1. The recipient's name.\n2. The date and time of the appointment, expressed naturally (e.g., at noon, quarter past noon, half past three, quarter to five).\n3. The complete address of the property, expressed naturally (e.g., 12 Baker Street in London, Madison Avenue in New York, 5 Oakwood Drive in Los Angeles).\n4. A mention of the sender: Mr. John Carpenter from Super Agency.\n5. A confirmation sentence or an invitation to contact if needed.\n\nInput variables:\n\u2022 Recipient's name (prefixed with Mr. or Ms.)\n\u2022 Time: Appointment time\n\u2022 Address: Complete property address (only the street, number, and city; not the postal code)\n\nThe tone should be cordial and professional, suitable for an automated voice message.\n\nExample expected output: \"Hello Mrs. Richard, this is Mr. John Carpenter from Super Immo Agency.\nI am reminding you of your appointment scheduled for tomorrow at 8:15, at 63 Taverniers Road in Talence. If you have any questions or need to reschedule, please do not hesitate to contact me. See you tomorrow and have a great day!\"\n\n**\nmail_object: a very short email subject\nExample: Your appointment reminder for tomorrow"
            }
          ]
        },
        "promptType": "define",
        "hasOutputParser": true
      },
      "typeVersion": 1.5
    },
    {
      "id": "3a071328-4160-4e95-9d86-fee74e7984c3",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        260,
        400
      ],
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "options": {}
      },
      "credentials": {
        "openAiApi": {
          "id": "Vx8lWByqVzq0mm68",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "5ac0dab0-ac52-4cc1-9e59-564c6c16f9e0",
      "name": "Structured Output Parser",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "position": [
        460,
        400
      ],
      "parameters": {
        "schemaType": "manual",
        "inputSchema": "{\n  \"type\": \"object\",\n  \"properties\": {\n    \"message\": {\n      \"type\": \"string\"\n    },\n    \"mail_object\": {\n      \"type\": \"string\"\n    }\n  }\n}"
      },
      "typeVersion": 1.2
    },
    {
      "id": "eb5fd7f8-d29e-423f-aa26-8a84b7ad1afc",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -160,
        80
      ],
      "parameters": {
        "rule": {
          "interval": [
            {}
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "ac8c36e8-f30c-44a8-b584-3d28e6ff8744",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        580,
        20
      ],
      "parameters": {
        "width": 260,
        "height": 120,
        "content": "## ElevenlabsAPI key\n**Click** to get your Elevenlabs  API key. [Elevenlabs](https://try.elevenlabs.io/text-audio)"
      },
      "typeVersion": 1
    },
    {
      "id": "fda6cf6c-909d-4013-b6ec-5d0264368cad",
      "name": "Change filename",
      "type": "n8n-nodes-base.code",
      "position": [
        880,
        180
      ],
      "parameters": {
        "jsCode": "/*\n * Filename: addFileName.js\n * Purpose: Add a file name to binary data in an n8n workflow using mail_object from input\n */\n\nconst mailObject = $input.first().json.output.mail_object;\nconst fileName = `${mailObject}.mp3`;\n\nreturn items.map(item => {\n  if (item.binary && item.binary.data) {\n    item.binary.data.fileName = fileName;\n  }\n  return item;\n});"
      },
      "typeVersion": 2
    },
    {
      "id": "7f1377c8-4048-44b7-800d-83a530bbd57c",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1020,
        20
      ],
      "parameters": {
        "width": 300,
        "height": 120,
        "content": "## Gmail API Credentials  \n**Click here** to view the [documentation](https://docs.n8n.io/integrations/builtin/credentials/google/) and configure your access permissions for the Google Gmail API."
      },
      "typeVersion": 1
    },
    {
      "id": "301b762b-7e8f-4aa8-b476-de21a79f6c97",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        0
      ],
      "parameters": {
        "width": 300,
        "height": 140,
        "content": "## Calendar API Credentials  \n**Click here** to view the [documentation](https://docs.n8n.io/integrations/builtin/credentials/google/) and configure your access permissions for the Google Calendar API."
      },
      "typeVersion": 1
    },
    {
      "id": "fa738922-8cf0-48be-8d29-e98c560cb993",
      "name": "Generate Voice Reminder",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        660,
        180
      ],
      "parameters": {
        "url": "https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "sendQuery": true,
        "authentication": "genericCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "text",
              "value": "={{ $json.output.message }}"
            },
            {
              "name": "model_id",
              "value": "eleven_multilingual_v2"
            }
          ]
        },
        "genericAuthType": "httpCustomAuth",
        "queryParameters": {
          "parameters": [
            {
              "name": "output_format",
              "value": "mp3_22050_32"
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
      "notesInFlow": true,
      "retryOnFail": true,
      "typeVersion": 4.2
    },
    {
      "id": "9ee109fc-ff6d-48cb-8067-fd4a8be15845",
      "name": "Send Voice Reminder",
      "type": "n8n-nodes-base.gmail",
      "position": [
        1100,
        180
      ],
      "webhookId": "5ba2c8cb-84f1-4363-8410-b8d138286c3a",
      "parameters": {
        "sendTo": "={{ $('Get Appointements').item.json.attendees[0].email }}",
        "message": "=\ud83d\udc47 Information for tomorrow \ud83d\udde3\ufe0f",
        "options": {
          "senderName": "John Carpenter",
          "attachmentsUi": {
            "attachmentsBinary": [
              {}
            ]
          },
          "appendAttribution": false
        },
        "subject": "={{ $('Basic LLM Chain').item.json.output.mail_object }}"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "IQ6yVYCzI1vS0w0k",
          "name": "Gmail credentials"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "d2dd427e-0cda-4dc0-ba71-2843f4fcc4aa",
      "name": "Get Appointements",
      "type": "n8n-nodes-base.googleCalendar",
      "position": [
        60,
        180
      ],
      "parameters": {
        "limit": 2,
        "options": {},
        "timeMax": "={{ $now.plus({ day: 2 }) }}",
        "calendar": {
          "__rl": true,
          "mode": "list",
          "value": "mymail@gmail.com",
          "cachedResultName": "mymail@gmail.com"
        },
        "operation": "getAll"
      },
      "credentials": {
        "googleCalendarOAuth2Api": {
          "id": "p07CrLRfaqU0LAaC",
          "name": "Google Calendar credentials"
        }
      },
      "typeVersion": 1.3
    }
  ],
  "pinData": {},
  "connections": {
    "Basic LLM Chain": {
      "main": [
        [
          {
            "node": "Generate Voice Reminder",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Change filename": {
      "main": [
        [
          {
            "node": "Send Voice Reminder",
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
            "node": "Get Appointements",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Appointements": {
      "main": [
        [
          {
            "node": "Basic LLM Chain",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Basic LLM Chain",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Generate Voice Reminder": {
      "main": [
        [
          {
            "node": "Change filename",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Structured Output Parser": {
      "ai_outputParser": [
        [
          {
            "node": "Basic LLM Chain",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "When clicking 'Test workflow'": {
      "main": [
        [
          {
            "node": "Get Appointements",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
