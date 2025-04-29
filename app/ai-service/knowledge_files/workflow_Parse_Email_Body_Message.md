# Parse Email Body Message

**[View Template](https://n8n.io/workflows/1453-/)**  **Published Date:** 02/16/2022  **Created By:** Miquel Colomer  **Categories:**   

## Template Description

Who we are

We are Aprende n8n, the first n8n Spanish course for all n8n lovers.
If you want to learn more, you can find out more at Aprende n8n.

Task goal

This task allows extracting data from any email body with a NoCode snippet.

An small explanation

You receive an email when a user submits a form from your website.

All those emails usually have the same structure as the next one:
Name: Miquel
Email: miquel@aprenden8n.com
Subject: Welcome aboard
Message: Hi Miquel!

Thank you for your signup!


This task allows to parse any email body and assign all values to the defined labels, getting an output like this:
{
"Name": "Miquel",
"Email": "miquel@aprenden8n.com",
"Subject": "Welcome aboard",
"Message" "Hi Miquel! Thank you for your signup!"
}

After importing it

When you import the import, you get the next task in your n8n:


We recommend importing this workflow into your current task and adapting it.
You define a couple of variables in the "Set values" SET:
body: the email body you want to parse. You can add this as an expression from previous variables.
labels: the keywords you want to detect and parse. Labels are case insensitive.

We define the next values:

Body
Name: Miquel
Email: miquel@aprenden8n.com
Subject: Welcome aboard
Message: Hi Miquel!

Thank you for your signup!
Labels
Name,Email,Subject,Message

A screenshot of the Set output is the next one


If we check the "Function item" Node, we get the next content after executing the task:

Capabilities

The task has the next features:
You can detect as many labels as you want.
Label detection is case insensitive.
You can use the snippet as an independent workflow to call it generically, adding the Function item to the workflow and passing body and labels as paremeters.

Limitations

This task has limitations:
The parser only accepts the multiline values at the end of the email. 

Help and comments

If you have any doubt about this snippet, please, contact us at miquel@aprenden8n.com.

You can contact us at Aprende n8n or in the Spanish n8n community


## Template JSON

```
{
  "id": "340",
  "name": "Email body parser by aprenden8n.com",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        300
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Email Parser Snippet",
      "type": "n8n-nodes-base.functionItem",
      "position": [
        670,
        300
      ],
      "parameters": {
        "functionCode": "var obj = {};\nvar labels = item.labels.split(\",\");\nitem.labels.split(\",\").forEach(function(label) {\n  var re = labels.indexOf(label) === labels.length - 1 ? \"\\\\b\" + label + \"\\\\b[: ]+([^$]+)\" : \"\\\\b\" + label + \"\\\\b[: ]+([^\\\\n$]+)\";\n  var found = item.body.match(new RegExp(re, \"i\"));\n  if (found && found.length > 1) {\n    obj[label] = found[1].trim();\n  }\n});\n\nreturn obj;"
      },
      "typeVersion": 1
    },
    {
      "name": "Set values",
      "type": "n8n-nodes-base.set",
      "position": [
        460,
        300
      ],
      "parameters": {
        "values": {
          "number": [],
          "string": [
            {
              "name": "body",
              "value": "Name: Miquel\nEmail: miquel@aprenden8n.com\nSubject: Welcome aboard\nMessage: Hi Miquel!\n\nThank you for your signup!"
            },
            {
              "name": "labels",
              "value": "Name,Email,Subject,Message"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {
    "Set values": {
      "main": [
        [
          {
            "node": "Email Parser Snippet",
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
            "node": "Set values",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
