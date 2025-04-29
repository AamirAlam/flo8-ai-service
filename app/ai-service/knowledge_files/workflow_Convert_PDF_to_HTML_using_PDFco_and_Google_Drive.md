# Convert PDF to HTML using PDF.co and Google Drive

**[View Template](https://n8n.io/workflows/3275-/)**  **Published Date:** 03/21/2025  **Created By:** WeblineIndia  **Categories:** `Development` `Core Nodes` `Data & Storage`  

## Template Description

This n8n workflow automates the process of converting a newly stored PDF file from Google Drive into an HTML file and saving it back to Google Drive. The workflow is triggered whenever a new PDF is uploaded to a specific folder, ensuring seamless conversion and storage without any manual intervention.

This workflow provides an efficient, automated solution for converting PDFs to HTML, eliminating the need for manual file handling and ensuring a smooth document transformation process. It is particularly useful for scenarios where PDFs need to be dynamically converted and stored in an organised manner for web usage, archiving, or further processing.
Prerequisites :

Before setting up this workflow, ensure the following:
PDF.co API Key: Sign up at PDF.co and obtain an API key for PDF to HTML conversion.
Proper Authentication: Ensure authentication is configured for Google Drive in n8n.

Customisation Options : 
Modify the API request to convert PDFs to other formats like Text, CSV, or XML.
Extend the IF Node to reject files based on size or other properties.
Send a notification once the conversion is complete using an Email or Telegram Node.

Steps :

Step 1: Google Drive Trigger Node (Watch for New Files)

Click "Add Node" and search for Google Drive.
Select "Google Drive Trigger" and add it to the workflow.
Authenticate with your Google Account.
Select the folder to monitor.
Set the trigger to activate whenever a new file is added.
Click "Execute Node" to test.
Click "Save".

Step 2: IF Node (Check if File is a PDF)

Click "Add Node" and search for IF.
Add a condition to check if the file extension is  .pdf
If true → Send the file to the next step.
If false → Stop the workflow.
Click "Execute Node" to test.
Click "Save".

Step 3: HTTP Request Node (Convert PDF to HTML)

Click "Add Node" and search for HTTP Request.
Set the Method to POST.
Enter the PDF.co API endpoint for PDF to HTML conversion.
In the Headers, add API key which we have get from pdf.co
Send the binary PDF data as the request body.
Click "Execute Node" to test.
Click "Save".

Step 4: Function Node (Convert Response to Binary)

Click "Add Node" and search for Function.
Write a JavaScript function to transform the API response into a binary file.
Click "Execute Node" to test.
Click "Save".

Step 5: Google Drive Node (Save Converted HTML File)

Click "Add Node" and search for Google Drive.
Select "Upload File" as the action.
Authenticate with your Google Account.
Set the destination folder for storing the HTML file.
Map the binary data from the Function Node.
Click "Execute Node" to test.
Click "Save".

Step 6: Connect & Test the Workflow

Link the nodes in this  order (Google Drive Trigger → IF Node → HTTP Request → Function Node → Google Drive Upload)
Run the workflow manually.
Upload a test PDF to Google Drive.
Check Google Drive for the converted HTML file.

Who’s behind this?

WeblineIndia’s AI development team. 

We've delivered 3500+ software projects across 25+ countries since 1999. From no-code automations to complex AI systems — our AI team builds tools that drive results. 

Looking to hire AI developers? Start with us.

## Template JSON

```
{
  "id": "3McL3itHTso0Cy10",
  "meta": {
    "instanceId": "14e4c77104722ab186539dfea5182e419aecc83d85963fe13f6de862c875ebfa",
    "templateCredsSetupCompleted": true
  },
  "name": "Automated PDF to HTML Conversion",
  "tags": [],
  "nodes": [
    {
      "id": "43950636-79d1-43c3-b5a1-44ace016257d",
      "name": "Google Drive Trigger",
      "type": "n8n-nodes-base.googleDriveTrigger",
      "position": [
        0,
        0
      ],
      "parameters": {
        "event": "fileCreated",
        "options": {},
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        },
        "triggerOn": "specificFolder",
        "folderToWatch": {
          "__rl": true,
          "mode": "url",
          "value": ""
        }
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "",
          "name": ""
        }
      },
      "typeVersion": 1
    },
    {
      "id": "b5e1c616-a809-4e38-a1dd-0f91123bd846",
      "name": "If",
      "type": "n8n-nodes-base.if",
      "position": [
        220,
        0
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "4fd733d3-d393-4aea-bc25-c1e8bda32b54",
              "operator": {
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $json.mimeType }}",
              "rightValue": "application/pdf"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "d13a2481-9c21-43f0-beb8-1881b6a6843b",
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        480,
        -20
      ],
      "parameters": {
        "url": "https://api.pdf.co/v1/pdf/convert/to/html",
        "method": "POST",
        "options": {
          "redirect": {
            "redirect": {}
          }
        },
        "sendBody": true,
        "sendHeaders": true,
        "authentication": "genericCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "url",
              "value": "={{ $json.webViewLink }}"
            },
            {
              "name": "inline",
              "value": "true"
            },
            {
              "name": "async",
              "value": false
            },
            {
              "name": "unwrap"
            },
            {
              "name": "pages",
              "value": "0-"
            },
            {
              "name": "rect"
            },
            {
              "name": "async",
              "value": "false"
            },
            {
              "name": "name",
              "value": "result.csv"
            },
            {
              "name": "password"
            },
            {
              "name": "lineGrouping"
            },
            {
              "name": "profiles"
            }
          ]
        },
        "genericAuthType": "httpHeaderAuth",
        "headerParameters": {
          "parameters": [
            {}
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "zTHQFpHDdUNXJ49g",
          "name": "Header Auth account 2"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "66d49dae-d282-4854-8674-69784110ee0b",
      "name": "Google Drive",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        1080,
        -20
      ],
      "parameters": {
        "name": "sample.html",
        "driveId": {
          "__rl": true,
          "mode": "url",
          "value": "",
          "__regex": "https:\\/\\/drive\\.google\\.com(?:\\/.*|)\\/folders\\/([0-9a-zA-Z\\-_]+)(?:\\/.*|)"
        },
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "url",
          "value": ""
        }
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "",
          "name": ""
        }
      },
      "typeVersion": 3
    },
    {
      "id": "461222d4-7a73-412f-aceb-81745f17f7ea",
      "name": "Convert to Binary File",
      "type": "n8n-nodes-base.code",
      "position": [
        780,
        -20
      ],
      "parameters": {
        "jsCode": "// Convert the HTML string to a Buffer\nconst buffer = Buffer.from($json.body, 'utf-8');\n\n// Return the buffer as binary data\nreturn [\n  {\n    binary: {\n      data: {\n        data: buffer.toString('base64'), // Convert buffer to base64 string\n        mimeType: 'text/html',\n        fileName: 'sample.html'\n      }\n    }\n  }\n];\n"
      },
      "typeVersion": 2
    },
    {
      "id": "543dd2ff-011f-4f83-a5c7-ffb80fc3910d",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -60,
        -120
      ],
      "parameters": {
        "width": 1340,
        "height": 280,
        "content": "## Automated PDF to HTML Conversion\n"
      },
      "typeVersion": 1
    },
    {
      "id": "f0d02b89-71d2-4239-833d-9e5235024291",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -60,
        200
      ],
      "parameters": {
        "width": 1340,
        "height": 180,
        "content": "## Description: \nThis n8n workflow automates the process of converting a newly stored PDF file from Google Drive into an HTML file and saving it back to Google Drive. The workflow is triggered whenever a new PDF is uploaded to a specific folder, ensuring seamless conversion and storage without any manual intervention.\n\nThis workflow provides an efficient, automated solution for converting PDFs to HTML, eliminating the need for manual file handling and ensuring a smooth document transformation process. It is particularly useful for scenarios where PDFs need to be dynamically converted and stored in an organized manner for web usage, archiving, or further processing.\n\n"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "224c9b46-dc5e-44de-8ec4-956d48f4f4f1",
  "connections": {
    "If": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Convert to Binary File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Drive Trigger": {
      "main": [
        [
          {
            "node": "If",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Convert to Binary File": {
      "main": [
        [
          {
            "node": "Google Drive",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
