#  Dynamically Run SuiteQL Queries in NetSuite via HTTP Webhook in n8n

**[View Template](https://n8n.io/workflows/3002-/)**  **Published Date:** 02/24/2025  **Created By:** DataAnts  **Categories:**   

## Template Description


Dynamically Run SuiteQL Queries in NetSuite via HTTP Webhook in n8n

&gt; Important: This template uses a NetSuite community node, so it only works on self-hosted n8n. Cloud-based n8n instances currently do not support community nodes.  

Summary

This workflow template allows you to dynamically run SuiteQL queries in NetSuite by sending an HTTP request to an n8n Webhook node. Once triggered, the workflow uses token-based authentication to execute your SuiteQL query and returns the results as JSON. This makes it easy to integrate real-time NetSuite data into dashboards, reporting tools, or other applications.

Who Is This For?

Developers & Integrators**: Easily embed NetSuite data retrieval into custom apps or internal tools.  
Enterprises & Consultants**: Integrate dynamic reporting or data enrichment from NetSuite without manual exports.  
System Administrators**: Automate routine queries and reduce manual intervention.

Use Cases & Benefits

1. Dynamic Data Access
Send any SuiteQL query on demand instead of hardcoding queries or manually running reports.

2. Seamless Integration
Quickly pull NetSuite data into front-end systems (like Excel dashboards, custom web apps, or internal tools) by calling the webhook endpoint.

3. Simplified Reporting
Automate data extraction and formatting, reducing the need for manual exports and improving efficiency.

How It Works

Trigger:  
   An HTTP request to the webhook node initiates the workflow.  

Input Processing:  
   The workflow reads the SuiteQL query from the incoming request parameter (suiteql).  

Query Execution:  
   The NetSuite node uses your token-based authentication credentials to run the SuiteQL query.  

Response:  
   Results are returned as JSON in the HTTP response, ready for further processing or immediate consumption.

Prerequisites & Setup

NetSuite Community Node  
   This workflow requires the NetSuite community node. Make sure your self-hosted n8n instance supports community nodes.

NetSuite Token-Based Authentication  
   Enable TBA in NetSuite. Obtain the required consumer key, consumer secret, token ID, and token secret.

n8n Webhook  
   Copy the auto-generated webhook URL (e.g. http://&lt;your-n8n-domain&gt;/webhook/unique-id) from the Webhook node.

Usage  
   Send an HTTP GET or POST request to the webhook with your SuiteQL query. For example:  
          curl "http://&lt;your-n8n-domain&gt;/webhook/unique-id?suiteql=SELECT%20*%20FROM%20account%20LIMIT%2010"
        The workflow will execute the query and return JSON data.

Customization

Change the Query**:  
  Simply adjust the suiteql parameter in your HTTP request to run different SuiteQL statements.

Data Transformation**:  
  Insert nodes (e.g., Function, Set, or Format) to modify or reformat the data before returning it.

Extend Integration**:  
  Chain additional nodes to push the retrieved data to other services (Google Sheets, Slack, custom dashboards, etc.).

Additional Notes

Remember that this template is only compatible with self-hosted n8n because it uses a community node. - 
[netsuite community node](https://www.npmjs.com/package/n8n-nodes-netsuite
)
If you have questions, suggestions, or need support, contact us at support@dataants.org.



## Template JSON

```
{
  "id": "FDl4Ho3KYiA7MIxR",
  "meta": {
    "instanceId": "f6d3344846b38f0c35c069a91b2450f6527b26bb735b6301a692ce1cca2b2682"
  },
  "name": "NetSuite Rest API workflow",
  "tags": [],
  "nodes": [
    {
      "id": "f7f90fb4-e29f-4bbf-a99d-ee2fde45cd06",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -380,
        -40
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "9fcc1ce7-e9bf-4592-8bcd-7c77272a9c59",
      "name": "NetSuite",
      "type": "n8n-nodes-netsuite.netsuite",
      "position": [
        -40,
        -180
      ],
      "parameters": {
        "query": "={{ $json.query.suiteql }}",
        "options": {},
        "operation": "runSuiteQL"
      },
      "credentials": {
        "netsuite": {
          "id": "ro6Rl1oWY4KkFUYn",
          "name": "NetSuite account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "1d615309-2cb0-4383-9698-2f80da0d4bf5",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [
        -380,
        -280
      ],
      "webhookId": "249328cc-587a-4269-b266-96fe60cfaeb9",
      "parameters": {
        "path": "249328cc-587a-4269-b266-96fe60cfaeb9",
        "options": {},
        "responseData": "allEntries",
        "responseMode": "lastNode"
      },
      "typeVersion": 2
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "d6823e59-8e07-44a6-b4af-b029da620523",
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "NetSuite",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "NetSuite": {
      "main": [
        []
      ]
    },
    "When clicking \u2018Test workflow\u2019": {
      "main": [
        [
          {
            "node": "NetSuite",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
