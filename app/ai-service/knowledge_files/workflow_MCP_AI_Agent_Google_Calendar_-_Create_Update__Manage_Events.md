# MCP AI Agent Google Calendar - Create, Update & Manage Events

**[View Template](https://n8n.io/workflows/3589-/)**  **Published Date:** 04/17/2025  **Created By:** Amanda Benks  **Categories:**   

## Template Description

Hi! I’m Amanda :) 💖 
I created this sweet little workflow with lots of love and care, just for you who wants to manage your Google Calendar in a smart and gentle way 💌

This AI-powered agent connects with MCP (Multi-Channel Protocol) and understands natural language like “book a meeting tomorrow at 3pm”, “reschedule my call to Monday”, or “what events do I have on Wednesday?” — and it does everything quietly and beautifully in your calendar 🧸

💡 What this lovely agent does

🗓️ Creates new events in your Google Calendar (with or without guests)  
✏️ Updates existing events with new times or details  
🧹 Deletes events you no longer need  
🔍 Retrieves scheduled events by date  
🤖 Works through GPT-4o or any AI via MCP Agent

⚙️ How to set it up (gently and step-by-step)

Webhook is ready for MCP messages at POST /mcp/calendar  
Connect your Google Calendar account using OAuth2 inside n8n  
Link it to your favorite AI tool (like LangChain, Typebot, etc.) that can talk to the MCP agent  
All details like title, time, date, and guests are parsed automatically from natural language 💫

✨ Requirements

Google Calendar connected to n8n  
n8n instance (Cloud or Self-hosted — both are supported!)  
An AI interface that talks to the MCP agent (like LangChain or Typebot)  
MCP Trigger API set up in your n8n environment

This agent is perfect for therapists, consultants, coaches, small teams, or anyone who wants to keep their calendar flowing naturally and peacefully with a little help from AI 💆‍♀️🧠

Want something customized just for you?
Chat with me 💻💛 Chat via WhatsApp (+55 17 99155-7874)
.
.
Tradução para Português:
💖 Oi! Eu sou a Amanda :)

Esse fluxinho aqui foi feito com muito cuidado pra você que quer automatizar sua agenda do Google Calendar de forma inteligente, simples e com muito carinho 💌

Ele funciona como um agente que conversa com outro sistema de IA (via MCP) e consegue entender pedidos como “agende uma consulta amanhã às 15h”, “remarque a reunião para segunda”, ou “quais eventos tenho na quarta?” — tudo isso feito direto no seu calendário, sem você precisar abrir nada 🧸

💡 O que ele faz com amor

🗓️ Cria eventos no seu Google Calendar (com ou sem convidados)  
✏️ Atualiza eventos já existentes com novos horários  
🧹 Exclui eventos que você não precisa mais  
🔍 Busca seus compromissos com base em datas específicas  
❤️ Tudo isso com suporte ao modelo GPT-4o via agente MCP

⚙️ Como configurar (bem facinho, prometo!)

Conecte o webhook: o endpoint do MCP já vem prontinho com o caminho mcp/calendar  
Conecte sua conta do Google Calendar usando o OAuth2 no n8n  
Adicione a integração do MCP Trigger com seu sistema de IA (LangChain, Typebot, etc.)  
Todos os campos como título, data, hora e convidados são extraídos automaticamente via IA 💫

✨ Requisitos

Conta Google Calendar integrada ao n8n  
Instância n8n (Cloud ou Self-hosted)  
Integração com uma IA que converse com o MCP Agent (como LangChain)  
Acesso à API MCP ativado no n8n

Esse agente é ideal pra psicólogos, consultores, times de atendimento, terapeutas — ou qualquer pessoa fofa que quer deixar sua agenda fluindo sozinha, com a ajuda de um toque de inteligência 💆‍♀️🧠

Quer algo feito só pra você?
Fala comigo com carinho 💻💛 Falar no WhatsApp (+55 17 99155-7874)

## Template JSON

```
{
  "id": "9np0mcrtxQ8Zk9fQ",
  "meta": {
    "instanceId": "6a52f06a38696cfa8d3a5b70f84891fab02c428a5c2d448dcef39b1f17adf12b",
    "templateCredsSetupCompleted": true
  },
  "name": "MCP Google Calendar",
  "tags": [],
  "nodes": [
    {
      "id": "9d5a8ad9-68ec-4bcb-928e-d016b78c58ec",
      "name": "MCP Server Trigger",
      "type": "@n8n/n8n-nodes-langchain.mcpTrigger",
      "position": [
        80,
        -60
      ],
      "webhookId": "23a95c27-5a91-49b1-8d99-1f64dfe04b2d",
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "e9b03b81-c28a-4fd0-b8ff-f514c82449da",
      "name": "Create Event with Attendee",
      "type": "n8n-nodes-base.googleCalendarTool",
      "position": [
        480,
        220
      ],
      "parameters": {},
      "typeVersion": 1.3
    },
    {
      "id": "ba53e659-005f-48a2-ac83-c263e2f85bdb",
      "name": "Create Event",
      "type": "n8n-nodes-base.googleCalendarTool",
      "position": [
        360,
        220
      ],
      "parameters": {},
      "typeVersion": 1.3
    },
    {
      "id": "a65c0783-9be7-498d-80b2-be6a81bfe81f",
      "name": "Get Events",
      "type": "n8n-nodes-base.googleCalendarTool",
      "position": [
        240,
        220
      ],
      "parameters": {},
      "typeVersion": 1.3
    },
    {
      "id": "06ad460f-b6a8-44be-8c5c-68ac0370771e",
      "name": "Delete Event",
      "type": "n8n-nodes-base.googleCalendarTool",
      "position": [
        120,
        220
      ],
      "parameters": {},
      "typeVersion": 1.3
    },
    {
      "id": "d0afcce9-0cee-4b74-9424-a94de98e78dd",
      "name": "Update Event",
      "type": "n8n-nodes-base.googleCalendarTool",
      "position": [
        0,
        220
      ],
      "parameters": {},
      "typeVersion": 1.3
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "ac760115-997f-4a45-a76a-f3aeb544f1f5",
  "connections": {
    "Get Events": {
      "ai_tool": [
        [
          {
            "node": "MCP Server Trigger",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Create Event": {
      "ai_tool": [
        [
          {
            "node": "MCP Server Trigger",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Delete Event": {
      "ai_tool": [
        [
          {
            "node": "MCP Server Trigger",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Update Event": {
      "ai_tool": [
        [
          {
            "node": "MCP Server Trigger",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Create Event with Attendee": {
      "ai_tool": [
        [
          {
            "node": "MCP Server Trigger",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
