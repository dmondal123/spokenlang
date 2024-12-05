from transformers import pipeline
transcriber = pipeline("automatic-speech-recognition", model="ai4bharat/indicwav2vec_v1_bengali")
transcription = transcriber("data/raw_data/bengali/_00BrgoiQL0.wav")
print(transcription)