"""
Genera el voiceover del video GAIATECH M1.0 con Gemini TTS · voz Kore.

Requiere:
  pip install google-genai
  Variable de entorno: GEMINI_API_KEY (o GOOGLE_API_KEY)

Modelos disponibles (en orden de preferencia):
  gemini-2.5-flash-preview-tts        # rápido y económico
  gemini-2.5-pro-preview-tts          # mejor expresividad

Voces (24 opciones, top picks para narrativa profesional):
  Kore       — femenina profunda (recomendada para narración técnica)
  Puck       — masculina cálida
  Charon     — masculina baja, autoritaria
  Aoede      — femenina brillante
  Zephyr     — femenina suave

Salida: voiceover.wav (PCM 16-bit, 24 kHz mono).
"""
import os
import sys
import wave
from pathlib import Path

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Falta dependencia. Instalar con: pip install google-genai")
    sys.exit(1)

HERE = Path(__file__).resolve().parent
TEXT_PATH = HERE / "voiceover.txt"
OUT_PATH = HERE / "voiceover.wav"

# Leer texto
with open(TEXT_PATH, "r", encoding="utf-8") as f:
    text = f.read().strip()

print(f"Texto: {len(text)} caracteres, {len(text.split())} palabras")
print(f"Estimación: {len(text.split()) / 175:.1f} minutos a 175 ppm")

# API key
api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
if not api_key:
    print("ERROR: define GEMINI_API_KEY o GOOGLE_API_KEY en el entorno.")
    print("PowerShell: $env:GEMINI_API_KEY = 'tu-key'")
    sys.exit(1)

client = genai.Client(api_key=api_key)

# Generar audio
print("Generando audio con Gemini TTS voz Kore...")
response = client.models.generate_content(
    model="gemini-2.5-flash-preview-tts",
    contents=text,
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Kore")
            )
        ),
    ),
)

audio_data = response.candidates[0].content.parts[0].inline_data.data

# Guardar como WAV (Gemini devuelve PCM 16-bit, 24 kHz, mono)
with wave.open(str(OUT_PATH), "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(24000)
    wf.writeframes(audio_data)

size_kb = OUT_PATH.stat().st_size / 1024
print(f"Audio guardado en {OUT_PATH}")
print(f"Tamaño: {size_kb:.1f} KB · Duración estimada: ~{len(audio_data) / (24000*2):.1f} s")
print("\nSiguiente paso:")
print(f"   Importar a DaVinci Resolve · timeline 90 s · pista A1.")
