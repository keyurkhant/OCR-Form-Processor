import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
client = vision.ImageAnnotatorClient()

FOLDER_PATH = r'/root/Keyur Khant/Study/Others/OCR Hackathon/'
IMAGE_FILE = '/root/Keyur Khant/Study/Others/OCR Hackathon/houghlines5.jpg'
FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)
response = client.document_text_detection(image=image)

docText = response.full_text_annotation.text


print(docText)

