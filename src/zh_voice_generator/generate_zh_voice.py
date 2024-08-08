from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import datetime
import os
import argparse

def generate_zh_voice(input_zn_text, output_sound_file=None):
    # Avoid overwriting existing files by appending timestamp to filename
    output_sound_file = avoid_overwrite_using_datetime(output_sound_file)

    # Generate and save the zn voice file using Google Text-to-Speech (gTTS)
    tts = gTTS(input_zn_text, lang='zh')
    tts.save(output_sound_file)
    
    # Play and save the generated zn voice file
    audio = AudioSegment.from_file(output_sound_file)
    play(audio)

    print(f"Voice generated and saved to {output_sound_file}")

def get_args():
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Generate Chinese voice from text')
    parser.add_argument('text', type=str, help='Chinese text to convert to voice')
    parser.add_argument('--output', type=str, help='Output MP3 filename', default=None)
    
    # Parse and return arguments
    return parser.parse_args()

def avoid_overwrite_using_datetime(output_sound_file):
    if output_sound_file is None:
        # Use the current timestamp to generate a unique filename if not provided
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H;%M;%S") # Avoid using ':' in filename for Windows compatibility
        return f"output_{timestamp}.mp3"
    elif os.path.exists(output_sound_file):
        # If the filename already exists, append the current timestamp to avoid overwriting
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return f"{os.path.splitext(output_sound_file)[0]}_{timestamp}.mp3"
    else:
        return output_sound_file

if __name__ == "__main__":
    # Get command-line arguments
    args = get_args()

    # Generate voice
    generate_zh_voice(args.text, args.output)
