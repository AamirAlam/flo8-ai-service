# Get local datetime into Function node using moment.js

**[View Template](https://n8n.io/workflows/695-/)**  **Published Date:** 10/01/2020  **Created By:** Trey  **Categories:**   

## Template Description



A quick example showing how to get the local date and time into a Function node using moment.js.

This relies on the GENERIC_TIMEZONE environment variable being correctly configured (see the docs here)

NOTE: In order for this to work, you must whitelist the moment library for use by setting the following environment variable:

NODE_FUNCTION_ALLOW_EXTERNAL=moment

For convenience, the Function code is as follows:

const moment = require('moment');

let date = moment().tz($env['GENERIC_TIMEZONE']);

let year = date.year();
let month = date.month(); // zero-indexed!
let day = date.date();
let hour = date.hours();
let minute = date.minutes();
let second = date.seconds();
let millisecond = date.millisecond();
let formatted = date.format('YYYY-MM-DD HH:mm:ss.SSS Z');

return [
  {
    json: {
      utc: date,
      year: year,
      month: month, // zero-indexed!
      day: day,
      hour: hour,
      minute: minute,
      second: second,
      millisecond: millisecond,
      formatted: formatted
    }
  }
];
`

## Template JSON

```
{
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
      "name": "Get Local Datetime",
      "type": "n8n-nodes-base.function",
      "position": [
        450,
        300
      ],
      "parameters": {
        "functionCode": "const moment = require('moment');\n\nlet date = moment().tz($env['GENERIC_TIMEZONE']);\n\nlet year = date.year();\nlet month = date.month(); // zero-indexed!\nlet day = date.date();\nlet hour = date.hours();\nlet minute = date.minutes();\nlet second = date.seconds();\nlet millisecond = date.millisecond();\nlet formatted = date.format('YYYY-MM-DD HH:mm:ss.SSS Z');\n\nreturn [\n  {\n    json: {\n      utc: date,\n      year: year,\n      month: month, // zero-indexed!\n      day: day,\n      hour: hour,\n      minute: minute,\n      second: second,\n      millisecond: millisecond,\n      formatted: formatted\n    }\n  }\n];\n"
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On clicking 'execute'": {
      "main": [
        [
          {
            "node": "Get Local Datetime",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
