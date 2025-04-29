# Transform Press Releases (PDF & Word) into Polished Articles with Gmail & OpenAI

**[View Template](https://n8n.io/workflows/3302-/)**  **Published Date:** 03/24/2025  **Created By:** Julian Reich   **Categories:** `Development` `Core Nodes` `Data & Storage` `Communication` `HITL` `AI` `Langchain`  

## Template Description

This n8n workflow automates the transformation of press releases into polished articles. It converts the content of an email and its attachments (PDF or Word documents) into an AI-written article/blog post. 

What does it do?
This workflow assists editors and journalists in managing incoming press-releases from governments, companies, NGOs, or individuals. The result is a draft article that can easily be reviewed by the editor, who receives it in a reply email containing both the original input and the output, plus an AI-generated self-assessment. This self-assessment represents an additional feedback loop where the AI compares the input with the output to evaluate the quality and accuracy of its transformation.

How does it work?
Triggered by incoming emails in Google, it first filters attachments, retaining only Word and PDF files while removing other formats like JPGs. The workflow then follows one of three paths:

    If no attachments remain, it processes the inline email message directly.
    For PDF attachments, it uses an extractor to obtain the document content.
    For Word attachments, it extracts the text content by a http request.

In each case, the extracted content is then passed to an AI agent that converts the press release into a well-structured article according to predefined prompts. A separate AI evaluation step provides a self-assessment by comparing the output with the original input to ensure quality and accuracy. Finally, the workflow generates a reply email to the sender containing three components: the original input, the AI-generated article, and the self-assessment. This streamlined process helps editors and journalists efficiently manage incoming press releases, delivering draft articles that require minimal additional editing."  

How to set it up
1. Configure Gmail Connection: 
Create or use an existing Gmail address
Connect it through the n8n credentials manager
Configure polling frequency according to your needs
Set the trigger event to "Message Received"
        Optional: Filter incoming emails by specifying authorized senders
Enable the "Download Attachments" option

2. Set Up AI Integration:
Create an OpenAI account if you don't have one
Create a new AI assistant or use an existing one
Customize the assistant with specific instructions, style guidelines, or response templates
Configure your API credentials in n8n to enable the connection

3. Configure Google Drive Integration:
Connect your Google Drive credentials in n8n
Set the operation mode to "Upload"
Configure the input data field name as "data"
-Set the file naming format to dynamic: {{ $json.fileName }}

4. Configure HTTP Request Node:
Set request method to "POST"
Enter the appropriate Google API endpoint URL
Include all required authorization headers
Structure the request body according to API specifications
Ensure proper error handling for API responses

5. Configure HTTP Request Node 2:

Set request method to "GET"
Enter the appropriate Google API endpoint URL
Include all required authorization headers
Configure query parameters as needed
Implement response validation and error handling

6.  Configure Self-Assessment Node:

Set operation to "Message a Model"
Select an appropriate AI model (e.g., GPT-4, Claude)
Configure the following prompt in the Message field:



Please analyze and compare the following input and output content:

(for example)

Original Input:
{{ $('HTTP Request3').item.json.data }}
{{ $('Gmail Trigger').item.json.text }}

Generated Output:
{{ $json.output }}

Provide a detailed self-assessment that evaluates:
Content accuracy and completeness
Structure and readability improvements
Tone and style appropriateness
Any information that may have been omitted or misrepresented
Overall quality of the transformation

7. Configure Reply Email Node:

Set operation to "Send" and select your Gmail account
Configure the "To" field to respond to the original sender: {{ $('Gmail Trigger').item.json.from }}
Set an appropriate subject line: RE: {{ $('Gmail Trigger').item.json.subject }}
Structure the email body with clear sections using the following template:

handlebars

EDITED ARTICLE*   

{{ $('AI Article Writer 2').item.json.output }}

SELF-ASSESSMENT*
Rating: 1 (poor) to 5 (excellent)
{{ $json.message.content }}

ORIGINAL MESSAGE*

{{ $('Gmail Trigger').item.json.text }}

ATTACHMENT CONTENT*

{{ $('HTTP Request3').item.json.data }}

    Note: Adjust the template fields according to the input source (PDF, Word document, or inline message). For inline messages, you may not need the "ATTACHMENT CONTENT" section.


## Template JSON

```
{
  "id": "l1wMIoms9BgoA2lV",
  "meta": {
    "instanceId": "05b0588df0f58c91cb668a930710fae1c12db867675e52c5c2912a7beee5342b",
    "templateCredsSetupCompleted": true
  },
  "name": "\"E-Mail to article/blog post\" - converter",
  "tags": [],
  "nodes": [
    {
      "id": "e24d8d7a-88b2-4ee2-9c38-4b6f4a88102c",
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmailTrigger",
      "position": [
        -100,
        360
      ],
      "parameters": {
        "simple": false,
        "filters": {
          "sender": "*@somedia.ch"
        },
        "options": {
          "downloadAttachments": true,
          "dataPropertyAttachmentsPrefixName": "attachment_"
        },
        "pollTimes": {
          "item": [
            {
              "mode": "everyX",
              "unit": "minutes",
              "value": 1
            }
          ]
        }
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "PNLoTfL8jP1YyGjJ",
          "name": "Gmail account 2"
        }
      },
      "notesInFlow": false,
      "typeVersion": 1.2
    },
    {
      "id": "b265f364-b246-4244-ab77-9812b90817e1",
      "name": "Extrahiere aus PDF1",
      "type": "n8n-nodes-base.extractFromFile",
      "position": [
        1120,
        -80
      ],
      "parameters": {
        "options": {},
        "operation": "pdf"
      },
      "typeVersion": 1
    },
    {
      "id": "2ff7ca6c-7ba6-4526-94fc-cb82b052648a",
      "name": "HTTP Request2",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1260,
        280
      ],
      "parameters": {
        "url": "=https://www.googleapis.com/drive/v3/files/{{$json[\"id\"]}}/copy\n",
        "method": "POST",
        "options": {},
        "jsonBody": "{\n  \"mimeType\": \"application/vnd.google-apps.document\"\n}\n",
        "sendBody": true,
        "jsonHeaders": "{\n  \"Authorization\": \"Bearer {{$credentials.googleDriveOAuth2.access_token}}\",\n  \"Content-Type\": \"application/json\"\n}\n",
        "sendHeaders": true,
        "specifyBody": "json",
        "authentication": "predefinedCredentialType",
        "specifyHeaders": "json",
        "nodeCredentialType": "googleDocsOAuth2Api"
      },
      "credentials": {
        "oAuth2Api": {
          "id": "INVJ4n7OLXgPI372",
          "name": "Unnamed credential"
        },
        "googleDocsOAuth2Api": {
          "id": "AeVFb8EMLqLEn7Db",
          "name": "Google Docs account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "1889bbb3-287b-4105-aea9-1b1f31e1bc1b",
      "name": "HTTP Request3",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1480,
        280
      ],
      "parameters": {
        "url": "=https://www.googleapis.com/drive/v3/files/{{$json[\"id\"]}}/export?mimeType=text/plain\n",
        "options": {
          "response": {
            "response": {
              "responseFormat": "text"
            }
          }
        },
        "jsonHeaders": "{\n  \"Authorization\": \"Bearer {{$credentials.googleDriveOAuth2.access_token}}\"\n}\n",
        "sendHeaders": true,
        "authentication": "predefinedCredentialType",
        "specifyHeaders": "json",
        "nodeCredentialType": "googleDocsOAuth2Api"
      },
      "credentials": {
        "oAuth2Api": {
          "id": "INVJ4n7OLXgPI372",
          "name": "Unnamed credential"
        },
        "googleDocsOAuth2Api": {
          "id": "AeVFb8EMLqLEn7Db",
          "name": "Google Docs account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "f6f0d96f-f1c8-4d6a-88c5-bfe86ff6a359",
      "name": "Anthropic Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatAnthropic",
      "position": [
        660,
        740
      ],
      "parameters": {
        "model": "claude-3-5-sonnet-20241022",
        "options": {}
      },
      "credentials": {
        "anthropicApi": {
          "id": "51YEx3VTC2IuyUTO",
          "name": "Anthropic account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "0f3fee05-3444-4046-96f6-b0978eb9d16e",
      "name": "Anthropic Chat Model1",
      "type": "@n8n/n8n-nodes-langchain.lmChatAnthropic",
      "position": [
        1780,
        500
      ],
      "parameters": {
        "model": "claude-3-5-sonnet-20241022",
        "options": {}
      },
      "credentials": {
        "anthropicApi": {
          "id": "51YEx3VTC2IuyUTO",
          "name": "Anthropic account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "34321fc9-ecaa-4f4c-a01c-b8cf0cd3df50",
      "name": "Anthropic Chat Model2",
      "type": "@n8n/n8n-nodes-langchain.lmChatAnthropic",
      "position": [
        1400,
        80
      ],
      "parameters": {
        "model": "claude-3-5-sonnet-20241022",
        "options": {}
      },
      "credentials": {
        "anthropicApi": {
          "id": "51YEx3VTC2IuyUTO",
          "name": "Anthropic account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "86315ae8-f456-4e06-a281-b04f75886232",
      "name": "Code: delete all but pdf and word",
      "type": "n8n-nodes-base.code",
      "position": [
        140,
        360
      ],
      "parameters": {
        "jsCode": "const allItems = $input.all();\nlet data = [];\nallItems.forEach(item => {\n  const binaryData = item.binary;\n  if (binaryData) {\n    Object.keys(binaryData).forEach(key => {\n      // MIME-Types f\u00fcr PDF und Word\n      const allowedMimeTypes = [\n        'application/pdf',\n        'application/msword',\n        'application/vnd.openxmlformats-officedocument.wordprocessingml.document'\n      ];\n      \n      if (allowedMimeTypes.includes(binaryData[key]?.mimeType)) {\n        data.push({\n          binary: { data: binaryData[key] },\n          json: {\n            fileName: binaryData[key].fileName,\n            mimeType: binaryData[key].mimeType\n          }\n        });\n      }\n    });\n  }\n});\nreturn data;"
      },
      "executeOnce": false,
      "typeVersion": 2,
      "alwaysOutputData": true
    },
    {
      "id": "6b95290e-4304-4187-8294-15f32e3227c9",
      "name": "has attachment?",
      "type": "n8n-nodes-base.if",
      "position": [
        380,
        360
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "loose"
          },
          "combinator": "or",
          "conditions": [
            {
              "id": "0cd4c70c-9562-486e-95bd-497ba4816aac",
              "operator": {
                "type": "number",
                "operation": "gt"
              },
              "leftValue": "={{ Object.keys($binary).length }}\n",
              "rightValue": 0
            }
          ]
        },
        "looseTypeValidation": true
      },
      "typeVersion": 2.2
    },
    {
      "id": "59688c51-64aa-47bb-80e3-33185e358122",
      "name": "PDF or WORD?",
      "type": "n8n-nodes-base.if",
      "position": [
        680,
        240
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "loose"
          },
          "combinator": "or",
          "conditions": [
            {
              "id": "0cd4c70c-9562-486e-95bd-497ba4816aac",
              "operator": {
                "type": "string",
                "operation": "contains"
              },
              "leftValue": "={{ $json.mimeType }}",
              "rightValue": "pdf"
            }
          ]
        },
        "looseTypeValidation": true
      },
      "typeVersion": 2.2
    },
    {
      "id": "8d767385-4e77-434f-8c47-1e5bbaae807f",
      "name": "OpenAI self assesment",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        1020,
        520
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
              "content": "=Deine Aufgabe ist es, den gegebenen Input-Text mit dem Output-Artikel zu vergleichen.\nBewerte, ob alle wesentlichen Informationen aus dem Input-Text im Output-Artikel korrekt enthalten sind, ohne dass neue, nicht im Input vorhandene Informationen hinzugef\u00fcgt wurden.\nVorgehensweise:\n\n    Vollst\u00e4ndigkeit pr\u00fcfen: Sind alle relevanten Informationen aus dem Input im Output enthalten?\n    Genauigkeit bewerten: Wurde der Inhalt korrekt wiedergegeben, ohne \u00c4nderungen oder Auslassungen?\n    Zus\u00e4tzliche Informationen erkennen: Wurden Inhalte hinzugef\u00fcgt, die nicht im Input vorhanden sind? Falls ja, welche?\n\nAusgabe:\n\n    Bewertung (1 bis 5):\n        1 = Sehr schlecht (viele fehlende oder falsche Informationen, erhebliche neue Inhalte)\n        2 = Unzureichend (mehrere wichtige Auslassungen oder falsche Inhalte)\n        3 = Mittelm\u00e4\u00dfig (einige kleinere Fehler oder Erg\u00e4nzungen)\n        4 = Gut (fast alles korrekt, minimale Abweichungen)\n        5 = Sehr gut (vollst\u00e4ndige, korrekte \u00dcbereinstimmung)\n    Textuelle Begr\u00fcndung: Eine kurze Analyse, warum diese Bewertung vergeben wurde.\n\n\nHier der Input:\n\n{{ $('Gmail Trigger').item.json.text }}\n\nUnd hier der Output:\n{{ $json.output }}"
            },
            {
              "role": "assistant",
              "content": "sei pedantisch"
            }
          ]
        }
      },
      "credentials": {
        "openAiApi": {
          "id": "DGnxI3xtf5aATUOp",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.8
    },
    {
      "id": "f9c7b8a8-2148-49f1-b604-4766deafadd1",
      "name": "OpenAI self-assesment2",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "onError": "continueRegularOutput",
      "position": [
        1740,
        -80
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
              "content": "=Deine Aufgabe ist es, den gegebenen Input-Text mit dem Output-Artikel zu vergleichen.\nBewerte, ob alle wesentlichen Informationen aus dem Input-Text im Output-Artikel korrekt enthalten sind, ohne dass neue, nicht im Input vorhandene Informationen hinzugef\u00fcgt wurden.\nVorgehensweise:\n\n    Vollst\u00e4ndigkeit pr\u00fcfen: Sind alle relevanten Informationen aus dem Input im Output enthalten?\n    Genauigkeit bewerten: Wurde der Inhalt korrekt wiedergegeben, ohne \u00c4nderungen oder Auslassungen?\n    Zus\u00e4tzliche Informationen erkennen: Wurden Inhalte hinzugef\u00fcgt, die nicht im Input vorhanden sind? Falls ja, welche?\n\nAusgabe:\n\n    Bewertung (1 bis 5):\n        1 = Sehr schlecht (viele fehlende oder falsche Informationen, erhebliche neue Inhalte)\n        2 = Unzureichend (mehrere wichtige Auslassungen oder falsche Inhalte)\n        3 = Mittelm\u00e4\u00dfig (einige kleinere Fehler oder Erg\u00e4nzungen)\n        4 = Gut (fast alles korrekt, minimale Abweichungen)\n        5 = Sehr gut (vollst\u00e4ndige, korrekte \u00dcbereinstimmung)\n    Textuelle Begr\u00fcndung: Eine kurze Analyse, warum diese Bewertung vergeben wurde.\n\n\nHier der Input:\n{{ $('Extrahiere aus PDF1').item.json.text }}\n{{ $('Gmail Trigger').item.json.text }}\n\nUnd hier der Output:\n {{ $json.output }}"
            },
            {
              "role": "assistant",
              "content": "sei pedantisch"
            }
          ]
        }
      },
      "credentials": {
        "openAiApi": {
          "id": "DGnxI3xtf5aATUOp",
          "name": "OpenAi account"
        }
      },
      "retryOnFail": true,
      "typeVersion": 1.8
    },
    {
      "id": "0c2c1c4d-b3ec-4e1d-b663-27c43dddb523",
      "name": "reply to sender (no attachment)",
      "type": "n8n-nodes-base.gmail",
      "position": [
        1440,
        520
      ],
      "webhookId": "521f7992-d12c-4485-92d8-41cc5567938b",
      "parameters": {
        "message": "=***REDIGIERTER ARTIKEL***  !!!-CLAUDE-!!!\n\n{{ $('AI Article Writer 3').item.json.output }}\n\n***SELBSTKRITIK***\n\n{{ $json.message.content }}\n\n***ORIGINALNACHRICHT***\n\n{{ $('Gmail Trigger').item.json.text }}",
        "options": {},
        "emailType": "text",
        "messageId": "={{ $('Gmail Trigger').item.json.id }}",
        "operation": "reply"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "BtnmuMmkgyJeYpoZ",
          "name": "Gmail account 3"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "de88f6fb-0e75-41d9-8e0c-7377ca1bdca4",
      "name": "reply to sender (word)",
      "type": "n8n-nodes-base.gmail",
      "position": [
        2360,
        280
      ],
      "webhookId": "5767887a-ca7a-41f9-9745-34d49bb79691",
      "parameters": {
        "message": "=***REDIGIERTER ARTIKEL***   !!!! CLAUDE !!!!\n\n\n{{ $('AI Article Writer 2').item.json.output }}\n\n***SELBSTKRITIK***\nBewertung: 1 (schlecht) bis 5 (sehr gut)\n{{ $json.message.content }}\n***ORIGINALNACHRICHT***\n\n{{ $('Gmail Trigger').item.json.text }}\n\n***INHALT ANHANG***\n\n{{ $('HTTP Request3').item.json.data }}",
        "options": {},
        "emailType": "text",
        "messageId": "={{ $('Gmail Trigger').item.json.id }}",
        "operation": "reply"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "BtnmuMmkgyJeYpoZ",
          "name": "Gmail account 3"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "0d9c55f9-3c53-44aa-b0d0-09141570b72b",
      "name": "reply to sender (pdf)",
      "type": "n8n-nodes-base.gmail",
      "position": [
        2140,
        -80
      ],
      "webhookId": "523f355b-404f-4a60-b393-e2c5d8f29098",
      "parameters": {
        "message": "=*****REDIGIERTE NACHRICHT*****   !!!!- CLAUDE -!!!\n{{ $('AI Article Writer 1').item.json.output }}\n\n*****SELBSTKRITIK****\nBewertung 1 (schlecht) bis 5 (sehr gut):\n{{ $json.message.content }}\n\n*****ORIGINAL-E-MAIL*****\n\n{{ $('Gmail Trigger').item.json.text }}\n\n\n*****TEXT AUS PDF*****\n\n{{ $('Extrahiere aus PDF1').item.json.text }}\n\n\n",
        "options": {},
        "emailType": "text",
        "messageId": "={{ $('Gmail Trigger').item.json.id }}",
        "operation": "reply"
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "BtnmuMmkgyJeYpoZ",
          "name": "Gmail account 3"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "695e80d4-dbe2-4476-b680-b90732a6136a",
      "name": "AI Article Writer 1",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "onError": "continueRegularOutput",
      "maxTries": 5,
      "position": [
        1380,
        -80
      ],
      "parameters": {
        "text": "=Du bist Redakteur*in beim Schweizer Kulturmagazin Terra Grischuna. Erstelle aus den Textinformationen einen publikationsfertigen Artikel mit folgender Struktur und Vorgehensweise:\n\n    Stil und Sprache\n    \u2013 Schreibe in einer neutralen, reduzierten und klaren Sprache.\n    \u2013 Verwende die Schweizer Rechtschreibung.\n    \u2013 Halte dich an ein genderneutrales, aktives und verst\u00e4ndliches Wording.\n\n    Form und Aufbau\n    \u2013 Nutze die Form der umgekehrten Pyramide (wichtigste Informationen zuerst, abnehmende Wichtigkeit im Verlauf).\n    \u2013 Verfasse einen Titel und klare Zwischentitel (keine Bulletpoints).\n    \u2013 Bei Veranstaltungshinweisen beginne den Artikel mit einem Satz, der Wer, wann, wo, was beantwortet (z. B. \u201eFranz Tomaschett spricht am 5. Dezember in Chur \u00fcber das Thema Arbeit.\u201c).\n    \u2013 Der Fliesstext sollte zwischen 250 und 500 W\u00f6rtern umfassen.\n\n    Inhalte und Daten\n    \u2013 Fasse alle relevanten Inhalte verst\u00e4ndlich zusammen.\n- halte dich an die Informationen aus der E-Mail. Erfinde nichts! Sei genau!\n- wenn dir Informationen fehlen, konstruiere keine neuen. \n    \u2013 Ignoriere alle anderen Dateiformate (z. B. Bilder, Excel-Tabellen).\n    \u2013 Verwende keine Aufz\u00e4hlungspunkte im finalen Artikel.\n- wenn subjektive oder streitbare Ansichten formuliert werden, attribuiere diese den Absendern dieser Ansichten. Nenne Quelle/Urheber solcher \u00c4usserungen. Beispiel: \"ZITAT in direkter oder indirekter Rede\", schreibt die Gruppe Wolf in ihrer Mitteilung. \n\n    Zus\u00e4tzliche Anweisung\n    \u2013 Extrahiere zun\u00e4chst alle wichtigen Daten, Personen und Schlagworte. Liste sie strukturiert (z. B. mit Abs\u00e4tzen oder klarer Trennung) vor dem eigentlichen Artikel auf. Z\u00e4hle zudem die Anzahl Zeichen und W\u00f6rter des Artikels.\n\nBeispielhafte Ausgabe-Struktur\n\nWichtige Daten und Personen\nNennehierknappundstrukturiertallerelevantenNamen,Daten,Orte,Termineetc.NennehierknappundstrukturiertallerelevantenNamen,Daten,Orte,Termineetc.\n\nTitel\nKurzer,pra\u00a8gnanterTitelKurzer,pra\u00a8gnanterTitel\n\n\nEinfu\u00a8hrenderAbsatzmitdenwichtigstenInfos(wer,wann,wo,was)Einfu\u00a8hrenderAbsatzmitdenwichtigstenInfos(wer,wann,wo,was)\n\nZwischentitel 1\nHintergrund,weitereZusammenha\u00a8nge,abnehmendwichtigeDetailsHintergrund,weitereZusammenha\u00a8nge,abnehmendwichtigeDetails\n\nZwischentitel 2\nRestlicheInformationen,kontextualisiertundzusammengefasstRestlicheInformationen,kontextualisiertundzusammengefasst\n\n(Ende des Artikels, maximal 500 W\u00f6rter.)\n\nNutze bitte diese Vorgaben, um den Artikel in hochwertiger, schweizkonformer Sprache zu verfassen.\n\nHier die Informationen aus dem E-Mail\n\n {{ $('Gmail Trigger').item.json.text }}\n\n{{ $json.text }}",
        "options": {},
        "promptType": "define"
      },
      "retryOnFail": true,
      "typeVersion": 1.7
    },
    {
      "id": "1d3988ea-b8ec-450a-a512-f5463953554b",
      "name": "AI Article Writer 2",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        1700,
        280
      ],
      "parameters": {
        "text": "=Du bist Redakteur*in beim Schweizer Kulturmagazin Terra Grischuna. Erstelle aus den Textinformationen einen publikationsfertigen Artikel mit folgender Struktur und Vorgehensweise:\n\n    Stil und Sprache\n    \u2013 Schreibe in einer neutralen, reduzierten und klaren Sprache.\n    \u2013 Verwende die Schweizer Rechtschreibung.\n    \u2013 Halte dich an ein genderneutrales, aktives und verst\u00e4ndliches Wording.\n\n    Form und Aufbau\n    \u2013 Nutze die Form der umgekehrten Pyramide (wichtigste Informationen zuerst, abnehmende Wichtigkeit im Verlauf).\n    \u2013 Verfasse einen Titel und klare Zwischentitel (keine Bulletpoints).\n    \u2013 Bei Veranstaltungshinweisen beginne den Artikel mit einem Satz, der Wer, wann, wo, was beantwortet (z. B. \u201eFranz Tomaschett spricht am 5. Dezember in Chur \u00fcber das Thema Arbeit.\u201c).\n    \u2013 Der Fliesstext sollte zwischen 250 und 500 W\u00f6rtern umfassen.\n\n    Inhalte und Daten\n    \u2013 Fasse alle relevanten Inhalte verst\u00e4ndlich zusammen.\n- halte dich an die Informationen aus der E-Mail. Erfinde nichts! Sei genau!\n- wenn dir Informationen fehlen, konstruiere keine neuen. \n    \u2013 Ignoriere alle anderen Dateiformate (z. B. Bilder, Excel-Tabellen).\n    \u2013 Verwende keine Aufz\u00e4hlungspunkte im finalen Artikel.\n- wenn subjektive oder streitbare Ansichten formuliert werden, attribuiere diese den Absendern dieser Ansichten. Nenne Quelle/Urheber solcher \u00c4usserungen. Beispiel: \"ZITAT in direkter oder indirekter Rede\", schreibt die Gruppe Wolf in ihrer Mitteilung. \n\n    Zus\u00e4tzliche Anweisung\n    \u2013 Extrahiere zun\u00e4chst alle wichtigen Daten, Personen und Schlagworte. Liste sie strukturiert (z. B. mit Abs\u00e4tzen oder klarer Trennung) vor dem eigentlichen Artikel auf. Z\u00e4hle zudem die Anzahl Zeichen und W\u00f6rter des Artikels.\n\nBeispielhafte Ausgabe-Struktur\n\nWichtige Daten und Personen\nNennehierknappundstrukturiertallerelevantenNamen,Daten,Orte,Termineetc.NennehierknappundstrukturiertallerelevantenNamen,Daten,Orte,Termineetc.\n\nTitel\nKurzer,pra\u00a8gnanterTitelKurzer,pra\u00a8gnanterTitel\n\n\nEinfu\u00a8hrenderAbsatzmitdenwichtigstenInfos(wer,wann,wo,was)Einfu\u00a8hrenderAbsatzmitdenwichtigstenInfos(wer,wann,wo,was)\n\nZwischentitel 1\nHintergrund,weitereZusammenha\u00a8nge,abnehmendwichtigeDetailsHintergrund,weitereZusammenha\u00a8nge,abnehmendwichtigeDetails\n\nZwischentitel 2\nRestlicheInformationen,kontextualisiertundzusammengefasstRestlicheInformationen,kontextualisiertundzusammengefasst\n\n(Ende des Artikels, maximal 500 W\u00f6rter.)\n\nNutze bitte diese Vorgaben, um den Artikel in hochwertiger, schweizkonformer Sprache zu verfassen.\n\nHier die Informationen aus dem E-Mail\n\n {{ $('Gmail Trigger').item.json.text }}{{ $json.data }}",
        "options": {},
        "promptType": "define"
      },
      "typeVersion": 1.7
    },
    {
      "id": "99b5a06e-5d1b-4797-a934-2c37b49caf47",
      "name": "AI Article Writer 3",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        660,
        520
      ],
      "parameters": {
        "text": "=Du bist Redakteur*in beim Schweizer Kulturmagazin Terra Grischuna. Erstelle aus den Textinformationen einen publikationsfertigen Artikel mit folgender Struktur und Vorgehensweise:\n\n    Stil und Sprache\n    \u2013 Schreibe in einer neutralen, reduzierten und klaren Sprache.\n    \u2013 Verwende die Schweizer Rechtschreibung.\n    \u2013 Halte dich an ein genderneutrales, aktives und verst\u00e4ndliches Wording.\n\n    Form und Aufbau\n    \u2013 Nutze die Form der umgekehrten Pyramide (wichtigste Informationen zuerst, abnehmende Wichtigkeit im Verlauf).\n    \u2013 Verfasse einen Titel und klare Zwischentitel (keine Bulletpoints).\n    \u2013 Bei Veranstaltungshinweisen beginne den Artikel mit einem Satz, der Wer, wann, wo, was beantwortet (z. B. \u201eFranz Tomaschett spricht am 5. Dezember in Chur \u00fcber das Thema Arbeit.\u201c).\n    \u2013 Der Fliesstext sollte zwischen 250 und 500 W\u00f6rtern umfassen.\n- wenn subjektive oder streitbare Ansichten formuliert werden, attribuiere diese den Absendern dieser Ansichten. Nenne Quelle/Urheber solcher \u00c4usserungen. Beispiel: \"ZITAT in direkter oder indirekter Rede\", schreibt die Gruppe Wolf in ihrer Mitteilung. \n\n    Inhalte und Daten\n    \u2013 Fasse alle relevanten Inhalte verst\u00e4ndlich zusammen.\n- halte dich an die Informationen aus der E-Mail. Erfinde nichts! Sei genau!\n- wenn dir Informationen fehlen, konstruiere keine neuen. \n    \u2013 Ignoriere alle anderen Dateiformate (z. B. Bilder, Excel-Tabellen).\n    \u2013 Verwende keine Aufz\u00e4hlungspunkte im finalen Artikel.\n\n    Zus\u00e4tzliche Anweisung\n    \u2013 Extrahiere zun\u00e4chst alle wichtigen Daten, Personen und Schlagworte. Liste sie strukturiert (z. B. mit Abs\u00e4tzen oder klarer Trennung) vor dem eigentlichen Artikel auf. Z\u00e4hle zudem die Anzahl Zeichen und W\u00f6rter des Artikels.\n\nBeispielhafte Ausgabe-Struktur\n\nWichtige Daten und Personen\nNennehierknappundstrukturiertallerelevantenNamen,Daten,Orte,Termineetc.NennehierknappundstrukturiertallerelevantenNamen,Daten,Orte,Termineetc.\n\nTitel\nKurzer,pra\u00a8gnanterTitelKurzer,pra\u00a8gnanterTitel\n\n\nEinfu\u00a8hrenderAbsatzmitdenwichtigstenInfos(wer,wann,wo,was)Einfu\u00a8hrenderAbsatzmitdenwichtigstenInfos(wer,wann,wo,was)\n\nZwischentitel 1\nHintergrund,weitereZusammenha\u00a8nge,abnehmendwichtigeDetailsHintergrund,weitereZusammenha\u00a8nge,abnehmendwichtigeDetails\n\nZwischentitel 2\nRestlicheInformationen,kontextualisiertundzusammengefasstRestlicheInformationen,kontextualisiertundzusammengefasst\n\n(Ende des Artikels, maximal 500 W\u00f6rter.)\n\nNutze bitte diese Vorgaben, um den Artikel in hochwertiger, Schweizkonformer Sprache zu verfassen.\n\nHier die Informationen aus dem E-Mail\n\n {{ $('Gmail Trigger').item.json.text }}",
        "options": {},
        "promptType": "define"
      },
      "typeVersion": 1.7
    },
    {
      "id": "f7280703-4570-4771-8a53-cac3a661f416",
      "name": "Google Drive",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        960,
        280
      ],
      "parameters": {
        "name": "={{ $json.fileName }}",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "options": {
          "useContentAsIndexableText": false
        },
        "folderId": {
          "__rl": true,
          "mode": "list",
          "value": "root",
          "cachedResultName": "/ (Root folder)"
        }
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "q0vkLLRJ0qE1Wnbo",
          "name": "Google Drive account"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "a83189ab-027d-4ed7-aa69-82e29270cd7c",
      "name": "OpenAI self-assesment",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        2020,
        280
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
              "content": "=Deine Aufgabe ist es, den gegebenen Input-Text mit dem Output-Artikel zu vergleichen.\nBewerte, ob alle wesentlichen Informationen aus dem Input-Text im Output-Artikel korrekt enthalten sind, ohne dass neue, nicht im Input vorhandene Informationen hinzugef\u00fcgt wurden.\nVorgehensweise:\n\n    Vollst\u00e4ndigkeit pr\u00fcfen: Sind alle relevanten Informationen aus dem Input im Output enthalten?\n    Genauigkeit bewerten: Wurde der Inhalt korrekt wiedergegeben, ohne \u00c4nderungen oder Auslassungen?\n    Zus\u00e4tzliche Informationen erkennen: Wurden Inhalte hinzugef\u00fcgt, die nicht im Input vorhanden sind? Falls ja, welche?\n\nAusgabe:\n\n    Bewertung (1 bis 5):\n        1 = Sehr schlecht (viele fehlende oder falsche Informationen, erhebliche neue Inhalte)\n        2 = Unzureichend (mehrere wichtige Auslassungen oder falsche Inhalte)\n        3 = Mittelm\u00e4\u00dfig (einige kleinere Fehler oder Erg\u00e4nzungen)\n        4 = Gut (fast alles korrekt, minimale Abweichungen)\n        5 = Sehr gut (vollst\u00e4ndige, korrekte \u00dcbereinstimmung)\n    Textuelle Begr\u00fcndung: Eine kurze Analyse, warum diese Bewertung vergeben wurde.\n\n\nHier der Input:\n{{ $('HTTP Request3').item.json.data }}\n{{ $('Gmail Trigger').item.json.text }}\nUnd hier der Output:\n{{ $json.output }}"
            },
            {
              "role": "assistant",
              "content": "sei pedantisch"
            }
          ]
        }
      },
      "credentials": {
        "openAiApi": {
          "id": "DGnxI3xtf5aATUOp",
          "name": "OpenAi account"
        }
      },
      "typeVersion": 1.8
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "timezone": "Europe/Rome",
    "callerPolicy": "workflowsFromSameOwner",
    "executionOrder": "v1"
  },
  "versionId": "0e0eba57-a154-48ee-a86a-d4c787805456",
  "connections": {
    "Google Drive": {
      "main": [
        [
          {
            "node": "HTTP Request2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "PDF or WORD?": {
      "main": [
        [
          {
            "node": "Extrahiere aus PDF1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Google Drive",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Gmail Trigger": {
      "main": [
        [
          {
            "node": "Code: delete all but pdf and word",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request2": {
      "main": [
        [
          {
            "node": "HTTP Request3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request3": {
      "main": [
        [
          {
            "node": "AI Article Writer 2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "has attachment?": {
      "main": [
        [
          {
            "node": "PDF or WORD?",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "AI Article Writer 3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Article Writer 1": {
      "main": [
        [
          {
            "node": "OpenAI self-assesment2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Article Writer 2": {
      "main": [
        [
          {
            "node": "OpenAI self-assesment",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Article Writer 3": {
      "main": [
        [
          {
            "node": "OpenAI self assesment",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extrahiere aus PDF1": {
      "main": [
        [
          {
            "node": "AI Article Writer 1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Anthropic Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "AI Article Writer 3",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Anthropic Chat Model1": {
      "ai_languageModel": [
        [
          {
            "node": "AI Article Writer 2",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Anthropic Chat Model2": {
      "ai_languageModel": [
        [
          {
            "node": "AI Article Writer 1",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI self assesment": {
      "main": [
        [
          {
            "node": "reply to sender (no attachment)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI self-assesment": {
      "main": [
        [
          {
            "node": "reply to sender (word)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI self-assesment2": {
      "main": [
        [
          {
            "node": "reply to sender (pdf)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Code: delete all but pdf and word": {
      "main": [
        [
          {
            "node": "has attachment?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
