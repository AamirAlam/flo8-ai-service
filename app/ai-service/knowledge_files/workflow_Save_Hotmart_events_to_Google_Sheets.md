# Save Hotmart events to Google Sheets

**[View Template](https://n8n.io/workflows/2702-/)**  **Published Date:** 01/06/2025  **Created By:** Solomon  **Categories:** `Data & Storage` `Productivity`  

## Template Description

Português

Acompanhe todos os seus eventos do Hotmart em um só lugar e mantenha seus dados organizados para análise.

Com este fluxo você pode registrar compras, reembolsos, eventos de assinatura e abandono de carrinho diretamente no Google Sheets.

Como funciona

O fluxo recebe os eventos da Hotmart e registra automaticamente no Google Sheets.

Por exemplo:

Compras são registradas com informações como nome do produto, valor pago e dados do comprador.
Abandono de carrinho registra informações sobre o produto visualizado, dados de contato do cliente e horários.
Eventos de assinatura mostram atualizações como cancelamentos ou renovações.

Para quem é?

Criadores, empreendedores e negócios que usam o Hotmart e precisam de uma forma clara e automatizada de acompanhar suas vendas e dados de assinatura.

Remova a necessidade de transferir dados manualmente – este fluxo de trabalho faz isso por você, economizando tempo e reduzindo erros.

Confira meus outros templates

👉 https://n8n.io/creators/solomon/

English

Track all your Hotmart events in one place and keep your data organized for analysis.

With this workflow, you can register purchases, refunds, subscription events, and cart abandonment directly in Google Sheets.

How it works

The workflow listens for events from Hotmart and automatically records the details in Google Sheets.

For example:

Purchases are logged with details like product name, amount paid, and buyer information.
Cart abandonment records include the product viewed, customer contact details, and timestamps.
Subscription events show updates like cancellations or renewals.

Who is this for?

Creators, entrepreneurs, and businesses using Hotmart who need a clear and automated way to track their sales and subscription data.

No need to manually transfer data – this workflow does it for you, saving time and reducing errors.

Check out my other templates

👉 https://n8n.io/creators/solomon/

## Template JSON

```
{
  "nodes": [
    {
      "id": "f3d411bd-3451-4150-ac3d-917680a7b520",
      "name": "Convert timestamp",
      "type": "n8n-nodes-base.dateTime",
      "position": [
        1760,
        560
      ],
      "parameters": {},
      "notesInFlow": false,
      "typeVersion": 2
    },
    {
      "id": "7d43d464-521f-472a-baf5-68398c02a1b8",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "notes": "- PURCHASE_PROTEST \u00e9 a primeira notifica\u00e7\u00e3o sobre pedido de reembolso;\n- SUBSCRIPTION_CANCELLATION acontece junto com o purchase_protest, quando o cliente pede reembolso dentro do per\u00edodo da garantia;\n- PURCHASE_REFUNDED s\u00f3 acontece quando ocorre o reembolso de fato;\n\n- PURCHASE_COMPLETE significa que acabou o per\u00edodo de garantia e o dinheiro j\u00e1 pertence ao vendedor;\n",
      "position": [
        1300,
        480
      ],
      "parameters": {},
      "typeVersion": 3
    },
    {
      "id": "9a5d6fa2-a3b2-4b31-b571-e89eb4adcfa9",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        640,
        -100
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "0556e91b-1d39-4a8b-a01a-e0a197769d64",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        640,
        280
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "e6e4eceb-f0b8-4249-8a67-fd3778592b93",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1660,
        180
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "561163ec-bb92-4ba9-8535-79616707e321",
      "name": "Save execution data",
      "type": "n8n-nodes-base.executionData",
      "position": [
        1300,
        240
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "9e46c093-b97d-459f-bcd0-fa88f89be573",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1200,
        -100
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "9453b331-89c5-40e3-a635-0ddd26589d72",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        1100,
        560
      ],
      "webhookId": "439a86fe-819c-4516-9ebf-54e779b560c3",
      "parameters": {},
      "typeVersion": 1.1
    },
    {
      "id": "75fbebfc-a5d5-4d23-a2b4-f00ceb20f360",
      "name": "Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        2300,
        560
      ],
      "parameters": {},
      "typeVersion": 4.5
    },
    {
      "id": "a6cd632c-783e-4808-9e6c-2235bfa1d3b8",
      "name": "Set some data",
      "type": "n8n-nodes-base.set",
      "position": [
        2040,
        560
      ],
      "parameters": {},
      "typeVersion": 3.4
    },
    {
      "id": "364118a0-03ee-41ba-8f33-901ef25dea6a",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2240,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Switch": {
      "main": [
        [
          {
            "node": "Convert timestamp",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Convert timestamp",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Convert timestamp",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Convert timestamp",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Convert timestamp",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Convert timestamp",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Convert timestamp",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Webhook": {
      "main": [
        [
          {
            "node": "Switch",
            "type": "main",
            "index": 0
          },
          {
            "node": "Save execution data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set some data": {
      "main": [
        [
          {
            "node": "Google Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Convert timestamp": {
      "main": [
        [
          {
            "node": "Set some data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
