# Convert Addresses to LatLong with Google Sheets and Google Maps API

**[View Template](https://n8n.io/workflows/2739-/)**  **Published Date:** 01/17/2025  **Created By:** Boriwat Chanruang  **Categories:** `Data & Storage` `Productivity` `Development` `Core Nodes`  

## Template Description

Template Detail
This template automates the process of converting a list of addresses into their latitude and longitude (LatLong) coordinates using Google Sheets and the Google Maps API. It's designed for businesses, developers, and analysts who need accurate geolocation data for use cases like delivery routing, event planning, or market analysis.

What the Template Does
Fetch Address Data: Retrieves addresses from a Google Sheet.
Google Maps API Integration: Sends each address to the Google Maps API and retrieves the corresponding LatLong coordinates.
Update Google Sheets: Automatically updates the same Google Sheet with the LatLong data for each address.

Enhancements
Google Sheets Template: Provide a pre-configured Google Sheets template that users can copy. Example link: Google Sheets Template. 

Columns required:
   Address: Column to input addresses.
   LatLong: Column for the latitude and longitude results.

Updated Workflow Structure

Trigger:
   A manual trigger node starts the workflow.
Retrieve Data from Google Sheets:
   Fetch addresses from a Google Sheet.
Send to Google Maps API:
   For each address, retrieve the LatLong coordinates directly via the Google Maps API.
Update Google Sheets:
   Write the LatLong results back into the Google Sheet.

Steps to Use
Prepare Google Sheet:
   Copy the provided Google Sheets template and add your addresses to the Address column.
Configure Google Cloud API:
   Enable the Maps API for your Google Cloud project.
   Generate an API key with the required permissions.
Run the Workflow:
   Start the workflow in n8n; it will process the addresses automatically.
   Updated LatLong data will appear in the corresponding Google Sheet.
Review the Results:
   Use the enriched LatLong data for mapping or analysis.


## Template JSON

```
{
  "id": "7ijhwXKPf6M2ZUBM",
  "meta": {
    "instanceId": "c59c4acfed171bdc864e7c432be610946898c3ee271693e0303565c953d88c1d"
  },
  "name": "Convert Addresses to LatLong with Google Sheets and Google Maps API",
  "tags": [],
  "nodes": [
    {
      "id": "9465735e-5d1d-4c93-b407-13ef79144f92",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -340,
        20
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "4041b7fa-c47e-44c2-b296-2913e8551c61",
      "name": "Using Google Map API to Return Lat Long Back",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        200,
        -40
      ],
      "parameters": {
        "url": "https://maps.googleapis.com/maps/api/place/textsearch/json",
        "options": {},
        "sendQuery": true,
        "queryParameters": {
          "parameters": [
            {
              "name": "query",
              "value": "={{ $json.Address }}"
            },
            {
              "name": "key",
              "value": "AIzaSyCwQkEAOhqxxyXygUri-6xhzFSQuidA5TM"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "20b26d33-2e4a-43ad-bc0f-bc510f02dbd0",
      "name": "Update Lat-Long in Each Places",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        540,
        -40
      ],
      "parameters": {
        "columns": {
          "value": {
            "Latlong": "={{ $json.results[0].geometry.location.lat }},{{ $json.results[0].geometry.location.lng }}",
            "row_number": "={{ $('Extract The Places from Google Sheet').item.json.row_number }}"
          },
          "schema": [
            {
              "id": "Address",
              "type": "string",
              "display": true,
              "removed": true,
              "required": false,
              "displayName": "Address",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "Latlong",
              "type": "string",
              "display": true,
              "required": false,
              "displayName": "Latlong",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "row_number",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": true,
              "required": false,
              "displayName": "row_number",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "row_number"
          ]
        },
        "options": {},
        "operation": "update",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": 1738976351,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/15Fz57qiARIJ6R5OzBAVgiAHnU8sOSX8eYFEP6thOrMM/edit#gid=1738976351",
          "cachedResultName": "Sheet2"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "15Fz57qiARIJ6R5OzBAVgiAHnU8sOSX8eYFEP6thOrMM",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/15Fz57qiARIJ6R5OzBAVgiAHnU8sOSX8eYFEP6thOrMM/edit?usp=drivesdk",
          "cachedResultName": "Latlong Testing"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "9NS1XgJlZuylm0QV",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "29f53c52-0cb3-44ae-85ad-a9f2cded8334",
      "name": "Extract The Places from Google Sheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        -120,
        -20
      ],
      "parameters": {
        "options": {},
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": 1738976351,
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/15Fz57qiARIJ6R5OzBAVgiAHnU8sOSX8eYFEP6thOrMM/edit#gid=1738976351",
          "cachedResultName": "Sheet2"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "15Fz57qiARIJ6R5OzBAVgiAHnU8sOSX8eYFEP6thOrMM",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/15Fz57qiARIJ6R5OzBAVgiAHnU8sOSX8eYFEP6thOrMM/edit?usp=drivesdk",
          "cachedResultName": "Latlong Testing"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "9NS1XgJlZuylm0QV",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "dad3affe-47d9-475e-bd8a-cf4a81eb0fde",
  "connections": {
    "Update Lat-Long in Each Places": {
      "main": [
        []
      ]
    },
    "When clicking \u2018Test workflow\u2019": {
      "main": [
        [
          {
            "node": "Extract The Places from Google Sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract The Places from Google Sheet": {
      "main": [
        [
          {
            "node": "Using Google Map API to Return Lat Long Back",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Using Google Map API to Return Lat Long Back": {
      "main": [
        [
          {
            "node": "Update Lat-Long in Each Places",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
