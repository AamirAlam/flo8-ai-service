# Save email attachments to Nextcloud

**[View Template](https://n8n.io/workflows/1344-/)**  **Published Date:** 11/29/2021  **Created By:** Manu  **Categories:** `Data & Storage`  

## Template Description

This workflow will take all emails you put into a certain folder, upload any attachements to Nextcloud, and mark the emails as read (configurable).

Attachements will be saved with automatically generated filenames:
2021-01-01_From-Sender-Name_Filename-of-attachement.pdf

Instructions:
Allow lodash to be used in n8n (or rewrite the code...)
  NODE_FUNCTION_ALLOW_EXTERNAL=lodash (environment variable)
Import workflow
Set credentials for Email & Nextcloud nodes
Configure to use correct folder / custom filters
Activate

Custom filter examples:
Only unread emails:
  Custom Email Config = ["UNSEEN"]
Filter emails by 'to' address:
  Custom Email Config = [["TO", "example+invoices@posteo.de"]]

## Template JSON

```
{
  "nodes": [
    {
      "name": "IMAP Email",
      "type": "n8n-nodes-base.emailReadImap",
      "position": [
        240,
        420
      ],
      "parameters": {
        "format": "resolved",
        "mailbox": "Invoices",
        "options": {
          "customEmailConfig": "[\"ALL\"]"
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Nextcloud",
      "type": "n8n-nodes-base.nextCloud",
      "position": [
        940,
        420
      ],
      "parameters": {
        "path": "=Documents/Invoices/{{$json[\"date\"]}}_{{$json[\"from\"]}}_{{$binary.file.fileName}}",
        "binaryDataUpload": true,
        "binaryPropertyName": "file"
      },
      "typeVersion": 1
    },
    {
      "name": "Map each attachment",
      "type": "n8n-nodes-base.function",
      "position": [
        620,
        420
      ],
      "parameters": {
        "functionCode": "const _ = require('lodash')\n\nconst sanitize = str => _.chain(str)\n  .replace(/[^A-Za-z0-9&.-]/g, '-') // sanitise via whitelist of characters\n  .replace(/-(?=-)/g, '') // remove repeated dashes - https://regexr.com/6ag8h\n  .trim('-') // trim any leading/trailing dashes\n  .truncate({\n    length: 60,\n    omission: '-' // when the string ends with '-', you'll know it was truncated\n  })\n  .value()\n\nconst result = _.flatMap(items.map(item => {\n  //console.log({item})\n\n  // Maps each attachment to a separate item\n  return _.values(item.binary).map(file => {\n    console.log(\"Saving attachement:\", file.fileName, 'from:', ...item.json.from.value)\n    \n    // sanitize filename but exclude extension\n    const filename_parts = file.fileName.split('.')\n    const ext = _.slice(filename_parts, filename_parts.length-1)\n    const filename_main = _.join(_.dropRight(filename_parts), '.')\n    file.fileName = sanitize(filename_main) + '.' + ext\n    \n    return {\n      json: {\n        from: sanitize(item.json.from.value[0].name),\n        date: sanitize(new Date(item.json.date).toISOString().split(\"T\")[0]) // get date part \"2020-01-01\"\n      }, \n      binary: { file }\n    }\n  })\n}))\n\n//console.log(result)\nreturn result"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "IMAP Email": {
      "main": [
        [
          {
            "node": "Map each attachment",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Map each attachment": {
      "main": [
        [
          {
            "node": "Nextcloud",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
