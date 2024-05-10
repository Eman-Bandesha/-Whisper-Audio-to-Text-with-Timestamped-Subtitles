import whisper_timestamped as whisper
model = whisper.load_model("base")

audio = whisper.load_audio("english.wav")
result = whisper.transcribe(model, audio)
all_word_texts = []
for segment in result['segments']:
    for word_info in segment['words']:
        word_text = word_info['text']
        all_word_texts.append(word_text)

combined_text = ' '.join(all_word_texts)
print(combined_text)