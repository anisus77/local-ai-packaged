from fastapi import FastAPI, UploadFile, File
from faster_whisper import WhisperModel

app = FastAPI()
model = WhisperModel("base")  # Choose model size as needed

@app.post("/transcribe")
async def transcribe(audio: UploadFile = File(...)):
    audio_path = "audio.wav"
    with open(audio_path, "wb") as f:
        f.write(await audio.read())
    segments, info = model.transcribe(audio_path)
    return {
        "segments": [s.text for s in segments],
        "info": info
    }
