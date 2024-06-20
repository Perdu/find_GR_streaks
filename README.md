# Find GR streaks

A small script to automate finding streaks in a video recording of Gun Raiders

Technique used is transcribing audio to text using OpenAI's whisper, then looking for streak keywords from announcer ("penta kill", "incredible" etc.).

It works kinda meh. Due to noise, words are often not recognized. Besides, some words are not common ("quad", "penta") and whisper will mistake them for something else. I included some misinterpretations I found (e.g. "penta kill" is "Tentacle", which, tbh, is funny) and this list should be updated. But the longer the streak, the more chance there is that at least one keyword is picked!

## Dependencies

- python
- ffmpeg
- whisper

## Usage

``` bash
look_for_streaks.sh <files>
```

This will display findings, and save full audio transcription in a .json file.

## Execution time

A one-and-a-half hour game recording takes about 5 minutes to process on a modern machine with a good CPU (i9-13900).

## Example run

```
$ ~/find_GR_streaks/look_for_streaks.sh streaks/20240612-170145_7+2.mp4 streaks/20240529-165847_8_and_7_and_9.mp4
20240612-170145_7+2.mp4:
6 at 0:00:22:  Incredible.
7 at 0:00:24:  Unbelievable.
7 at 0:00:28:  Unbelievable.

20240529-165847_8_and_7_and_9.mp4:
4 at 0:00:42:  Quad kill.
5 at 0:00:46:  Tenta kill.
6 at 0:00:48:  Incredible.
7 at 0:00:50:  Unbelievable.
4 at 0:01:06:  Quad kill.
5 at 0:01:08:  Tenta kill.
6 at 0:01:10:  Incredible.
7 at 0:01:12:  Unbelievable.
8 at 0:01:16:  Amazing.
```
