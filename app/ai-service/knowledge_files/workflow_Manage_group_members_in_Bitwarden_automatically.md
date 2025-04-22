# Manage group members in Bitwarden automatically

**[View Template](https://n8n.io/workflows/1001-/)**  **Published Date:** 03/25/2021  **Created By:** ghagrawal17  **Categories:** `Data & Storage`  

## Template Description

This workflow allows you to create a group, add members to the group, and get the members of the group.



Bitwarden node: This node will create a new group called documentation in Bitwarden.

Bitwarden1 node: This node will get all the members from Bitwarden.

Bitwarden2 node: This node will update all the members in the group that we created earlier.

Bitwarden3 node: This node will get all the members in the group that we created earlier.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Bitwarden",
      "type": "n8n-nodes-base.bitwarden",
      "position": [
        470,
        320
      ],
      "parameters": {
        "name": "documentation",
        "resource": "group",
        "operation": "create",
        "additionalFields": {}
      },
      "credentials": {
        "bitwardenApi": "Bitwarden API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Bitwarden1",
      "type": "n8n-nodes-base.bitwarden",
      "position": [
        670,
        320
      ],
      "parameters": {
        "resource": "member",
        "operation": "getAll",
        "returnAll": true
      },
      "credentials": {
        "bitwardenApi": "Bitwarden API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Bitwarden2",
      "type": "n8n-nodes-base.bitwarden",
      "position": [
        870,
        320
      ],
      "parameters": {
        "groupId": "={{$node[\"Bitwarden\"].json[\"id\"]}}",
        "resource": "group",
        "memberIds": "={{$json[\"id\"]}}",
        "operation": "updateMembers"
      },
      "credentials": {
        "bitwardenApi": "Bitwarden API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Bitwarden3",
      "type": "n8n-nodes-base.bitwarden",
      "position": [
        1070,
        320
      ],
      "parameters": {
        "groupId": "={{$node[\"Bitwarden\"].json[\"id\"]}}",
        "resource": "group",
        "operation": "getMembers"
      },
      "credentials": {
        "bitwardenApi": "Bitwarden API Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Bitwarden": {
      "main": [
        [
          {
            "node": "Bitwarden1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Bitwarden1": {
      "main": [
        [
          {
            "node": "Bitwarden2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Bitwarden2": {
      "main": [
        [
          {
            "node": "Bitwarden3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
