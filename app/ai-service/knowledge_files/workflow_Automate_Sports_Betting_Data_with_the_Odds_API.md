# Automate Sports Betting Data with the Odds API

**[View Template](https://n8n.io/workflows/2843-/)**  **Published Date:** 02/04/2025  **Created By:** Marketing Canopy  **Categories:** `Data & Storage` `Development` `Core Nodes`  

## Template Description

Automate Sports Betting Data with TheOddsAPI  

This workflow enables you to create and update a table using TheOddsAPI for sports betting data. It automatically pulls upcoming Ice Hockey games at the start of the day and updates the table with results at the end of the day. You can modify it to retrieve odds and game data for any sport.  

This setup is particularly useful for sports betting applications, such as tracking the results of a predictive model. It leverages scheduled triggers to activate HTTP requests, which then create or update fields in Airtable by matching on the game ID.  

Prerequisites  

Before implementing this workflow, ensure you have the following:  

TheOddsAPI Account & API Key  
   Sign up at TheOddsAPI and obtain an API key.  
   Ensure you have the correct API permissions to access sports odds and results.  

Airtable Account & API Key  
   Create an account at Airtable and set up a database.  
   Obtain an API key from the Account Settings page.  

API Access & Rate Limits  
   Review TheOddsAPI’s rate limits and ensure your account tier allows for scheduled API calls.  
   Confirm that Airtable API limits align with your expected data retrieval frequency.  

Step-by-Step Guide to Integrating TheOddsAPI  

1. Schedule API Requests  
Set up a trigger to automatically pull upcoming Ice Hockey games at the start of each day.  

2. Fetch Data from TheOddsAPI  
Retrieve the latest sports betting data, including game details and odds, using TheOddsAPI.  

3. Store Data in Airtable  
Insert or update records in Airtable by matching game IDs, ensuring data accuracy.  

Sample Airtable Template Column Setup for Ice Hockey  
(Table can adjust depending on sport and data needs. Reference TheOddsAPI for more documentation.)  

Game ID**  
Sport**  
League**  
Game Date (UTC)**  
Home Team**  
Away Team**  
Completed** (Boolean: TRUE/FALSE for game completion status)  
Scores** (JSON or String for final scores)  
Last Update** (Timestamp of the latest update)  

4. Schedule an End-of-Day Update  
Configure another trigger to fetch final game results at the end of the day.  

5. Update Records in Airtable  
Modify existing Airtable records with final scores and game outcomes for complete tracking.  

6. Customize for Other Sports  
Adjust API parameters to retrieve data for different sports and betting odds, making the system flexible for multiple use cases.  

This structured workflow automates sports betting data collection and updates, ensuring accurate and real-time tracking of odds and game results. By integrating TheOddsAPI with Airtable, you can build scalable applications for predictive sports analytics and betting insights.  




## Template JSON

```
{
  "id": "6sBxOuYYcJjIBmVJ",
  "meta": {
    "instanceId": "73d9d5380db181d01f4e26492c771d4cb5c4d6d109f18e2621cf49cac4c50763",
    "templateCredsSetupCompleted": true
  },
  "name": "Automating Betting Data Retrieval with TheOddsAPI and Airtable",
  "tags": [],
  "nodes": [
    {
      "id": "3f7d9313-2a46-4869-a1f5-33976352961c",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -520,
        -300
      ],
      "parameters": {
        "width": 300,
        "height": 440,
        "content": "The following triggers start the workflow at the Start of the day and the End of the day. Times can be adjusted to user's preference. "
      },
      "typeVersion": 1
    },
    {
      "id": "a535c540-c186-466f-97e2-4d96d02c1f1d",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -100,
        -660
      ],
      "parameters": {
        "color": 4,
        "width": 460,
        "height": 660,
        "content": "Once activated, HTTP Requests pulls the upcoming data for the sport of the user's choosing. The following is set for Ice Hockey. More documentation can be found within the link below: \n\nhttps://the-odds-api.com/liveapi/guides/v4/#get-events\n\nIf you would like to add more data such as the sport books or odds, you can find documentation within the documentation below: \n\nhttps://the-odds-api.com/liveapi/guides/v4/#get-odds\n\nOnce the data is pulled, the records are created within the Airtable.\n"
      },
      "typeVersion": 1
    },
    {
      "id": "29335df8-6aab-475c-8d8b-38b27eb66bb9",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        440,
        -280
      ],
      "parameters": {
        "color": 3,
        "width": 800,
        "height": 540,
        "content": "At the end of the day, the Schedule Trigger will activate a HTTP request for the scores of the events. This is set for Ice Hockey but can be adjusted for the user's preference. \n\nAfter the data is pulled, it will merge the data with upcoming events to combine the results matching the id. \n\nThe Airtable is then updated with the result records. This can be adjusted to pull in sports odds or the different sports book data. "
      },
      "typeVersion": 1
    },
    {
      "id": "01134aa4-cc3c-42ed-bc96-f737f1434ed6",
      "name": "Morning Trigger To Pull Data At 7:00am",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -420,
        -200
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "triggerAtHour": 7
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "c0b4c27f-bb17-4d85-a042-aa2db5060a6f",
      "name": "Evening Trigger To Pull Data At 11:00pm",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -420,
        -20
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "triggerAtHour": 23
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "0a38de6c-4f2e-46ba-8c10-8f12b0a4abe2",
      "name": "Retrieve Data Of Upcoming Sport Events For The Day",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        20,
        -200
      ],
      "parameters": {
        "url": "=https://api.the-odds-api.com/v4/sports/icehockey_nhl/events?apiKey=60019f5ac82b8d5d508b2dc8393384c1",
        "options": {},
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "headerParameters": {
          "parameters": [
            {}
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "qbYtAoCFY2cLFvOU",
          "name": "Header Auth account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "28393bd9-17ed-48b1-ba6f-f62b51ce137c",
      "name": "Create Records Of Upcoming Events For The Day",
      "type": "n8n-nodes-base.airtable",
      "position": [
        180,
        -380
      ],
      "parameters": {
        "base": {
          "__rl": true,
          "mode": "list",
          "value": "appIXd8a8JeB9bPaL",
          "cachedResultUrl": "https://airtable.com/appIXd8a8JeB9bPaL",
          "cachedResultName": "Untitled Base"
        },
        "table": {
          "__rl": true,
          "mode": "list",
          "value": "tbldpnP52opBEtKEy",
          "cachedResultUrl": "https://airtable.com/appIXd8a8JeB9bPaL/tbldpnP52opBEtKEy",
          "cachedResultName": "Table 1"
        },
        "columns": {
          "value": {
            "id": "={{ $json.id }}",
            "away_team": "={{ $json.away_team }}",
            "home_team": "={{ $json.home_team }}",
            "sports_key": "={{ $json.sport_key }}",
            "sport_title": "={{ $json.sport_title }}",
            "commence_time": "={{ $json.commence_time }}"
          },
          "schema": [
            {
              "id": "id",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "id",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "sports_key",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "sports_key",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "sport_title",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "sport_title",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "commence_time",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "commence_time",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "home_team",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "home_team",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "away_team",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "away_team",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "completed",
              "type": "string",
              "display": true,
              "removed": true,
              "readOnly": false,
              "required": false,
              "displayName": "completed",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "scores",
              "type": "string",
              "display": true,
              "removed": true,
              "readOnly": false,
              "required": false,
              "displayName": "scores",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "last_update",
              "type": "string",
              "display": true,
              "removed": true,
              "readOnly": false,
              "required": false,
              "displayName": "last_update",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "create"
      },
      "credentials": {
        "airtableTokenApi": {
          "id": "0ApVmNsLu7aFzQD6",
          "name": "Airtable Personal Access Token account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "086e599b-fc74-4ed5-a36f-fb80e385e625",
      "name": "Retrieve Sport Results Data At The End Of The Day",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        500,
        20
      ],
      "parameters": {
        "url": "https://api.the-odds-api.com/v4/sports/icehockey_nhl/scores?daysFrom=1&apiKey=60019f5ac82b8d5d508b2dc8393384c1",
        "options": {},
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "headerParameters": {
          "parameters": [
            {}
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "qbYtAoCFY2cLFvOU",
          "name": "Header Auth account"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "1b5ec6f2-d913-4005-89f0-d566e896c344",
      "name": "Combine Sport Results With Upcoming Events Records By Matching ID",
      "type": "n8n-nodes-base.merge",
      "position": [
        740,
        -120
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "fieldsToMatchString": "id"
      },
      "typeVersion": 3
    },
    {
      "id": "f1765871-6f9e-416b-8ee8-696bc4dbf6bb",
      "name": "Update Table Records With Scores And Results For Sport Events",
      "type": "n8n-nodes-base.airtable",
      "position": [
        1020,
        -60
      ],
      "parameters": {
        "base": {
          "__rl": true,
          "mode": "list",
          "value": "appIXd8a8JeB9bPaL",
          "cachedResultUrl": "https://airtable.com/appIXd8a8JeB9bPaL",
          "cachedResultName": "Untitled Base"
        },
        "table": {
          "__rl": true,
          "mode": "list",
          "value": "tbldpnP52opBEtKEy",
          "cachedResultUrl": "https://airtable.com/appIXd8a8JeB9bPaL/tbldpnP52opBEtKEy",
          "cachedResultName": "Table 1"
        },
        "columns": {
          "value": {
            "id": "={{ $json.id }}",
            "scores": "={{ $json.scores }}",
            "completed": "={{ $json.completed }}",
            "last_update": "={{ $json.last_update }}"
          },
          "schema": [
            {
              "id": "id",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": true,
              "required": false,
              "displayName": "id",
              "defaultMatch": true
            },
            {
              "id": "id",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "id",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "sports_key",
              "type": "string",
              "display": true,
              "removed": true,
              "readOnly": false,
              "required": false,
              "displayName": "sports_key",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "sport_title",
              "type": "string",
              "display": true,
              "removed": true,
              "readOnly": false,
              "required": false,
              "displayName": "sport_title",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "commence_time",
              "type": "string",
              "display": true,
              "removed": true,
              "readOnly": false,
              "required": false,
              "displayName": "commence_time",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "home_team",
              "type": "string",
              "display": true,
              "removed": true,
              "readOnly": false,
              "required": false,
              "displayName": "home_team",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "away_team",
              "type": "string",
              "display": true,
              "removed": true,
              "readOnly": false,
              "required": false,
              "displayName": "away_team",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "completed",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "completed",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "scores",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "scores",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "last_update",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": false,
              "required": false,
              "displayName": "last_update",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "id"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "update"
      },
      "credentials": {
        "airtableTokenApi": {
          "id": "0ApVmNsLu7aFzQD6",
          "name": "Airtable Personal Access Token account"
        }
      },
      "typeVersion": 2.1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "bf20603b-eb12-4156-94fe-fb18ecf6a454",
  "connections": {
    "Morning Trigger To Pull Data At 7:00am": {
      "main": [
        [
          {
            "node": "Retrieve Data Of Upcoming Sport Events For The Day",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Evening Trigger To Pull Data At 11:00pm": {
      "main": [
        [
          {
            "node": "Retrieve Sport Results Data At The End Of The Day",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Retrieve Sport Results Data At The End Of The Day": {
      "main": [
        [
          {
            "node": "Combine Sport Results With Upcoming Events Records By Matching ID",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Retrieve Data Of Upcoming Sport Events For The Day": {
      "main": [
        [
          {
            "node": "Combine Sport Results With Upcoming Events Records By Matching ID",
            "type": "main",
            "index": 0
          },
          {
            "node": "Create Records Of Upcoming Events For The Day",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Combine Sport Results With Upcoming Events Records By Matching ID": {
      "main": [
        [
          {
            "node": "Update Table Records With Scores And Results For Sport Events",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
