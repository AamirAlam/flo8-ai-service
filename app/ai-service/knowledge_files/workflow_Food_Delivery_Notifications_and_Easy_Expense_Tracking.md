# Food Delivery Notifications and Easy Expense Tracking

**[View Template](https://n8n.io/workflows/2707-/)**  **Published Date:** 01/08/2025  **Created By:** darrell_tw  **Categories:** `Communication` `HITL`  

## Template Description

Workflow Description
This workflow automates the process of retrieving emails from a food delivery platform, extracting key order details, and sending notifications to a Slack channel. Additionally, the Slack message includes a Moze accounting app URL scheme link for quick expense tracking.

Key Features
Manual Trigger: Allows the workflow to be executed manually for immediate testing.
Gmail Integration: Retrieves emails containing specific keywords in the subject line (e.g., "透過 Uber Eats 系統送出的訂單"). (You can adjust the keywords to fit your language.)
Data Extraction: Parses the email content to extract key details such as:
   Order price
   Shop name
   Order date and time
Slack Notification: Sends a notification to a specified Slack channel using a structured block format, including a link to record the expense in the Moze accounting app.

Node Configurations

1. Manual Trigger
Purpose**: Starts the workflow manually for testing or immediate execution.
Configuration**: No setup needed.

2. Gmail Trigger
Purpose**: Automatically polls Gmail for new emails matching specific subject keywords.
Configuration**:
  Filters:
    q: subject:透過 Uber Eats 系統送出的訂單 (You can adjust the keywords to fit your language.)
  Polling Frequency: Every hour at 30 minutes past the hour.
  Credentials: Linked Gmail account.

3. Extract Price, Shop, Date, Time
Purpose**: Extracts key information from the email content using regular expressions.
Extracted Data**:
  price: Order price (e.g., $200).
  shop: Shop name (e.g., "店名").
  date: Order date (e.g., 2024.01.01).
  time: Order time converted to 24-hour format (e.g., 14:30).

4. Slack Notification
Purpose**: Sends a formatted message to a Slack channel with extracted order details.
Message Content**:
  Text:
        Ubereat 訂餐資訊:
    商家: {{ shop }}
    金額: {{ price }}
    日期: {{ date }}
      Moze App Link: Includes a clickable button in the Slack message with a pre-filled Moze app URL scheme:
        moze3://expense?amount={{ price }}&account=信用卡&subcategory=外送&store={{ shop }}&date={{ date }}&time={{ time }}&project=生活開銷
      Channel: Slack channel ID associated with food delivery notifications.

Additional Notes
Customization**: Adjust the email subject filter (subject) to match other types of food delivery platforms or services.
Error Handling**: Ensure regular expressions for data extraction match the email format. Test with sample emails before deployment.
Moze URL Scheme Reference**: Learn more about Moze app URL schemes for customization by visiting the Moze Documentation.

This workflow is ideal for automating expense tracking and centralizing notifications for food delivery orders, streamlining personal or team expense management.

Image:
UberEat Gmail with order information


Slack text with button


Click the button will call moze url scheme

工作流程描述
此工作流程自動化從外送平台獲取郵件，提取關鍵訂單詳細資訊，並將通知發送到指定的 Slack 頻道。此外，Slack 消息中包含一個 Moze 記帳 App URL Scheme 的連結，方便快速記帳。

主要功能
Manual Trigger：允許手動執行工作流程，方便測試。
Gmail Integration：從 Gmail 中提取包含特定關鍵字（例如：「透過 Uber Eats 系統送出的訂單」）的郵件。
資料提取：解析郵件內容，提取以下關鍵資訊：
   訂單金額
   商家名稱
   訂單日期與時間
Slack 通知：將結構化的通知發送到指定的 Slack 頻道，並包含一個連結供用戶快速記帳。

節點設定

1. Manual Trigger
用途**：手動啟動工作流程以進行測試或即時執行。
設定**：無需額外設定。

2. Gmail Trigger
用途**：自動檢查 Gmail 中是否有符合特定主題關鍵字的新郵件。
設定**：
  篩選條件：
    q: subject:透過 Uber Eats 系統送出的訂單
  檢查頻率：每小時的 30 分。
  憑證：已連結的 Gmail 帳號。

3. Extract Price, Shop, Date, Time
用途**：使用正則表達式從郵件內容中提取關鍵資訊。
提取的資料**：
  price：訂單金額（例如：$200）。
  shop：商家名稱（例如：「店名」）。
  date：訂單日期（例如：2024.01.01）。
  time：訂單時間（24 小時制，例如：14:30）。

4. Slack 通知
用途**：將訂單詳細資訊以格式化消息發送到 Slack。
消息內容**：
  文字：
        Ubereat 訂餐資訊:
    商家: {{ shop }}
    金額: {{ price }}
    日期: {{ date }}
      Moze App 連結：Slack 消息中包含一個可點擊按鈕，預填 Moze App URL Scheme：
        moze3://expense?amount={{ price }}&account=信用卡&subcategory=外送&store={{ shop }}&date={{ date }}&time={{ time }}&project=生活開銷
      頻道：與外送通知相關的 Slack 頻道。

補充說明
自訂化**：可調整郵件主題篩選條件（subject），以匹配其他外送平台或服務。
錯誤處理**：確保正則表達式匹配郵件格式。在部署前使用樣本郵件進行測試。
Moze URL Scheme 參考**：了解更多關於 Moze App URL Scheme 的客製化資訊，請參閱 Moze 官方文件。

此工作流程適合自動化費用記帳以及集中管理外送訂單通知，提升個人或團隊的費用管理效率。

## Template JSON

```
{
  "id": "dDInVHNAfSedBUCb",
  "meta": {
    "instanceId": "fddb3e91967f1012c95dd02bf5ad21f279fc44715f47a7a96a33433621caa253"
  },
  "name": "\u5916\u9001\u8a18\u5e33",
  "tags": [],
  "nodes": [
    {
      "id": "09c19ba1-45f2-43af-9985-3508d801c1b7",
      "name": "Loop Over Items",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        440,
        0
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 3
    },
    {
      "id": "18625b1d-f8ff-4e48-8b64-a9d42d24eccc",
      "name": "Click to Test Flow",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        40,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "649933c4-b16b-46de-9038-7d8c0b3d8e88",
      "name": "Get emails from Gmail with certain subject",
      "type": "n8n-nodes-base.gmail",
      "position": [
        220,
        0
      ],
      "webhookId": "99c4deca-17c7-47ae-a38c-50344938e792",
      "parameters": {
        "simple": false,
        "filters": {
          "q": "subject:\u900f\u904e Uber Eats \u7cfb\u7d71\u9001\u51fa\u7684\u8a02\u55ae"
        },
        "options": {},
        "operation": "getAll",
        "returnAll": true
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "34rX9kxKlJadOY6u",
          "name": "Gmail account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "b2118a34-52ad-4464-b7ea-7f3105536fad",
      "name": "Receive certain keyword Gmail Trigger",
      "type": "n8n-nodes-base.gmailTrigger",
      "position": [
        120,
        -180
      ],
      "parameters": {
        "simple": false,
        "filters": {
          "q": "subject:\u900f\u904e Uber Eats \u7cfb\u7d71\u9001\u51fa\u7684\u8a02\u55ae"
        },
        "options": {},
        "pollTimes": {
          "item": [
            {
              "mode": "everyHour",
              "minute": 30
            }
          ]
        }
      },
      "credentials": {
        "gmailOAuth2": {
          "id": "34rX9kxKlJadOY6u",
          "name": "Gmail account"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "00986543-d01a-4b11-bbaa-60c73a1dae02",
      "name": "Extract Price, Shop, Date, TIme",
      "type": "n8n-nodes-base.set",
      "position": [
        620,
        60
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "c24405f8-267f-4933-a178-1b51145d62bf",
              "name": "price",
              "type": "string",
              "value": "={{ $json[\"text\"].match(/\\$(\\d+(\\.\\d{2})?)/)[1] }}"
            },
            {
              "id": "968cf7cd-6e28-4328-a829-3fe2cb327643",
              "name": "shop",
              "type": "string",
              "value": "={{ $json[\"text\"].match(/\u4ee5\u4e0b\u662f\u60a8\u5728([\\u4e00-\\u9fa5a-zA-Z0-9\\s]+)\u8a02\u8cfc/)[1] }}"
            },
            {
              "id": "53642bcb-f3a6-4086-bdc1-2f8d27927462",
              "name": "date",
              "type": "string",
              "value": "={{ $json[\"text\"].match(/Date: (\\d{4}\u5e74\\d{1,2}\u6708\\d{1,2}\u65e5)/)[1].replace(\"\u5e74\", \".\").replace(\"\u6708\", \".\").replace(\"\u65e5\", \"\") }}"
            },
            {
              "id": "cd227132-971b-4970-8b5d-724463efe036",
              "name": "time",
              "type": "string",
              "value": "={{ \n  $json[\"text\"].match(/(\u4e0a\u5348|\u4e0b\u5348) (\\d{1,2}):(\\d{2})/) ? \n  ($json[\"text\"].match(/(\u4e0a\u5348|\u4e0b\u5348) (\\d{1,2}):(\\d{2})/)[1] === '\u4e0b\u5348' && $json[\"text\"].match(/(\u4e0a\u5348|\u4e0b\u5348) (\\d{1,2}):(\\d{2})/)[2] !== '12' \n    ? (parseInt($json[\"text\"].match(/(\u4e0a\u5348|\u4e0b\u5348) (\\d{1,2}):(\\d{2})/)[2]) + 12) + ':' + $json[\"text\"].match(/(\u4e0a\u5348|\u4e0b\u5348) (\\d{1,2}):(\\d{2})/)[3] \n    : $json[\"text\"].match(/(\u4e0a\u5348|\u4e0b\u5348) (\\d{1,2}):(\\d{2})/)[2] + ':' + $json[\"text\"].match(/(\u4e0a\u5348|\u4e0b\u5348) (\\d{1,2}):(\\d{2})/)[3]\n  )\n  : null \n}}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "3d8f97ea-4a0d-4939-898f-8a0ca9415e7d",
      "name": "Send to Slack with Block",
      "type": "n8n-nodes-base.slack",
      "position": [
        800,
        60
      ],
      "webhookId": "0e812732-74d2-4924-8db3-6b9234965937",
      "parameters": {
        "text": "=Ubereat \u8a02\u9910\u8cc7\u8a0a: \n\u5546\u5bb6:  {{ $json.shop }}\n\u91d1\u984d: {{ $json.price }}\n\u65e5\u671f: {{ $json.date }}\n\n\u8a18\u5e33\u7db2\u5740:\nmoze3://expense?amount={{ $json.price }}&account=\u4fe1\u7528\u5361&subcategory=\u5916\u9001&store={{ $json.shop }}&date={{ $json.date }}",
        "select": "channel",
        "blocksUi": "={\n\t\"blocks\": [\n\t\t{\n\t\t\t\"type\": \"section\",\n\t\t\t\"text\": {\n\t\t\t\t\"type\": \"mrkdwn\",\n\t\t\t\t\"text\": \"Ubereat \u8a02\u9910\u8cc7\u8a0a:\\n\\n*\u5546\u5bb6:* {{ $json.shop }}\\n*\u91d1\u984d:* {{ $json.price }}\\n*\u65e5\u671f:* {{ $json.date }}\"\n\t\t\t}\n\t\t},\n\t\t{\n\t\t\t\"type\": \"divider\"\n\t\t},\n\t\t{\n\t\t\t\"type\": \"section\",\n\t\t\t\"text\": {\n\t\t\t\t\"type\": \"mrkdwn\",\n\t\t\t\t\"text\": \"Moze \u8a18\u5e33\u8acb\u9ede\u6211\"\n\t\t\t},\n\t\t\t\"accessory\": {\n\t\t\t\t\"type\": \"button\",\n\t\t\t\t\"text\": {\n\t\t\t\t\t\"type\": \"plain_text\",\n\t\t\t\t\t\"text\": \"\u8a18\u5e33\",\n\t\t\t\t\t\"emoji\": true\n\t\t\t\t},\n\t\t\t\t\"value\": \"click\",\n\t\t\t\t\"url\": \"moze3://expense?amount={{ $json.price }}&account=\u4fe1\u7528\u5361&subcategory=\u5916\u9001&store={{ $json.shop }}&date={{ $json.date }}&&project=\u751f\u6d3b\u958b\u92b7&&time={{ $json.time }}\",\n\t\t\t\t\"action_id\": \"button-action\"\n\t\t\t}\n\t\t}\n\t]\n}",
        "channelId": {
          "__rl": true,
          "mode": "list",
          "value": "C0883CJM1UH",
          "cachedResultName": "\u5916\u9001\u8a18\u5e33\u81ea\u52d5\u5316"
        },
        "messageType": "block",
        "otherOptions": {},
        "authentication": "oAuth2"
      },
      "credentials": {
        "slackOAuth2Api": {
          "id": "sD1J9ZLyEhcglrRa",
          "name": "Slack account"
        }
      },
      "typeVersion": 2.3
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "0840254c-0058-47fe-9b22-7fbb93144788",
  "connections": {
    "Loop Over Items": {
      "main": [
        [],
        [
          {
            "node": "Extract Price, Shop, Date, TIme",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Click to Test Flow": {
      "main": [
        [
          {
            "node": "Get emails from Gmail with certain subject",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send to Slack with Block": {
      "main": [
        [
          {
            "node": "Loop Over Items",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Price, Shop, Date, TIme": {
      "main": [
        [
          {
            "node": "Send to Slack with Block",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Receive certain keyword Gmail Trigger": {
      "main": [
        [
          {
            "node": "Loop Over Items",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get emails from Gmail with certain subject": {
      "main": [
        [
          {
            "node": "Loop Over Items",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
