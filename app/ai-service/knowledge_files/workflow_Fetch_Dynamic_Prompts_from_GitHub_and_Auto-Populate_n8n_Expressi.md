# Fetch Dynamic Prompts from GitHub and Auto-Populate n8n Expressions in Prompt

**[View Template](https://n8n.io/workflows/2893-/)**  **Published Date:** 02/12/2025  **Created By:** RealSimple Solutions  **Categories:** `Development` `Core Nodes` `AI` `Langchain`  

## Template Description

Who Is This For?

This workflow is designed for AI engineers, automation specialists, and content creators who need a scalable system to dynamically manage prompts stored in GitHub. It eliminates manual updates, enforces required variable checks, and ensures that AI interactions always receive fully processed prompts.

🚀 What Problem Does This Solve?

Manually managing AI prompts can be inefficient and error-prone. This workflow:  
✅ Fetches dynamic prompts from GitHub  
✅ Auto-populates placeholders with values from the setVars node  
✅ Ensures all required variables are present before execution  
✅ Processes the formatted prompt through an AI agent

🛠 How This Workflow Works

This workflow consists of three key branches, ensuring smooth prompt retrieval, variable validation, and AI processing.

1️⃣ Retrieve the Prompt from GitHub (HTTP Request → Extract from File → SetPrompt)

The workflow starts manually or via an external trigger.
It fetches a text-based prompt stored in a GitHub repository.
The Extract from File Node retrieves the content from the GitHub file.
The SetPrompt Node stores the prompt, making it accessible for processing.

📌 Note:  
The prompt must contain n8n expression format variables (e.g., {{ $json.company }}) so they can be dynamically replaced.

2️⃣ Extract & Auto-Populate Variables (Check All Prompt Vars → Replace Variables)

A Code Node scans the prompt for placeholders in the n8n expression format ({{ $json.variableName }}).
The workflow compares required variables against the setVars node:
    ✅ If all variables are present, it proceeds to variable replacement.
    ❌ If any variables are missing, the workflow stops and returns an error listing them.
The Replace Variables Node replaces all placeholders with values from setVars.

📌 Example of a properly formatted GitHub prompt:

Hello {{ $json.company }}, your product {{ $json.features }} launches on {{ $json.launch_date }}.

This ensures seamless replacement when processed in n8n.

3️⃣ AI Processing & Output (AI Agent → Prompt Output)

The Set Completed Prompt Node stores the final, processed prompt.
The AI Agent Node (Ollama Chat Model) processes the prompt.
The Prompt Output Node returns the fully formatted response.

📌 Optional: Modify this to use OpenAI, Claude, or other AI models.

⚠️ Error Handling: Missing Variables

If a required variable is missing, the workflow stops execution and provides an error message:

⚠️ Missing Required Variables: ["launch_date"]

This ensures no incomplete prompts are sent to AI agents.

✅ Example Use Case

📜 GitHub Prompt File (Using n8n Expressions)

Hello {{ $json.company }}, your product {{ $json.features }} launches on {{ $json.launch_date }}.

🔹 Variables in setVars Node

{
  "company": "PropTechPro",
  "features": "AI-powered Property Management",
  "launch_date": "March 15, 2025"
}

✅ Successful Output

Hello PropTechPro, your product AI-powered Property Management launches on March 15, 2025.

🚨 Error Output (If Missing launch_date)

⚠️ Missing Required Variables: ["launch_date"]

🔧 Setup Instructions

1️⃣ Connect Your GitHub Repository

Store your prompt in a public or private GitHub repo.
The workflow will fetch the raw file using the GitHub API.

2️⃣ Configure the SetVars Node

Define the required variables in the SetVars Node.
Make sure the variable names match those used in the prompt.

3️⃣ Test & Run

Click Test Workflow to execute.
If variables are missing, it will show an error.
If everything is correct, it will output the fully formatted prompt.

⚡ How to Customize This Workflow

💡 Need CRM or Database Integration?

Connect the setVars node to an Airtable, Google Sheets, or HubSpot API to pull variables dynamically.

💡 Want to Modify the AI Model?

Replace the Ollama Chat Model with OpenAI, Claude, or a custom LLM endpoint.

📌 Why Use This Workflow?

✅ No Manual Updates Required – Fetches prompts dynamically from GitHub.  
✅ Prevents Broken Prompts – Ensures required variables exist before execution.  
✅ Works for Any Use Case – Handles AI chat prompts, marketing messages, and chatbot scripts.  
✅ Compatible with All n8n Deployments – Works on Cloud, Self-Hosted, and Desktop versions.

## Template JSON

```
{
  "id": "QyMyf3zraY0wxXDf",
  "meta": {
    "instanceId": "ba3fa76a571c35110ef5f67e5099c9a5c1768ef125c2f3b804ba20de75248c0b",
    "templateCredsSetupCompleted": true
  },
  "name": "Load Prompts from Github Repo and auto populate n8n expressions",
  "tags": [],
  "nodes": [
    {
      "id": "34781446-b06e-41eb-83b8-b96bda1a5595",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -80,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "c53b7243-7c82-47e0-a5ee-bd82bc51c386",
      "name": "GitHub",
      "type": "n8n-nodes-base.github",
      "position": [
        600,
        0
      ],
      "parameters": {
        "owner": {
          "__rl": true,
          "mode": "name",
          "value": "={{ $json.Account }}"
        },
        "filePath": "={{ $json.path }}{{ $json.prompt }}",
        "resource": "file",
        "operation": "get",
        "repository": {
          "__rl": true,
          "mode": "name",
          "value": "={{ $json.repo }}"
        },
        "additionalParameters": {}
      },
      "credentials": {
        "githubApi": {
          "id": "ostHZNoe8GSsbaQM",
          "name": "The GitHub account"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "9976b199-b744-47a7-9d75-4b831274c01b",
      "name": "Extract from File",
      "type": "n8n-nodes-base.extractFromFile",
      "position": [
        840,
        0
      ],
      "parameters": {
        "options": {},
        "operation": "text"
      },
      "typeVersion": 1
    },
    {
      "id": "26aa4e6a-c487-4cdf-91d5-df660cf826a6",
      "name": "setVars",
      "type": "n8n-nodes-base.set",
      "position": [
        180,
        0
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "150618c5-09b1-4f8b-a7b4-984662bf3381",
              "name": "Account",
              "type": "string",
              "value": "TPGLLC-US"
            },
            {
              "id": "22e8a3b0-bd53-485c-b971-7f1dd0686f0e",
              "name": "repo",
              "type": "string",
              "value": "PeresPrompts"
            },
            {
              "id": "ab94d0a1-ef3a-4fe9-9076-6882c6fda0ac",
              "name": "path",
              "type": "string",
              "value": "SEO/"
            },
            {
              "id": "66f122eb-1cbd-4769-aac8-3f05cdb6c116",
              "name": "prompt",
              "type": "string",
              "value": "keyword_research.md"
            },
            {
              "id": "03fe26a3-04e6-439c-abcb-d438fc5203c0",
              "name": "company",
              "type": "string",
              "value": "South Nassau Physical Therapy"
            },
            {
              "id": "c133d216-a457-4872-a060-0ba4d94549af",
              "name": "product",
              "type": "string",
              "value": "Manual Therapy"
            },
            {
              "id": "584864dd-2518-45e2-b501-02828757fc3a",
              "name": "features",
              "type": "string",
              "value": "pain relief"
            },
            {
              "id": "0c4594cc-302a-4215-bdad-12cf54f57967",
              "name": "sector",
              "type": "string",
              "value": "physical therapy"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "9d92f581-8cd9-448c-aa1d-023a96c1ddda",
      "name": "replace variables",
      "type": "n8n-nodes-base.code",
      "position": [
        1900,
        -20
      ],
      "parameters": {
        "jsCode": "// Fetch the prompt text\nconst prompt = $('SetPrompt').first().json.data;  // Ensure the prompt contains placeholders like {{ some.node.value }}\n\n// Example variables object\nconst variables = {\n  company: $('setVars').first().json.company,\n  features: \"Awesome Software\",\n  keyword: \"2025-02-07\"\n};\n\n// Function to replace placeholders dynamically\nconst replaceVariables = (text, vars) => {\n  return text.replace(/{{(.*?)}}/g, (match, key) => {\n    const trimmedKey = key.trim();\n    \n    // Extract last part after the last dot\n    const finalKey = trimmedKey.split('.').pop();\n\n    // Replace if key exists, otherwise leave placeholder unchanged\n    return vars.hasOwnProperty(finalKey) ? vars[finalKey] : match;\n  });\n};\n\n// Replace and return result\nreturn [{\n  prompt: replaceVariables(prompt, variables)\n}];\n"
      },
      "typeVersion": 2
    },
    {
      "id": "6c6c4fde-6ee5-47a8-894d-44d1afcedc2a",
      "name": "If",
      "type": "n8n-nodes-base.if",
      "position": [
        1560,
        0
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
              "id": "2717a7e5-095a-42bf-8b5b-8050c3389ec5",
              "operator": {
                "type": "boolean",
                "operation": "true",
                "singleValue": true
              },
              "leftValue": "={{ $json.success }}",
              "rightValue": "={{ $('Check All Prompt Vars Present').item.json.keys()}}"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "3b7712b8-5152-4f60-9401-03c89c39e227",
      "name": "Check All Prompt Vars Present",
      "type": "n8n-nodes-base.code",
      "position": [
        1280,
        0
      ],
      "parameters": {
        "jsCode": "// Get prompt text\nconst prompt = $json.data;\n\n// Extract variables inside {{ }} dynamically\nconst matches = [...prompt.matchAll(/{{(.*?)}}/g)];\nconst uniqueVars = [...new Set(matches.map(match => match[1].trim().split('.').pop()))];\n\n// Get variables from the Set Node\nconst setNodeVariables = $node[\"setVars\"].json || {};\n\n// Log extracted variables and Set Node keys\nconsole.log(\"Extracted Variables:\", uniqueVars);\nconsole.log(\"Set Node Keys:\", Object.keys(setNodeVariables));\n\n// Check if all required variables are present in the Set Node\nconst missingKeys = uniqueVars.filter(varName => !setNodeVariables.hasOwnProperty(varName));\n\nconsole.log(\"Missing Keys:\", missingKeys);\n\n// Return false if any required variable is missing, otherwise return true\nreturn [{\n  success: missingKeys.length === 0,\n  missingKeys: missingKeys\n}];\n"
      },
      "typeVersion": 2
    },
    {
      "id": "32618e10-3285-4c16-9e78-058dde329337",
      "name": "SetPrompt",
      "type": "n8n-nodes-base.set",
      "position": [
        1060,
        0
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "335b450d-542a-4714-83d8-ccc237188fc5",
              "name": "data",
              "type": "string",
              "value": "={{ $json.data }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "4d8b34ca-50dd-4f37-b4f7-542291461662",
      "name": "Stop and Error",
      "type": "n8n-nodes-base.stopAndError",
      "position": [
        1900,
        200
      ],
      "parameters": {
        "errorMessage": "=Missing Prompt Variables : {{ $('Check All Prompt Vars Present').item.json.missingKeys }}\n"
      },
      "typeVersion": 1
    },
    {
      "id": "a78c1e17-9152-4241-bcdf-c0d723da543b",
      "name": "Set Completed Prompt",
      "type": "n8n-nodes-base.set",
      "position": [
        2220,
        -20
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "57a9625b-adea-4ee7-a72a-2be8db15f3d4",
              "name": "Prompt",
              "type": "string",
              "value": "={{ $json.prompt }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "51447c90-a222-4172-a49b-86ec43332559",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        2440,
        -20
      ],
      "parameters": {
        "text": "={{ $json.Prompt }}",
        "options": {},
        "promptType": "define"
      },
      "typeVersion": 1.7
    },
    {
      "id": "f15b6af1-7af2-4515-be8f-960211118dce",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        60,
        -120
      ],
      "parameters": {
        "width": 340,
        "height": 260,
        "content": "# Set The variables in your prompt here"
      },
      "typeVersion": 1
    },
    {
      "id": "163db6cc-5b06-4ae6-ac97-5890b37cdb18",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        520,
        -120
      ],
      "parameters": {
        "color": 5,
        "content": "## The repo is currently public for you to test with"
      },
      "typeVersion": 1
    },
    {
      "id": "83ff6a86-a759-42a9-ace4-e20d57b906db",
      "name": "Sticky Note2",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        1780,
        -200
      ],
      "parameters": {
        "width": 360,
        "height": 260,
        "content": "## Replaces the values in the prompt with the variables in the \n# 'setVars' Node"
      },
      "typeVersion": 1
    },
    {
      "id": "7dd61153-84ac-4b59-b449-333825476c33",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        2000,
        180
      ],
      "parameters": {
        "color": 3,
        "content": "## If you're missing variables they will be listed here"
      },
      "typeVersion": 1
    },
    {
      "id": "1f070dc3-3d25-41d8-b534-912ba7c8b2b0",
      "name": "Prompt Output",
      "type": "n8n-nodes-base.set",
      "position": [
        2800,
        -20
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "01a30683-c348-4712-a3b1-739fc4a17718",
              "name": "promptResponse",
              "type": "string",
              "value": "={{ $json.output }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "2d12a6e2-7976-41b0-8cb2-01466b28269d",
      "name": "Ollama Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOllama",
      "position": [
        2480,
        200
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "ollamaApi": {
          "id": "ERfZ8mAfQ1b0aoxZ",
          "name": "Ollama account"
        }
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "4327a337-59e7-4b5b-98e8-93c6be550972",
  "connections": {
    "If": {
      "main": [
        [
          {
            "node": "replace variables",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Stop and Error",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "GitHub": {
      "main": [
        [
          {
            "node": "Extract from File",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "setVars": {
      "main": [
        [
          {
            "node": "GitHub",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Agent": {
      "main": [
        [
          {
            "node": "Prompt Output",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "SetPrompt": {
      "main": [
        [
          {
            "node": "Check All Prompt Vars Present",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract from File": {
      "main": [
        [
          {
            "node": "SetPrompt",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Ollama Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "replace variables": {
      "main": [
        [
          {
            "node": "Set Completed Prompt",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Completed Prompt": {
      "main": [
        [
          {
            "node": "AI Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check All Prompt Vars Present": {
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
            "node": "setVars",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
