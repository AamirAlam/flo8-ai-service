# Receive messages for a MQTT queue

**[View Template](https://n8n.io/workflows/657-/)**  **Published Date:** 09/14/2020  **Created By:** ghagrawal17  **Categories:**   

## Template Description



## Template JSON

```
{
  "id": "51",
  "name": "Receive messages for a MQTT queue",
  "nodes": [
    {
      "name": "MQTT Trigger",
      "type": "n8n-nodes-base.mqttTrigger",
      "position": [
        690,
        260
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "mqtt": "mqtt"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "settings": {},
  "connections": {}
}
```
