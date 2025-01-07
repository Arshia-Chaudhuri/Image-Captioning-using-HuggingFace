from flask import Flask, render_template, request, jsonify
from transformers import BlipForConditionalGeneration, AutoTokenizer, pipeline, BlipProcessor
from PIL import Image
import os

app = Flask(__name__)

# Load the model, tokenizer, and processor
def load_model():
    model_name = "blip-image-captioning"  # Your saved folder
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = BlipForConditionalGeneration.from_pretrained(model_name)
    processor = BlipProcessor.from_pretrained(model_name)

    # Create the pipeline
    caption_generator = pipeline("image-to-text", model=model, tokenizer=tokenizer, image_processor=processor)
    return caption_generator

caption_generator = load_model()

# Set upload folder
UPLOAD_FOLDER = './static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_caption', methods=['POST'])
def generate_caption():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided."}), 400

    image_file = request.files['image']

    if image_file.filename == '':
        return jsonify({"error": "No selected image."}), 400

    # Save the uploaded image
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
    image_file.save(image_path)

    # Generate the caption
    try:
        caption = caption_generator(image_path)[0]['generated_text']
        return jsonify({"caption": caption})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
