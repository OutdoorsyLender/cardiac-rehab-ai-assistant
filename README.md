# cardiac-rehab-ai-assistant
# Heart Recovery Q&A Assistant

This project is a simple question and answer tool designed to help cardiac rehab patients quickly find the right information in their recovery guide. Users can ask a question in plain English and the assistant searches the rehab booklet for the most relevant sections. The project was inspired by conversations with a cardiac rehab specialist and created to help patients feel more confident and informed at home.

## How It Works

The program removes filler words, looks at the important keywords, and scores each section of the recovery guide. The sections with the highest scores are shown to the user. If the question contains language that suggests a medical emergency, the assistant warns the user right away.

## Features

* Detects emergency related phrases and warns the user  
* Ranks and returns the most relevant sections based on keyword matching  
* Reads from a structured JSON version of the recovery guide  
* Simple interactive question and answer flow  
* Lightweight and easy to run on any computer with Python

## How to Run

1. Make sure Python is installed (tested with Python 3.10 or later)  
2. Place these files in the same folder  
   * heart_assistant.py  
   * heart_guide_sections_fixed.json  
   * section_keywords.json  
3. Open a terminal in that folder and run:  
   ```
   python heart_assistant.py
   ```

## Project Files

* **heart_assistant.py**  
  Main program that handles user questions, runs keyword scoring, detects emergencies, and displays matching sections

* **section_keywords_counter.py**  
  Script used to extract the most common keywords from each section and build the keyword index

* **heart_guide_sections_fixed.json**  
  Structured text of the cardiac recovery booklet

* **section_keywords.json**  
  Keyword map created by the counter script

* **Final_Project_Paper.pdf**  
  Full writeup explaining the design, purpose, and results of the project

## Example Use Case

A patient might ask a question like “Can I walk up stairs yet” or “How long until I can drive.” The assistant finds the top sections related to activity, movement restrictions, or driving guidelines and prints them for the user.

## Disclaimer

This tool provides general informational support only. It is not medical advice. Always contact a healthcare provider for medical concerns or emergencies.

## Author

Brandon Everett  
MS Machine Learning and AI Candidate  

