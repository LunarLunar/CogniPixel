from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from tensorflow.keras.applications import mobilenet_v2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np
import io
import threading
import webbrowser
import os

app = Flask(__name__)
CORS(app) # This will allow the frontend to make requests to the backend

# Load the pre-trained MobileNetV2 model
model = mobilenet_v2.MobileNetV2(weights='imagenet')

def prepare_image(img):
    img = image.load_img(io.BytesIO(img), target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array_expanded_dims)

@app.route('/classify', methods=['POST'])
def classify():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        try:
            img_bytes = file.read()
            preprocessed_image = prepare_image(img_bytes)
            predictions = model.predict(preprocessed_image)
            decoded_predictions = decode_predictions(predictions, top=5)[0]

            results = []
            for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
                results.append(f"{label} ({score:.2%})")

            return jsonify({'results': results})
        except Exception as e:
            return jsonify({'error': str(e)})

def open_browser():
    # Open the HTML file in the default web browser
    # The path is relative to the script's location
    webbrowser.open('file://' + os.path.realpath('index.html'))

if __name__ == '__main__':
    # Use a timer to open the browser 1 second after the server starts
    # Running with use_reloader=False prevents the script from running twice
    threading.Timer(1, open_browser).start()
    app.run(debug=True, use_reloader=False)