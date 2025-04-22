# Export n8n Cloud execution data to CSV

**[View Template](https://n8n.io/workflows/2295-/)**  **Published Date:** 06/20/2024  **Created By:** Ludwig  **Categories:**   

## Template Description

Overview

This template helps n8n cloud plan users execute all executions to a CSV for easy data analysis. Identify what workflows are generating the most executions or could be optimized.

How this workflow works
Click "Test Workflow" to manually execute the workflow
Open the "Convert to CSV" node to access the binary data of the CSV file
Download the CSV file

Nodes included:
n8n node
Convert to File
No Operation, do nothing - replace with another

Set up steps
Import the workflow to your workspace
Add your n8n API credential

Benefits of Exporting n8n Cloud Executions to CSV

Exporting n8n Cloud executions to CSV offers significant advantages for enhancing workflow management and data analysis capabilities. Here are three key benefits:

Enhanced Data Analysis:
   Comprehensive Insights: Exporting execution data allows for in-depth analysis of workflow performance, helping identify bottlenecks and optimize processes.
   Custom Reporting: CSV files can be easily imported into various data analysis tools (e.g., Excel, Google Sheets, or BI software) to create custom reports and visualizations tailored to specific business needs.

Improved Workflow Monitoring:
   Historical Data Review: Accessing historical execution data enables users to track workflow changes and their impacts over time, facilitating better decision-making.
   Error Tracking and Debugging: By reviewing execution logs, users can quickly identify and address errors or failures, ensuring smoother and more reliable workflow operations.

Regulatory Compliance and Auditing:
   Audit Trails: Keeping a record of all executions provides a clear audit trail, essential for regulatory compliance and internal audits.
   Data Retention: Exported data ensures that execution records are preserved according to organizational data retention policies, safeguarding against data loss.

By leveraging the capabilities of CSV exports, users can gain valuable insights, streamline workflow management, and ensure robust data handling practices, ultimately driving better performance and efficiency in their n8n Cloud operations.

## Template JSON

```
{
  "meta": {
    "instanceId": "d7fca24febd307481e0bbb00524fea1b07b7a70804c772daa0c99b9ce35883b9",
    "templateCredsSetupCompleted": true
  },
  "nodes": [
    {
      "id": "9b5b5af9-8a56-40a3-ad75-1e1186e96439",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        640,
        360
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "7c99e8d9-ef79-4833-bb0c-5005d210418e",
      "name": "n8n | Get all executions",
      "type": "n8n-nodes-base.n8n",
      "position": [
        880,
        360
      ],
      "parameters": {
        "filters": {},
        "options": {},
        "resource": "execution",
        "returnAll": true
      },
      "credentials": {
        "n8nApi": {
          "id": "3c3kWsiMeyTemNnV",
          "name": "n8n account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "95ae4ed4-22d4-41dc-be75-ea1224985f80",
      "name": "Convert to CSV",
      "type": "n8n-nodes-base.convertToFile",
      "position": [
        1140,
        360
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.1
    },
    {
      "id": "07665975-a07c-4c7c-b9ec-cad583b17c07",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        800,
        220
      ],
      "parameters": {
        "color": 5,
        "width": 254,
        "height": 355,
        "content": "## Get all executions\n**Workflow and Status Filters can be applied here**"
      },
      "typeVersion": 1
    },
    {
      "id": "14e2f531-5902-4c58-946c-a8571266c5e4",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1080,
        220
      ],
      "parameters": {
        "color": 4,
        "width": 214.03132502922975,
        "height": 355,
        "content": "## Convert to CSV\n**CSV for easy parsing**"
      },
      "typeVersion": 1
    },
    {
      "id": "e1bc72a9-3378-4dd4-88b0-3fb4eee1fea8",
      "name": "No Operation, do nothing",
      "type": "n8n-nodes-base.noOp",
      "position": [
        1380,
        360
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "066fa340-98d6-4e18-87f0-f995083d041d",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1320,
        220
      ],
      "parameters": {
        "width": 214.07781344172514,
        "height": 356,
        "content": "## Replace this node\n**Replace this node with any cloud storage destination**"
      },
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "Convert to CSV": {
      "main": [
        [
          {
            "node": "No Operation, do nothing",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "n8n | Get all executions": {
      "main": [
        [
          {
            "node": "Convert to CSV",
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
            "node": "n8n | Get all executions",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
