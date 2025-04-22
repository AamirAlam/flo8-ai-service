# Automatically prune n8n execution history

**[View Template](https://n8n.io/workflows/2646-/)**  **Published Date:** 12/17/2024  **Created By:** Danger  **Categories:**   

## Template Description

Automated Execution Pruning

This workflow is designed to help you manage and optimize your n8n instance by automatically pruning old workflow executions, ensuring a cleaner environment and improved performance. You can customize the retention period to suit your needs.

Key Features:
Configurable Retention Period:  
   The workflow is preconfigured to delete workflow executions older than 10 days. You can easily adjust this duration by modifying the condition in the If node.

Daily Automation:  
   Using the Schedule Trigger, the workflow runs daily at the specified time (default: 4:44 AM), retrieving all workflow executions and identifying those that are older than the defined retention period.

On-Demand Testing:  
   The Manual Trigger allows you to test the workflow at any time, ensuring everything is working as expected.

Decision Making:  
   The If node evaluates each execution based on its start date and determines whether it should be deleted or retained.

Execution Pruning:  
   Delete Action: Executions meeting the criteria are removed via the Delete Execution node.  
   No-Operation: Executions that don't meet the criteria remain untouched.

Workflow Nodes:
Manual Trigger: Enables on-demand testing of the workflow.  
Schedule Trigger: Runs the workflow daily at the configured time.  
n8n List Execution: Fetches all executions in your n8n instance.  
If Node: Compares the execution's start date with the configured retention period.  
Delete Execution: Deletes executions older than the specified retention period.  
No Operation: Serves as a placeholder for executions that don't meet the pruning criteria.  

How to Customize:
Retention Period**:  
   Update the If node's condition to modify the retention period. For instance, change 10 * 24 * 60 * 60 * 1000 to the desired number of days in milliseconds.
   
Schedule**:  
   Adjust the timing of the Schedule Trigger to match your preferred automation schedule.

This workflow ensures your instance remains efficient by keeping only the relevant execution logs. Use it to maintain a streamlined and clutter-free environment effortlessly.

## Template JSON

```
{
  "meta": {
    "instanceId": "d68b0885df4f6057c27649c0cc1cdbf154a8c3c6de34051d82d8f9164d66f031"
  },
  "nodes": [
    {
      "id": "648130c4-5195-4b91-995b-443624019cd0",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        820,
        280
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "c25e5656-9ce2-4429-98f5-f86a88a8fe16",
      "name": "n8n1",
      "type": "n8n-nodes-base.n8n",
      "position": [
        2380,
        140
      ],
      "parameters": {
        "filters": {},
        "options": {},
        "resource": "execution",
        "returnAll": true,
        "requestOptions": {}
      },
      "credentials": {
        "n8nApi": {
          "id": "23",
          "name": "n8n account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "93acd82f-22ce-435c-b89e-a3f8ae876bc5",
      "name": "n8n list execution",
      "type": "n8n-nodes-base.n8n",
      "position": [
        1040,
        380
      ],
      "parameters": {
        "filters": {},
        "options": {},
        "resource": "execution",
        "returnAll": true,
        "requestOptions": {}
      },
      "credentials": {
        "n8nApi": {
          "id": "23",
          "name": "n8n account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "da03ff80-480d-4616-8aed-dd955d5e92d8",
      "name": "If",
      "type": "n8n-nodes-base.if",
      "position": [
        1260,
        380
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
              "id": "6a124591-3347-4224-a997-a7824de12c96",
              "operator": {
                "type": "dateTime",
                "operation": "before"
              },
              "leftValue": "={{ $json.startedAt }}",
              "rightValue": "={{ new Date(Date.now() - 10 * 24 * 60 * 60 * 1000).toISOString();  }}"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "6bc96f0a-5ed9-43f9-91e8-ced15ae53ef5",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        820,
        500
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "triggerAtHour": 4,
              "triggerAtMinute": 44
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "272f94d2-fcb5-4e6a-a32e-655ac1db9a00",
      "name": "delete execution",
      "type": "n8n-nodes-base.n8n",
      "position": [
        1480,
        280
      ],
      "parameters": {
        "resource": "execution",
        "operation": "delete",
        "executionId": "={{ $json.id }}",
        "requestOptions": {}
      },
      "credentials": {
        "n8nApi": {
          "id": "23",
          "name": "n8n account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "b2067d59-3678-400a-a464-cb7aab62413f",
      "name": "No Operation, do nothing",
      "type": "n8n-nodes-base.noOp",
      "position": [
        1480,
        480
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "pinData": {},
  "connections": {
    "If": {
      "main": [
        [
          {
            "node": "delete execution",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "No Operation, do nothing",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Schedule Trigger": {
      "main": [
        [
          {
            "node": "n8n list execution",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "n8n list execution": {
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
    "When clicking \u2018Test workflow\u2019": {
      "main": [
        [
          {
            "node": "n8n list execution",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
