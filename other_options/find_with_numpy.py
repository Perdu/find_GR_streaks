# This solution is very very slow
# Another option would be to try with dejavu
# Most of this is unedited chatGPT code

from pydub import AudioSegment
from scipy.signal import correlate
import numpy as np

def load_audio(file_path):
    return AudioSegment.from_file(file_path)

def find_audio_match(long_audio, short_audio, threshold=0.7):
    long_audio_array = np.array(long_audio.get_array_of_samples())
    short_audio_array = np.array(short_audio.get_array_of_samples())
    
    correlation = correlate(long_audio_array, short_audio_array)
    match = np.max(correlation) / len(short_audio_array)
    
    if match > threshold:
        match_position = np.argmax(correlation)
        start_time = match_position - len(short_audio_array) + 1
        start_time_seconds = start_time / long_audio.frame_rate
        return start_time_seconds
    return None

def find_matches(long_audio_path, short_audio_paths, threshold=0.7):
    long_audio = load_audio(long_audio_path)
    matches = []
    
    for short_audio_path in short_audio_paths:
        short_audio = load_audio(short_audio_path)
        match_time = find_audio_match(long_audio, short_audio, threshold)
        if match_time is not None:
            matches.append((short_audio_path, match_time))
    
    return matches

if __name__ == "__main__":
    long_audio_path = "/tmp/output_audio.wav"
    short_audio_paths = [
#        "announcer/AnnouncerDouble Kill.ogg",
#        "announcer/AnnouncerTripleKill.ogg",
#        "announcer/AnnouncerQuadKill.ogg",
        "announcer/AnnouncerPentaKill.ogg",
        "announcer/AnnouncerIncredible.ogg",
        "announcer/AnnouncerUnbelievable.ogg",
 #       "announcer/AnnouncerAmazing.ogg",
 #       "announcer/AnnouncerUnstoppable.ogg",
 #       "announcer/AnnouncerEpic.ogg",
    ]
    
    matches = find_matches(long_audio_path, short_audio_paths, threshold=0.7)
    
    for match in matches:
        print(f"Match found for {match[0]} at {match[1]:.2f} seconds")
