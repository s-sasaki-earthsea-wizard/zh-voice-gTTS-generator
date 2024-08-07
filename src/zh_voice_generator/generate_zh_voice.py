from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import datetime

def generate_zh_voice(input_zn_text, output_sound_file=None):
    if output_sound_file is None:
        # Use the current timestamp to generate a unique filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_sound_file = f"output_{timestamp}.mp3"
    
    # Generate and save the zn voice file using Google Text-to-Speech (gTTS)
    tts = gTTS(input_zn_text, lang='zh')
    tts.save(output_sound_file)
    
    # Play and save the generated zn voice file
    audio = AudioSegment.from_file(output_sound_file)
    play(audio)

    print(f"Voice generated and saved to {output_sound_file}")

if __name__ == "__main__":
    # Chinese text for testing
    sample_text = "你好，这是一个示例。"
    sample_filename = "sample.mp3"
    generate_zh_voice(sample_text, sample_filename)
