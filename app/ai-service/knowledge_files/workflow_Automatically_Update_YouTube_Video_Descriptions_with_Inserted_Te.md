# Automatically Update YouTube Video Descriptions with Inserted Text

**[View Template](https://n8n.io/workflows/3080-/)**  **Published Date:** 03/04/2025  **Created By:** Akram Kadri  **Categories:** `Marketing` `Development` `Core Nodes`  

## Template Description

Who is this for?

This workflow is designed for YouTubers who want to update their video descriptions in bulk without manually editing each one. It's especially useful for creators who include a standard set of links in their descriptions and need to insert a new link between existing ones across multiple videos.
What problem does this workflow solve?

Manually updating video descriptions for multiple videos can be tedious and time-consuming. If you have a section in your video descriptions that contains important links, adding a new one in a specific position (e.g., between two existing links) can be a challenge. This workflow automates that process, allowing you to insert a specific string between two predefined rows in all of your video descriptions at once.
What this workflow does

Fetches all videos from your YouTube channel.
Iterates through each video to retrieve its existing description.
Identifies two predefined rows in the description.
Inserts a new row between the two specified rows.
Updates the video description with the modified text.

Setup

Connect your YouTube account to n8n and grant necessary permissions.
Define your variables in the "Set String to Insert" node:
   rowBefore: The existing row after which the new row will be inserted.
   rowToInsert: The new text or link to insert.
   rowAfter: The existing row before which the new row will be inserted.
Run the workflow using the manual trigger.
Review the updated descriptions to ensure accuracy.

How to customize this workflow to your needs

Change the insertion criteria** by modifying the rowBefore and rowAfter values.
Insert multiple rows** by adjusting the JavaScript code in the Code node.
Extend the workflow** by adding conditions (e.g., only updating descriptions of videos with certain tags).
Filter specific** videos instead of updating all by modifying the "Get All Videos" node.

This workflow ensures that all your YouTube descriptions stay updated and consistent with minimal effort.

## Template JSON

```
{
  "name": "Automatically Update YouTube Video Descriptions with Inserted Text",
  "tags": [],
  "nodes": [
    {
      "id": "19cafddc-6199-4418-8213-9743c34c9176",
      "name": "Get All Videos",
      "type": "n8n-nodes-base.youTube",
      "position": [
        480,
        380
      ],
      "parameters": {
        "limit": 3,
        "filters": {},
        "options": {
          "order": "date"
        },
        "resource": "video"
      },
      "typeVersion": 1
    },
    {
      "id": "63a6a8e6-994f-46ab-a731-609549fec99f",
      "name": "Update Video Description",
      "type": "n8n-nodes-base.youTube",
      "position": [
        1320,
        460
      ],
      "parameters": {
        "title": "={{ $('Get Specific Video').item.json.snippet.title }}",
        "videoId": "={{ $('Get Specific Video').item.json.id}}",
        "resource": "video",
        "operation": "update",
        "categoryId": "={{ $('Get Specific Video').item.json.snippet.categoryId }}",
        "regionCode": "US",
        "updateFields": {
          "tags": "={{ $('Get Specific Video').item.json.snippet.tags.join() }}",
          "description": "={{ $json.updatedDescription }}"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "ce147272-f6c3-4cfb-954b-9a77c63a6232",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        120,
        380
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "9ba206b2-1161-41a3-8581-d60dae665096",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        100,
        120
      ],
      "parameters": {
        "color": 5,
        "width": 580,
        "height": 180,
        "content": "## Insert Text into YouTube Video Descriptions\n**Automatically insert a row of text between two specified rows** in all your YouTube video descriptions. \n\nThis workflow is ideal for YouTubers who need to update multiple video descriptions at once. Easily add a new link or text between existing lines, ensuring consistency across all your video descriptions without manual edits."
      },
      "typeVersion": 1
    },
    {
      "id": "e05f5b9c-c160-45d7-b67a-62d68acc0829",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        100,
        560
      ],
      "parameters": {
        "color": 4,
        "width": 340,
        "height": 260,
        "content": "## Configure text string to insert \ud83d\udc46 \nDefine the text string (row) that will be added to your YouTube video descriptions.\n\n### Variables\n- **rowBefore** \u2192 The new row will be inserted *after* this line.\n- **rowToInsert** -\u2192 The text or link you want to add.\n- **rowAfter**\u2192 The new row will be inserted *before* this line.\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "51a3fd15-8767-4cc0-98a8-fe98ec90db70",
      "name": "Set String to Insert",
      "type": "n8n-nodes-base.set",
      "position": [
        300,
        380
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "a05b56b1-6f18-4359-aa4b-127399877301",
              "name": "rowBefore",
              "type": "string",
              "value": "=https://firstlink.com"
            },
            {
              "id": "95ac4a95-cdf4-4d7a-b9a3-78d54c879115",
              "name": "rowToInsert",
              "type": "string",
              "value": "https://mynewlinktoinsert.com"
            },
            {
              "id": "ded86a1f-f0a5-42b8-9176-9be4038f6290",
              "name": "rowAfter",
              "type": "string",
              "value": "https://secondlink.com"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "590b8bb3-6eb4-4bb8-af4c-c2d95221f045",
      "name": "Loop Over Videos",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        700,
        380
      ],
      "parameters": {
        "options": {
          "reset": false
        }
      },
      "typeVersion": 3
    },
    {
      "id": "a80ac941-0a99-4eab-8a6c-effef1e136fa",
      "name": "Get Specific Video",
      "type": "n8n-nodes-base.youTube",
      "position": [
        900,
        460
      ],
      "parameters": {
        "options": {},
        "videoId": "={{ $json.id.videoId }}",
        "resource": "video",
        "operation": "get"
      },
      "typeVersion": 1
    },
    {
      "id": "2c4519e2-1af9-42d7-818c-8165365587fb",
      "name": "Create New Video Description with Row Inserted",
      "type": "n8n-nodes-base.code",
      "position": [
        1100,
        460
      ],
      "parameters": {
        "jsCode": "// Access the input data (YouTube description)\nconst description = $('Get Specific Video').first().json.snippet.description;\n//console.log(inputData)\n\nconst variables = $('Set String to Insert').first().json\n// Define the rows to search for and the row to insert\nconst rowBefore = variables.rowBefore;\nconst rowAfter = variables.rowAfter;\nconst rowToInsert = variables.rowToInsert;\n\n// Split the description into an array of rows\nconst rows = description.split(\"\\n\");\nconsole.log(rows)\n// Find the index of the rowBefore and rowAfter\nconst indexBefore = rows.findIndex(row => row.trim() === rowBefore);\nconst indexAfter = rows.findIndex(row => row.trim() === rowAfter);\n\n// Check if both rows are found and rowBefore comes before rowAfter\nif (indexBefore !== -1 && indexAfter !== -1 && indexBefore < indexAfter) {\n  // Insert the new row between rowBefore and rowAfter\n  rows.splice(indexBefore + 1, 0, rowToInsert);\n}\n\n// Join the rows back into a single string\nconst updatedDescription = rows.join(\"\\n\");\n\n// Return the updated description in the correct n8n output structure\nreturn [\n  {\n    json: {\n      updatedDescription: updatedDescription\n    }\n  }\n];"
      },
      "typeVersion": 2
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "50fd0bcb-7441-45eb-ab58-ca2a7de78516",
  "connections": {
    "Get All Videos": {
      "main": [
        [
          {
            "node": "Loop Over Videos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Loop Over Videos": {
      "main": [
        [],
        [
          {
            "node": "Get Specific Video",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Specific Video": {
      "main": [
        [
          {
            "node": "Create New Video Description with Row Inserted",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set String to Insert": {
      "main": [
        [
          {
            "node": "Get All Videos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Update Video Description": {
      "main": [
        [
          {
            "node": "Loop Over Videos",
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
            "node": "Set String to Insert",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create New Video Description with Row Inserted": {
      "main": [
        [
          {
            "node": "Update Video Description",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
