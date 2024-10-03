# services/call_service.py

import json
import requests
from vosk import Model, KaldiRecognizer
import wave
import os
import spacy
from models.call import Call

# Load the English model from spaCy
nlp = spacy.load("en_core_web_sm")


# Function to transcribe audio
def transcribe_audio(audio_path: str) -> str:
    wf = wave.open(audio_path, "rb")
    rec = KaldiRecognizer(Model("model/vosk-model-small-en-us-0.15"), wf.getframerate())
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

    call = Call(
        name=names[0] if names else None,
        location=locations[0] if locations else None,
        emotional_tone="Neutral",  # Placeholder; implement emotional tone analysis as needed
        text=transcribed_text,
        categories=["Visa and Passport Services"]  # Default category; implement logic as needed
    )

    # Save the call to a JSON file
    with open(f"./calls/{call.id}.json", "w") as f:
        json.dump(call.dict(), f)

    return call
