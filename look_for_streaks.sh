#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <video_recording.mp4>"
    exit 1
fi

for file in "$@"; do
    # echo "Converting audio..."
    ffmpeg -y -loglevel quiet -i "$file" -q:a 0 -map a /tmp/output_audio.wav
    # echo "Transcribing audio..."
    python transcribe_with_whisper.py $(basename "$file")
    echo
done
