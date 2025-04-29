# 🦅 Get a bird's-eye view of your n8n instance with the Workflow Dashboard!

**[View Template](https://n8n.io/workflows/2269-/)**  **Published Date:** 05/17/2024  **Created By:** Eduard  **Categories:** `Development` `Core Nodes`  

## Template Description

Using n8n a lot?

Soar above the limitations of the default n8n dashboard! This template gives you an overview of your workflows, nodes, and tags – all in one place. 💪

Built using XML stylesheets and the Bootstrap 5 library, this workflow is self-contained and does not depend on any third-party software. 🙌 It generates a comprehensive overview JSON that can be easily integrated with other BI tools for further analysis and visualization. 📊

Reach out to Eduard if you need help adapting this workflow to your specific use-case!

🚀 Benefits:
Workflow Summary** 📈: Instant overview of your workflows, active counts, and triggers.
Left-Side Panel** 📋: Quick access to all your workflows, nodes, and tags for seamless navigation.
Workflow Details** 🔬: Deep dive into each workflow's nodes, timestamps, and tags.
Node Analysis** 🧩: Identify the most frequently used nodes across your workflows.
Tag Organization** 🗂️: Workflows are grouped according to their tags.
Visually Stunning** 🎨: Clean, intuitive, and easy-to-navigate dashboard design.
XML & Bootstrap 5** 🛠️: Built using XML stylesheets and Bootstrap 5, ensuring a self-contained and responsive dashboard.
No Dependencies** 🔒: The workflow does not rely on any third-party software. Bootstrap 5 files are loaded via CDN but can be delivered directly from your server.

⚠️ Important note for cloud users
Since the cloud version doesn't support environmental variables, please make the following changes:

get-nodes-via-jmespath node. Update the instance_url variable: enter your n8n URL instead of {{$env["N8N_PROTOCOL"]}}://{{$env["N8N_HOST"]}}
Create HTML node. Please provide the n8n instance URL instead of {{ $env.WEBHOOK_URL }}

🌟Example:

Check out our other workflows:
n8n.io/creators/eduard
n8n.io/creators/yulia

## Template JSON

```
{
  "id": "D0I76cew5KOnlem0",
  "meta": {
    "instanceId": "fb924c73af8f703905bc09c9ee8076f48c17b596ed05b18c0ff86915ef8a7c4a"
  },
  "name": "Workflow stats",
  "tags": [],
  "nodes": [
    {
      "id": "b1a73981-db6a-4fd2-9cad-d02bfecc7d3d",
      "name": "When clicking \"Test workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        1060,
        440
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "cbe2d1a8-51e9-4f3d-8ca5-321f3edf9a92",
      "name": "nodes-section",
      "type": "n8n-nodes-base.code",
      "position": [
        1900,
        500
      ],
      "parameters": {
        "jsCode": "// Initialize an empty object to hold the mapping between nodes and workflows\nconst nodeToWorkflowsMap = {};\n\n// Iterate over each workflow in the input\n$input.all().forEach(item => {\n  const { wf_stats } = item.json;\n  const { nodes_unique, wf_name, wf_url, wf_id } = wf_stats;\n\n  // For each unique node in the workflow, update the mapping\n  nodes_unique.forEach(node => {\n    if (!nodeToWorkflowsMap[node]) {\n      // If the node has not been added to the map, initialize it with the current workflow\n      nodeToWorkflowsMap[node] = [{ wf_name, wf_url, wf_id }];\n    } else {\n      // If the node is already in the map, append the current workflow to its list\n      nodeToWorkflowsMap[node].push({ wf_name, wf_url, wf_id });\n    }\n  });\n});\n\n// Convert the map into an array format suitable for n8n's output\nconst result = Object.keys(nodeToWorkflowsMap).map(node => ({\n  json: {\n    node,\n    count: nodeToWorkflowsMap[node].length,\n    workflows: nodeToWorkflowsMap[node]\n  }\n}));\n\nreturn result;"
      },
      "typeVersion": 2
    },
    {
      "id": "49a10bf3-f2e6-4fe9-8390-2a266f1b52a9",
      "name": "workflows-section",
      "type": "n8n-nodes-base.set",
      "position": [
        1680,
        340
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "fd4aa80c-cd88-4a97-b943-dfcf1ab222ee",
              "name": "wf_stats",
              "type": "object",
              "value": "={{ { nodes_unique     :[...new Set($json.nodes_array)],\n     nodes_count_total:$json.nodes_array.length,\n     nodes_count_uniq :[...new Set($json.nodes_array)].length,\n     wf_created       :DateTime.fromISO($json.createdAt).toFormat('yyyy-MM-dd HH:mm:ss'),\n     wf_updated       :DateTime.fromISO($json.updatedAt).toFormat('yyyy-MM-dd HH:mm:ss'),\n     wf_name          :$json.name,\n     wf_id            :`wf-${$json.id}`,\n     wf_url           :`${$json.instance_url}/workflow/${$json.id}` || \"\",\n     wf_active        :$json.active,\n     wf_trigcount     :$json.triggerCount,\n     wf_tags          :$json.tags_array\n} }}"
            }
          ]
        }
      },
      "typeVersion": 3.3
    },
    {
      "id": "afbbc6a0-dcb8-48e7-b2d1-ef00c769d3b7",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1240,
        -390.1630350920236
      ],
      "parameters": {
        "width": 1669.556429251995,
        "height": 1194.6716567919582,
        "content": "## Create the main JSON object with the workflow statistics\n* `globals` - general information (# of workflows, active workflows, total trigger count)\n* `wf_stats` - summary per workflow (number or nodes, unique nodes, list of nodes and tags)\n* `nodes-section` - summary per node (number of workflows that use a node and their URLs)\n* `tags-section` - summary per tag (number of workflows that use a node and their URLs)\n\n### You can use this JSON in BI tools to create a custom dashboard\n\n## Learn JS tips & tricks\n### Instead of just using one Code node, the workflow contains several nodes with useful advanced tricks.\n\n### JMESPath\n* Make a simple array of strings out of a complex array: `$jmespath($json,'nodes[*].type')`\n* Extract values based on condition: `$jmespath($input.all(),'[?json.wf_stats.wf_active == `true`]')`\n\n### Map and arrow functions\n* Perform operation on each array element: `.map(item => (item.split('.').pop().toUpperCase() ))`\n* Calculate sum of values from an array: `.reduce((accumulator, currentValue) => accumulator + currentValue, 0)`\n\n### Create an array with only unique values\n* `[...new Set($json.nodes_array)]`\n\n### Date-time conversions with the Luxon library:\n* `DateTime.fromISO($json.createdAt).toFormat('yyyy-MM-dd HH:mm:ss')`\n\n### Template literals (Template strings) for creating strings in JS\n* `wf-${$json.id}`"
      },
      "typeVersion": 1
    },
    {
      "id": "9dcb369b-fe22-45e1-906d-848a85b0c1e4",
      "name": "tags-section",
      "type": "n8n-nodes-base.code",
      "position": [
        1900,
        660
      ],
      "parameters": {
        "jsCode": "// Initialize an empty object to hold the mapping between nodes and workflows\nconst tagToWorkflowsMap = {};\n\n// Iterate over each workflow in the input\n$input.all().forEach(item => {\n  const { wf_stats } = item.json;\n  const { wf_tags, wf_name, wf_id } = wf_stats;\n\n  // Check if the workflow has tags\n  if (wf_tags.length > 0) {\n    // For each tag in the workflow, update the mapping\n    wf_tags.forEach(tag => {\n      if (!tagToWorkflowsMap[tag]) {\n        // If the tag has not been added to the map, initialize it with the current workflow\n        tagToWorkflowsMap[tag] = [{ wf_name, wf_id }];\n      } else {\n        // If the tag is already in the map, append the current workflow to its list\n        tagToWorkflowsMap[tag].push({ wf_name, wf_id });\n      }\n    });\n  } else {\n    // Handle workflows with no tags, categorizing them under a 'No Tags' category\n    const noTagKey = 'No Tags'; // or any other placeholder you prefer\n    if (!tagToWorkflowsMap[noTagKey]) {\n      tagToWorkflowsMap[noTagKey] = [{ wf_name, wf_id }];\n    } else {\n      tagToWorkflowsMap[noTagKey].push({ wf_name, wf_id });\n    }\n  }\n});\n\n// Convert the map into an array format suitable for n8n's output\nconst result = Object.keys(tagToWorkflowsMap).map(tag => ({\n  json: {\n    tag,\n    count    : tagToWorkflowsMap[tag].length,   \n    workflows: tagToWorkflowsMap[tag]\n  }\n}));\n\nreturn result;"
      },
      "typeVersion": 2
    },
    {
      "id": "7509c96c-0907-4cf1-94cf-f9dfbc0d3f9d",
      "name": "globals-section",
      "type": "n8n-nodes-base.set",
      "position": [
        1900,
        220
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "9e1284bd-73c5-4d3d-bb5d-3437fca97780",
              "name": "globals",
              "type": "object",
              "value": "={{ { global_total : $input.all().length,\n     global_active : $jmespath($input.all(),'[?json.wf_stats.wf_active == `true`]').length,\n     global_trigger: $jmespath($input.all(),'[].json.wf_stats.wf_trigcount').reduce((accumulator, currentValue) => accumulator + currentValue, 0) }  }}"
            }
          ]
        }
      },
      "executeOnce": true,
      "typeVersion": 3.3
    },
    {
      "id": "594e7b18-2244-48a9-9722-836b1ac47137",
      "name": "Merge",
      "type": "n8n-nodes-base.merge",
      "position": [
        2520,
        320
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combinationMode": "mergeByPosition"
      },
      "typeVersion": 2.1
    },
    {
      "id": "ef599477-a00c-403d-8a24-7431b09913e3",
      "name": "Merge1",
      "type": "n8n-nodes-base.merge",
      "position": [
        2520,
        520
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combinationMode": "mergeByPosition"
      },
      "typeVersion": 2.1
    },
    {
      "id": "2c0bc2dd-63d9-4b65-9e4e-2920892efaf7",
      "name": "Execute Workflow Trigger",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "position": [
        1060,
        240
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "8bceb3e9-e1d9-4ca0-af91-5377d4300346",
      "name": "Convert to XML",
      "type": "n8n-nodes-base.xml",
      "position": [
        1480,
        1180
      ],
      "parameters": {
        "mode": "jsonToxml",
        "options": {
          "headless": true
        }
      },
      "typeVersion": 1
    },
    {
      "id": "6151d4b8-f592-418d-b099-17c71b1de0e4",
      "name": "Create HTML",
      "type": "n8n-nodes-base.html",
      "position": [
        1680,
        1180
      ],
      "parameters": {
        "html": "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"{{ $env.WEBHOOK_URL }}webhook/73a91e4d-143d-4168-9efb-6c56f2258aec/dashboard.xsl\"?>\n\n{{ $json.data }}"
      },
      "typeVersion": 1
    },
    {
      "id": "e5ebc5c1-0fcc-4f9d-b8eb-df3a367cc097",
      "name": "Move Binary Data",
      "type": "n8n-nodes-base.moveBinaryData",
      "position": [
        1880,
        1180
      ],
      "parameters": {
        "mode": "jsonToBinary",
        "options": {
          "mimeType": "text/xml",
          "keepSource": false,
          "useRawData": true
        },
        "sourceKey": "html",
        "convertAllData": false
      },
      "typeVersion": 1
    },
    {
      "id": "5fdb74f7-6b2a-4042-91a2-c2088e8ea712",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        2080,
        1180
      ],
      "parameters": {
        "options": {
          "responseCode": 200,
          "responseHeaders": {
            "entries": [
              {
                "name": "Content-Type",
                "value": "text/xml"
              },
              {
                "name": "Control-Allow-Origin",
                "value": "*"
              }
            ]
          }
        },
        "respondWith": "binary"
      },
      "typeVersion": 1
    },
    {
      "id": "ed113e7c-c49f-4854-8fbf-5f7bf3591ede",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1000,
        1389
      ],
      "parameters": {
        "width": 809.0870333783894,
        "height": 425.91038036809823,
        "content": "## This webhook is needed to comply with the CORS policy of modern browsers.\n### It generates XML template and serves it using your n8n URL\n\nXSLT template is created with 2 Set nodes:\n1. `Template elements` node defines each section of the Dashboard\n2. `Final template` node puts everything together\n3. Bootstrap 5.3 styling is added. You can save the .css and .js files on your server. Right now a CDN version of the librarly is used."
      },
      "typeVersion": 1
    },
    {
      "id": "b6674f77-7797-4090-a4f9-56a9ddc0d4e0",
      "name": "Respond to Webhook2",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [
        1660,
        1660
      ],
      "parameters": {
        "options": {
          "responseCode": 200,
          "responseHeaders": {
            "entries": [
              {
                "name": "Content-Type",
                "value": "text/xsl"
              }
            ]
          }
        },
        "respondWith": "text",
        "responseBody": "={{ $json.xsl_template }}"
      },
      "typeVersion": 1
    },
    {
      "id": "c8c906da-0b61-46b0-be96-11da3c203e3f",
      "name": "Final template",
      "type": "n8n-nodes-base.set",
      "position": [
        1460,
        1660
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "2a42cfed-0451-41c2-9634-865cac2ea68d",
              "name": "xsl_template",
              "type": "string",
              "value": "=<xsl:stylesheet version=\"1.0\" xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\">\n  <xsl:template match=\"/\">\n    <html>\n      <head>\n        <title>n8n Workflows Dashboard</title>\n        <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH\" crossorigin=\"anonymous\" />\n        <script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz\" crossorigin=\"anonymous\"></script>\n        <style>\n          body {\n            position: relative;\n          }\n          \n          section {\n            scroll-margin-top: 20px;\n          }\n\n          .form-check-overlay {\n            position: absolute;\n            top: 0;\n            left: 0;\n            width: 100%;\n            height: 100%;\n            cursor: default;\n            z-index: 1;\n          }\n\n          .badge-link {\n            scroll-margin-top: 80px;\n          }\n\n          .sidebar {\n            position: fixed;\n            top: 0;\n            bottom: 0;\n            left: 0;\n            z-index: 100;\n            padding: 20px 0 0;\n            box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);\n            overflow-y: auto;\n          }\n\n          .sidebar-sticky {\n            position: relative;\n            top: 0;\n            height: calc(100vh - 20px);\n            overflow-x: hidden;\n            overflow-y: auto;\n            padding-left: .25rem;\n          }\n\n          .nooverflow {\n            overflow-x: hidden;\n          }\n\n          .sidebar .nav-link {\n            font-weight: 500;\n            color: var(--bs-gray-800);\n            white-space: nowrap;\n            overflow: hidden;\n            text-overflow: ellipsis;\n          }\n\n          .sidebar .nav-link.active {\n            color: var(--bs-primary);\n          }\n\n          .sidebar .btn {\n            padding: .25rem .5rem;\n            font-weight: 600;\n            color: var(--bs-gray-800);\n          }\n\n          .sidebar-a {\n            padding: .25rem .5rem;\n            margin-left: 1.25rem;\n            color: var(--bs-gray-800);\n            background-color: transparent;\n          }\n\n          .sidebar-bottom {\n            padding: .25rem .5rem;\n            margin-left: 1.25rem;\n          }\n\n          .btn-toggle::before {\n            width: 1.25em;\n            line-height: 0;\n            content: url(\"data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='rgba%280,0,0,.5%29' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M5 14l6-6-6-6'/%3e%3c/svg%3e\");\n            transition: transform .35s ease;\n            transform-origin: .5em 50%;\n          }\n\n          .btn-toggle[aria-expanded=\"true\"] {\n            color: var(--bs-gray-800);\n          }\n\n          .btn-toggle[aria-expanded=\"true\"]::before {\n            transform: rotate(90deg);\n          }\n\n          .btn-toggle-nav a {\n            padding: .1rem .5rem;\n            margin-top: .125rem;\n          }\n\n          .sidebar-a:hover,\n          .sidebar-a:focus,\n\t\t  .btn-toggle:hover,\n          .btn-toggle:focus {\n            background-color: var(--bs-primary-bg-subtle);\n          }\n\n          .content {\n            margin-left: 16.66%;\n            padding: 20px;\n          }\n\n          .card-img-container {\n            max-height: 150px;\n            overflow: hidden;\n            display: flex;\n            align-items: center;\n            justify-content: center;\n          }\n          \n          .card-img-top {\n            object-fit: cover;\n            object-position: top;\n            height: 100%;\n            width: 100%;\n          }\n\n        </style>\n      </head>\n      <body data-bs-spy=\"scroll\" data-bs-target=\"#sidebar\" data-bs-offset=\"10\">\n        <div class=\"container-fluid\">\n          <div class=\"row\">\n{{ $json.sidebar }}\n\n            <main class=\"col-10 content\">\n\n<!-- Overview section -->\n{{ $json.overview }}\n<!-- Workflows section -->\n{{ $json.workflows }}\n<!-- Nodes section -->\n{{ $json.nodes }}\n<!-- Tags section -->\n{{ $json.tags }}\n<!-- About section -->\n{{ $json.about }}\n\n            </main>\n          </div>\n        </div>\n      </body>\n    </html>\n  </xsl:template>\n</xsl:stylesheet>"
            }
          ]
        }
      },
      "typeVersion": 3.3
    },
    {
      "id": "173493c0-1f96-4416-a545-6d8c6034ac76",
      "name": "Template elements",
      "type": "n8n-nodes-base.set",
      "position": [
        1260,
        1660
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "afbcca70-2977-46a3-89c3-27a96f791d13",
              "name": "sidebar",
              "type": "string",
              "value": "=            <nav id=\"sidebar\" class=\"col-2 bg-light sidebar\">\n              <div class=\"sidebar-sticky\">\n                <ul class=\"list-unstyled ps-0\">\n                  <li class=\"mb-1\">\n                    <a href=\"#overview\" class=\"btn d-inline-flex align-items-center rounded border-0 sidebar-a\">Overview</a>\n                  </li>\n                  <li class=\"mb-1\">\n                    <button class=\"btn btn-toggle d-inline-flex align-items-center rounded border-0 collapsed\" data-bs-toggle=\"collapse\" data-bs-target=\"#workflows-collapse\" aria-expanded=\"false\">\n                      Workflows\n                    </button>\n                    <div class=\"collapse\" id=\"workflows-collapse\">\n                      <ul class=\"btn-toggle-nav list-unstyled fw-normal pb-1 small\">\n                        <xsl:for-each select=\"root/wf_stats\">\n                          <li><a href=\"#{wf_id}\" class=\"link-dark d-inline-flex text-decoration-none rounded sidebar-a\"><xsl:value-of select=\"wf_name\" /></a></li>\n                        </xsl:for-each>\n                      </ul>\n                    </div>\n                  </li>\n                  <li class=\"mb-1\">\n                    <button class=\"btn btn-toggle d-inline-flex align-items-center rounded border-0 collapsed\" data-bs-toggle=\"collapse\" data-bs-target=\"#nodes-collapse\" aria-expanded=\"false\">\n                      Nodes\n                    </button>\n                    <div class=\"collapse\" id=\"nodes-collapse\">\n                      <ul class=\"btn-toggle-nav list-unstyled fw-normal pb-1 small\">\n                        <xsl:for-each select=\"root/nodes-section\">\n                          <li><a href=\"#node-{node}\" class=\"link-dark d-inline-flex text-decoration-none rounded sidebar-a\"><xsl:value-of select=\"node\" /></a></li>\n                        </xsl:for-each>\n                      </ul>\n                    </div>\n                  </li>\n                  <li class=\"mb-1\">\n                    <button class=\"btn btn-toggle d-inline-flex align-items-center rounded border-0 collapsed\" data-bs-toggle=\"collapse\" data-bs-target=\"#tags-collapse\" aria-expanded=\"false\">\n                      Tags\n                    </button>\n                    <div class=\"collapse\" id=\"tags-collapse\">\n                      <ul class=\"btn-toggle-nav list-unstyled fw-normal pb-1 small\">\n                        <xsl:for-each select=\"root/tags-section\">\n                          <li><a href=\"#tag-{tag}\" class=\"link-dark d-inline-flex text-decoration-none rounded sidebar-a\"><xsl:value-of select=\"tag\" /></a></li>\n                        </xsl:for-each>\n                      </ul>\n                    </div>\n                  </li>\n                  <li class=\"border-top my-3\"></li>\n                  <li class=\"mb-1\">\n                    <a href=\"#about\" class=\"btn d-inline-flex align-items-center rounded border-0 sidebar-a\">About</a>\n                  </li>\n                </ul>\n                <div class=\"sidebar-bottom\">\n                  <p>n8n Dashboard ver 0.5<br/>\nContacts: <a class=\"link-offset-1 link-offset-1-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover\" href=\"https://www.linkedin.com/in/parsadanyan/\" target=\"_blank\">Eduard</a>, <a class=\"link-offset-1 link-offset-1-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover\" href=\"https://www.linkedin.com/in/yulia-dmitrievna-1112361b5/\" target=\"_blank\">Yulia</a></p>\n                </div>\n              </div>\n</nav>"
            },
            {
              "id": "d6dc34a7-3c79-44ef-957c-63aec4b2d75a",
              "name": "overview",
              "type": "string",
              "value": "=<section  id=\"overview\" class=\"container\">\n  <h1>n8n Workflow Dashboard</h1>\n</section>\n\n<section class=\"container mt-3\">\n  <h2>Overview</h2>\n  <div class=\"row\">\n    <div class=\"col-md-4\">\n      <div class=\"card bg-body-secondary mb-2 shadow-sm\">\n        <div class=\"card-body text-center\">\n          <h5 class=\"card-title\">Total Workflows</h5>\n          <p class=\"card-text display-4\">\ud83d\udcca <xsl:value-of select=\"root/globals/global_total\" /></p>\n        </div>\n      </div>\n    </div>\n    <div class=\"col-md-4\">\n      <div class=\"card bg-body-secondary mb-2 shadow-sm\">\n        <div class=\"card-body text-center\">\n          <h5 class=\"card-title\">Active Workflows</h5>\n          <p class=\"card-text display-4\">\u2705 <xsl:value-of select=\"root/globals/global_active\" /></p>\n        </div>\n      </div>\n    </div>\n    <div class=\"col-md-4\">\n      <div class=\"card bg-body-secondary mb-2 shadow-sm\">\n        <div class=\"card-body text-center\">\n          <h5 class=\"card-title\">Triggers Count</h5>\n          <p class=\"card-text display-4\">\u26a1 <xsl:value-of select=\"root/globals/global_trigger\" /></p>\n        </div>\n      </div>\n    </div>\n  </div>\n</section>"
            },
            {
              "id": "19ed123c-404b-4a68-a298-8f24c285f71c",
              "name": "workflows",
              "type": "string",
              "value": "=<section id=\"workflows\" class=\"container mt-3\">\n  <h2>Workflows</h2>\n  <xsl:for-each select=\"root/wf_stats\">\n    <div class=\"card mb-3 shadow-sm nooverflow\">\n      <div class=\"card-body\">\n        <div class=\"d-flex align-items-center mb-2\">\n          <div class=\"form-check form-switch me-3 position-relative\">\n            <input class=\"form-check-input\" type=\"checkbox\" role=\"switch\">\n              <xsl:attribute name=\"id\">\n                <xsl:value-of select=\"concat('switch-', wf_id)\" />\n              </xsl:attribute>\n              <xsl:if test=\"wf_active = 'true'\">\n                <xsl:attribute name=\"checked\">checked</xsl:attribute>\n              </xsl:if>\n            </input>\n            <label class=\"form-check-label\">\n              <xsl:attribute name=\"for\">\n                <xsl:value-of select=\"concat('switch-', wf_id)\" />\n              </xsl:attribute>\n            </label>\n            <div class=\"form-check-overlay\"></div>\n          </div>\n          <h5 class=\"card-title mb-0\">\n            <a class=\"link-offset-1 link-offset-1-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover\" href=\"{wf_url}\" target=\"_blank\" title=\"Open workflow in a new window\">\n              <xsl:attribute name=\"id\">\n                <xsl:value-of select=\"wf_id\" />\n              </xsl:attribute>\n              <xsl:value-of select=\"wf_name\" />\n            </a>\n          </h5>\n          <div class=\"ms-auto\">\n            <span class=\"badge bg-light font-monospace text-dark me-2\">\n              Updated At: <xsl:value-of select=\"wf_updated\" />\n            </span>\n            <span class=\"badge bg-light font-monospace text-dark me-2\">\n              Created At: <xsl:value-of select=\"wf_created\" />\n            </span>\n            <span class=\"badge bg-light font-monospace text-dark me-2\">\n              Nodes (Tot | Uniq | Trig): <xsl:value-of select=\"nodes_count_total\" /> | <xsl:value-of select=\"nodes_count_uniq\" /> | <xsl:value-of select=\"wf_trigcount\" />\n            </span>\n          </div>\n        </div>\n        <div class=\"row\">\n          <div class=\"d-flex\">\n            <div>\n              <xsl:for-each select=\"nodes_unique\">\n                <a href=\"#node-{.}\" title=\"Jump to this node\" class=\"badge-link\">\n                  <span class=\"badge bg-info-subtle border border-info-subtle text-info-emphasis rounded-pill me-2 mb-2\">\n                    <xsl:value-of select=\".\" />\n                  </span>\n                </a>\n              </xsl:for-each>\n            </div>\n            <xsl:if test=\"wf_tags\">\n              <div class=\"ms-auto\">\n                <xsl:for-each select=\"wf_tags\">\n                  <a href=\"#tag-{.}\" title=\"Jump to this tag\" class=\"badge-link\">\n                    <span class=\"badge bg-light-subtle border border-light-subtle text-light-emphasis rounded-pill me-2 mb-2\">\n                      <xsl:value-of select=\".\" />\n                    </span>\n                  </a>\n                </xsl:for-each>\n              </div>\n            </xsl:if>\n          </div>\n        </div>\n      </div>\n    </div>\n  </xsl:for-each>\n</section>"
            },
            {
              "id": "9869134d-ee39-49a2-a978-eb3adaac482d",
              "name": "nodes",
              "type": "string",
              "value": "=<section id=\"nodes\" class=\"container mt-3\">\n  <h2>Nodes</h2>\n  <div class=\"accordion\" id=\"nodesAccordion\">\n    <xsl:for-each select=\"root/nodes-section\">\n      <div class=\"accordion-item shadow-sm\">\n        <h3 class=\"accordion-header\">\n          <button class=\"accordion-button collapsed\" type=\"button\" data-bs-toggle=\"collapse\">\n            <xsl:attribute name=\"data-bs-target\">\n              <xsl:value-of select=\"concat('#collapse-', position())\" />\n            </xsl:attribute>\n            <xsl:attribute name=\"aria-controls\">\n              <xsl:value-of select=\"concat('collapse-', position())\" />\n            </xsl:attribute>\n            <a>\n              <xsl:attribute name=\"id\">\n                <xsl:value-of select=\"concat('node-', node)\" />\n              </xsl:attribute>\n              <xsl:value-of select=\"node\" /> <span class=\"badge bg-info-subtle text-info-emphasis rounded-pill ms-2\"><xsl:value-of select=\"count\" /></span>\n            </a>\n          </button>\n        </h3>\n        <div class=\"accordion-collapse collapse\">\n          <xsl:attribute name=\"id\">\n            <xsl:value-of select=\"concat('collapse-', position())\" />\n          </xsl:attribute>\n          <xsl:attribute name=\"aria-labelledby\">\n            <xsl:value-of select=\"concat('heading-', position())\" />\n          </xsl:attribute>\n          <div class=\"accordion-body\">\n            <xsl:for-each select=\"workflows\">\n              <span class=\"badge bg-info-subtle border border-info-subtle text-info-emphasis rounded-pill me-2 mb-2\">\n                <a href=\"#{wf_id}\" class=\"text-primary-emphasis text-decoration-none me-1 section-offset\" title=\"Jump to workflow details\">\n                  <xsl:value-of select=\"wf_name\" />\n                </a>\n                <a href=\"{wf_url}\" target=\"_blank\" class=\"text-primary-emphasis text-decoration-none\" title=\"Open workflow in a new window\">\n                  \ud83d\udd17\n                </a>\n              </span>\n            </xsl:for-each>\n          </div>\n        </div>\n      </div>\n    </xsl:for-each>\n  </div>\n</section>"
            },
            {
              "id": "f09bc0d1-017e-44f5-bc39-6bdfeffe22ec",
              "name": "tags",
              "type": "string",
              "value": "=<section id=\"tags\" class=\"container mt-3\">\n  <h2>Tags</h2>\n  <div class=\"accordion\" id=\"tagsAccordion\">\n    <xsl:for-each select=\"root/tags-section\">\n      <div class=\"accordion-item shadow-sm\">\n        <h3 class=\"accordion-header\">\n          <button class=\"accordion-button collapsed\" type=\"button\" data-bs-toggle=\"collapse\">\n            <xsl:attribute name=\"data-bs-target\">\n              <xsl:value-of select=\"concat('#collapse-tag-', position())\" />\n            </xsl:attribute>\n            <xsl:attribute name=\"aria-controls\">\n              <xsl:value-of select=\"concat('collapse-tag-', position())\" />\n            </xsl:attribute>\n            <a>\n              <xsl:attribute name=\"id\">\n                <xsl:value-of select=\"concat('tag-', tag)\" />\n              </xsl:attribute>\n              <xsl:value-of select=\"tag\" /> <span class=\"badge bg-light-subtle text-light-emphasis rounded-pill ms-2\"><xsl:value-of select=\"count\" /></span>\n            </a>\n          </button>\n        </h3>\n        <div class=\"accordion-collapse collapse\">\n          <xsl:attribute name=\"id\">\n            <xsl:value-of select=\"concat('collapse-tag-', position())\" />\n          </xsl:attribute>\n          <xsl:attribute name=\"aria-labelledby\">\n            <xsl:value-of select=\"concat('heading-tag-', position())\" />\n          </xsl:attribute>\n          <div class=\"accordion-body\">\n            <xsl:for-each select=\"workflows\">\n              <span class=\"badge bg-light-subtle border border-light-subtle text-light-emphasis rounded-pill me-2 mb-2\">\n                <a href=\"#{wf_id}\" class=\"text-primary-emphasis text-decoration-none me-1 section-offset\" title=\"Jump to workflow details\">\n                  <xsl:value-of select=\"wf_name\" />\n                </a>\n                <a href=\"{wf_url}\" target=\"_blank\" class=\"text-primary-emphasis text-decoration-none\" title=\"Open workflow in a new window\">\n                  \ud83d\udd17\n                </a>\n              </span>\n            </xsl:for-each>\n          </div>\n        </div>\n      </div>\n    </xsl:for-each>\n  </div>\n</section>"
            },
            {
              "id": "2af68003-c9b9-4e60-8836-195da026ad2f",
              "name": "about",
              "type": "string",
              "value": "=<hr class=\"featurette-divider border-dark\" />\n<section id=\"about\" class=\"container mt-3\">\n  <h2 class=\"text-center mb-5\">About</h2>\n  <div class=\"row\">\n\n    <div class=\"col-lg-3 text-center\">\n      <img src=\"https://gravatar.com/avatar/a551e67c6fe7affd5f882a527dee154bb6c3ac90cf878326accb3fb3ec77c8a6?r=pg&amp;d=retro&amp;size=200\" alt=\"Eduard\" class=\"rounded-circle mb-3\" width=\"140\" height=\"140\" />\n      <h3 class=\"fw-normal\">Eduard</h3>\n      <p><a class=\"btn btn-warning\" href=\"https://n8n.io/creators/eduard/\" target=\"_blank\">More templates</a></p>\n      <p><a class=\"btn btn-outline-primary\" href=\"https://www.linkedin.com/in/parsadanyan/\" target=\"_blank\">LinkedIn</a></p>\n    </div>\n\n    <div class=\"col-lg-3 text-center\">\n      <img src=\"https://gravatar.com/avatar/d29a8262aa8835d430919f8002957a77169f8da987dee0740aa494ae67a061b7?r=pg&amp;d=retro&amp;size=200\" alt=\"Yulia\" class=\"rounded-circle mb-3\" width=\"140\" height=\"140\" />\n      <h3 class=\"fw-normal\">Yulia</h3>\n      <p><a class=\"btn btn-warning\" href=\"https://n8n.io/creators/yulia/\" target=\"_blank\">More templates</a></p>\n      <p><a class=\"btn btn-outline-primary\" href=\"https://www.linkedin.com/in/yulia-dmitrievna-1112361b5/\" target=\"_blank\">LinkedIn</a></p>\n    </div>\n\n<div class=\"col-lg-6 text-center\">\n  <div class=\"card shadow-sm mb-3\">\n    <div class=\"card-img-container\">\n      <img src=\"https://blog.n8n.io/content/images/size/w800/2023/09/gg.png\" class=\"card-img-top\" alt=\"How to work with XML and SQL using n8n\" />\n    </div>\n    <div class=\"card-body\">\n      <h5 class=\"card-title\">Read the article to find out more!</h5>\n      <p class=\"card-text\">This dashboard was created using XML template language (XSLT) in n8n.</p>\n      <a href=\"https://blog.n8n.io/sql-xml/#how-to-deliver-the-xml-file\" class=\"btn btn-primary\" target=\"_blank\">Read Article</a>\n    </div>\n  </div>\n</div>\n\n  </div>\n</section>"
            }
          ]
        }
      },
      "typeVersion": 3.3
    },
    {
      "id": "3555218e-8df2-4ae8-9482-2c8ec99798c0",
      "name": "Sort-workflows",
      "type": "n8n-nodes-base.sort",
      "position": [
        2080,
        340
      ],
      "parameters": {
        "options": {},
        "sortFieldsUi": {
          "sortField": [
            {
              "order": "descending",
              "fieldName": "wf_stats.wf_updated"
            },
            {
              "fieldName": "wf_stats.wf_name"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "2d893970-825e-4842-811f-7e7a24dd3bac",
      "name": "Sort-nodes",
      "type": "n8n-nodes-base.sort",
      "position": [
        2080,
        500
      ],
      "parameters": {
        "options": {},
        "sortFieldsUi": {
          "sortField": [
            {
              "order": "descending",
              "fieldName": "count"
            },
            {
              "fieldName": "node"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "c197f00e-d147-45af-b121-a70d28912a7f",
      "name": "Sort-tags",
      "type": "n8n-nodes-base.sort",
      "position": [
        2080,
        660
      ],
      "parameters": {
        "options": {},
        "sortFieldsUi": {
          "sortField": [
            {
              "order": "descending",
              "fieldName": "count"
            },
            {
              "fieldName": "tag"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "4f28a9f6-b67e-42d8-8843-480803932c27",
      "name": "Aggregate-workflows",
      "type": "n8n-nodes-base.aggregate",
      "position": [
        2260,
        340
      ],
      "parameters": {
        "options": {},
        "fieldsToAggregate": {
          "fieldToAggregate": [
            {
              "fieldToAggregate": "wf_stats"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "id": "f4521a5c-8cc3-4831-90e2-1a1fda06fdac",
      "name": "Aggregate-nodes",
      "type": "n8n-nodes-base.aggregate",
      "position": [
        2260,
        500
      ],
      "parameters": {
        "options": {},
        "aggregate": "aggregateAllItemData",
        "destinationFieldName": "nodes-section"
      },
      "typeVersion": 1
    },
    {
      "id": "ae5040f7-4ae3-41e7-9afc-ebb625d303e7",
      "name": "Aggregate-tags",
      "type": "n8n-nodes-base.aggregate",
      "position": [
        2260,
        660
      ],
      "parameters": {
        "options": {},
        "aggregate": "aggregateAllItemData",
        "destinationFieldName": "tags-section"
      },
      "typeVersion": 1
    },
    {
      "id": "138d2a7a-8628-474c-9307-508bc5ddc629",
      "name": "Final-json",
      "type": "n8n-nodes-base.merge",
      "position": [
        2740,
        420
      ],
      "parameters": {
        "mode": "combine",
        "options": {},
        "combinationMode": "mergeByPosition"
      },
      "typeVersion": 2.1
    },
    {
      "id": "69a22d56-3b4e-4d5d-b351-3c787f23e9c9",
      "name": "n8n-get-workflows",
      "type": "n8n-nodes-base.n8n",
      "position": [
        1260,
        340
      ],
      "parameters": {
        "filters": {}
      },
      "credentials": {
        "n8nApi": {
          "id": "45",
          "name": "n8n account 4"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "35564537-0053-4cdb-a05d-153ad4825393",
      "name": "Prepare JSON object",
      "type": "n8n-nodes-base.executeWorkflow",
      "position": [
        1260,
        1180
      ],
      "parameters": {
        "options": {},
        "workflowId": "={{ $workflow.id }}"
      },
      "typeVersion": 1
    },
    {
      "id": "9fd045f1-7126-4611-b26d-c45139429c6b",
      "name": "get-nodes-via-jmespath",
      "type": "n8n-nodes-base.set",
      "position": [
        1460,
        340
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "51f83719-066f-4231-a418-ba64a3b5b831",
              "name": "nodes_array",
              "type": "array",
              "value": "={{$jmespath($json,'nodes[*].type').map(item => (item.split('.').pop().toUpperCase() ))}}"
            },
            {
              "id": "bbc40849-66a7-4583-8c2c-ac590be59e38",
              "name": "tags_array",
              "type": "array",
              "value": "={{$jmespath($json,'tags[*].name')}}"
            },
            {
              "id": "08064cc3-f34e-4f05-9975-726378fe63ae",
              "name": "instance_url",
              "type": "string",
              "value": "={{$env[\"N8N_PROTOCOL\"]}}://{{$env[\"N8N_HOST\"]}}"
            }
          ]
        },
        "includeOtherFields": true
      },
      "typeVersion": 3.3
    },
    {
      "id": "45723a66-03be-4be7-ae4a-978adb5b7e7b",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        960,
        855.3819018404909
      ],
      "parameters": {
        "color": 6,
        "width": 1301.92628220859,
        "height": 1000.0640426993867,
        "content": "## Additional section to create a standalone dashboard via XLM templates\n### This section is not required if you only need a JSON\n\n### *IMPORTANT!*\n### This webhook is not protected. Everyone who knows the URL endpoint can get access to the Dashboard. Please consider adding authentication.\n\n1. `Request HTML dashboard` node runs that main section of the workflow\n2. It converts the JSON into an XML structure\n3. A final HTML page is created with the link to an XML stylesheet (this stylesheet controls the look of the dashboard)\n4. The resulting page is returned via `Respond to Webhook` node"
      },
      "typeVersion": 1
    },
    {
      "id": "b17fbec5-03e2-4836-8704-6b31cdf92a5b",
      "name": "Request HTML dashboard",
      "type": "n8n-nodes-base.webhook",
      "position": [
        1060,
        1180
      ],
      "webhookId": "fb550a01-12f2-4709-ba2d-f71197b68340",
      "parameters": {
        "path": "fb550a01-12f2-4709-ba2d-f71197b68340",
        "options": {},
        "responseMode": "responseNode"
      },
      "typeVersion": 2
    },
    {
      "id": "70fd1bbb-24e2-4fde-b054-6319120a7ac4",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        880,
        600
      ],
      "parameters": {
        "color": 3,
        "width": 663.915516288839,
        "height": 251.8866653838499,
        "content": "## IMPORTANT NOTE FOR CLOUD USERS\n### Since the cloud version doesn't support environmental variables, please make the following changes:\n\n1. **get-nodes-via-jmespath** node. Update the `instance_url` variable: enter your n8n URL instead of `{{$env[\"N8N_PROTOCOL\"]}}://{{$env[\"N8N_HOST\"]}}`\n2. **Create HTML** node. Please provide the n8n instance URL instead of `{{ $env.WEBHOOK_URL }}`"
      },
      "typeVersion": 1
    },
    {
      "id": "36288776-5f67-40fd-872f-0eeac0dd03b0",
      "name": "Request xsl template",
      "type": "n8n-nodes-base.webhook",
      "position": [
        1060,
        1660
      ],
      "webhookId": "73a91e4d-143d-4168-9efb-6c56f2258aec",
      "parameters": {
        "path": "73a91e4d-143d-4168-9efb-6c56f2258aec/dashboard.xsl",
        "options": {},
        "responseMode": "responseNode"
      },
      "typeVersion": 2
    }
  ],
  "active": true,
  "pinData": {},
  "settings": {
    "callerPolicy": "workflowsFromSameOwner",
    "executionOrder": "v1",
    "saveManualExecutions": true,
    "saveDataSuccessExecution": "all"
  },
  "versionId": "8f939c01-0b5d-4363-80bc-8a355865360f",
  "connections": {
    "Merge": {
      "main": [
        [
          {
            "node": "Final-json",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Merge1": {
      "main": [
        [
          {
            "node": "Final-json",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Sort-tags": {
      "main": [
        [
          {
            "node": "Aggregate-tags",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Sort-nodes": {
      "main": [
        [
          {
            "node": "Aggregate-nodes",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create HTML": {
      "main": [
        [
          {
            "node": "Move Binary Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "tags-section": {
      "main": [
        [
          {
            "node": "Sort-tags",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "nodes-section": {
      "main": [
        [
          {
            "node": "Sort-nodes",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Aggregate-tags": {
      "main": [
        [
          {
            "node": "Merge1",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Convert to XML": {
      "main": [
        [
          {
            "node": "Create HTML",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Final template": {
      "main": [
        [
          {
            "node": "Respond to Webhook2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Sort-workflows": {
      "main": [
        [
          {
            "node": "Aggregate-workflows",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Aggregate-nodes": {
      "main": [
        [
          {
            "node": "Merge1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "globals-section": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Move Binary Data": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Template elements": {
      "main": [
        [
          {
            "node": "Final template",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "n8n-get-workflows": {
      "main": [
        [
          {
            "node": "get-nodes-via-jmespath",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "workflows-section": {
      "main": [
        [
          {
            "node": "nodes-section",
            "type": "main",
            "index": 0
          },
          {
            "node": "tags-section",
            "type": "main",
            "index": 0
          },
          {
            "node": "globals-section",
            "type": "main",
            "index": 0
          },
          {
            "node": "Sort-workflows",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Aggregate-workflows": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Prepare JSON object": {
      "main": [
        [
          {
            "node": "Convert to XML",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Request xsl template": {
      "main": [
        [
          {
            "node": "Template elements",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Request HTML dashboard": {
      "main": [
        [
          {
            "node": "Prepare JSON object",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "get-nodes-via-jmespath": {
      "main": [
        [
          {
            "node": "workflows-section",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Execute Workflow Trigger": {
      "main": [
        [
          {
            "node": "n8n-get-workflows",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When clicking \"Test workflow\"": {
      "main": [
        [
          {
            "node": "n8n-get-workflows",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
