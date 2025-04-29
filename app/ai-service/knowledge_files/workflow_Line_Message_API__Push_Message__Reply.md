# Line Message API : Push Message & Reply

**[View Template](https://n8n.io/workflows/2733-/)**  **Published Date:** 01/15/2025  **Created By:** darrell_tw  **Categories:** `Development` `Core Nodes`  

## Template Description

Workflow Description
This workflow demonstrates how to use the LINE Messaging API to handle two scenarios:
Replying to a user's message using a reply token.
Sending a push message to a specific LINE user using their user ID.

Key Features
Webhook Integration: Receives and processes incoming messages from LINE using a webhook.
Conditional Logic: Checks if the received event type is a message and handles it accordingly.
Reply Message: Automatically responds to the user's message using the LINE reply token.
Push Message: Sends a test message to a specific LINE user using their unique user ID.

Pre-Configuration
To simplify the setup process, create a Header Auth credential in n8n:
Name**: Authorization
Value**: Bearer {line token}  
This will authenticate all API requests to the LINE Messaging API.
Node Configurations

1.1. Webhook from LINE Message
Purpose**: Captures incoming events from the LINE Messaging API.
Configuration**:
  HTTP Method: POST
  Path: {n8n-webhook-page}

1.2. If Condition
Purpose**: Checks if the received event type is message.
Configuration**:
  Condition:
    {{ $json.body.events[0].type }} equals "message"

1.3. Line: Reply with Token
Purpose**: Replies to the user's message using the LINE reply token.
Configuration**:
  Method: POST
  URL: https://api.line.me/v2/bot/message/reply
  JSON Body:
        {
      "replyToken": "{{ $('Webhook from Line Message').item.json.body.events[0].replyToken }}",
      "messages": [
        {
          "type": "text",
          "text": "收到您的訊息 : {{ $('Webhook from Line Message').item.json.body.events[0].message.text }}"
        }
      ]
    }
2.1. Manual Trigger: Test Workflow
Purpose**: Triggers the workflow for testing the push message functionality.
Configuration**: No additional setup required.

2.2. Edit Fields
Purpose**: Prepares the unique LINE user ID for the push message.
Configuration**:
  Field:
    line_uid: Uxxxxxxxxxxxx

2.3. Line: Push Message
Purpose**: Sends a test message to a specific LINE user.
Configuration**:
  Method: POST
  URL: https://api.line.me/v2/bot/message/push
  JSON Body:
        {
      "to": "{{ $json.line_uid }}",
      "messages": [
        {
          "type": "text",
          "text": "推播測試"
        }
      ]
    }
工作流程描述
此工作流程展示如何使用 LINE Messaging API 處理兩種情境：
使用 reply token 回應使用者的訊息。
使用使用者的 user ID 發送 推播訊息。

主要功能
Webhook 整合：透過 Webhook 接收並處理來自 LINE 的訊息。
條件邏輯：檢查接收到的事件類型是否為訊息並進行處理。
回應訊息：使用 LINE 的 reply token 自動回覆使用者的訊息。
推播訊息：使用 LINE User ID 向指定用戶發送測試訊息。

預先設定
為簡化設定流程，請在 n8n 中建立 Header Auth 憑證：
名稱**：Authorization
值**：Bearer {line token}  
此設定將用於認證所有 LINE Messaging API 的請求。
節點設定

1.1. Webhook from LINE Message
用途**：接收來自 LINE Messaging API 的事件。
設定**：
  HTTP 方法：POST
  路徑：{n8n-webhook-page}

1.2. If 條件判斷
用途**：檢查接收到的事件類型是否為 message。
設定**：
  條件：
    {{ $json.body.events[0].type }} 等於 "message"

1.3. Line: Reply with Token
用途**：使用 LINE reply token 回應使用者訊息。
設定**：
  方法：POST
  URL：https://api.line.me/v2/bot/message/reply
  JSON 主體：
        {
      "replyToken": "{{ $('Webhook from Line Message').item.json.body.events[0].replyToken }}",
      "messages": [
        {
          "type": "text",
          "text": "收到您的訊息 : {{ $('Webhook from Line Message').item.json.body.events[0].message.text }}"
        }
      ]
    }
2.1. 手動觸發：測試工作流程
用途**：測試推播訊息功能。
設定**：無需額外設定。

2.2. Edit Fields
用途**：準備推播訊息所需的 LINE 使用者 ID。
設定**：
  欄位：
    line_uid：Uxxxxxxxxxxxx

2.3. Line: 推播訊息
用途**：向特定 LINE 使用者發送測試訊息。
設定**：
  方法：POST
  URL：https://api.line.me/v2/bot/message/push
  JSON 主體：
        {
      "to": "{{ $json.line_uid }}",
      "messages": [
        {
          "type": "text",
          "text": "推播測試"
        }
      ]
    }
    
完成示意圖 (Storyboard Example):



## Template JSON

```
{
  "id": "a5tCsfMzJPd8WDUj",
  "meta": {
    "instanceId": "fddb3e91967f1012c95dd02bf5ad21f279fc44715f47a7a96a33433621caa253",
    "templateCredsSetupCompleted": true
  },
  "name": "line message api demo",
  "tags": [],
  "nodes": [
    {
      "id": "2bc1cc31-136c-46a4-a789-476e33c76f3d",
      "name": "Line : Reply with token",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -540,
        -460
      ],
      "parameters": {
        "url": "https://api.line.me/v2/bot/message/reply",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"replyToken\": \"{{ $('Webhook from Line Message').item.json.body.events[0].replyToken }}\",\n  \"messages\": [\n    {\n      \"type\": \"text\",\n      \"text\": \"\u6536\u5230\u60a8\u7684\u8a0a\u606f : {{ $('Webhook from Line Message').item.json.body.events[0].message.text }}\"\n    }\n  ]\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "xB2Ip7YKSIDq7BoI",
          "name": "Line n8n demo auth"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "a1d9c986-4712-4d40-955d-40d1b19d74db",
      "name": "Webhook from Line Message",
      "type": "n8n-nodes-base.webhook",
      "position": [
        -1020,
        -440
      ],
      "webhookId": "638c118e-1c98-4491-b6ff-14e2e75380b6",
      "parameters": {
        "path": "638c118e-1c98-4491-b6ff-14e2e75380b6",
        "options": {},
        "httpMethod": "POST"
      },
      "typeVersion": 2
    },
    {
      "id": "a0c94852-290f-48b9-8e11-b498ada90c8f",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1100,
        -620
      ],
      "parameters": {
        "width": 720,
        "height": 340,
        "content": "## Line Message API Reply\n\nReceived Message from user and reply with same text by using reply token  \n\nThere are many event types. So we need to determine if the type is message."
      },
      "typeVersion": 1
    },
    {
      "id": "278aff13-c081-47f0-a1f6-67920642e991",
      "name": "If",
      "type": "n8n-nodes-base.if",
      "position": [
        -800,
        -440
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "b63773bb-f010-4018-8142-240c9aaa4570",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $json.body.events[0].type }}",
              "rightValue": "message"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "cff2f1d3-b7a4-4940-a1d1-1e5a80d6ea28",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -1100,
        -200
      ],
      "parameters": {
        "width": 720,
        "height": 340,
        "content": "## Line Message API Send Message\n\nYou need to get the Line UID first.\nEvery user is differnt.\n\nIf you have the Line UID. Then you can push the message to the User."
      },
      "typeVersion": 1
    },
    {
      "id": "9348fc83-0aeb-4591-85b6-48f556512478",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -1020,
        -20
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "74db3e1b-9a22-4033-bf04-a8ff485a5d3b",
      "name": "Edit Fields",
      "type": "n8n-nodes-base.set",
      "position": [
        -800,
        -20
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "6278f340-6287-4e89-b774-f6c584954d5b",
              "name": "line_uid",
              "type": "string",
              "value": "Uxxxxxxxxxxxx"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "c593bd58-8f6a-4689-bb12-e71256ccf6e6",
      "name": "Line : Push Message",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -560,
        -20
      ],
      "parameters": {
        "url": "https://api.line.me/v2/bot/message/push",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n  \"to\": \"{{ $json.line_uid }}\",\n  \"messages\": [\n    {\n      \"type\": \"text\",\n      \"text\": \"\u63a8\u64ad\u6e2c\u8a66\"\n    }\n  ]\n}",
        "sendBody": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "xB2Ip7YKSIDq7BoI",
          "name": "Line n8n demo auth"
        }
      },
      "typeVersion": 4.2
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "240dc848-8803-4776-b01d-5f10c765f72b",
  "connections": {
    "If": {
      "main": [
        [
          {
            "node": "Line : Reply with token",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Edit Fields": {
      "main": [
        [
          {
            "node": "Line : Push Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Webhook from Line Message": {
      "main": [
        [
          {
            "node": "If",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When clicking \u2018Test workflow\u2019": {
      "main": [
        [
          {
            "node": "Edit Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
