# 📂 Automatically Update Stock Portfolio from OneDrive to Excel

**[View Template](https://n8n.io/workflows/2507-/)**  **Published Date:** 10/29/2024  **Created By:** Louis  **Categories:** `Data & Storage` `Productivity` `Development` `Core Nodes`  

## Template Description

Seamlessly Sync and Update Data from a csv in OneDrive to Excel with n8n

This workflow is perfect for users who need a reliable, automated way to transfer and organize data from OneDrive into Excel—especially for tasks like portfolio tracking, inventory management, and record-keeping. By monitoring your OneDrive folder for new CSV files, it performs data cleaning, transformation, and real-time updates in an Excel sheet, ensuring only new or changed records are added.

How it Works

Automated Monitoring: Every minute, the workflow scans a designated OneDrive folder for new files.
File Verification: It checks if the detected file is in CSV format; if not, the process stops with an error message.
Data Extraction and Cleaning: CSV data is loaded, and irrelevant headers are removed before mapping to specified columns in Excel.
Excel Update: The workflow maps data to your Excel sheet, updating only new or modified entries based on a unique identifier ("Ticker/ISIN").
Cleanup: To keep your OneDrive organized, processed files are deleted after updating Excel.

Setup Steps

Connect OneDrive and Excel Accounts: Link your Microsoft OneDrive and Excel accounts in n8n.
Designate Folder and Worksheet: Specify the OneDrive folder for monitoring and the Excel sheet for data updates.
Configure Sync Frequency and CSV Validation: Set the monitoring frequency to every minute and ensure the workflow identifies CSV files accurately.

Once configured, this workflow offers a hands-free, efficient solution to keep your OneDrive and Excel data synchronized effortlessly.

## Template JSON

```
{
  "meta": {
    "instanceId": "6045c639951d83c8706b0dd8d6330164bda01fe58f103cedc2c276bf1f9c11f1"
  },
  "nodes": [
    {
      "id": "fc4361c6-494a-4962-9488-2fe8dda1948c",
      "name": "Triggers if new file in watched folder",
      "type": "n8n-nodes-base.microsoftOneDriveTrigger",
      "position": [
        -400,
        380
      ],
      "parameters": {
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "id",
          "value": "2D96E50BD60B2B58%2115362"
        },
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        },
        "watchFolder": true
      },
      "credentials": {
        "microsoftOneDriveOAuth2Api": {
          "id": "WbTC1RWEJEZv7psj",
          "name": "Microsoft Drive account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "7e914111-ed3b-42c1-9461-5d36739db2b3",
      "name": "Not CSV",
      "type": "n8n-nodes-base.stopAndError",
      "position": [
        520,
        500
      ],
      "parameters": {
        "errorMessage": "The file is not a csv"
      },
      "typeVersion": 1
    },
    {
      "id": "43f092fe-9bc5-4e5f-a80b-db8aae53c9af",
      "name": "Extracts data from csv",
      "type": "n8n-nodes-base.extractFromFile",
      "position": [
        520,
        260
      ],
      "parameters": {
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "id": "142f14e7-663f-4225-8e58-551c1e089450",
      "name": "Microsoft OneDrive2",
      "type": "n8n-nodes-base.microsoftOneDrive",
      "onError": "continueErrorOutput",
      "position": [
        1300,
        260
      ],
      "parameters": {
        "fileId": "={{ $('Downloads the new file').item.json.id }}",
        "operation": "delete"
      },
      "credentials": {
        "microsoftOneDriveOAuth2Api": {
          "id": "WbTC1RWEJEZv7psj",
          "name": "Microsoft Drive account"
        }
      },
      "typeVersion": 1,
      "alwaysOutputData": true
    },
    {
      "id": "4d62251b-9a0d-4426-bf31-6fab04a645a7",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -960,
        200
      ],
      "parameters": {
        "color": 3,
        "width": 507.2258064516131,
        "height": 502.8225806451611,
        "content": "# \ud83d\udcc2 Automated OneDrive-to-Excel Data Sync with n8n\n\nEffortlessly manage your data with this n8n workflow that automatically monitors a OneDrive folder for new CSV uploads, processes the data, and updates your Excel sheet in real-time.\n\n### \ud83d\udd04 How It Works\n- **Real-Time Monitoring**: Every minute, the workflow checks for new CSV files in your OneDrive folder.\n- **Data Processing & Cleaning**: Upon detection, it downloads the file, removes irrelevant headers, and formats the data for Excel.\n- **Automatic Updates**: The cleaned data is mapped to your Excel sheet, updating only new or changed entries.\n- **Cleanup**: After updating, the CSV file is deleted, keeping your folder organized.\n\nIdeal for automating portfolio management, inventory tracking, or any workflow needing seamless data syncing between OneDrive and Excel. Set it up, and let your data handle itself!\n"
      },
      "typeVersion": 1
    },
    {
      "id": "48186060-343b-458c-bf2e-a5df501445e2",
      "name": "Cleans the output",
      "type": "n8n-nodes-base.code",
      "position": [
        740,
        260
      ],
      "parameters": {
        "jsCode": "// Get all input data\nconst items = $input.all();\n\n// Remove the first item (which is the irrelevant line)\n// Ensure that we have more than one item to avoid errors\nif (items.length > 1) {\n    return items.slice(1); // Return all items except the first one\n} else {\n    return items; // Return the original items if there's only one item\n}\n"
      },
      "notesInFlow": false,
      "typeVersion": 2
    },
    {
      "id": "5914197f-f217-447b-acab-b149f70b11ab",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        660,
        5.929829979644694
      ],
      "parameters": {
        "width": 269.9227895272578,
        "height": 412.7089638732373,
        "content": "### Code Explanation\n\nThis JavaScript code snippet is part of a data-processing workflow.\nThe code:\n\nGets all input data.\nChecks if there\u2019s more than one item.\nIf so, it removes the first item (usually a header) and returns the rest.\nIf not, it returns the original data as-is."
      },
      "typeVersion": 1
    },
    {
      "id": "c2d9e3a4-b9de-4b25-a06d-49d30402dab0",
      "name": "No Operation, do nothing",
      "type": "n8n-nodes-base.noOp",
      "position": [
        1540,
        280
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "8d65a94e-3946-4586-ad65-15f765f1b38c",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1500,
        80
      ],
      "parameters": {
        "width": 183.09709642798296,
        "height": 321.9023514071676,
        "content": "## Explanation \n\nEven though it exectutes correctly, the  Delete Node outputs an error of a missing item. therefore I put a \"Do nothing Node\""
      },
      "typeVersion": 1
    },
    {
      "id": "d2e0d8d2-f62a-4831-be0c-049d735c1fd5",
      "name": "Logs the update on sheet",
      "type": "n8n-nodes-base.microsoftExcel",
      "position": [
        -220,
        380
      ],
      "parameters": {
        "table": {
          "__rl": true,
          "mode": "list",
          "value": "{CE1FB867-1EB3-EE42-B7F5-3470275BDE2B}",
          "cachedResultUrl": "https://onedrive.live.com/edit.aspx?resid=2D96E50BD60B2B58!15370&activeCell=Portfolio!H1:H8",
          "cachedResultName": "Table4"
        },
        "options": {},
        "fieldsUi": {
          "values": [
            {
              "column": "Last updated",
              "fieldValue": "={{ new Date().toLocaleString('en-GB', { timeZone: 'Etc/GMT-1', hour12: false }) }}"
            }
          ]
        },
        "resource": "table",
        "workbook": {
          "__rl": true,
          "mode": "list",
          "value": "2D96E50BD60B2B58!15370",
          "cachedResultUrl": "https://1drv.ms/x/s!AFgrC9YL5ZYt-Ao",
          "cachedResultName": "My_investandearnings3"
        },
        "worksheet": {
          "__rl": true,
          "mode": "list",
          "value": "{08628863-6D0A-3B40-996C-B27E26CCFD8E}",
          "cachedResultUrl": "https://onedrive.live.com/edit.aspx?resid=2D96E50BD60B2B58!15370&activeCell=Portfolio!A1",
          "cachedResultName": "Portfolio"
        }
      },
      "credentials": {
        "microsoftExcelOAuth2Api": {
          "id": "YBKmpPrbgwZqZID4",
          "name": "Microsoft Excel account"
        }
      },
      "typeVersion": 2.1
    },
    {
      "id": "ff21f07d-7b6a-46cc-87db-2a3fdcd9614f",
      "name": "Gets the new file infos",
      "type": "n8n-nodes-base.microsoftOneDrive",
      "position": [
        -40,
        380
      ],
      "parameters": {
        "folderId": "2D96E50BD60B2B58%2115362",
        "resource": "folder"
      },
      "credentials": {
        "microsoftOneDriveOAuth2Api": {
          "id": "WbTC1RWEJEZv7psj",
          "name": "Microsoft Drive account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "7cfa40a4-f3c9-464f-83d4-1eea2a869c75",
      "name": "Downloads the new file",
      "type": "n8n-nodes-base.microsoftOneDrive",
      "position": [
        160,
        380
      ],
      "parameters": {
        "fileId": "={{ $json.id }}",
        "operation": "download"
      },
      "credentials": {
        "microsoftOneDriveOAuth2Api": {
          "id": "WbTC1RWEJEZv7psj",
          "name": "Microsoft Drive account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "e936a8ec-5544-4d13-9dca-747983ab7e50",
      "name": "Checks if it's CSV format",
      "type": "n8n-nodes-base.if",
      "position": [
        340,
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
              "id": "b4c5c8b8-7c02-435b-b9a8-8006ad173656",
              "operator": {
                "type": "string",
                "operation": "contains"
              },
              "leftValue": "={{ $json.name }}",
              "rightValue": "csv"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "f5b24101-4cb9-4a4a-be33-9b6191e20401",
      "name": "Prepares the fields to put in the excel table",
      "type": "n8n-nodes-base.set",
      "position": [
        940,
        260
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "5389492c-4352-451d-a4f2-73006a73f16b",
              "name": "Ticker/ISIN",
              "type": "string",
              "value": "={{ $json['Ticker/ISIN'] }}"
            },
            {
              "id": "df10d62b-8f55-45a9-bffb-b3c09b184111",
              "name": "Quantit\u00e9",
              "type": "number",
              "value": "={{ $json['Quantit\u00e9'] }}"
            },
            {
              "id": "ed70855d-2a24-4df9-86fd-c1dd3e26e774",
              "name": "Montant en EUR",
              "type": "number",
              "value": "={{ parseFloat($json[\"Montant en EUR\"].replace(\",\", \".\")) }}"
            },
            {
              "id": "02aa653e-d0e5-42d8-acdb-dd151c857f29",
              "name": "Produit",
              "type": "string",
              "value": "={{ $json.Produit }}"
            },
            {
              "id": "e75b1c9a-2807-4bb9-b080-1d97323b4d69",
              "name": "Cl\u00f4ture",
              "type": "number",
              "value": "={{ parseFloat($json[\"Cl\u00f4ture\"].replace(\",\", \".\")) }}"
            },
            {
              "id": "2cffba9a-64b5-497a-8b36-93c8705e389a",
              "name": "Devise",
              "type": "string",
              "value": "={{ $json.Devise }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "47793366-1655-4322-ba74-14a5b31b03e8",
      "name": "Updates the excel table",
      "type": "n8n-nodes-base.microsoftExcel",
      "position": [
        1120,
        260
      ],
      "parameters": {
        "options": {},
        "dataMode": "autoMap",
        "resource": "worksheet",
        "workbook": {
          "__rl": true,
          "mode": "list",
          "value": "2D96E50BD60B2B58!15370",
          "cachedResultUrl": "https://1drv.ms/x/s!AFgrC9YL5ZYt-Ao",
          "cachedResultName": "My_investandearnings3"
        },
        "operation": "upsert",
        "worksheet": {
          "__rl": true,
          "mode": "list",
          "value": "{08628863-6D0A-3B40-996C-B27E26CCFD8E}",
          "cachedResultUrl": "https://onedrive.live.com/edit.aspx?resid=2D96E50BD60B2B58!15370&activeCell=Portfolio!A1",
          "cachedResultName": "Portfolio"
        },
        "columnToMatchOn": "Ticker/ISIN"
      },
      "credentials": {
        "microsoftExcelOAuth2Api": {
          "id": "YBKmpPrbgwZqZID4",
          "name": "Microsoft Excel account"
        }
      },
      "typeVersion": 2.1
    }
  ],
  "pinData": {},
  "connections": {
    "Cleans the output": {
      "main": [
        [
          {
            "node": "Prepares the fields to put in the excel table",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Microsoft OneDrive2": {
      "main": [
        null,
        [
          {
            "node": "No Operation, do nothing",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Downloads the new file": {
      "main": [
        [
          {
            "node": "Checks if it's CSV format",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extracts data from csv": {
      "main": [
        [
          {
            "node": "Cleans the output",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Gets the new file infos": {
      "main": [
        [
          {
            "node": "Downloads the new file",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Updates the excel table": {
      "main": [
        [
          {
            "node": "Microsoft OneDrive2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Logs the update on sheet": {
      "main": [
        [
          {
            "node": "Gets the new file infos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Checks if it's CSV format": {
      "main": [
        [
          {
            "node": "Extracts data from csv",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Not CSV",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Triggers if new file in watched folder": {
      "main": [
        [
          {
            "node": "Logs the update on sheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Prepares the fields to put in the excel table": {
      "main": [
        [
          {
            "node": "Updates the excel table",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
