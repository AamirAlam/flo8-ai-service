# TW-Request-Agri Data Open Platform-Daily Market Sheep Pricing

**[View Template](https://n8n.io/workflows/2687-/)**  **Published Date:** 01/01/2025  **Created By:** darrell_tw  **Categories:** `Data & Storage` `Productivity` `Development` `Core Nodes`  

## Template Description

This workflow automates the process of fetching agricultural transaction data from the Taiwan Agricultural Products Open Data Platform and storing it in a Google Sheets document for further analysis.

Key Features
Manual Trigger: Allows manual execution of the workflow to control when data is fetched.
HTTP Request: Sends a request to the Open Data Platform's API to retrieve detailed transaction data, including:
   Pricing (Upper, Middle, Lower, Average)
   Transaction quantities
   Crop and market details
Split Out Node: Processes each record individually, ensuring accurate handling of every data entry.
Google Sheets Integration: Appends the data into a structured Google Sheets document for easy access and analysis.

Node Configurations

1. Manual Trigger
Purpose**: Start the workflow manually.
Configuration**: No setup needed.

2. HTTP Request
Purpose**: Fetch agricultural data.
Configuration**:
  URL: https://data.moa.gov.tw/api/v1/SheepQuotation
  Query Parameters:
    Start_time: 2024/12/01
    End_time: 2024/12/31
    MarketName: 台北二
    api_key: &lt;your_api_key&gt;
  Headers:
    accept: application/json

3. Split Out
Purpose**: Split the API response data array into individual items.
Configuration**:
  Field to Split Out: Data

4. Google Sheets
Purpose**: Append the data to Google Sheets.
Configuration**:
  Operation: Append
  Document ID: &lt;your_document_id&gt;
  Sheet Name: Sheet1
  Mapped Fields:
    TransDate, TcType, CropCode, CropName, MarketCode, MarketName
    Upper_Price, Middle_Price, Lower_Price, Avg_Price, Trans_Quantity


此 Workflow 從 台灣農業產品開放資料平臺 獲取農產品交易數據，並將其儲存到 Google Sheets 文件 中進行進一步分析。

主要功能
Manual Trigger：允許手動執行工作流程，以控制數據獲取的時間。
HTTP Request：向開放資料平臺的 API 發送請求，獲取詳細的交易數據，包括：
   價格 (Upper, Middle, Lower, Average)
   交易數量
   作物和市場詳細資料
Split Out Node：逐筆處理每一筆記錄，確保數據準確無誤。
Google Sheets Integration：將數據追加到結構化的 Google Sheets 文件中，方便存取和分析。

節點設定

1. Manual Trigger
用途**：手動啟動工作流程。
設定**：無需額外設定。

2. HTTP Request
用途**：抓取農產品數據。
設定**：
  URL: https://data.moa.gov.tw/api/v1/SheepQuotation
  查詢參數 (Query Parameters)：
    Start_time: 2024/12/01
    End_time: 2024/12/31
    MarketName: 台北二
    api_key: &lt;your_api_key&gt;
  標頭 (Headers)：
    accept: application/json

3. Split Out
用途**：將 API 回應的數據陣列分解為個別項目。
設定**：
  Field to Split Out: Data

4. Google Sheets
用途**：將數據追加至 Google Sheets。
設定**：
  Operation：Append
  Document ID：&lt;your_document_id&gt;
  Sheet Name：Sheet1
  映射欄位 (Mapped Fields)：
    TransDate, TcType, CropCode, CropName, MarketCode, MarketName
    Upper_Price, Middle_Price, Lower_Price, Avg_Price, Trans_Quantity

請多利用 Curl Import 功能
例如
curl -X GET "https://data.moa.gov.tw/api/v1/AgriProductsTransType/?Start_time=114.01.01&End_time=114.01.01&MarketName=%E5%8F%B0%E5%8C%97%E4%BA%8C" -H "accept: application/json"

農業資料開放平台 文件


## Template JSON

```
{
  "id": "ziJG3tgG91Gkbina",
  "meta": {
    "instanceId": "fddb3e91967f1012c95dd02bf5ad21f279fc44715f47a7a96a33433621caa253"
  },
  "name": "n8n-\u8fb2\u7522\u54c1",
  "tags": [
    {
      "id": "YaVjRtdJOQvaEnU3",
      "name": "testing",
      "createdAt": "2024-12-29T07:47:44.069Z",
      "updatedAt": "2024-12-29T07:47:44.069Z"
    }
  ],
  "nodes": [
    {
      "id": "07d7241d-480b-4d53-96ba-485d1dc469f6",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        0,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "02dfaea7-be8c-49fd-a869-39cccf6e6dde",
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        220,
        0
      ],
      "parameters": {
        "url": "https://data.moa.gov.tw/api/v1/SheepQuotation",
        "options": {},
        "sendQuery": true,
        "sendHeaders": true,
        "queryParameters": {
          "parameters": [
            {
              "name": "Start_time",
              "value": "2024/12/01"
            },
            {
              "name": "End_time",
              "value": "2024/12/31"
            },
            {
              "name": "MarketName",
              "value": "\u53f0\u5317\u4e8c"
            },
            {
              "name": "api_key",
              "value": "3AFID4BGE9PDQ2WTFDO1X61H4RNQLE"
            }
          ]
        },
        "headerParameters": {
          "parameters": [
            {
              "name": "accept",
              "value": "application/json"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "69a1d5c6-a59f-4b4b-9e51-d75f319a75c6",
      "name": "Split Out",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        440,
        0
      ],
      "parameters": {
        "options": {},
        "fieldToSplitOut": "Data"
      },
      "typeVersion": 1
    },
    {
      "id": "082828e0-4cc6-465c-bfe4-561f8e4e3c50",
      "name": "Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        660,
        0
      ],
      "parameters": {
        "columns": {
          "value": {},
          "schema": [
            {
              "id": "TransDate",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "TransDate",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "TcType",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "TcType",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CropCode",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "CropCode",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "CropName",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "CropName",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MarketCode",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "MarketCode",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "MarketName",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "MarketName",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Upper_Price",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Upper_Price",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Middle_Price",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Middle_Price",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Lower_Price",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Lower_Price",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Avg_Price",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Avg_Price",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Trans_Quantity",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Trans_Quantity",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "autoMapInputData",
          "matchingColumns": []
        },
        "options": {},
        "operation": "append",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/17EJTOetBsfoGkzADCUHPoXaQW7FLQziYmQxKNJNnDIU/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "17EJTOetBsfoGkzADCUHPoXaQW7FLQziYmQxKNJNnDIU",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/17EJTOetBsfoGkzADCUHPoXaQW7FLQziYmQxKNJNnDIU/edit?usp=drivesdk",
          "cachedResultName": "n8n\u722c\u87f2-\u8fb2\u7522\u54c1"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "atsKA0m2aQXeL6i6",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "b7991044-da7e-425f-a2ea-692e3d8d642b",
  "connections": {
    "Split Out": {
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
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Split Out",
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
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
