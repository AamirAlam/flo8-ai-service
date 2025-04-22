# Git backup of workflows and credentials

**[View Template](https://n8n.io/workflows/1053-/)**  **Published Date:** 04/22/2021  **Created By:** Allan Daemon  **Categories:**   

## Template Description

This creates a git backup of the workflows and credentials.

It uses the n8n export command with git diff, so you can run as many times as you want, but only when there are changes they will create a commit.

Setup
You need some access to the server.

Create a repository in some remote place to host your project, like Github, Gitlab, or your favorite private repo.

Clone the repository in the server in a place that the n8n has access. In the example, it's the ., and the repository name is repo. Change it in the commands and in the workflow commands (you can set it as a variable in the wokflow). Checkout to another branch if you won't use the master one.

cd .
git clone repository

Or you could git init and then add the remote (git remote add origin YOUR_REPO_URL), whatever pleases you more.

As the server, check if everything is ok for beeing able to commit. Very likely you'll need to setup the user email and name. Try to create a commit, and push it to upstream, and everything you need (like config a user to comit) will appear in way. I strong suggest testing with exporting the commands to garantee it will work too.

cd ./repo

git commit -c "Initial commmit" --allow-empty

-u is the same as --set-upstream

git push -u origin master 

Testing to push to upstream with the first exported data

npx n8n export:workflow --backup --output ./repo/workflows/
npx n8n export:credentials --backup --output repo/credentials/

cd ./repo
git add .
git commit -c "manual backup: first export"
git push

After that, if everything is ok, the workflow should work just fine.

Adjustments

Adjust the path in used in the workflow. See the the git -C PATH command is the same as cd PATH; git ....

Also, adjust the cron to run as you need. As I said in the beginning, you can run it even for every minute, but it will create commits only when there are changes.

Credentials encryption

The default for exporting the credentials is to do them encrypted. You can add the flag --decrypted to the n8n export:credentials command if you need to save them in plain. But as general rule, it's better to save the encryption key, that you only need to do that once, and them export it safely encrypted.

## Template JSON

```
{
  "id": "15",
  "name": "Tools / Backup Gitlab",
  "nodes": [
    {
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        250,
        400
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "name": "Export Workflows",
      "type": "n8n-nodes-base.executeCommand",
      "position": [
        450,
        300
      ],
      "parameters": {
        "command": "npx n8n export:workflow --backup --output repo/workflows/"
      },
      "typeVersion": 1
    },
    {
      "name": "Export Credentials",
      "type": "n8n-nodes-base.executeCommand",
      "position": [
        600,
        300
      ],
      "parameters": {
        "command": "npx n8n export:credentials --backup --output repo/credentials/"
      },
      "typeVersion": 1
    },
    {
      "name": "git add",
      "type": "n8n-nodes-base.executeCommand",
      "position": [
        750,
        300
      ],
      "parameters": {
        "command": "git -C repo add ."
      },
      "typeVersion": 1
    },
    {
      "name": "git commit",
      "type": "n8n-nodes-base.executeCommand",
      "position": [
        900,
        300
      ],
      "parameters": {
        "command": "=git -C repo commit -m \"Auto backup ({{ new Date().toISOString() }})\""
      },
      "typeVersion": 1
    },
    {
      "name": "git push",
      "type": "n8n-nodes-base.executeCommand",
      "position": [
        1050,
        300
      ],
      "parameters": {
        "command": "git -C repo push"
      },
      "typeVersion": 1
    },
    {
      "name": "Cron",
      "type": "n8n-nodes-base.cron",
      "position": [
        250,
        200
      ],
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 0
            },
            {
              "hour": 12
            },
            {
              "hour": 6
            },
            {
              "hour": 18
            }
          ]
        }
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
            "node": "Export Workflows",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "git add": {
      "main": [
        [
          {
            "node": "git commit",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "git commit": {
      "main": [
        [
          {
            "node": "git push",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Export Workflows": {
      "main": [
        [
          {
            "node": "Export Credentials",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Export Credentials": {
      "main": [
        [
          {
            "node": "git add",
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
            "node": "Export Workflows",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
