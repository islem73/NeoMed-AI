#Step1: Setup Audio Recoder 
import logging
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import which
from io import BytesIO

logging.basicConfig(level=logging.INFO , format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path , timeout=20, phrase_time_limit=None):
    """
    Record audio from the microphone and save it to a file.
    """
    recognizer = sr.Recognizer()
    AudioSegment.converter = which("ffmpeg")


    try:
        with sr.Microphone() as source:
            logging.info(" Adjusting for ambient noise... ")
            # Adjust for ambient noise and record audio
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Please start speaking...")

            
            #Record audio
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recondoring Finished...")

            # Save the audio to a file
            wav_data = audio.get_wav_data()  
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="wav")

            logging.info(f"Audio saved to {file_path}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


audio_filepath="patient_voice_test.mp3"
#record_audio(file_path=audio_filepath)

#Step2: Record Speech to text_model for transcription
import os 
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
stt_model="whisper-large-v3"

def transcribe_audio(stt_model, audio_filepath,GROQ_API_KEY):

    client = Groq(api_key=GROQ_API_KEY)
    audio_file=open(audio_filepath, "rb")
    transcript = client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en",
    )

    return transcript.text
