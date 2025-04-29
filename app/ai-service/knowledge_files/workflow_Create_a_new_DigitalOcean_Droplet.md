# Create a new DigitalOcean Droplet

**[View Template](https://n8n.io/workflows/435-/)**  **Published Date:** 06/29/2020  **Created By:** amudhan  **Categories:** `Development` `Core Nodes`  

## Template Description

Uses a DigitalOcean Personal Access Token to create a new Droplet.

Add your personal access token and change the parameters to create droplets of different sizes.

You can also specify more options; refer the API docs

## Template JSON

```
{
  "nodes": [
    {
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        450,
        300
      ],
      "parameters": {
        "url": "https://api.digitalocean.com/v2/droplets",
        "options": {
          "bodyContentType": "json"
        },
        "requestMethod": "POST",
        "bodyParametersUi": {
          "parameter": [
            {
              "name": "name",
              "value": "API-creation-test"
            },
            {
              "name": "region",
              "value": "blr1"
            },
            {
              "name": "size",
              "value": "s-1vcpu-1gb"
            },
            {
              "name": "image",
              "value": "ubuntu-20-04-x64"
            }
          ]
        },
        "headerParametersUi": {
          "parameter": [
            {
              "name": "Authorization",
              "value": "Bearer {your_personal_access_token}"
            }
          ]
        }
      },
      "typeVersion": 1
    }
  ],
  "connections": {}
}
```
