# Get Slack notifications when new product published on WooCommerce

**[View Template](https://n8n.io/workflows/1765-/)**  **Published Date:** 08/12/2022  **Created By:** n8n Team  **Categories:** `Communication` `HITL`  

## Template Description

This workflow let's a bot in Slack notify a specific channel when a new product in WooCommerce is published and live on the site. 

Prerequisites

WooCommerce account
Slack and a Slack bot

How it works

Listen for WooCommerce product creation
If permalink starts with https://[your-url-here].com/product/
Slack bot notifies channel that a new product has been added. 

Please note, you must update the URL in the IF node to match your url. If your WooCommerce doesn't use the slug /product/, that will need to be updated too. 


## Template JSON

```
{
  "id": 1016,
  "name": "Woocommerce to slack: notify new product created",
  "tags": [
    {
      "id": "5",
      "name": "FVF",
      "createdAt": "2022-07-30T07:43:44.795Z",
      "updatedAt": "2022-07-30T07:43:44.795Z"
    }
  ],
  "nodes": [
    {
      "name": "If URL has /product/",
      "type": "n8n-nodes-base.if",
      "position": [
        640,
        300
      ],
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"permalink\"]}}",
              "value2": "https://[add-your-url-here]/product/",
              "operation": "startsWith"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Send message to slack",
      "type": "n8n-nodes-base.slack",
      "position": [
        920,
        260
      ],
      "parameters": {
        "text": ":new: A new product has been added! :new:",
        "channel": "newproducts",
        "blocksUi": {
          "blocksValues": []
        },
        "attachments": [
          {
            "color": "#66FF00",
            "fields": {
              "item": [
                {
                  "short": false,
                  "title": "Name",
                  "value": "={{$json[\"name\"]}}"
                },
                {
                  "short": true,
                  "title": "Price",
                  "value": "={{$json[\"regular_price\"]}}"
                },
                {
                  "short": true,
                  "title": "Sale Price",
                  "value": "={{$json[\"sale_price\"]}}"
                },
                {
                  "short": false,
                  "title": "Link",
                  "value": "={{$json[\"permalink\"]}}"
                }
              ]
            },
            "footer": "=Added: {{$json[\"date_created\"]}}"
          }
        ],
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": {
          "id": "21",
          "name": "FVF bot"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "On product creation",
      "type": "n8n-nodes-base.wooCommerceTrigger",
      "position": [
        460,
        300
      ],
      "webhookId": "267c4855-6227-4d33-867e-74600097473e",
      "parameters": {
        "event": "product.created"
      },
      "credentials": {
        "wooCommerceApi": {
          "id": "20",
          "name": "WooCommerce account FVF"
        }
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "On product creation": {
      "main": [
        [
          {
            "node": "If URL has /product/",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If URL has /product/": {
      "main": [
        [
          {
            "node": "Send message to slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
