import json
import datetime
import sys

import whisper


AUDIO_FILE='/tmp/output_audio.wav'


def transcribe_audio(audio_file):
    # You can choose "tiny", "base", "small", "medium", or "large"
    # Anything below "medium" gives poor results though
    model = whisper.load_model("medium")
    result = model.transcribe(audio_file, language='en')
    return result


def find_streak_words(result):
    # Print the result for review
    words = {'triple kill': 3, 'quad kill': 4, 'one kill': 4, 'what kill': 4, 'penta kill': 5, 'tentacle': 5, 'tentacule': 5, 'tenta kill': 5, 'incredible': 6, 'unbelievable': 7, 'amazing': 8, 'sensational': 9, 'sensation': 9, 'unstoppable': 10, 'epic': 11}
    for i in result['segments']:
        found_words = [word for word in words if word in i['text'].lower()]
        for word in found_words:
            print(f"{words[word]} at {str(datetime.timedelta(seconds=i['start']))}: {i['text']}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "tmp"

    result = transcribe_audio(AUDIO_FILE)

    # Save transcription with timestamps
    with open(f'transcription_{filename}.json', "w") as f:
        json.dump(result, f, indent=2)

    if filename != "tmp":
        print(f"{filename}:")
    find_streak_words(result)
