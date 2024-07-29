# ExamProctorGPT

ExamProctorGPT is an automated system designed to assist in online exams by utilizing dual camera inputs (front and back), capturing screenshots, extracting text using OCR (Optical Character Recognition), and generating intelligent responses through the ChatGPT API. This project aims to streamline the process of monitoring and answering questions during exams, ensuring a seamless and efficient experience.
![ExamProctorGPT](Picture1.png)
![ExamProctorGPT](Picture2.png)

## Features

- **Dual Camera Monitoring:** Utilizes both front and back cameras to ensure comprehensive monitoring without the user being aware of the camera operation.
- **Automated Screenshot Capture:** Periodically takes screenshots during the exam to capture relevant information.
- **OCR Integration:** Extracts text from screenshots using advanced OCR technology.
- **ChatGPT Response Generation:** Uses the extracted text to generate accurate and context-aware responses through the ChatGPT API.
- **Seamless Integration:** Designed to integrate smoothly with existing online exam platforms.

## How It Works

1. **Screenshot Capture:** The system takes periodic screenshots from the camera feeds without notifying the user.
2. **Text Extraction:** OCR processes the screenshots to extract text content.
3. **Response Generation:** Extracted text is sent to the ChatGPT API, which generates appropriate responses.
4. **Output:** Responses are displayed or sent to the designated interface for review.

## Getting Started

# Screenshot to ChatGPT

This project automates the process of taking a screenshot, extracting text from it using OCR, and generating a response using the ChatGPT API.

## Requirements

- Python 3.x
- PyAutoGUI
- Pillow
- pytesseract
- openai
- OpenCV
- Tesseract OCR
- ChatGPT API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/raja21068/ExamProctorGPT.git
   cd ExamProctorGPT```
   
   
2. Install the required packages:
pip install pyautogui Pillow pytesseract openai
Ensure Tesseract is installed and configured on your system.
Replace 'your-api-key' in screenshot_to_chatgpt.py with your OpenAI API key.

3. Run the script:
python screenshot_to_chatgpt.py

##  Additional Resources
For more information on a similar project, visit the following GitHub repository:
AI Desktop Assistant - Agent Based Smart Automation Task Management Platform: https://github.com/raja21068/AI-Desktop-Assistant-Agent-Based-Smart-Automation-Task-Management-Platform--chatgpt-4






