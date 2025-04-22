# Discover company data by name with uProc

**[View Template](https://n8n.io/workflows/860-/)**  **Published Date:** 12/30/2020  **Created By:** Miquel Colomer  **Categories:** `Data & Storage`  

## Template Description

Do you want to discover company-related information to enrich a signup process?

This workflow enriches any company by name using the uProc Get Company by Name tool.
This tool combines Google Maps and emails research on the internet to return results. You get no results if the company has no presence on Google Maps. 



You need to add your credentials (Email and API Key - real -) located at Integration section to n8n.

You can replace node "Create Company Item" with any other supported service returning Company names and countries, like Hubspot, Google Sheets, MySQL, or Typeform.

You can set up the uProc node with several parameters:
country: the country name you want to use.
name: the name of the company you need to locate.

Every "uProc" node returns the next fields per every located company:
name: Contains the company's given name.
email: Contains the company's given email.
cif: Contains company's cif number.
address: Contains company's formatted address.
city: Contains the city location of the company.
state: Contains province location of the company.
county: Contains state location of the company
country: Contains country location of the company
zipcode: Contains zipcode code of the company
phone: Contains phone number of the company
website: Contains website of the company
latitude: Contains latitude of the company
longitude: Contains longitude of the company
 
Next, you can save results to a CRM or Google Sheets, and prepare returned email or phone to launch an email or telemarketing campaign.

## Template JSON

```
{
  "id": "112",
  "name": "Get Company by Name",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        440,
        510
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Create Company Item",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        640,
        510
      ],
      "parameters": {
        "functionCode": "item.company = \"Killia technologies\";\nitem.country = \"Spain\";\n\nreturn item;"
      },
      "typeVersion": 1
    },
    {
      "name": "Get Company by Name",
      "type": "n8n-nodes-base.uproc",
      "position": [
        850,
        510
      ],
      "parameters": {
        "name": "={{$node[\"Create Company Item\"].json[\"company\"]}}",
        "tool": "getCompanyByName",
        "group": "company",
        "country": "={{$node[\"Create Company Item\"].json[\"country\"]}}",
        "additionalOptions": {}
      },
      "credentials": {
        "uprocApi": "miquel-uproc"
      },
      "typeVersion": 1
    },
    {
      "name": "Company Found?",
      "type": "n8n-nodes-base.if",
      "position": [
        1050,
        510
      ],
      "parameters": {
        "conditions": {
          "number": [],
          "string": [
            {
              "value1": "={{$node[\"Get Company by Name\"].json[\"message\"][\"name\"]}}",
              "value2": ".+",
              "operation": "regex"
            }
          ]
        }
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Create Company Item": {
      "main": [
        [
          {
            "node": "Get Company by Name",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Company by Name": {
      "main": [
        [
          {
            "node": "Company Found?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Create Company Item",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
