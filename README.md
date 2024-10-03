## About Project

This project is an audio call processing and analysis API designed to handle transcription, categorization, and emotional tone detection of telephone conversations. The API allows users to submit audio files (in formats like WAV and MP3), where the service processes these files, transcribes the spoken content, and extracts key information such as the caller’s name and location. Additionally, it performs sentiment analysis to determine the emotional tone of the conversation, classifying it as Neutral, Positive, Negative, or Angry.

Categories are another core feature of the API. These represent conversation topics (e.g., Visa and Passport Services, Diplomatic Inquiries, etc.), and conversations may be assigned to one or more categories. The API includes CRUD (Create, Read, Update, Delete) operations for managing these categories, which are stored locally in a JSON file, allowing dynamic updates and deletions without relying on a database.


## User Documentation

Prerequisites

Install Python 3.9:
Download the Python 3.9 installer from the official Python website.
Follow the installation instructions specific to your operating system (Windows, macOS, Linux).
Install Required Dependencies: After installing Python, you will need to install the required libraries. You can use pip to install these dependencies.
Create a file named ```requirements.txt``` in the root of your project with the following content:


plaintext
Copy code
fastapi
uvicorn
pydantic
vosk
spacy
python-multipart
Run the following command to install all dependencies:

bash
Copy code
```pip install -r requirements.txt```
Download Voice Recognition Models:
Visit the Vosk website to download the necessary voice recognition models.
Extract the downloaded model files and ensure they are placed in a directory accessible by your application (e.g., model/).

Your audio files moves to folder audio_files

All recognitions files saved in call folder