# Effortless Job Hunting: Let this Automation Find Your Next Role

**[View Template](https://n8n.io/workflows/3051-/)**  **Published Date:** 03/01/2025  **Created By:** Mateo Fiorito Rocha  **Categories:** `Data & Storage` `Productivity` `Development` `Core Nodes` `AI` `Langchain`  

## Template Description

Find Job Postings from LinkedIn, Indeed, and Glassdoor and Save Them to Google Sheets Using AI

Overview
Effortlessly discover and apply to jobs tailored to your profile—AI handles the search, you handle the interviews.

Say goodbye to endless job board scrolling. This automation leverages AI to analyze your resume, identify your skills, experience, and more, to match you with the most relevant job opportunities. It sources job postings from LinkedIn, Indeed, Glassdoor, ZipRecruiter, Monster, and other public job sites on the web. With seamless integration and automatic organization of results, you can focus on applying rather than searching.

Key Features

Intelligent Resume Parsing
Extracts key information from your PDF resume using AI.
Identifies skills, experience, education, and job preferences.

Targeted Job Matching
Uses the parsed resume data to search for jobs that align with your profile.
Ensures relevance by analyzing job descriptions for matching criteria.

Automated Data Organization
Compiles job listings into a structured Google Spreadsheet.
Eliminates the need for manual data entry, saving valuable time.

Easy Access and Review
Stores results in a familiar Google Sheets format for easy tracking.
Allows for filtering and sorting to prioritize applications.

Setup Instructions

Prerequisites
A free API key for the job search service.
Google Drive and Google Sheets accounts.
An updated resume in PDF format.

Step 1: Connect Your Resume Parsing AI
Upload your PDF resume to Google Drive.
Configure the AI parser node in n8n to extract relevant information.
Map the extracted fields (e.g., skills, job title, experience) for job searching.

Step 2: Automate the Job Search
Use the extracted data to perform a job search on LinkedIn, Indeed, Glassdoor, and other supported job sites.
Retrieve job postings based on relevant keywords and location preferences.

Step 3: Save Job Listings to Google Sheets
Create a new Google Sheet to store job listings.
Set up the automation to write job details (e.g., title, company, location, link) into the sheet.
Format the sheet for better readability and tracking.

Step 4: Review and Apply to Jobs
Open your Google Sheet to view job matches.
Click on the links to apply directly on the respective job sites.
Update the status of each job application as you progress.

Why Use This Automation?
Saves Time**: Automates job searching and listing compilation.
Enhances Efficiency**: Eliminates manual scrolling and data entry.
Improves Organization**: Keeps all job opportunities in a structured format.
Optimizes Your Job Hunt**: Increases chances of landing the perfect role.

Designed specifically for job seekers aiming to optimize their search process, this automation integrates with Google Drive and Sheets, streamlining your job hunt and enhancing your chances of finding the right opportunity. Get started today and accelerate your career growth!

## Template JSON

```
{
  "id": "lN9uOQVOTZqFlVsj",
  "meta": {
    "instanceId": "143d2ab55c8bffb06f8b9c7ad30335764fdc48bbbacecbe2218dadb998a32213",
    "templateCredsSetupCompleted": true
  },
  "name": "My workflow 3",
  "tags": [],
  "nodes": [
    {
      "id": "e5442c6a-ef95-4b78-b09a-35dee425d6f6",
      "name": "On clicking 'execute'",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        0,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "527cc819-c439-4353-a247-c3e832485ff0",
      "name": "Read PDF",
      "type": "n8n-nodes-base.readPDF",
      "position": [
        440,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "da9591a1-87fd-4b4e-bcae-ec2fc5264b9a",
      "name": "Download Resume (PDF File)",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        220,
        0
      ],
      "parameters": {},
      "typeVersion": 3
    },
    {
      "id": "2534a95b-7c65-4c3b-b927-9cdbfbb400a7",
      "name": "Filter Relevant Information",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        660,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "79a1858d-a405-4e09-8375-538550323cea",
      "name": "Analyse Resume",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        880,
        0
      ],
      "parameters": {},
      "typeVersion": 1.8
    },
    {
      "id": "fa7e3279-b59d-4c65-bb94-9910f47ec315",
      "name": "Find Suitable Job Offers ",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        1240,
        0
      ],
      "parameters": {},
      "typeVersion": 4.2
    },
    {
      "id": "f85c66f9-08a7-472f-9cf2-8049ccf62ac4",
      "name": "Organise the Job Posts",
      "type": "n8n-nodes-base.splitOut",
      "position": [
        1460,
        0
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "5fb3753e-b5b9-4a8f-942b-986cd571764d",
      "name": "Upload Job Posts Organised in a Spreadsheet",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        1700,
        0
      ],
      "parameters": {},
      "typeVersion": 4.5
    },
    {
      "id": "2a7c8960-b9ec-4114-bc5e-0d878d7485ed",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -840,
        -180
      ],
      "parameters": {
        "content": ""
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "aa3dddb1-e084-448d-befc-dc430ad6bb48",
  "connections": {
    "Read PDF": {
      "main": [
        [
          {
            "node": "Filter Relevant Information",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Analyse Resume": {
      "main": [
        [
          {
            "node": "Find Suitable Job Offers ",
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
            "node": "Download Resume (PDF File)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Organise the Job Posts": {
      "main": [
        [
          {
            "node": "Upload Job Posts Organised in a Spreadsheet",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Find Suitable Job Offers ": {
      "main": [
        [
          {
            "node": "Organise the Job Posts",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Download Resume (PDF File)": {
      "main": [
        [
          {
            "node": "Read PDF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter Relevant Information": {
      "main": [
        [
          {
            "node": "Analyse Resume",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
