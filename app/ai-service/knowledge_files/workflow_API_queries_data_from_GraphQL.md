# API queries data from GraphQL

**[View Template](https://n8n.io/workflows/216-/)**  **Published Date:** 12/17/2019  **Created By:** Jan Oberhauser  **Categories:** `Data & Storage` `Development`  

## Template Description



Simpe API which queries the received country code via GraphQL and returns it.

Example URL: https://n8n.exampl.ecom/webhook/1/webhook/webhook?code=DE

Receives country code from an incoming HTTP Request
Reads data via GraphQL
Converts the data to JSON
Constructs return string




## Template JSON

```
{
  "nodes": [
    {
      "name": "GraphQL",
      "type": "n8n-nodes-base.graphql",
      "position": [
        800,
        300
      ],
      "parameters": {
        "query": "=query {\n  country(code: \"{{$node[\"Webhook\"].data[\"query\"][\"code\"].toUpperCase()}}\") {\n    name\n    phone\n    emoji\n  } \n}",
        "endpoint": "https://countries.trevorblades.com/",
        "requestMethod": "GET",
        "responseFormat": "string"
      },
      "typeVersion": 1
    },
    {
      "name": "Function",
      "type": "n8n-nodes-base.function",
      "position": [
        1000,
        300
      ],
      "parameters": {
        "functionCode": "items[0].json = JSON.parse(items[0].json.data).data.country;\nreturn items;"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        1200,
        300
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "data",
              "value": "=The country code of {{$node[\"Function\"].data[\"name\"]}} {{$node[\"Function\"].data[\"emoji\"]}} is {{$node[\"Function\"].data[\"phone\"]}}"
            }
          ],
          "boolean": []
        },
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        600,
        300
      ],
      "parameters": {
        "path": "webhook",
        "options": {},
        "responseMode": "lastNode"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "GraphQL": {
      "main": [
        [
          {
            "node": "Function",
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
            "node": "GraphQL",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Function": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
