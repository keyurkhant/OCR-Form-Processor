import os, io
import cv2 as cv
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'VisionModule/ServiceAccountToken.json'
client = vision.ImageAnnotatorClient()

def Text_Recognize(img):
    success, encoded_image = cv.imencode('.png', img)
    content = encoded_image.tobytes()
    image = vision.types.Image(content = content)
    response = client.text_detection(image=image, image_context = { "language_hints" : ["en"]})

    docText = response.full_text_annotation.text
    return docText

def Document_Text_Recognize(img):
    success, encoded_image = cv.imencode('.png', img)
    content = encoded_image.tobytes()
    image = vision.types.Image(content = content)
    response = client.document_text_detection(image=image, image_context = { "language_hints" : ["en"]})

    docText = response.full_text_annotation.text
    return docText