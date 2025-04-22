# Add the affiliate to a program automatically

**[View Template](https://n8n.io/workflows/936-/)**  **Published Date:** 02/12/2021  **Created By:** ghagrawal17  **Categories:** `Sales`  

## Template Description

This workflow allows you to create an affiliate, add metadata, and add the affiliate to a program.



Tapfiliate node: This node allows you to create a new affiliate in Tapfiliate.

Tapfiliate1 node: This node allows you add metadata to the affiliate that you created previously. Based on your use-case, you may or may not require this node.

Tapfiliate2 node: This node allows you to add the affiliate that you created previously to a program. 

Based on your use-case, you might want to replace the Start node with a trigger node that gets you the information of an affiliate.

## Template JSON

```
{
  "nodes": [
    {
      "name": "Tapfiliate2",
      "type": "n8n-nodes-base.tapfiliate",
      "position": [
        870,
        300
      ],
      "parameters": {
        "resource": "programAffiliate",
        "programId": "testing-program-5",
        "affiliateId": "={{$node[\"Tapfiliate\"].json[\"id\"]}}",
        "additionalFields": {}
      },
      "credentials": {
        "tapfiliateApi": "Tapfiliate API credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Tapfiliate1",
      "type": "n8n-nodes-base.tapfiliate",
      "position": [
        670,
        300
      ],
      "parameters": {
        "resource": "affiliateMetadata",
        "metadataUi": {
          "metadataValues": [
            {
              "key": "tag",
              "value": "n8n"
            }
          ]
        },
        "affiliateId": "={{$json[\"id\"]}}"
      },
      "credentials": {
        "tapfiliateApi": "Tapfiliate API credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "Tapfiliate",
      "type": "n8n-nodes-base.tapfiliate",
      "position": [
        470,
        300
      ],
      "parameters": {
        "email": "n8ndocsburner@gmail.com",
        "lastname": "Ryan",
        "firstname": "Jack",
        "additionalFields": {}
      },
      "credentials": {
        "tapfiliateApi": "Tapfiliate API credentials"
      },
      "typeVersion": 1
    },
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        270,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    }
  ],
  "connections": {
    "Tapfiliate": {
      "main": [
        [
          {
            "node": "Tapfiliate1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Tapfiliate1": {
      "main": [
        [
          {
            "node": "Tapfiliate2",
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
            "node": "Tapfiliate",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
