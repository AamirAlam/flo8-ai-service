# Send Hourly Crypto Market Analysis from Binance to Telegram

**[View Template](https://n8n.io/workflows/3621-/)**  **Published Date:** 04/20/2025  **Created By:** Aurélien P.  **Categories:** `Development` `Core Nodes` `Communication` `HITL`  

## Template Description

📈 Daily Crypto Market Summary Bot (Binance to Telegram)

This workflow fetches 24h price change data from Binance for selected crypto pairs (BTC/USDC, ETH/USDC, SOL/USDC) every hour using a cron schedule.  
It performs in-depth analysis—including volatility, volume, bid-ask spread, momentum, and market comparison—then formats a detailed market summary.  
The final report is sent to a Telegram chat using HTML formatting, highlighting top gainers, losers, and key metrics in a clean, readable layout.

🔑 Key Features
⏱ Runs every hour (cron: 5 * * * *)
🔍 Filters and analyzes major coins: BTC, ETH, SOL
📊 Calculates market metrics:
  Volatility
  Bid-ask spread
  Momentum
  Estimated market cap
  Market average comparison
📈 Highlights gainers, losers, and top coins by volume
✂️ Splits messages to fit Telegram’s 4096 character limit
💬 Sends output in rich HTML format to a Telegram group or chat

🎯 Use Cases
✅ Crypto traders wanting hourly performance insights
✅ Telegram groups needing automated market updates
✅ Analysts monitoring key coin metrics in real-time
✅ Bot developers creating crypto dashboards or alerts

🛠 Technical Details
Data Source:** Binance 24hr ticker API (/api/v3/ticker/24hr)
Coins Monitored:** BTCUSDC, ETHUSDC, SOLUSDC (can be expanded)
Metrics Calculated:**
  Price change percentage
  Volatility (high vs low price)
  Bid-ask spread %
  Momentum (vs weighted average)
  Estimated market cap
  Number of trades
  Market average movement
Message Format:**
  HTML with emojis, bold styling, and section headings
  Auto-split messages when exceeding Telegram's 4096-char limit
Error Handling:**
  Retry on HTTP failure (up to 5 times with 5s delay)
  Message length checked and split for Telegram compatibility

⚙️ Setup Requirements
Telegram Bot Token — Create a bot via @BotFather on Telegram
Chat ID — Use a personal ID or group chat ID (add the bot to the group)
n8n Instance — Either cloud or self-hosted
(Optional) Modify relevantSymbols in the Function node to track different coins

🧠 Notes
This workflow is highly customizable—feel free to modify the analytics, tracked pairs, or formatting.
Great base for alerting systems or crypto dashboards.

📷 Example Output (Telegram)
📊 Crypto Market Summary — 2025-04-20 14:05:05 UTC

🌐 Market Overview (BTC, ETH, SOL)
Average Change: -1.54%
24h Volume: $850,358,765.46
Most Volatile: SOLUSDC (4.53%)
Most Liquid: BTCUSDC (0.0000% spread)

💹 Top by Volume
ETHUSDC: $403,860,356.75 | -1.640%
SOLUSDC: $279,241,338.60 | -1.706%
BTCUSDC: $167,257,070.12 | -1.261%

📉 Losers

SOLUSDC
🔻 Change: -1.71% (24h)
💰 Current: $137.10
📊 Range: $135.82 - $141.97
📈 Volatility: 4.53%
🔄 Volume: 2.01M | $279,241,338.60
⚖️ Bid-Ask Spread: 0.0073%
⬇️ vs Market Avg: -0.17%
🔽 Momentum: -1.42%
🔢 Trades: 366,119

ETHUSDC
🔻 Change: -1.64% (24h)
💰 Current: $1,577.42
📊 Range: $1,565.60 - $1,631.98
📈 Volatility: 4.24%
🔄 Volume: 252.11K | $403,860,356.75
⚖️ Bid-Ask Spread: 0.0044%
⬇️ vs Market Avg: -0.10%
🔽 Momentum: -1.53%
🔢 Trades: 596,801

BTCUSDC
🔻 Change: -1.26% (24h)
💰 Current: $84,336.65
📊 Range: $83,963.35 - $85,634.50
📈 Volatility: 1.99%
🔄 Volume: 1.97K | $167,257,070.12
⚖️ Bid-Ask Spread: 0.0000%
⭐ vs Market Avg: 0.27%
🔽 Momentum: -0.68%
🔢 Trades: 124,202

## Template JSON

```
{
  "meta": {
    "instanceId": "411a4eea57cf88d4a82c27728a11bad4fe2fdcbc1ab5eae589890a37e4b909ca",
    "templateId": "2043"
  },
  "nodes": [
    {
      "id": "9fd007e4-9d21-4fef-8a28-3be3e92af6f7",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        260,
        600
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "cronExpression",
              "expression": "5 * * * *"
            }
          ]
        }
      },
      "typeVersion": 1.1
    },
    {
      "id": "cd23c427-56f1-4924-8adf-4b38417ba652",
      "name": "Binance 24h Price Change",
      "type": "n8n-nodes-base.httpRequest",
      "notes": "Get data of changed price coins in last 24h",
      "maxTries": 5,
      "position": [
        600,
        600
      ],
      "parameters": {
        "url": "https://api.binance.com/api/v3/ticker/24hr",
        "options": {}
      },
      "notesInFlow": true,
      "retryOnFail": true,
      "typeVersion": 1,
      "waitBetweenTries": 5000
    },
    {
      "id": "40e4f7bd-ac47-4617-9177-5a84ada3a92f",
      "name": "Send Telegram Message",
      "type": "n8n-nodes-base.telegram",
      "position": [
        1560,
        600
      ],
      "webhookId": "75a4f97f-1a11-47fd-9f90-cbecd75ad2df",
      "parameters": {
        "text": "={{ $json.data }}\n\n",
        "chatId": "-4685771678",
        "additionalFields": {
          "parse_mode": "HTML"
        }
      },
      "credentials": {
        "telegramApi": {
          "id": "d6O4BUmt3I6XZJ1D",
          "name": "Telegram account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "424bbed3-f134-418c-9961-e966c8dc2592",
      "name": "Analyze & Format Market Data",
      "type": "n8n-nodes-base.function",
      "position": [
        900,
        600
      ],
      "parameters": {
        "functionCode": "function escapeHTML(text) {\n  return String(text)\n    .replace(/&/g, \"&amp;\")\n    .replace(/</g, \"&lt;\")\n    .replace(/>/g, \"&gt;\");\n}\n\nfunction formatVolume(volume) {\n  const vol = parseFloat(volume);\n  if (vol >= 1_000_000_000) return (vol / 1_000_000_000).toFixed(2) + 'B';\n  if (vol >= 1_000_000) return (vol / 1_000_000).toFixed(2) + 'M';\n  if (vol >= 1_000) return (vol / 1_000).toFixed(2) + 'K';\n  return vol.toString();\n}\n\nfunction formatMoney(amount) {\n  return parseFloat(amount).toLocaleString('en-US', {\n    minimumFractionDigits: 2,\n    maximumFractionDigits: 2\n  });\n}\n\nfunction calculateVolatility(coin) {\n  const high = parseFloat(coin.highPrice);\n  const low = parseFloat(coin.lowPrice);\n  const volatility = ((high - low) / low) * 100;\n  return volatility.toFixed(2);\n}\n\nfunction calculateSpread(coin) {\n  const ask = parseFloat(coin.askPrice);\n  const bid = parseFloat(coin.bidPrice);\n  const spread = ((ask - bid) / bid) * 100;\n  return spread.toFixed(4);\n}\n\nfunction calculateMarketComparison(coin, avgMarketChange) {\n  const coinChange = parseFloat(coin.priceChangePercent);\n  const comparison = coinChange - avgMarketChange;\n  return comparison.toFixed(2);\n}\n\nfunction formatActivity(count) {\n  return count.toLocaleString('en-US');\n}\n\nfunction calculateMomentum(coin) {\n  const current = parseFloat(coin.lastPrice);\n  const weighted = parseFloat(coin.weightedAvgPrice);\n  return ((current - weighted) / weighted * 100).toFixed(2);\n}\n\nfunction estimateMarketCap(coin) {\n  return parseFloat(coin.lastPrice) * parseFloat(coin.quoteVolume);\n}\n\nfunction formatCoinWithAnalytics(coin, avgMarketChange) {\n  const change = parseFloat(coin.priceChangePercent);\n  const arrow = change > 0 ? '\ud83d\udd3a' : '\ud83d\udd3b';\n  const volatility = calculateVolatility(coin);\n  const spread = calculateSpread(coin);\n  const marketComparison = calculateMarketComparison(coin, avgMarketChange);\n  const momentum = calculateMomentum(coin);\n  \n  const comparisonEmoji = marketComparison > 0 ? '\u2b50' : '\u2b07\ufe0f';\n  const momentumEmoji = parseFloat(momentum) > 0 ? '\ud83d\udd3c' : '\ud83d\udd3d';\n  \n  const timeFrameHours = (coin.closeTime - coin.openTime) / (1000 * 60 * 60);\n  \n  return `<b>${escapeHTML(coin.symbol)}</b>\\n` +\n         `${arrow} Change: ${escapeHTML(change.toFixed(2))}% (${timeFrameHours.toFixed(0)}h)\\n` +\n         `\ud83d\udcb0 Current: $${formatMoney(coin.lastPrice)}\\n` +\n         `\ud83d\udcca Range: $${formatMoney(coin.lowPrice)} - $${formatMoney(coin.highPrice)}\\n` +\n         `\ud83d\udcc8 Volatility: ${volatility}%\\n` +\n         `\ud83d\udd04 Volume: ${escapeHTML(formatVolume(coin.volume))} | $${formatMoney(coin.quoteVolume)}\\n` +\n         `\u2696\ufe0f Bid-Ask Spread: ${spread}%\\n` +\n         `${comparisonEmoji} vs Market Avg: ${marketComparison}%\\n` +\n         `${momentumEmoji} Momentum: ${momentum}%\\n` +\n         `\ud83d\udd22 Trades: ${formatActivity(coin.count)}\\n\\n`;\n}\n\nfunction calculateMarketStats(coins) {\n  const totalVolume = coins.reduce((sum, coin) => sum + parseFloat(coin.quoteVolume), 0);\n  const averageChange = coins.reduce((sum, coin) => sum + parseFloat(coin.priceChangePercent), 0) / coins.length;\n  const mostVolatile = [...coins].sort((a, b) => calculateVolatility(b) - calculateVolatility(a))[0];\n  const mostTraded = [...coins].sort((a, b) => parseFloat(b.quoteVolume) - parseFloat(a.quoteVolume))[0];\n  const leastSpread = [...coins].sort((a, b) => calculateSpread(a) - calculateSpread(b))[0];\n  \n  const topByVolume = [...coins]\n    .sort((a, b) => parseFloat(b.quoteVolume) - parseFloat(a.quoteVolume))\n    .slice(0, 3);\n  \n  return {\n    totalVolume,\n    averageChange,\n    mostVolatile,\n    mostTraded,\n    leastSpread,\n    topByVolume\n  };\n}\n\nconst now = new Date();\nconst dateString = now.toISOString().replace('T', ' ').split('.')[0] + ' UTC';\nconst rawData = items[0].json;\n\nconst binanceData = Array.isArray(rawData) ? rawData : [];\nconst usdcPairs = binanceData.filter(coin => coin.symbol.endsWith('USDC'));\n\n// Filter only for Solana, Bitcoin, Ethereum\nconst relevantSymbols = ['SOLUSDC', 'BTCUSDC', 'ETHUSDC'];\nconst filteredCoins = usdcPairs.filter(coin => relevantSymbols.includes(coin.symbol));\n\n// Calculate market cap for each coin\nfilteredCoins.forEach(coin => {\n  coin.estimatedMarketCap = estimateMarketCap(coin);\n});\n\nconst marketStats = calculateMarketStats(filteredCoins);\nconst avgMarketChange = marketStats.averageChange;\n\nconst gainers = filteredCoins\n  .filter(c => parseFloat(c.priceChangePercent) > 0)\n  .sort((a, b) => parseFloat(b.priceChangePercent) - parseFloat(a.priceChangePercent));\n\nconst losers = filteredCoins\n  .filter(c => parseFloat(c.priceChangePercent) < 0)\n  .sort((a, b) => parseFloat(a.priceChangePercent) - parseFloat(b.priceChangePercent));\n\n// Build message\nlet summary = `<b>\ud83d\udcca Crypto Market Summary \u2014 ${escapeHTML(dateString)}</b>\\n\\n`;\n\nsummary += `<b>\ud83c\udf10 Market Overview (BTC, ETH, SOL)</b>\\n` +\n           `Average Change: ${avgMarketChange.toFixed(2)}%\\n` +\n           `24h Volume: $${formatMoney(marketStats.totalVolume)}\\n` +\n           `Most Volatile: ${marketStats.mostVolatile.symbol} (${calculateVolatility(marketStats.mostVolatile)}%)\\n` +\n           `Most Liquid: ${marketStats.leastSpread.symbol} (${calculateSpread(marketStats.leastSpread)}% spread)\\n\\n`;\n\nsummary += `<b>\ud83d\udcb9 Top by Volume</b>\\n`;\nmarketStats.topByVolume.forEach(coin => {\n  summary += `${coin.symbol}: $${formatMoney(coin.quoteVolume)} | ${coin.priceChangePercent}%\\n`;\n});\nsummary += `\\n`;\n\nif (gainers.length) {\n  summary += `<b>\ud83d\udcc8 Gainers</b>\\n\\n`;\n  summary += gainers.map(coin => formatCoinWithAnalytics(coin, avgMarketChange)).join('');\n}\n\nif (losers.length) {\n  summary += `<b>\ud83d\udcc9 Losers</b>\\n\\n`;\n  summary += losers.map(coin => formatCoinWithAnalytics(coin, avgMarketChange)).join('');\n}\n\nconst chunks = [];\nlet current = \"\";\nsummary.split(/\\n/g).forEach(line => {\n  const lineWithBreak = line + \"\\n\";\n  if ((current + lineWithBreak).length > 4000) {\n    chunks.push({ json: { data: current.trim() } });\n    current = lineWithBreak;\n  } else {\n    current += lineWithBreak;\n  }\n});\n\nif (current.trim()) {\n  chunks.push({ json: { data: current.trim() } });\n}\n\nreturn chunks;"
      },
      "notesInFlow": true,
      "typeVersion": 1
    },
    {
      "id": "1c43afdc-b15a-4380-9c6f-2056e28a37f7",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        220,
        -100
      ],
      "parameters": {
        "color": 6,
        "width": 940,
        "height": 620,
        "content": "## \ud83d\udccc Daily Crypto Market Summary Bot\n\n### \ud83d\udcc8 What It Does\nFetches hourly 24h price data from Binance for **BTC**, **ETH**, and **SOL** (USDC pairs), analyzes key market trends, and sends a well-formatted HTML summary to a Telegram chat.\n\n---\n### \ud83d\udcca Metrics Analyzed\n- \ud83d\udd3a Gainers / \ud83d\udcc9 Losers\n- \ud83d\udcb0 Price change %\n- \ud83d\udcc8 Volatility (High vs Low)\n- \u2696\ufe0f Bid-Ask Spread %\n- \ud83d\udd3c Momentum (vs Weighted Avg)\n- \u2b50 vs Market Average\n - \ud83d\udd22 Number of Trades\n\n---\n### \u26a0\ufe0f Notes\n- Message output is automatically **split into chunks** to stay under Telegram\u2019s **4096 character limit**.\n- Output is sent in **rich HTML format** for better readability.\n\n---\n\n\u2705 This note is for internal guidance. Feel free to delete or update it after setup.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "5bbd9227-2a52-4130-abf1-f6745327dbd4",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1540,
        780
      ],
      "parameters": {
        "width": 340,
        "height": 240,
        "content": "### \ud83d\udee0\ufe0f Setup Instructions\n\n4. **Telegram**\n   - Create a bot via [@BotFather](https://t.me/BotFather)\n   - Add the bot to a Telegram group or use a personal chat\n   - In the **Send Telegram Message** node:\n     - Add your bot token under credentials\n     - Replace the default `chatId` with your group/user chat ID\n"
      },
      "typeVersion": 1
    },
    {
      "id": "ffa51aa0-181a-415b-933c-44fd01ca27da",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        560,
        800
      ],
      "parameters": {
        "height": 180,
        "content": "**Binance**\n   - No Binance API key required (uses public endpoint)\n   - Ensure internet access to call Binance API"
      },
      "typeVersion": 1
    },
    {
      "id": "ba902bcb-f24c-491a-bcaa-ab7bf16e5bb1",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        220,
        800
      ],
      "parameters": {
        "height": 180,
        "content": "\n### \u23f1 Schedule\n- Runs **every hour**\n- Cron expression: `5 * * * *`  \n  _(At minute 5 of every hour)_"
      },
      "typeVersion": 1
    },
    {
      "id": "ae8b4d48-90ab-4b28-bbc7-07ed5d333815",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        900,
        820
      ],
      "parameters": {
        "width": 560,
        "content": "\n3. **Optional: Add More Coins**\n   - In the **Function node**, find the line:\n     ```js\n     const relevantSymbols = ['SOLUSDC', 'BTCUSDC', 'ETHUSDC'];\n     ```\n   - Add your preferred trading pairs (must end in `USDC`)"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
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
    "Binance 24h Price Change": {
      "main": [
        [
          {
            "node": "Analyze & Format Market Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Analyze & Format Market Data": {
      "main": [
        [
          {
            "node": "Send Telegram Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
