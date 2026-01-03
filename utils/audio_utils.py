import whisper
import tempfile
import os

# Load Whisper model once (important for performance)
model = whisper.load_model("base")

def transcribe_audio(audio_bytes) -> str:
    """
    Takes raw audio bytes from Streamlit uploader
    Returns transcribed text
    """

    # Save audio temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        temp_path = tmp.name

    try:
        result = model.transcribe(temp_path)
        text = result.get("text", "").strip()
    finally:
        os.remove(temp_path)

    return text
