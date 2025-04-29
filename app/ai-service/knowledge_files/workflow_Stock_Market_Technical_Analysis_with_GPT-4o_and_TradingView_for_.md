# Stock Market Technical Analysis with GPT-4o and TradingView for Telegram

**[View Template](https://n8n.io/workflows/3202-/)**  **Published Date:** 03/17/2025  **Created By:** Badr  **Categories:** `Development` `Core Nodes` `Communication` `HITL` `AI` `Langchain`  

## Template Description


Overview: Transform Your Trading with AI-Driven Technical Analysis

The Stock Market Technical Analysis Bot is an advanced n8n workflow that brings professional-grade stock analysis to Telegram users. This powerful AI agent analyzes stock charts in real-time, providing detailed technical insights that would typically require expensive software or expert knowledge.

By combining artificial intelligence with technical analysis indicators, this bot delivers actionable trading insights directly to your Telegram chat, making sophisticated market analysis accessible to traders of all experience levels.

Key Features and Capabilities

Advanced Technical Analysis Tools
Japanese Candlestick Pattern Recognition**: Automatically identifies bullish engulfing, doji, hammer patterns and more
MACD Indicator Analysis**: Detects bullish/bearish crossovers and divergence signals
Volume Trend Analysis**: Validates price movements with volume confirmation
Support & Resistance Level Identification**: Pinpoints key price levels for potential reversals
Bollinger Bands & RSI Analysis**: Measures volatility and overbought/oversold conditions
Real-Time TradingView Charts**: Professional-quality charts with multiple indicators

AI-Powered Trading Assistant
Natural Language Interface**: Interact with the bot using simple conversational commands
Context-Aware Responses**: The bot remembers your previous interactions for more relevant analysis
GPT-4o Integration**: Leverages advanced language models for detailed explanations
Actionable Trading Insights**: Receive clear, jargon-free analysis with practical implications

Technical Implementation
Telegram Bot Integration**: Seamless messaging experience with instant responses
n8n Workflow Automation**: No-code solution for complex trading analysis
Memory System**: Maintains conversation context for personalized interactions
API Connections**: Integrates with TradingView, chart-img.com, and OpenAI

Setup Instructions

Prerequisites
n8n Instance: A running n8n installation with the following nodes:
   Telegram nodes
   LangChain nodes
   HTTP Request nodes
   Code node

Required API Credentials:
   Telegram Bot API token (obtain from @BotFather)
   OpenAI API key
   Chart-img.com API key

Installation Process
Import the workflow template into your n8n instance
Configure your Telegram bot credentials
Set up your OpenAI API credentials
Enter your chart-img.com API key in the HTTP Request node
Activate the workflow to start receiving analysis requests

How It Works: The Technical Analysis Process

1. User Interaction Flow
When a user sends a message to the Telegram bot:
The Telegram Trigger node captures the incoming message
The AI Agent processes the request using natural language understanding
If a stock symbol is detected, the GetChart tool is invoked

2. Chart Generation System
The workflow creates professional TradingView charts with:
Candlestick price data
Bollinger Bands for volatility measurement
Volume indicators for trade validation
RSI (Relative Strength Index) for momentum analysis

3. AI Analysis Engine
The GPT-4o model analyzes the chart and provides:
Detailed breakdown of candlestick patterns
MACD trend confirmation signals
Volume analysis to validate price movements
Support and resistance level identification
Overall market sentiment assessment

4. Response Delivery
The analysis is formatted and sent back to the user via Telegram, including:
The generated chart image
Comprehensive technical analysis text
Actionable insights based on the indicators

Use Cases and Applications

For Day Traders
Receive quick technical analysis before making trading decisions
Validate your own analysis with AI-generated insights
Track multiple stocks efficiently throughout the trading day

For Swing Traders
Analyze medium-term trends and potential entry/exit points
Identify key support and resistance levels for stop-loss placement
Get objective analysis to complement your trading strategy

For Trading Communities
Share consistent, AI-generated analysis among group members
Create a common analytical framework for discussion
Reduce the learning curve for technical analysis concepts

For Financial Educators
Demonstrate technical analysis concepts with real-time examples
Provide students with accessible tools for practice
Illustrate the application of various technical indicators

Advanced Configuration Options

The workflow can be customized to:
Add additional technical indicators (Fibonacci retracements, Moving Averages, etc.)
Modify the analysis parameters for different trading styles
Integrate with other financial data sources for fundamental analysis
Connect to different messaging platforms beyond Telegram
Create scheduled analysis for watchlist stocks

Troubleshooting Common Issues

If you encounter problems:
Authentication Errors: Verify all API credentials are correctly configured
Telegram Connection Issues: Ensure your Telegram bot is properly set up
Chart Generation Failures: Check your chart-img.com API key and quota
Slow Response Times: Consider upgrading your OpenAI plan for faster processing
Missing Indicators: Verify the chart configuration in the HTTP Request node

About This Template

This n8n workflow template demonstrates the power of combining conversational AI with technical analysis tools to create a sophisticated financial assistant. It showcases advanced workflow automation features including AI integration, external API connections, and complex data processing.

By leveraging the latest advancements in AI and technical analysis, this template provides traders with professional-grade insights without requiring expensive software or deep technical expertise.

Keywords: stock market analysis bot, AI trading assistant, technical analysis indicators, n8n workflow, Telegram trading bot, candlestick pattern recognition, MACD analysis, trading signals, automated stock analysis, GPT-4o financial analysis, TradingView charts, RSI indicator, volume analysis, support resistance levels, day trading bot, swing trading analysis, AI financial advisor


## Template JSON

```
{
  "meta": {
    "instanceId": "4786bf0f18c0e8e92c361de5a158cabf4eb0bb3b9c113091b054ff26e359a029",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "57a8cbd8-bc2f-4600-a077-c2cec70962d8",
      "name": "Telegram Trigger",
      "type": "n8n-nodes-base.telegramTrigger",
      "position": [
        220,
        100
      ],
      "webhookId": "5c56b0ad-c452-4ada-aba6-ac4da8238aca",
      "parameters": {},
      "typeVersion": 1.1
    },
    {
      "id": "c0794d04-4a75-4e78-93c8-fd6dbecfb87c",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        580,
        100
      ],
      "parameters": {},
      "typeVersion": 1.7
    },
    {
      "id": "a7a243d2-80f7-4ace-b758-74770c83be0e",
      "name": "Window Buffer Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        640,
        320
      ],
      "parameters": {},
      "typeVersion": 1.3
    },
    {
      "id": "aa4d7ada-5275-4271-8b9f-e0ec32f0c699",
      "name": "GetChart",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "position": [
        860,
        320
      ],
      "parameters": {},
      "typeVersion": 2
    },
    {
      "id": "c8f7d274-930e-4a23-ac6e-ab8a3b434c70",
      "name": "Response2",
      "type": "n8n-nodes-base.telegram",
      "position": [
        980,
        100
      ],
      "webhookId": "a2e618b0-f2a6-4d64-8782-7069e39a59bd",
      "parameters": {},
      "typeVersion": 1.2
    },
    {
      "id": "9580a9a5-3153-4fa9-8862-8e2e08506fac",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        0
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "4c40f975-b35d-4706-9935-de521db30cd2",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "position": [
        420,
        320
      ],
      "parameters": {},
      "typeVersion": 1.2
    },
    {
      "id": "26b9939c-dec4-4142-b884-6cbef56adb26",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        460
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    },
    {
      "id": "19b572cf-1a26-4e83-bdf6-d005cf2e9ea1",
      "name": "When Executed by Another Workflow",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        40,
        560
      ],
      "parameters": {},
      "typeVersion": 1.1
    },
    {
      "id": "0e76105a-62b1-4b2f-9e84-7c4f11b3b0c4",
      "name": "Download Chart",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        840,
        560
      ],
      "parameters": {},
      "typeVersion": 4.2
    },
    {
      "id": "6f506393-e225-45ec-a49f-eb473585e877",
      "name": "Analysis",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        1020,
        560
      ],
      "parameters": {},
      "typeVersion": 1.8
    },
    {
      "id": "1188a40d-16a2-4536-8d60-1be4eaccd353",
      "name": "Response",
      "type": "n8n-nodes-base.set",
      "position": [
        1420,
        560
      ],
      "parameters": {},
      "typeVersion": 3.4
    },
    {
      "id": "655d3289-55c6-49e3-8e1d-c7883ce57415",
      "name": "Telegram",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1220,
        560
      ],
      "webhookId": "31b77856-a976-4e63-9e6b-aeada64aeaab",
      "parameters": {},
      "typeVersion": 1.2
    },
    {
      "id": "562a4d01-5a27-466d-9114-c5edc4205885",
      "name": "Get Chart",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        640,
        560
      ],
      "parameters": {},
      "typeVersion": 4.2
    },
    {
      "id": "4fb8a467-b3b1-49c6-9eb9-c24e439fdfc4",
      "name": "Symbol And ChatId",
      "type": "n8n-nodes-base.set",
      "position": [
        440,
        560
      ],
      "parameters": {},
      "typeVersion": 3.4
    },
    {
      "id": "61e766ff-1b07-4bbc-9d48-fe996281fc00",
      "name": "Code",
      "type": "n8n-nodes-base.code",
      "position": [
        240,
        560
      ],
      "parameters": {},
      "typeVersion": 2
    }
  ],
  "pinData": {},
  "connections": {
    "Code": {
      "main": [
        [
          {
            "node": "Symbol And ChatId",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Agent": {
      "main": [
        [
          {
            "node": "Response2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Analysis": {
      "main": [
        [
          {
            "node": "Telegram",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "GetChart": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Telegram": {
      "main": [
        [
          {
            "node": "Response",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Chart": {
      "main": [
        [
          {
            "node": "Download Chart",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Download Chart": {
      "main": [
        [
          {
            "node": "Analysis",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Telegram Trigger": {
      "main": [
        [
          {
            "node": "AI Agent",
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
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Symbol And ChatId": {
      "main": [
        [
          {
            "node": "Get Chart",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Window Buffer Memory": {
      "ai_memory": [
        [
          {
            "node": "AI Agent",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "When Executed by Another Workflow": {
      "main": [
        [
          {
            "node": "Code",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
