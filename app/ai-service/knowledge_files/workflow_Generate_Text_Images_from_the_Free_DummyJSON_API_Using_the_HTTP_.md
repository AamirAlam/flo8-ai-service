# Generate Text Images from the Free DummyJSON API Using the HTTP Request Node

**[View Template](https://n8n.io/workflows/2990-/)**  **Published Date:** 02/23/2025  **Created By:** Akram Kadri  **Categories:** `Development` `Core Nodes`  

## Template Description

Who is this for?

This workflow template is ideal for marketers, designers, content creators, and developers who need to generate custom text-based images dynamically. Whether you want to create social media graphics, placeholder images, or text-based LinkedIn carousels, this workflow provides a simple, no-code solution using an API that requires no authentication.

What problem does this workflow solve?

Creating text-based images often requires design software or complex integrations with graphic tools. This workflow eliminates that hassle by allowing users to generate images with custom text, font styles, colors, and background colors using a simple HTTP request. It’s perfect for automating image generation without relying on external tools or manual effort.

What this workflow does

This workflow leverages an HTTP request to a free API that generates text-based images dynamically. Here's what it enables you to do:

Define custom image text
Set image dimensions (width x height)
Choose a background color and text color using hex codes
Select a font family and font size
Specify the image format (PNG, JPG, or WebP)

The generated image can be used immediately, making it ideal for automating content creation workflows.

Setup

Open the workflow in n8n.
Modify the Set node to define your preferred image properties:
text: The message displayed on the image.
size: Image dimensions (e.g., 500x300 pixels).
backgroundColor: Hex color code for the background.
textColor: Hex color code for the text.
fontFamily: Select from available font options (e.g., Pacifico, Ubuntu).
fontSize: Define the text size.
type: Choose the image format (PNG, JPG, or WebP).

Execute the workflow to generate an image.
The HTTP request returns the generated image, ready for use.

How to customize this workflow

1.     Adjust the Set node values to match your desired design.
2.     Use dynamic data for text, allowing personalized images based on user input.
3.     Automate image delivery by adding email or social media posting nodes.
4.     Integrate this workflow into larger automation sequences, such as content marketing pipelines.

## Template JSON

```
{
  "name": "Generate Image Workflow",
  "tags": [],
  "nodes": [
    {
      "id": "0a657f21-f0fe-4521-be7f-aa245f86f5d3",
      "name": "When clicking \u2018Test workflow\u2019",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        340,
        -200
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "54ead951-03fb-4741-9e66-bffa0ff42302",
      "name": "Fetch Image from API",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        780,
        -200
      ],
      "parameters": {
        "url": "=https://dummyjson.com/image/{{ $json.size }}/{{ $json.backgroundColor }}/{{ $json.textColor }}",
        "options": {},
        "sendQuery": true,
        "queryParameters": {
          "parameters": [
            {
              "name": "text",
              "value": "={{ $json.text }}"
            },
            {
              "name": "fontSize",
              "value": "={{ $json.fontSize }}"
            },
            {
              "name": "type",
              "value": "={{ $json.type }}"
            },
            {
              "name": "fontFamily",
              "value": "={{ $json.fontFamily }}"
            }
          ]
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "9b60f208-7bbc-4c35-9303-797aabef478d",
      "name": "Set Image Properties",
      "type": "n8n-nodes-base.set",
      "position": [
        560,
        -200
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "25b4c572-4ba6-4719-b547-8d3787ba557b",
              "name": "size",
              "type": "string",
              "value": "600x400"
            },
            {
              "id": "a6689fdb-b212-4c88-b80f-64aabe61daa1",
              "name": "backgroundColor",
              "type": "string",
              "value": "cc22e3"
            },
            {
              "id": "f9dcc452-4dd5-46fc-948b-39194bf0637d",
              "name": "textColor",
              "type": "string",
              "value": "ffffff"
            },
            {
              "id": "89842462-d3ac-4267-a40a-3e98e8823ef3",
              "name": "text",
              "type": "string",
              "value": "Generated!"
            },
            {
              "id": "59eb064d-1cc3-4b7d-92ec-594dadbd38cd",
              "name": "fontSize",
              "type": "string",
              "value": "100"
            },
            {
              "id": "ccbae0db-559a-4de2-be63-4238feca6498",
              "name": "fontFamily",
              "type": "string",
              "value": "pacifico"
            },
            {
              "id": "ab88695a-d223-4f26-9ded-3e4c965ca28c",
              "name": "type",
              "type": "string",
              "value": "png"
            }
          ]
        }
      },
      "typeVersion": 3.4
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "c2d9939a-6766-4b7c-8331-63a655946208",
  "connections": {
    "Set Image Properties": {
      "main": [
        [
          {
            "node": "Fetch Image from API",
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
            "node": "Set Image Properties",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
