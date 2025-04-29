# Create, update and get a task in Microsoft To Do

**[View Template](https://n8n.io/workflows/1114-/)**  **Published Date:** 06/07/2021  **Created By:** ghagrawal17  **Categories:** `Productivity`  

## Template Description

This workflow allows you to create, update and get a task in Microsoft To Do.



Microsoft To Do node: This node will create a task with the importance High in the Tasks list. You can select a different list as well as the importance level.

Microsoft To Do1 node: This node will update the status of the task that we created in the previous node.

Microsoft To Do2 node: This node will get the task that we created earlier.

## Template JSON

```
{
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        200
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Microsoft To Do",
      "type": "n8n-nodes-base.microsoftToDo",
      "position": [
        450,
        200
      ],
      "parameters": {
        "title": "Document Microsoft To Do node",
        "operation": "create",
        "taskListId": "AQMkADAwATNiZmYAZC0zOTkAMy02ZWZjLTAwAi0wMAoALgAAA3i1fHMTrftIhQBzhywL64UBAFB0wRiJW1FJmmlvlAkVFQA-AAACARIAAAA=",
        "additionalFields": {
          "importance": "high"
        }
      },
      "credentials": {
        "microsoftToDoOAuth2Api": "Microsoft OAuth Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Microsoft To Do1",
      "type": "n8n-nodes-base.microsoftToDo",
      "position": [
        650,
        200
      ],
      "parameters": {
        "taskId": "={{$json[\"id\"]}}",
        "operation": "update",
        "taskListId": "={{$node[\"Microsoft To Do\"].parameter[\"taskListId\"]}}",
        "updateFields": {
          "status": "inProgress"
        }
      },
      "credentials": {
        "microsoftToDoOAuth2Api": "Microsoft OAuth Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Microsoft To Do2",
      "type": "n8n-nodes-base.microsoftToDo",
      "position": [
        850,
        200
      ],
      "parameters": {
        "taskId": "={{$json[\"id\"]}}",
        "taskListId": "={{$node[\"Microsoft To Do\"].parameter[\"taskListId\"]}}"
      },
      "credentials": {
        "microsoftToDoOAuth2Api": "Microsoft OAuth Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Microsoft To Do": {
      "main": [
        [
          {
            "node": "Microsoft To Do1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Microsoft To Do1": {
      "main": [
        [
          {
            "node": "Microsoft To Do2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Microsoft To Do",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
