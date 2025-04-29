# Automatic Event Creation in Google Calendar from Google Sheets Data

**[View Template](https://n8n.io/workflows/3300-/)**  **Published Date:** 03/24/2025  **Created By:** WeblineIndia  **Categories:** `Productivity` `Development` `Core Nodes`  

## Template Description

This workflow streamlines the process of creating events in Google Calendar using event data stored in a Google Sheet.

The process begins by retrieving the latest event entry from Google Sheets, ensuring only the most recent event details are processed. Once fetched, a Function node formats the event date to align with Google Calendar's required format—ensuring consistency and preventing date-related errors.

After formatting, the structured event details are sent to Google Calendar, where an event is created with essential information such as the event title (summary), description, date, and location. Additionally, the workflow allows customization by setting the event's status as either "Busy" or "Available," helping attendees manage their schedules. A background color can also be assigned for better visibility and categorization.

By automating this process, you eliminate the need for manual event creation, ensuring seamless synchronization between Google Sheets and Google Calendar. This improves efficiency, accuracy, and productivity, making event management effortless.
Prerequisites : 

Before setting up this workflow, ensure the following:

You have an active Google account connected to Google Sheets and Google Calendar.
The Google Sheets API and Google Calendar API are enabled in the Google Cloud Console.
n8n has the necessary OAuth2 authentication configured for both Google Sheets and Google Calendar.
Your Google Sheet has columns for event details (event name, description, location, date, etc.).

|Event Name|Event Description|Event Start Date|Location|
|-|-|-|-|
|Birthday|Celebration|27-Mar-1989|City|
|Anniversary|Celebration|10-Jun-2015|City|

Customization Options : 

Modify the Google Sheets trigger to track updates in specific columns.
Adjust the data formatting function to support:
	Different date/time formats
	Time zone settings
	Custom event colors
	Attendee invitations

Steps :
Step 1: Add the Google Sheets Trigger Node

Click "Add Node" and search for Google Sheets.
Select "Google Sheets Trigger" and add it to the workflow.
Authenticate using your Google account (select an existing account if already authenticated).
Select the Spreadsheet and Sheet Name to monitor.
Set the Trigger Event to "Row Added".
Click "Execute Node" to test the connection.
Click "Save".

Step 2: Process Data with Function Node

Click "Add Node" and search for Function.
Add the Function Node and connect it to the Google Sheets Trigger Node.
In the function editor, write a script to extract and format data.
Ensure the required fields (title, location, date) are properly structured.
Click "Execute Node" to verify the formatted output.
Click "Save".

Step 3: Add the Google Calendar Node

Click "Add Node" and search for Google Calendar.
Select "Create Event" operation.
Authenticate with Google Calendar.
Map the required fields
	Title
	Description
	Location
	Start time
Optional: Set Event Status and Event Colors.
Click "Execute Node" to test event creation.
Click "Save".

Step 4: Final Steps

Connect all nodes in sequence (Google Sheets Trigger → Function Node → Google Calendar Node).
Test the workflow by adding a sample row in Google Sheets.
Verify that the event is created in Google Calendar with the correct title, description, date, and location.

About WeblineIndia

This workflow was built by the AI development team at WeblineIndia. We help businesses automate processes, reduce repetitive work, and scale faster. Need something custom? You can hire AI developers to build workflows tailored to your needs.

## Template JSON

```
{
  "id": "AvCMhDoSUAYXsrQX",
  "meta": {
    "instanceId": "14e4c77104722ab186539dfea5182e419aecc83d85963fe13f6de862c875ebfa"
  },
  "name": "Automate Event Creation in Google Calendar from Google Sheets",
  "tags": [],
  "nodes": [
    {
      "id": "b973046b-ff52-464e-8d34-fe57c5b1df7d",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -240,
        0
      ],
      "parameters": {
        "color": 6,
        "width": 1200,
        "height": 280,
        "content": "# Automate Event Creation in Google Calendar from Google Sheets\n"
      },
      "typeVersion": 1
    },
    {
      "id": "e845b624-6c0a-4d31-aace-cc050f8613dc",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -240,
        300
      ],
      "parameters": {
        "color": 6,
        "width": 1200,
        "height": 280,
        "content": "## Description \nIn this workflow, we streamline the process of creating events in Google Calendar using event data stored in a Google Sheet through n8n automation. The workflow begins by retrieving the latest event entry from Google Sheets, ensuring that only the most recent event details are processed. Once the event data is fetched, a Function node is used to format the event date so that it aligns with Google Calendar's required format. This step ensures consistency and prevents any date-related errors.\n\nAfter formatting, the workflow sends the structured event details to Google Calendar, where the event is created with essential information such as the event title (summary), description, event date, and location. Additionally, the workflow allows customization by setting the event's status as either \"Busy\" or \"Available,\" helping attendees manage their schedules effectively. Furthermore, a background color can be assigned to the event to enhance visibility and categorization in the calendar.\n\nBy automating this process, the workflow eliminates the need for manual event creation, ensuring seamless synchronization between Google Sheets and Google Calendar. This approach improves efficiency, accuracy, and productivity, making event management effortless."
      },
      "typeVersion": 1
    },
    {
      "id": "60f2c8b8-a953-4fc1-8751-01d8b7924cb2",
      "name": "Event Date Formatter",
      "type": "n8n-nodes-base.code",
      "position": [
        320,
        100
      ],
      "parameters": {
        "jsCode": "// Get the last item from the input data\nconst lastEvent = items[items.length - 1].json;\n\n// Extract relevant fields\nconst eventName = lastEvent[\"Event Name\"];\nconst eventDescription = lastEvent[\"Event Description\"];\nconst currentYear = new Date().getFullYear(); \n// Get the current year\nconst location = lastEvent[\"Location\"];\n\n// Ensure the date includes the year\nconst formatDateWithYear = (dateStr) => {\n    return dateStr.includes(currentYear) ? dateStr : `${dateStr} ${currentYear}`;\n};\n\n// Format the start date\nconst startDateString = formatDateWithYear(lastEvent[\"Event Start Date\"]); // Example: \"11 March 2024\"\n\n// Convert to JavaScript Date object\nconst startDate = new Date(startDateString);\n\n// Convert to ISO format (YYYY-MM-DD)\nconst formattedStartDate = startDate.toISOString().split(\"T\")[0]; // Extract only the date\n\n// Return the last event's formatted data\nreturn [{\n    json: {\n        eventName,\n        eventDescription,\n        startDate: formattedStartDate,\n      location: location,\n    }\n}];\n"
      },
      "typeVersion": 2
    },
    {
      "id": "e27e0d10-71bb-4d01-ba92-5fb8c3195422",
      "name": "New Event Entry Listener",
      "type": "n8n-nodes-base.googleSheetsTrigger",
      "position": [
        -120,
        100
      ],
      "parameters": {
        "event": "rowAdded",
        "options": {
          "valueRender": "FORMULA"
        },
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            },
            {}
          ]
        },
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1dKjIGmcnQgSEMVuWAAFVDaj_MCBFKBX8hCOk5OH2dK4/edit#gid=0",
          "cachedResultName": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1dKjIGmcnQgSEMVuWAAFVDaj_MCBFKBX8hCOk5OH2dK4",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1dKjIGmcnQgSEMVuWAAFVDaj_MCBFKBX8hCOk5OH2dK4/edit?usp=drivesdk",
          "cachedResultName": "N8n Event List"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "04864602-bf6a-4def-9bc3-c5ab4b5c8336",
      "name": "Google Calendar Event Creator",
      "type": "n8n-nodes-base.googleCalendar",
      "position": [
        700,
        100
      ],
      "parameters": {
        "end": "={{ $json.startDate }}",
        "start": "={{ $json.startDate }}",
        "calendar": {
          "__rl": true,
          "mode": "list",
          "value": "",
          "cachedResultName": ""
        },
        "additionalFields": {
          "color": "3",
          "allday": "yes",
          "summary": "={{ $json.eventName }}",
          "location": "={{ $json.location }}",
          "showMeAs": "transparent",
          "description": "={{ $json.eventDescription }}",
          "guestsCanInviteOthers": true
        }
      },
      "typeVersion": 1.3
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "98bd043e-8dce-4eca-a22f-95ff61f07a1f",
  "connections": {
    "Event Date Formatter": {
      "main": [
        [
          {
            "node": "Google Calendar Event Creator",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "New Event Entry Listener": {
      "main": [
        [
          {
            "node": "Event Date Formatter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
