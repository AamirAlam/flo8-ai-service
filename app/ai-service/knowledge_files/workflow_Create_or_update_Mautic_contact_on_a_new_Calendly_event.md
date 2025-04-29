# Create or update Mautic contact on a new Calendly event

**[View Template](https://n8n.io/workflows/1828-/)**  **Published Date:** 11/23/2022  **Created By:** n8n Team  **Categories:** `Communication` `Marketing`  

## Template Description

This workflow creates or updates a Mautic contact when a new event is scheduled in Calendly. The first name and email address are the only two fields that get updated.

Prerequisites

Calendly account and Calendly credentials.
Mautic account and Mautic credentials.

How it works

Triggers on a new event in Calendly.
Creates a new contact in Mautic if the email address does not exist in Mautic.
Updates the contact's first name in Mautic if the email address exists in Mautic.

## Template JSON

```
{
  "meta": {
    "instanceId": "237600ca44303ce91fa31ee72babcdc8493f55ee2c0e8aa2b78b3b4ce6f70bd9"
  },
  "nodes": [
    {
      "id": "40216649-af2c-44df-83c6-75afe75dcdaf",
      "name": "On new event",
      "type": "n8n-nodes-base.calendlyTrigger",
      "position": [
        400,
        240
      ],
      "webhookId": "28087fc9-e623-48fe-949e-e002cbc7a817",
      "parameters": {
        "events": [
          "invitee.created"
        ]
      },
      "credentials": {
        "calendlyApi": {
          "id": "38",
          "name": "[UPDATE ME]"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "46914a34-984e-4736-b2a3-6e97555b73c7",
      "name": "Create/update contact",
      "type": "n8n-nodes-base.mautic",
      "position": [
        620,
        240
      ],
      "parameters": {
        "email": "={{$node[\"On new event\"].json[\"payload\"][\"email\"]}}",
        "options": {},
        "firstName": "={{$json[\"payload\"][\"name\"]}}",
        "additionalFields": {}
      },
      "credentials": {
        "mauticApi": {
          "id": "34",
          "name": "[UPDATE ME]"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "df809a8d-7b05-4ecc-a022-7bb12842b4bc",
      "name": "Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -20,
        180
      ],
      "parameters": {
        "width": 313,
        "height": 229,
        "content": "### Create/update Mautic contact on a new Calendly event\n1. `On new event` triggers on new Calendly events.\n2. `Create/update contact` will create a contact in Mautic or update the contact's first name. If the contact's email is already in Mautic, then the first name will be overwritten to the new first name."
      },
      "typeVersion": 1
    }
  ],
  "connections": {
    "On new event": {
      "main": [
        [
          {
            "node": "Create/update contact",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
