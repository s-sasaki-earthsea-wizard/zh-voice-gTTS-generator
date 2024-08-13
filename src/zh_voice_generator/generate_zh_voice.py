import sys
import os
import argparse
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Add the project root directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.audio_utils import prepare_output_path

def generate_zh_voice(input_zn_text, output_sound_file=None):
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
    parser.add_argument('--output-dir', type=str, help='Output directory', default='output')
    parser.add_argument('--filename', type=str, help='Output MP3 filename', default=None)
    
    # Parse and return arguments
    return parser.parse_args()

if __name__ == "__main__":
    # Get command-line arguments
    args = get_args()

    # Prepare output path
    output_sound_file = prepare_output_path(args.output_dir, args.filename)
    
    # Generate voice
    generate_zh_voice(args.text, output_sound_file)
