# Convert Parquet, Feather, ORC & Avro Files with ParquetReader

**[View Template](https://n8n.io/workflows/3365-/)**  **Published Date:** 03/30/2025  **Created By:** ParquetReader  **Categories:** `Development` `Core Nodes`  

## Template Description

📄 Convert Parquet, Feather, ORC & Avro Files with ParquetReader

This workflow allows you to upload and inspect Parquet, Feather, ORC, or Avro files via the ParquetReader API. It instantly returns a structured JSON preview of your data — including rows, schema, and metadata — without needing to write any custom code.

✅ Perfect For
Validating schema and structure before syncing or transformation
Previewing raw columnar files on the fly
Automating QA, ETL, or CI/CD workflows
Converting Parquet, Avro, Feather, or ORC to JSON

⚙️ Use Cases
Catch schema mismatches before pipeline runs
Automate column audits in incoming data files
Enrich metadata catalogs with real-time schema detection
Integrate file validation into automated workflows

🚀 How to Use This Workflow

📥 Trigger via File Upload

You can trigger this flow by sending a POST request with a file using curl, Postman, or from another n8n flow.

🔧 Example (via curl):
curl -X POST http://localhost:5678/webhook-test/convert \
-F "file=@converted.parquet"
&gt; Replace converted.parquet with your local file path. You can also send Avro, ORC or Feather files.

🔁 Reuse from Other Flows
You can reuse this flow by calling the webhook from another n8n workflow using an HTTP Request node.  
Make sure to send the file as form-data with the field name file.

🔍 What This Flow Does:
Receives the uploaded file via webhook (file)
Sends it to https://api.parquetreader.com/parquet as multipart/form-data (field name: file)
Receives parsed data (rows), schema, and metadata in JSON format

🧪 Example JSON Response from this flow
{
  "data": [
    {
      "full_name": "Pamela Cabrera",
      "email": "bobbyharrison@example.net",
      "age": "24",
      "active": "True",
      "latitude": "-36.1577385",
      "longitude": "63.014954",
      "company": "Carter, Shaw and Parks",
      "country": "Honduras"
    }
  ],
  "meta_data": {
    "created_by": "pyarrow",
    "num_columns": 21,
    "num_rows": 10,
    "serialized_size": 7598,
    "format_version": "0.12"
  },
  "schema": [
    { "column_name": "full_name", "column_type": "string" },
    { "column_name": "email", "column_type": "string" },
    { "column_name": "age", "column_type": "int64" },
    { "column_name": "active", "column_type": "bool" },
    { "column_name": "latitude", "column_type": "double" },
    { "column_name": "longitude", "column_type": "double" },
    { "column_name": "company", "column_type": "string" },
    { "column_name": "country", "column_type": "string" }
  ]
}

🔐 API Info
Authentication: None required
Supported formats: .parquet, .avro, .orc, .feather
Free usage: No signup needed; API is currently open to the public
Limits: Usage and file size limits may apply in the future (TBD)

## Template JSON

```
{
  "id": "VU0kmvnWzctSFm2M",
  "meta": {
    "instanceId": "534a4ec070e550167af0cc407c76e029ac0ae69bef901c2f9ef440d79bfa5792"
  },
  "name": "Convert Parquet, Avro, ORC & Feather via ParquetReader to JSON",
  "tags": [
    {
      "id": "1PTaY70kFjD8F12p",
      "name": "Convert",
      "createdAt": "2025-03-30T09:38:16.466Z",
      "updatedAt": "2025-03-30T09:38:16.466Z"
    },
    {
      "id": "98v0QSKrvfH5dl34",
      "name": "Avro",
      "createdAt": "2025-03-30T09:38:06.656Z",
      "updatedAt": "2025-03-30T09:38:06.656Z"
    },
    {
      "id": "Q0sqo52DKATPDab2",
      "name": "ORC",
      "createdAt": "2025-03-30T09:38:09.923Z",
      "updatedAt": "2025-03-30T09:38:09.923Z"
    },
    {
      "id": "b1s8WFj3TfMpoOQu",
      "name": "Feather",
      "createdAt": "2025-03-30T09:38:12.227Z",
      "updatedAt": "2025-03-30T09:38:12.227Z"
    },
    {
      "id": "fFnESRcynarFqlLf",
      "name": "Parquet",
      "createdAt": "2025-03-30T09:38:04.286Z",
      "updatedAt": "2025-03-30T09:38:04.286Z"
    }
  ],
  "nodes": [
    {
      "id": "651a10dc-1c91-4957-bcdd-3e55d7328f04",
      "name": "Send to Parquet API",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1100,
        440
      ],
      "parameters": {
        "url": "https://api.parquetreader.com/parquet?source=n8n",
        "options": {
          "bodyContentType": "multipart-form-data"
        },
        "requestMethod": "POST",
        "jsonParameters": true,
        "sendBinaryData": true,
        "binaryPropertyName": "=file0"
      },
      "typeVersion": 1
    },
    {
      "id": "42a7e623-ca11-4d38-94bb-cfb48d021a5c",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "notes": "Example trigger flow:\n\ncurl -X POST http://localhost:5678/webhook-test/convert \\\n  -F \"file=@converted.parquet\"",
      "position": [
        900,
        440
      ],
      "webhookId": "0b1223c9-c117-45f9-9931-909f2db28955",
      "parameters": {
        "path": "convert",
        "options": {
          "binaryPropertyName": "file"
        },
        "httpMethod": "POST",
        "responseData": "allEntries",
        "responseMode": "lastNode"
      },
      "notesInFlow": false,
      "typeVersion": 2
    },
    {
      "id": "9b87f027-7ef2-40a7-88d7-a0ae9ef73375",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        0,
        0
      ],
      "parameters": {
        "width": 840,
        "height": 580,
        "content": "### \u2705 **How to Use This Flow**\n\n#### \ud83d\udce5 Trigger via File Upload\n\nYou can trigger this flow by sending a `POST` request with a file using **curl**, **Postman**, or **from another n8n flow**.\n\n#### \ud83d\udd27 Example (via `curl`):\n```bash\ncurl -X POST http://localhost:5678/webhook-test/convert \\\n-F \"file=@converted.parquet\"\n```\n> Replace `converted.parquet` with your local file path. You can also send Avro, ORC or Feather files.\n\n#### \ud83d\udd01 Reuse from Other Flows\nYou can **reuse this flow** by calling the webhook from another n8n workflow using an **HTTP Request** node.  \nMake sure to send the file as **form-data** with the field name `file`.\n\n#### \ud83d\udd0d What This Flow Does:\n- Receives the uploaded file via webhook (`file`)\n- Sends it to `https://api.parquetreader.com/parquet` as `multipart/form-data` (field name: `file`)\n- Receives parsed data, schema, and metadata\n"
      },
      "typeVersion": 1
    },
    {
      "id": "06d3e569-8724-48f2-951f-a1af5e0f9362",
      "name": "Parse API Response",
      "type": "n8n-nodes-base.code",
      "position": [
        1280,
        440
      ],
      "parameters": {
        "jsCode": "const item = items[0];\n\n// Convert `data` (stringified JSON array) \u2192 actual array\nif (typeof item.json.data === 'string') {\n  item.json.data = JSON.parse(item.json.data);\n}\n\n// Convert `meta_data` (stringified JSON object) \u2192 actual object\nif (typeof item.json.meta_data === 'string') {\n  item.json.meta_data = JSON.parse(item.json.meta_data);\n}\n\nreturn [item];\n"
      },
      "typeVersion": 2
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "c10e1897-094e-42c6-bde9-1724972ada3e",
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Send to Parquet API",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send to Parquet API": {
      "main": [
        [
          {
            "node": "Parse API Response",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
