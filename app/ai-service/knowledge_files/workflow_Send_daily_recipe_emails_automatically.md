# Send daily recipe emails automatically 

**[View Template](https://n8n.io/workflows/856-/)**  **Published Date:** 12/28/2020  **Created By:** jason  **Categories:** `Communication` `Core Nodes` `HITL` `Development`  

## Template Description

Not sure what to eat tonight? Have recipes emailed to you daily based on your criterial.

To run this workflow, you will need to have:
A Recipe Search API key from Edamam
An active email account with configured credentials

To set up your credentials:
Set your Edamam AppID and AppKey in the Search Criteria node
Select (or create) your email credentials in the Send Recipes node (and set up the to: and from: email addresses while you are at it)

To customize the recipes that you receive, open up the Search Criteria node and modify one or more of the following:
RecipeCount** - the numner of recipes you would like to receive
IngredientCount** - the maximum number of ingredients you would like each recipe to have
CaloriesMin** - the minimum number of calories the recipe will have
CaloriesMax** - the maximum number of calories the recipe will have
TimeMin** - the minimum amount of time (in minutes) the recipe will take to prepare
TimeMax** - the maximum amount of time (in minutes) the recipe will take to prepare
Diet** - Select one of the following options:
	balanced - Protein/Fat/Carb values in 15/35/50 ratio
	high-fiber - More than 5g fiber per serving
	high-protein - More than 50% of total calories from proteins
	low-carb - Less than 20% of total calories from carbs
	low-fat - Less than 15% of total calories from fat
	low-sodium - Less than 140mg Na per serving
	random - selects a different random diet each day
Health** - Select one of the following options:
	alcohol-free - No alcohol used or contained
	immuno-supportive - Recipes which fit a science-based approach to eating to strengthen the immune system
	celery-free - does not contain celery or derivatives
	crustacean-free - does not contain crustaceans (shrimp, lobster etc.) or derivatives
	dairy-free - No dairy; no lactose
	egg-free - No eggs or products containing eggs
	fish-free - No fish or fish derivatives
	fodmap-free - Does not contain FODMAP foods
	gluten-free - No ingredients containing gluten
	keto-friendly - Maximum 7 grams of net carbs per serving
	kidney-friendly - per serving – phosphorus less than 250 mg AND potassium less than 500 mg AND sodium: less than 500 mg
	kosher - contains only ingredients allowed by the kosher diet. However it does not guarantee kosher preparation of the ingredients themselves
	low-potassium - Less than 150mg per serving
	lupine-free - does not contain lupine or derivatives
	mustard-free - does not contain mustard or derivatives
	low-fat-abs - Less than 3g of fat per serving
	no-oil-added - No oil added except to what is contained in the basic ingredients
	low-sugar - No simple sugars – glucose, dextrose, galactose, fructose, sucrose, lactose, maltose
	paleo - Excludes what are perceived to be agricultural products; grains, legumes, dairy products, potatoes, refined salt, refined sugar, and processed oils
	peanut-free - No peanuts or products containing peanuts
	pecatarian - Does not contain meat or meat based products, can contain dairy and fish
	pork-free - does not contain pork or derivatives
	red-meat-free - does not contain beef, lamb, pork, duck, goose, game, horse, and other types of red meat or products containing red meat.
	sesame-free - does not contain sesame seed or derivatives
	shellfish-free - No shellfish or shellfish derivatives
	soy-free - No soy or products containing soy
	sugar-conscious - Less than 4g of sugar per serving
	tree-nut-free - No tree nuts or products containing tree nuts
	vegan - No meat, poultry, fish, dairy, eggs or honey
	vegetarian - No meat, poultry, or fish
	wheat-free - No wheat, can have gluten though
	random - selects a different random health option each day
SearchItem* - the general term that you are looking for e.g. *chicken



## Template JSON

```
{
  "id": "11",
  "name": "What To Eat",
  "nodes": [
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        100,
        400
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 10
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Search Criteria",
      "type": "n8n-nodes-base.set",
      "position": [
        300,
        400
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "RecipeCount",
              "value": 3
            },
            {
              "name": "IngredientCount",
              "value": 5
            },
            {
              "name": "CaloriesMin"
            },
            {
              "name": "CaloriesMax",
              "value": 1500
            },
            {
              "name": "TimeMin"
            },
            {
              "name": "TimeMax",
              "value": 30
            }
          ],
          "string": [
            {
              "name": "Diet",
              "value": "balanced"
            },
            {
              "name": "Health",
              "value": "random"
            },
            {
              "name": "SearchItem",
              "value": "chicken"
            },
            {
              "name": "AppID",
              "value": "Enter Your Edamam AppID Here"
            },
            {
              "name": "AppKey",
              "value": "Enter Your Edamam AppKey Here"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 1
    },
    {
      "name": "Set Query Values",
      "type": "n8n-nodes-base.function",
      "position": [
        500,
        400
      ],
      "parameters": {
        "functionCode": "items[0].json.calories = items[0].json.CaloriesMin + \"-\" + items[0].json.CaloriesMax;\nitems[0].json.time = items[0].json.TimeMin + \"-\" + items[0].json.TimeMax;\n\nif (items[0].json.Diet.toUpperCase() == \"RANDOM\") {\n  arrDiet = [\"balanced\",\"high-fiber\",\"high-protein\",\"low-carb\",\"low-fat\",\"low-sodium\"];\n  intRandomNumber = Math.floor(Math.random() * 6);\n  items[0].json.Diet = arrDiet[intRandomNumber];\n}\n\nif (items[0].json.Health.toUpperCase() == \"RANDOM\") {\n  arrHealth = [\"alcohol-free\",\"immuno-supportive\",\"celery-free\",\"crustacean-free\",\"dairy-free\",\"egg-free\",\"fish-free\",\"fodmap-free\",\"gluten-free\",\"keto-friendly\",\"kidney-friendly\",\"kosher\",\"low-potassium\",\"lupine-free\",\"mustard-free\",\"low-fat-abs\",\"no-oil-added\",\"low-sugar\",\"paleo\",\"peanut-free\",\"pecatarian\",\"pork-free\",\"red-meat-free\",\"sesame-free\",\"shellfish-free\",\"soy-free\",\"sugar-conscious\",\"tree-nut-free\",\"vegan\",\"vegetarian\",\"wheat-free\"];\n  intRandomNumber = Math.floor(Math.random() * 31);\n  items[0].json.Health = arrHealth[intRandomNumber];\n}\n\nreturn items;"
      },
      "typeVersion": 1
    },
    {
      "name": "Set Recipe ID Values",
      "type": "n8n-nodes-base.function",
      "position": [
        1080,
        400
      ],
      "parameters": {
        "functionCode": "items[0].json.from = Math.floor(Math.random() * items[0].json.RecipeCount) + 1;\nitems[0].json.to = items[0].json.from + items[0].json.ReturnCount;\n\nreturn items;"
      },
      "typeVersion": 1
    },
    {
      "name": "Retrieve Recipe Counts",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        700,
        400
      ],
      "parameters": {
        "url": "https://api.edamam.com/search",
        "options": {},
        "queryParametersUi": {
          "parameter": [
            {
              "name": "q",
              "value": "={{$node[\"Set Query Values\"].json[\"SearchItem\"]}}"
            },
            {
              "name": "app_id",
              "value": "={{$node[\"Set Query Values\"].json[\"AppID\"]}}"
            },
            {
              "name": "app_key",
              "value": "={{$node[\"Set Query Values\"].json[\"AppKey\"]}}"
            },
            {
              "name": "ingr",
              "value": "={{$node[\"Set Query Values\"].json[\"IngredientCount\"]}}"
            },
            {
              "name": "diet",
              "value": "={{$node[\"Set Query Values\"].json[\"Diet\"]}}"
            },
            {
              "name": "calories",
              "value": "={{$node[\"Set Query Values\"].json[\"calories\"]}}"
            },
            {
              "name": "time",
              "value": "={{$node[\"Set Query Values\"].json[\"time\"]}}"
            },
            {
              "name": "from",
              "value": "1"
            },
            {
              "name": "to",
              "value": "2"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Retrieve Recipes",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1260,
        400
      ],
      "parameters": {
        "url": "https://api.edamam.com/search",
        "options": {},
        "queryParametersUi": {
          "parameter": [
            {
              "name": "q",
              "value": "={{$node[\"Search Criteria\"].json[\"SearchItem\"]}}"
            },
            {
              "name": "app_id",
              "value": "={{$node[\"Search Criteria\"].json[\"AppID\"]}}"
            },
            {
              "name": "app_key",
              "value": "={{$node[\"Search Criteria\"].json[\"AppKey\"]}}"
            },
            {
              "name": "from",
              "value": "={{$node[\"Set Recipe ID Values\"].json[\"from\"]}}"
            },
            {
              "name": "to",
              "value": "={{$node[\"Set Recipe ID Values\"].json[\"to\"]}}"
            },
            {
              "name": "ingr",
              "value": "={{$node[\"Search Criteria\"].json[\"IngredientCount\"]}}"
            },
            {
              "name": "diet",
              "value": "={{$node[\"Search Criteria\"].json[\"Diet\"]}}"
            },
            {
              "name": "calories",
              "value": "={{$node[\"Set Query Values\"].json[\"calories\"]}}"
            },
            {
              "name": "time",
              "value": "={{$node[\"Set Query Values\"].json[\"time\"]}}"
            }
          ]
        }
      },
      "typeVersion": 1
    },
    {
      "name": "Set Counts",
      "type": "n8n-nodes-base.set",
      "position": [
        880,
        400
      ],
      "parameters": {
        "values": {
          "number": [
            {
              "name": "RecipeCount",
              "value": "={{$node[\"Retrieve Recipe Counts\"].json[\"count\"]}}"
            },
            {
              "name": "ReturnCount",
              "value": "={{$node[\"Search Criteria\"].json[\"RecipeCount\"]}}"
            }
          ]
        },
        "options": {},
        "keepOnlySet": true
      },
      "typeVersion": 1
    },
    {
      "name": "Send Recipes",
      "type": "n8n-nodes-base.emailSend",
      "position": [
        1660,
        400
      ],
      "parameters": {
        "html": "={{$node[\"Create Email Body in HTML\"].json[\"emailBody\"]}}",
        "options": {},
        "subject": "={{$node[\"Set Query Values\"].json[\"RecipeCount\"]}} {{$node[\"Set Query Values\"].json[\"Diet\"]}}, {{$node[\"Set Query Values\"].json[\"Health\"]}} {{$node[\"Set Query Values\"].json[\"SearchItem\"]}} recipes under {{$node[\"Set Query Values\"].json[\"CaloriesMax\"]}} calories ready in under {{$node[\"Set Query Values\"].json[\"TimeMax\"]}} minutes",
        "toEmail": "Enter Your Email Address Here",
        "fromEmail": "Enter Your Email Address Here"
      },
      "credentials": {
        "smtp": "Gmail Creds"
      },
      "typeVersion": 1
    },
    {
      "name": "Create Email Body in HTML",
      "type": "n8n-nodes-base.function",
      "position": [
        1460,
        400
      ],
      "parameters": {
        "functionCode": "arrRecipes = items[0].json.hits;\nitems[0].json = {};\n\nstrEmailBody = \"Here are your recipes for today:<br><ul>\";\n\narrRecipes.forEach(createHTML);\n\nfunction createHTML(value, index, array) {\n  strEmailBody = strEmailBody + \"<li><a href=\\\"\"+ value.recipe.shareAs + \"\\\">\" + value.recipe.label + \"</a></li>\";\n}\n\nstrEmailBody = strEmailBody + \"</ul>\";\n\nitems[0].json.emailBody = strEmailBody\n\nreturn items;"
      },
      "typeVersion": 1
    }
  ],
  "active": true,
  "settings": {},
  "connections": {
    "Cron": {
      "main": [
        [
          {
            "node": "Search Criteria",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Counts": {
      "main": [
        [
          {
            "node": "Set Recipe ID Values",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Search Criteria": {
      "main": [
        [
          {
            "node": "Set Query Values",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Retrieve Recipes": {
      "main": [
        [
          {
            "node": "Create Email Body in HTML",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Query Values": {
      "main": [
        [
          {
            "node": "Retrieve Recipe Counts",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Recipe ID Values": {
      "main": [
        [
          {
            "node": "Retrieve Recipes",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Retrieve Recipe Counts": {
      "main": [
        [
          {
            "node": "Set Counts",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create Email Body in HTML": {
      "main": [
        [
          {
            "node": "Send Recipes",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
