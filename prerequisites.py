from transformers import pipeline
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

caption = pipeline('image-to-text', model="Salesforce/blip-image-captioning-base")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
processor.save_pretrained("./blip-image-captioning")
model.save_pretrained("./blip-image-captioning")
print("Model and processor saved locally!")