

# -*- coding: utf-8 -*-

import requests
import json
from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from PIL import Image, ImageDraw, ImageFont
import os
import tempfile

app = Flask(__name__)

# Définissez votre clé API Hugging Face
os.environ["HUGGINGFACE_TOKEN"] = 'votre_clé_hugging_face'

# Fonction pour transcrire l'audio en texte Bamanankan
def transcribe_audio(file_path):
    url = "https://bamanankanapi.kabakoo.africa/hackathon/transcribe_to_bam"
    token = "votre_api_kabakoo"

    with open(file_path, 'rb') as audio_file:
        files = {'file': audio_file}
        data = {'token': token}
        response = requests.post(url, files=files, data=data)

        if response.status_code == 200:
            response_data = json.loads(response.text)
            message = response_data.get('data', {}).get('message', '')
            return clean_transcription(message)
        else:
            raise Exception(f"Error in transcription: {response.status_code}, {response.text}")

# Fonction pour nettoyer la transcription
def clean_transcription(transcription):
    # Exemple de nettoyage simple, à personnaliser selon les besoins
    cleaned = transcription.lower().replace(",", "").replace("barama", "").strip()
    return cleaned

# Charger le modèle et le tokenizer pour la traduction
translator_model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
translator_tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")

# Fonction pour traduire le texte Bamanankan en anglais
def translate_text_bamanankan_to_english(text):
    inputs = translator_tokenizer(text, return_tensors="pt")
    translated_tokens = translator_model.generate(**inputs, forced_bos_token_id=translator_tokenizer.lang_code_to_id["eng_Latn"])
    translated_text = translator_tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)
    return translated_text[0]

# Fonction simplifiée pour générer une image basique
def generate_image(description):
    img = Image.new('RGB', (512, 512), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((10, 10), description, fill=(255, 255, 0), font=font)
    return img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    tmp_dir = tempfile.gettempdir()
    file_path = os.path.join(tmp_dir, file.filename)
    file.save(file_path)

    try:
        transcription = transcribe_audio(file_path)
        translated_text = translate_text_bamanankan_to_english(transcription)
        image = generate_image(translated_text)
        image_path = os.path.join(tmp_dir, "generated_image.png")
        image.save(image_path)
        return jsonify({"transcription": transcription, "translation": translated_text, "image_url": image_path}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
