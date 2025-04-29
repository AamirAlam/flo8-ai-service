# Enviar Miembros del CMS Ghost hacia Newsletter Sendy

**[View Template](https://n8n.io/workflows/629-/)**  **Published Date:** 09/03/2020  **Created By:** The { AI } rtist  **Categories:** `Development` `Core Nodes` `Communication` `HITL`  

## Template Description

Ghost + Sendy Integration
Está es una integración del CMS Ghost hacia Sendy

Sendy ( www.sendy.co )
Ghost ( www.ghost.org )

Con esta integración podrás importar los miembros del CMS Ghost en su nueva versión que incluye la parte de Membresía hacía el Software de newsletter sendy.

Está integración además nos avisa si se ha registrado un nuevo miembro via telegram.

Para realizar esta customización es necesaria la creación de una custom integration en Ghost.

Para ello desde el panel de Administración vamos a CUSTOM INTEGRATIONS / + Add custom Integration

Una vez allí nos solicitará un nombre le ponemos el que queramos y añadimos un nuevo Hook:



En Target URL debe ir La url que nos genera nuestro webhook dentro de n8n:



Pegamos la URL y acamos de rellenar los datos del HTTP REQUEST1 con los datos de nuestra lista rellenando los campos.

api_key
list

Que encontaras en tú instalación de Sendy

Por último faltara añadir las credenciales de Telegram de Nuestro BOT 
( https://docs.n8n.io/credentials/telegram/ ) e indicar el grupo o usuario donde queremos que notifique.

Saludos,



## Template JSON

```
{
  "id": "3",
  "name": "RegisterSendly",
  "nodes": [
    {
      "name": "HTTP Request1",
      "type": "n8n-nodes-base.httpRequest",
      "color": "#BB1AE3",
      "notes": "Registrar Miembro en Newsletter\n",
      "position": [
        810,
        140
      ],
      "parameters": {
        "url": "https://yoursendyinstallation.com/subscribe",
        "options": {
          "bodyContentType": "form-urlencoded"
        },
        "requestMethod": "POST",
        "responseFormat": "string",
        "bodyParametersUi": {
          "parameter": [
            {
              "name": "api_key",
              "value": "your-main-api-key"
            },
            {
              "name": "boolean",
              "value": "true"
            },
            {
              "name": "silent",
              "value": "true"
            },
            {
              "name": "name",
              "value": "n8n automated"
            },
            {
              "name": "email",
              "value": "={{$node[\"Webhook\"].json[\"body\"][\"member\"][\"current\"][\"email\"]}}"
            },
            {
              "name": "list",
              "value": "your-list-id"
            }
          ]
        },
        "queryParametersUi": {
          "parameter": []
        }
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "color": "#76F507",
      "notes": "Webhook para Ghost",
      "position": [
        450,
        190
      ],
      "webhookId": "bf898631-50bc-40a2-9a10-f146f47075fa",
      "parameters": {
        "path": "06cfbe404338f125f6cdeab8d2b7ff1e",
        "options": {},
        "httpMethod": "POST"
      },
      "executeOnce": false,
      "notesInFlow": true,
      "typeVersion": 1,
      "alwaysOutputData": false
    },
    {
      "name": "Telegram",
      "type": "n8n-nodes-base.telegram",
      "notes": "Mandar notificaci\u00f3n en Telegram",
      "position": [
        860,
        400
      ],
      "parameters": {
        "text": "=Nuevo Integrante registrado: {{$node[\"Webhook\"].json[\"body\"][\"member\"][\"current\"][\"email\"]}}",
        "chatId": "@yourtelegramgroup",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "yourtelegram_bot"
      },
      "notesInFlow": true,
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "HTTP Request1",
            "type": "main",
            "index": 0
          },
          {
            "node": "Telegram",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
