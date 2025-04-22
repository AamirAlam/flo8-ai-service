# Exponential Backoff for Google APIs

**[View Template](https://n8n.io/workflows/2556-/)**  **Published Date:** 11/18/2024  **Created By:** Alex Kim  **Categories:** `Data & Storage` `Productivity` `Development` `Core Nodes`  

## Template Description

n8n Workflow: Exponential Backoff for Google APIs

Overview
This n8n workflow implements an Exponential Backoff mechanism to handle retries when interacting with Google APIs. It ensures that failed API requests are retried with increasing delays, up to a specified maximum retry count. This approach helps mitigate transient errors (e.g., rate limits or temporary network issues) while maintaining workflow efficiency.

Key Features:
Exponential Backoff Logic**: Dynamically increases wait time between retries based on the retry count.
Error Handling**: Stops the workflow and raises an error after a specified number of retries.
Dynamic Waiting**: Waits for a calculated duration before each retry.
Scalable Design**: Modular nodes for easy debugging and customization.

Workflow Details

Nodes in the Workflow:

Trigger (When clicking "Test Workflow"):
   Manually starts the workflow for testing.

Loop Over Items:
   Iterates over multiple input items to process Google API requests row by row.

Google API Node (Example: Update Sheet):
   Sends a request to a Google API endpoint (e.g., updating a row in Google Sheets).
   On success: Moves to the next item in the loop.
   On error: Passes the error to the Exponential Backoff node.

Exponential Backoff:
   Calculates the delay for the next retry based on the retry count.
   Logic:
          const retryCount = $json["retryCount"] || 0;
     const maxRetries = 5;
     const initialDelay = 1; // in seconds

     if (retryCount &lt; maxRetries) {
         const currentDelayInSeconds = initialDelay * Math.pow(2, retryCount);
         return {
             json: {
                 retryCount: retryCount + 1,
                 waitTimeInSeconds: currentDelayInSeconds,
                 status: 'retrying',
             }
         };
     } else {
         return {
             json: {
                 error: 'Max retries exceeded',
                 retryCount: retryCount,
                 status: 'failed'
             }
         };
     }
     
Wait:
   Dynamically waits for the waitTimeInSeconds value calculated in the Exponential Backoff node.
   Configuration:
     Resume: After Time Interval
     Wait Amount: {{ $json["waitTimeInSeconds"] }}
     Unit: Seconds

Check Max Retries:
   Evaluates whether the retry count has exceeded the maximum limit.
   Routes the workflow:
     True: Passes to the Stop and Error node.
     False: Loops back to the Google API node for retry.

Stop and Error:
   Stops the workflow and logs the error when the maximum retry count is reached.

Parameters
Configurable Settings:
Max Retries:
   Defined in the Exponential Backoff node (const maxRetries = 5).
   Adjust this value based on your requirements.

Initial Delay:
   The starting wait time for retries, defined as 1 second.

Google API Configuration:
   Ensure your Google API node is properly authenticated and configured with the desired endpoint and parameters.

How to Use
Import the Workflow:
   Copy the workflow JSON and import it into your n8n instance.

Configure Google API Node:
   Set up the Google API node with your credentials and target API endpoint (e.g., Google Sheets, Gmail, etc.).

Test the Workflow:
   Manually trigger the workflow and observe the retry behavior in case of errors.

Monitor Logs:
   Use the console logs in the Exponential Backoff node to debug retry timings and status.

Example Scenarios
Scenario 1: Successful Execution
The Google API processes all requests without errors.
Workflow completes without triggering the retry logic.

Scenario 2: Transient API Errors
The Google API returns an error (e.g., 429 Too Many Requests).
The workflow retries the request with increasing wait times.

Scenario 3: Maximum Retries Exceeded
The workflow reaches the maximum retry count (e.g., 5 retries).
An error is raised, and the workflow stops.

Considerations
Jitter:
   This workflow does not implement jitter (randomized delay) since it's not required for low-volume use cases.
   If needed, jitter can be added to the exponential backoff calculation.

Retry Storms:
   If multiple workflows run simultaneously, ensure your API quotas can handle potential retries.

Error Handling Beyond Max Retries:
   Customize the Stop and Error node to notify stakeholders or log errors in a centralized system.

Customization Options
Adjust the maximum retry limit and delay calculation to suit your use case.
Add additional logic to handle specific error codes differently.
Extend the workflow to notify stakeholders when an error occurs (e.g., via Slack or email).

Troubleshooting
Retry Not Triggering**:
  Ensure the retryCount variable is passed correctly between nodes.
  Confirm that the error output from the Google API node flows to the Exponential Backoff node.

Incorrect Wait Time**:
  Verify the Wait node is referencing the correct field for waitTimeInSeconds.

Request for Feedback
We are always looking to improve this workflow. If you have suggestions, improvements, or ideas for additional features, please feel free to share them. Your feedback helps us refine and enhance this solution!



## Template JSON

```
{
  "id": "2NhqmUqW3KruEkaE",
  "meta": {
    "instanceId": "d868e3d040e7bda892c81b17cf446053ea25d2556fcef89cbe19dd61a3e876e9"
  },
  "name": "Exponential Backoff for Google APIs",
  "tags": [
    {
      "id": "nezaWFCGa7eZsVKu",
      "name": "Utility",
      "createdAt": "2024-11-13T18:08:08.207Z",
      "updatedAt": "2024-11-13T18:08:08.207Z"
    }
  ],
  "nodes": [
    {
      "id": "5d6b1730-33c5-401c-b73f-2b7ea8eedfe3",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -580,
        -80
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "6726b630-597c-46cf-8839-75cd80108f2f",
      "name": "Exponential Backoff",
      "type": "n8n-nodes-base.code",
      "position": [
        160,
        120
      ],
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "// Define the retry count (coming from a previous node or set manually)\nconst retryCount = $json[\"retryCount\"] || 0;  // If not present, default to 0\nconst maxRetries = 5;  // Define the maximum number of retries\nconst initialDelay = 1;  // Initial delay in seconds (1 second)\n\n// If the retry count is less than the max retries, calculate the delay\nif (retryCount < maxRetries) {\n    const currentDelayInSeconds = initialDelay * Math.pow(2, retryCount);  // Exponential backoff delay in seconds\n    \n    // Log the delay time for debugging\n    console.log(`Waiting for ${currentDelayInSeconds} seconds before retry...`);\n    \n    return {\n        json: {\n            retryCount: retryCount + 1,  // Increment retry count\n            waitTimeInSeconds: currentDelayInSeconds, // Pass the delay time in seconds\n            status: 'retrying',\n        }\n    };\n} else {\n    // If max retries are exceeded, return a failure response\n    return {\n        json: {\n            error: 'Max retries exceeded',\n            retryCount: retryCount,\n            status: 'failed'\n        }\n    };\n}\n"
      },
      "typeVersion": 2
    },
    {
      "id": "605b8ff0-aa19-42dd-8dbb-aa12380ac4bc",
      "name": "Stop and Error",
      "type": "n8n-nodes-base.stopAndError",
      "position": [
        760,
        120
      ],
      "parameters": {
        "errorMessage": "Google Sheets API Limit has been triggered and the workflow has stopped"
      },
      "typeVersion": 1
    },
    {
      "id": "97818e8b-e0cc-4a49-8797-43e02535740f",
      "name": "Loop Over Items",
      "type": "n8n-nodes-base.splitInBatches",
      "position": [
        -360,
        -80
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 3
    },
    {
      "id": "0583eabd-bd97-4330-8a38-b2aed3a90c37",
      "name": "Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "onError": "continueErrorOutput",
      "position": [
        -120,
        20
      ],
      "parameters": {
        "options": {},
        "sheetName": {
          "__rl": true,
          "mode": "name",
          "value": "Sheet1"
        },
        "documentId": {
          "__rl": true,
          "mode": "url",
          "value": "https://docs.google.com/spreadsheets/d/1_gxZl6n_AYPHRFRTWfhy7TZnhEYuWzh8UvGdtWCD3sU/edit?gid=0#gid=0"
        },
        "authentication": "serviceAccount"
      },
      "credentials": {
        "googleApi": {
          "id": "lm7dPHYumCy6sP6k",
          "name": "AlexK1919 Google Service"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "0d8023f8-f7ac-4303-b18e-821690cc9f94",
      "name": "Wait",
      "type": "n8n-nodes-base.wait",
      "position": [
        360,
        120
      ],
      "webhookId": "f1651aa1-6497-4496-9e07-240dcf1852f3",
      "parameters": {
        "amount": "={{ $json[\"waitTime\"] }}"
      },
      "typeVersion": 1.1
    },
    {
      "id": "72e0001e-f99b-4d57-9006-4a4dd5d3d8d5",
      "name": "Check Max Retries",
      "type": "n8n-nodes-base.if",
      "position": [
        560,
        120
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
              "id": "51e191cb-af20-423b-9303-8523caa4ae0d",
              "operator": {
                "type": "number",
                "operation": "gt"
              },
              "leftValue": "={{ $('Exponential Backoff').item.json[\"retryCount\"] }}",
              "rightValue": 10
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "2ea14bb0-4313-4595-811d-729ca6d37420",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        100,
        -80
      ],
      "parameters": {
        "color": 3,
        "width": 820,
        "height": 460,
        "content": "# Exponential Backoff for Google APIs \n## Connect these nodes to any Google API node such as the Google Sheets node example in this workflow"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "729e3a54-6238-4e4c-833e-8e37dba16dbb",
  "connections": {
    "Wait": {
      "main": [
        [
          {
            "node": "Check Max Retries",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Sheets": {
      "main": [
        [
          {
            "node": "Loop Over Items",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Exponential Backoff",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Loop Over Items": {
      "main": [
        [],
        [
          {
            "node": "Google Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check Max Retries": {
      "main": [
        [
          {
            "node": "Stop and Error",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Google Sheets",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Exponential Backoff": {
      "main": [
        [
          {
            "node": "Wait",
            "type": "main",
            "index": 0
          },
          {
            "node": "Check Max Retries",
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
            "node": "Loop Over Items",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
