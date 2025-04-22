# Get new time entries from Toggl

**[View Template](https://n8n.io/workflows/517-/)**  **Published Date:** 07/15/2020  **Created By:** tanaypant  **Categories:**   

## Template Description



## Template JSON

```
{
  "id": "138",
  "name": "Get new time entries from Toggl",
  "nodes": [
    {
      "name": "Toggl",
      "type": "n8n-nodes-base.togglTrigger",
      "position": [
        650,
        250
      ],
      "parameters": {
        "pollTimes": {
          "item": [
            {}
          ]
        }
      },
      "credentials": {
        "togglApi": ""
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {}
}
```
