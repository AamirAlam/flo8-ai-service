# Crypto Market Alert System with Binance and Telegram Integration

**[View Template](https://n8n.io/workflows/2043-/)**  **Published Date:** 01/08/2024  **Created By:** Nskha  **Categories:** `Development` `Core Nodes` `Communication` `HITL`  

## Template Description

An innovative N8N workflow that monitors cryptocurrency prices on Binance, identifies significant market movements, and sends customized alerts through Telegram. Ideal for traders and enthusiasts seeking real-time market insights.

How It Works

Trigger Options: Choose between a manual trigger or a scheduled trigger to start the workflow.
Fetch Market Data: The 'Binance 24h Price Change' node retrieves the latest 24-hour price changes for cryptocurrencies from Binance.
Identify Significant Changes: The 'Filter by 10% Change rate' node filters out cryptocurrencies with price changes of 10% or more.
Aggregate Data: The 'Aggregate' node combines all significant changes into a single dataset.
Format Data for Telegram: The 'Split By 1K chars' node formats this data into chunks suitable for Telegram's message size limit.
Send Telegram Message: The 'Send Telegram Message' node broadcasts the formatted message to a specified Telegram chat.

Set Up Steps
Estimated Time**: About 1-5 minutes for setup.
Initial Configuration**: Set up a Binance API connection (Optional) and your Telegram bot credentials.
Customization**: Adjust the trigger according to your preference (manual or scheduled) and update the Telegram chat ID.

Create Telegram bot steps**:-
Setting up a Telegram bot and obtaining its token involves several steps. Here's a detailed guide:

Start a Chat with BotFather:
   Open Telegram and search for "BotFather". This is the official bot that allows you to create new bots.
   Start a chat with BotFather by clicking on the "Start" button at the bottom of the screen.

Create a New Bot:
   In the chat with BotFather, type /newbot and send the message.
   BotFather will ask you to choose a name for your bot. This is a display name and can be anything you like.
   Next, you'll need to choose a username for your bot. This must be unique and end in bot. For example, my_crypto_alert_bot.

Receive Your Token:
   After you've set the name and username, BotFather will provide you with a token. This token is like a password for your bot, so keep it secure.
   The message will look something like this: 
          Done! Congratulations on your new bot. You will find it at t.me/my_crypto_alert_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. Use this token to access the HTTP API: 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
        The token in this case is 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11.

Test Your Bot:
   You can find your bot by searching for its username in Telegram.
   Start a chat with your bot and try sending it a message. Although it won't respond yet, this step is essential to ensure it's set up correctly.

Use the Token in n8n:
   In your n8n workflow, when setting up the Telegram node, you'll be prompted to enter credentials.
   Choose to add new credentials and paste the token you received from BotFather.

Get Your Chat ID:
   To send messages to a specific chat, you need to know the chat ID.
   The easiest way to find this is to first message your bot, then use a bot like @userinfobot to get your chat ID.
   Once you have the chat ID, you can configure it in the Telegram node in your n8n workflow.

Finalize Your Workflow:
   With the bot token and chat ID set up in n8n, your Telegram notifications should work as intended in your workflow.

Remember, keep your bot token secure and never share it publicly. If your token is compromised, you can always generate a new one by chatting with BotFather and selecting /token.

Example result



Keywords: n8n workflow, cryptocurrency market, Binance API, Telegram bot, price alert system, automated trading signals, market analysis
`

## Template JSON

```
{
  "meta": {
    "instanceId": "dbd43d88d26a9e30d8aadc002c9e77f1400c683dd34efe3778d43d27250dde50"
  },
  "nodes": [
    {
      "id": "f305e08e-d4b4-4ec6-be74-5edb7a3711e5",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        520,
        1279
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "minutes"
            }
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "abac20ef-6319-40e3-8d30-806d7499a427",
      "name": "Send Telegram Message",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1360,
        1279
      ],
      "parameters": {
        "text": "={{ $json.data.replaceAll(/(Last Price: \\S+)$/gm,\"$1\\n\").slice(0,1000) }}",
        "chatId": "-1002138086614",
        "additionalFields": {}
      },
      "typeVersion": 1
    },
    {
      "id": "d23c3277-62ca-4e1f-ad5d-48c07e0d6b94",
      "name": "Aggregate",
      "type": "n8n-nodes-base.aggregate",
      "notes": "Combine all items",
      "position": [
        1020,
        1279
      ],
      "parameters": {
        "options": {},
        "aggregate": "aggregateAllItemData"
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "ba174e7f-4377-46dc-aca8-30adf81e5d61",
      "name": "Binance 24h Price Change",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Get data of changed price coins in last 24h",
      "position": [
        680,
        1279
      ],
      "parameters": {
        "url": "https://api.binance.com/api/v1/ticker/24hr",
        "options": {}
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "575563d5-3fb5-40f3-8017-d015cc822d5f",
      "name": "Filter by 10% Change rate",
      "type": "n8n-nodes-base.function",
      "notes": "Filter by 10% Up & Down",
      "position": [
        860,
        1279
      ],
      "parameters": {
        "functionCode": "// Iterate over all coins and check for 10% price change\nconst significantChanges = [];\nfor (const coin of items[0].json) {\n  const priceChangePercent = parseFloat(coin.priceChangePercent);\n  if (Math.abs(priceChangePercent) >= 15) {\n    significantChanges.push({ \n      symbol: coin.symbol, \n      priceChangePercent, \n      lastPrice: coin.lastPrice \n    });\n  }\n}\n\n// Sort the items by percent rate from high to low\nsignificantChanges.sort((a, b) => b.priceChangePercent - a.priceChangePercent);\n\n// Format the sorted data for output\nconst sortedOutput = significantChanges.map(change => ({\n  json: { message: `\\`\\`\\`${change.symbol} Price changed by ${change.priceChangePercent}% \\n Last Price: ${change.lastPrice}\\`\\`\\`` }\n}));\n\nreturn sortedOutput;\n"
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "dcfeae2e-bcdd-472d-98e4-8c1772ccdf1b",
      "name": "Split By 1K chars",
      "type": "n8n-nodes-base.code",
      "notes": "Split them for telegram message limit",
      "position": [
        1180,
        1279
      ],
      "parameters": {
        "jsCode": "// Function to split the data into chunks of approximately 1000 characters\nfunction splitDataIntoChunks(data) {\n    const chunks = [];\n    let currentChunk = \"\";\n\n    data.forEach(item => {\n        // Ensure that each item has a 'message' property\n        if (item && item.message) {\n            const message = item.message + \"\\n\"; // Adding a newline for separation\n            // Check if adding this message to the current chunk would exceed the 1000 characters limit\n            if (currentChunk.length + message.length > 1000) {\n                // If so, push the current chunk to the chunks array and start a new chunk\n                chunks.push({ json: { data: currentChunk } });\n                currentChunk = message;\n            } else {\n                // Otherwise, add the message to the current chunk\n                currentChunk += message;\n            }\n        }\n    });\n\n    // Add the last chunk if it's not empty\n    if (currentChunk) {\n        chunks.push({ json: { data: currentChunk } });\n    }\n\n    return chunks;\n}\n\n// The input data is passed from the previous node\nconst inputData = items[0].json.data; // Accessing the 'data' property\n\n// Process the data\nconst result = splitDataIntoChunks(inputData);\n\n// Output the result\nreturn result;\n"
      },
      "notesInFlow": true,
      "typeVersion": 2
    },
    {
      "id": "40e25c71-641a-4b69-afec-b8a93d5d6448",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        483.54457851446114,
        1040
      ],
      "parameters": {
        "color": 5,
        "width": 1040.928205084989,
        "height": 183.94838465674636,
        "content": "### Workflow Setup Steps:\n1. Ensure the **_Schedule Trigger_** is active to desired cron time (Default 5 minutes).\n2. [_Optional_] Configure the **_Binance 24h Price Change_** node with your API details (Default one is Free Public API Call - Free).\n3. Set up your **Telegram bot** token in the **Telegram node credentials**.\n4. Update the **_Chat ID_** in the **_Send Telegram Message_** node.\n5. Test the workflow to ensure everything is set up correctly.\n* **Notes**: Detailed telegram bot setup instructions are available in the [workflow's n8n page](https://n8n.io/workflows/2043-crypto-market-alert-system-with-binance-and-telegram-integration)."
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Aggregate": {
      "main": [
        [
          {
            "node": "Split By 1K chars",
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
            "node": "Binance 24h Price Change",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split By 1K chars": {
      "main": [
        [
          {
            "node": "Send Telegram Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Binance 24h Price Change": {
      "main": [
        [
          {
            "node": "Filter by 10% Change rate",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter by 10% Change rate": {
      "main": [
        [
          {
            "node": "Aggregate",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
