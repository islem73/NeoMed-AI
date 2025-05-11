#Step1a: Setup Text to Speech-TTS-model with  gTTs
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(text,output_filepath):
    language = 'en'

    audioobj = gTTS(text=text, lang=language, slow=False)
    audioobj.save(output_filepath)

text='Hello, I am the voice of the NEoMed AI. How can I help you?'
text_to_speech_with_gtts_old(text=text, output_filepath='output.mp3')

#Step1a: Setup Text to Speech-TTS-model with ElevenLabs
import elevenlabs
from elevenlabs import ElevenLabs
from dotenv import load_dotenv
load_dotenv()

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs_old(text,output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=text,
        voice="Sarah",
        output_format="mp3_44100_128",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio,output_filepath)

#text_to_speech_with_elevenlabs_old(text,output_filepath="output_elevenlabs.mp3")

#Stp2: Use Model for Text to voice
import subprocess
import platform

def text_to_speech_with_gtts (text,output_filepath):
    language = 'en'

    audioobj = gTTS(text=text, lang=language, slow=False)
    audioobj.save(output_filepath)
    os_name = platform.system()

    try:
        if os_name == 'Windows':
            subprocess.call(['start', output_filepath], shell=True)
        elif os_name == 'Darwin':  # macOS
            subprocess.call(['open', output_filepath])
        elif os_name == 'Linux':
            subprocess.call(['xdg-open', output_filepath])
        else:
            print("Unsupported OS")

    except Exception as e:
        print(f"Error playing audio: {e}")

text='Hello, I am the voice of the NEoMed AI. How can I help you?'
#text_to_speech_with_gtts(text=text, output_filepath='output_newversion.mp3')


def text_to_speech_with_elevenlabs(text,output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=text,
        voice="Sarah",
        output_format="mp3_44100_128",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio,output_filepath)

    return output_filepath 




#text_to_speech_with_elevenlabs(text,output_filepath="output_elevenlabs_newversion.mp3")

