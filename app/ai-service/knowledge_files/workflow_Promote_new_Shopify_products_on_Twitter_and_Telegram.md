# Promote new Shopify products on Twitter and Telegram

**[View Template](https://n8n.io/workflows/1205-/)**  **Published Date:** 08/24/2021  **Created By:** Lorena  **Categories:** `Communication` `HITL` `Marketing`  

## Template Description

This workflow automatically promotes your new Shopify products on Twitter and Telegram. This workflow is also featured in the blog post 6 e-commerce workflows to power up your Shopify store.

Prerequisites

A Shopify account and credentials
A Twitter account and credentials
A Telegram account and credentials for the channel you want to send messages to.

Nodes

Shopify Trigger node triggers the workflow when you create a new product in Shopify.
Twitter node posts a tweet with the text "Hey there, my design is now on a new product! Visit my {shop name} to get this cool {product title} (and check out more {product type})".
Telegram node posts a message with the same text as above in a Telegram channel.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Twitter",
      "type": "n8n-nodes-base.twitter",
      "position": [
        720,
        -220
      ],
      "parameters": {
        "text": "=Hey there, my design is now on a new product \u2728\nVisit my {{$json[\"vendor\"]}} shop to get this cool{{$json[\"title\"]}} (and check out more {{$json[\"product_type\"]}}) \ud83d\udecd\ufe0f",
        "additionalFields": {}
      },
      "credentials": {
        "twitterOAuth1Api": "twitter"
      },
      "typeVersion": 1
    },
    {
      "name": "Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        720,
        -20
      ],
      "parameters": {
        "text": "=Hey there, my design is now on a new product!\nVisit my {{$json[\"vendor\"]}} shop to get this cool{{$json[\"title\"]}} (and check out more {{$json[\"product_type\"]}})",
        "chatId": "123456",
        "additionalFields": {}
      },
      "credentials": {
        "telegramApi": "telegram_habot"
      },
      "typeVersion": 1
    },
    {
      "name": "product created",
      "type": "n8n-nodes-base.shopifyTrigger",
      "position": [
        540,
        -110
      ],
      "webhookId": "2a7e0e50-8f09-4a2b-bf54-a849a6ac4fe0",
      "parameters": {
        "topic": "products/create"
      },
      "credentials": {
        "shopifyApi": "shopify_nodeqa"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "product created": {
      "main": [
        [
          {
            "node": "Twitter",
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
