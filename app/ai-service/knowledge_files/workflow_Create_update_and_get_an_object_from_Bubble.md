# Create, update, and get an object from Bubble

**[View Template](https://n8n.io/workflows/1041-/)**  **Published Date:** 04/15/2021  **Created By:** ghagrawal17  **Categories:** `Development`  

## Template Description

This workflow allows you to create, update, and get an object from Bubble.



Bubble node: This node will create a new object of the type Doc in Bubble. If you want to create an object with a different type, use that type instead.

Bubble1 node: This node will update the object that we created using the previous node.

Bubble2 node: This node will retrieve the information of the object that we created earlier.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Bubble",
      "type": "n8n-nodes-base.bubble",
      "position": [
        450,
        280
      ],
      "parameters": {
        "typeName": "Doc",
        "operation": "create",
        "properties": {
          "property": [
            {
              "key": "Name",
              "value": "Bubble"
            }
          ]
        }
      },
      "credentials": {
        "bubbleApi": "Bubble API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Bubble1",
      "type": "n8n-nodes-base.bubble",
      "position": [
        650,
        280
      ],
      "parameters": {
        "objectId": "={{$json[\"id\"]}}",
        "typeName": "={{$node[\"Bubble\"].parameter[\"typeName\"]}}",
        "operation": "update",
        "properties": {
          "property": [
            {
              "key": "Name",
              "value": "Bubble node"
            }
          ]
        }
      },
      "credentials": {
        "bubbleApi": "Bubble API Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Bubble2",
      "type": "n8n-nodes-base.bubble",
      "position": [
        850,
        280
      ],
      "parameters": {
        "objectId": "={{$node[\"Bubble\"].json[\"id\"]}}",
        "typeName": "={{$node[\"Bubble\"].parameter[\"typeName\"]}}"
      },
      "credentials": {
        "bubbleApi": "Bubble API Credentials"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "Bubble": {
      "main": [
        [
          {
            "node": "Bubble1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Bubble1": {
      "main": [
        [
          {
            "node": "Bubble2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
