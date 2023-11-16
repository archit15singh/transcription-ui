# customer support telephonic conversation transcription
UI for playing a conversational mp3 and get the highlighted transcriptions for it while it plays.
This matches the output of openAI whisper.cpp which is a .json file.

uses voice activity detection AI models to filter out segments with no human voice
uses ffmpeg for sampling at 16kHz
uses openAI whisper.cpp for transcription (multiple process setup, CPU/GPU support)
sqs and s3 for orchestration and persistence


Demo:
https://jmp.sh/8VcYb3Qh

image
