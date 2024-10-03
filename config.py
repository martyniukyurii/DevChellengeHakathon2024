import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    AUDIO_FILE_PATH = os.getenv("AUDIO_FILE_PATH", "audio.json")
