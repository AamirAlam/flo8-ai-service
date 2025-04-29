# Create, update, and get a document in Google Cloud Firestore

**[View Template](https://n8n.io/workflows/839-/)**  **Published Date:** 12/21/2020  **Created By:** ghagrawal17  **Categories:** `Data & Storage`  

## Template Description



This example workflow allows you to create, update, and get a document in Google Cloud Firestore. 

The workflow uses the Set node to set the data, however, you might receive data from a different source. Add the node that receives the data before the Set node and set the values you want to insert in a document, in the Set node. Also, update the Columns/ attributes fields in the Google Cloud Firestore node.

## Template JSON

```
{
  "id": "179",
  "name": "Create, update, and get a document in Google Cloud Firestore",
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
      "name": "Google Cloud Firestore",
      "type": "n8n-nodes-base.googleFirebaseCloudFirestore",
      "position": [
        650,
        300
      ],
      "parameters": {
        "columns": "id, name",
        "operation": "create",
        "projectId": "docs-f8925",
        "collection": "n8n"
      },
      "credentials": {
        "googleFirebaseCloudFirestoreOAuth2Api": "Cloud Firestore Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "position": [
        450,
        300
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "id",
              "value": 1
            }
          ],
          "string": [
            {
              "name": "name",
              "value": "n8n"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "Set1",
      "type": "n8n-nodes-base.set",
      "position": [
        850,
        300
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "name",
              "value": "nodemation"
            },
            {
              "name": "document_id",
              "value": "={{$node[\"Google Cloud Firestore\"].json[\"_id\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "Google Cloud Firestore1",
      "type": "n8n-nodes-base.googleFirebaseCloudFirestore",
      "position": [
        1050,
        300
      ],
      "parameters": {
        "columns": "name",
        "operation": "upsert",
        "projectId": "={{$node[\"Google Cloud Firestore\"].parameter[\"projectId\"]}}",
        "updateKey": "document_id",
        "collection": "={{$node[\"Google Cloud Firestore\"].parameter[\"collection\"]}}"
      },
      "credentials": {
        "googleFirebaseCloudFirestoreOAuth2Api": "Cloud Firestore Credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Google Cloud Firestore2",
      "type": "n8n-nodes-base.googleFirebaseCloudFirestore",
      "position": [
        1250,
        300
      ],
      "parameters": {
        "projectId": "={{$node[\"Google Cloud Firestore\"].parameter[\"projectId\"]}}",
        "collection": "={{$node[\"Google Cloud Firestore\"].parameter[\"collection\"]}}",
        "documentId": "={{$node[\"Set1\"].json[\"document_id\"]}}"
      },
      "credentials": {
        "googleFirebaseCloudFirestoreOAuth2Api": "Cloud Firestore Credentials"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Set": {
      "main": [
        [
          {
            "node": "Google Cloud Firestore",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set1": {
      "main": [
        [
          {
            "node": "Google Cloud Firestore1",
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
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Cloud Firestore": {
      "main": [
        [
          {
            "node": "Set1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Cloud Firestore1": {
      "main": [
        [
          {
            "node": "Google Cloud Firestore2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
