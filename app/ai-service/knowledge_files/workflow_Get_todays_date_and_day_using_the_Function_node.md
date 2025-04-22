# Get today's date and day using the Function node

**[View Template](https://n8n.io/workflows/524-/)**  **Published Date:** 07/16/2020  **Created By:** tanaypant  **Categories:**   

## Template Description



## Template JSON

```
{
  "id": "140",
  "name": "Get today's date and day using the Function node",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Function",
      "type": "n8n-nodes-base.function",
      "position": [
        450,
        300
      ],
      "parameters": {
        "functionCode": "var date = new Date().toISOString();\nvar day = new Date().getDay();\nconst weekday = [\"Sunday\", \"Monday\", \"Tuesday\", \"Wednesday\", \"Thursday\", \"Friday\", \"Saturday\"];\n\nitems[0].json.date_today = date;\nitems[0].json.day_today = weekday[day];\n\nreturn items;"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Function",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
