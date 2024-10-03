# services/call_service.py

import json
import os
import wave
from vosk import Model, KaldiRecognizer
import spacy
from models.call import Call

# Load the English model from spaCy
nlp = spacy.load("en_core_web_sm")


# Example keyword-based emotional tone analysis
def analyze_emotional_tone(text: str) -> str:
    positive_keywords = ["good", "great", "happy", "positive", "excellent"]
    negative_keywords = ["bad", "sad", "angry", "negative", "poor"]

    # Basic keyword-based analysis
    positive_count = sum(word in text.lower() for word in positive_keywords)
    negative_count = sum(word in text.lower() for word in negative_keywords)

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"


# Example of category keywords
category_keywords = {
    "Visa and Passport Services": ["visa", "passport", "border"],
    "Diplomatic Inquiries": ["diplomatic", "embassy", "consulate"],
    "Travel Advisories": ["travel", "advisory", "health"],
    "Consular Assistance": ["assistance", "emergency", "help"],
    "Trade and Economic Cooperation": ["trade", "economic", "business"],
}


# Function to dynamically assign categories based on text
def assign_categories(text: str) -> list:
    assigned_categories = []
    for category, keywords in category_keywords.items():
        if any(keyword in text.lower() for keyword in keywords):
            assigned_categories.append(category)
    return assigned_categories


def transcribe_audio(audio_path: str) -> str:
    wf = wave.open(audio_path, "rb")
    rec = KaldiRecognizer(Model("model"), wf.getframerate())
    text = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            text += json.loads(result)["text"] + " "

    text += json.loads(rec.FinalResult())["text"]
    return text.strip()


def extract_entities(text: str):
    doc = nlp(text)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    return names, locations


def process_audio_call(audio_url: str) -> Call:
    # Download the audio file (assuming it's local for this project)
    audio_path = f"./audio_files/{os.path.basename(audio_url)}"

    # Transcribe audio
    transcribed_text = transcribe_audio(audio_path)

    # Extract entities
    names, locations = extract_entities(transcribed_text)

    # Analyze emotional tone
    emotional_tone = analyze_emotional_tone(transcribed_text)

    # Assign categories dynamically
    categories = assign_categories(transcribed_text)

    # Create Call object
    call = Call(
        name=names[0] if names else None,
        location=locations[0] if locations else None,
        emotional_tone=emotional_tone,
        text=transcribed_text,
        categories=categories
    )

    # Save the call to a JSON file
    with open(f"./calls/{call.id}.json", "w") as f:
        json.dump(call.dict(), f)

    return call
