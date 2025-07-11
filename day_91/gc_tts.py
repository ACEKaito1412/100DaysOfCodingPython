import os
from google.cloud import texttospeech

class TTService():
    def __init__(self, gc_path:str):
        self.client = texttospeech.TextToSpeechClient()
        self.voice = texttospeech.VoiceSelectionParams(
            language_code = "en-US",
            name = "en-US-Studio-O"
        )

        self.audio_config = texttospeech.AudioConfig(
            audio_encoding = texttospeech.AudioEncoding.MP3,
            effects_profile_id = ["small-bluetooth-speaker-class-device"],
            speech_rate = 1,
            pitch = 1
        )

        self.synthesis_input = ""


    def convert_text_to_speech(self, text_content, output_path):
        if text_content == "":
            return
        
        self.synthesis_input = texttospeech.SynthesisInput(text=text_content)

        response = self.client(
            input = self.synthesis_input,
            voice = self.voice,
            audio_config = self.audio_config
        )

        with open(output_path, "wb") as out:
            out.write(response.audio_content)
            print(f"Audio content written to file {output_path}.")
