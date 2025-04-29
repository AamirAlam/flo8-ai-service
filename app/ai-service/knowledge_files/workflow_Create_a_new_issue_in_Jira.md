# Create a new issue in Jira

**[View Template](https://n8n.io/workflows/459-/)**  **Published Date:** 07/09/2020  **Created By:** tanaypant  **Categories:** `Productivity` `Development`  

## Template Description



## Template JSON

```
{
  "id": "87",
  "name": "Create a new issue in Jira",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        350,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Jira",
      "type": "n8n-nodes-base.jira",
      "position": [
        550,
        300
      ],
      "parameters": {
        "project": "",
        "summary": "Firewall on fire",
        "issueType": "10001",
        "additionalFields": {}
      },
      "credentials": {
        "jiraSoftwareCloudApi": ""
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
            "node": "Jira",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
