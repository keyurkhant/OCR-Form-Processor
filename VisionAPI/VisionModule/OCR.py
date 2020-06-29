# Import required libraries and module
import os, io
import cv2 as cv
from google.cloud import vision    # Vision API module
from google.cloud.vision import types   # For Image type for text detection
import pandas as pd

# From virtual environment define credential json file.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'VisionModule/ServiceAccountToken.json'
client = vision.ImageAnnotatorClient()  # Create Vision API client

'''

Here, below both functions do same work to detect text from image.

But Text_Recognize used for printed text and some times give better 
accuracy for handwritten text also.
For numbers, it gives more accuracy.

Document_Text_Recognition method mainly used for handwritten.

'''

def Text_Recognize(img):
    '''
    This function take an argument as image

    It convert image(numpy array) into bytes and apply 
    text detection method to detect text for english language.
    '''
    success, encoded_image = cv.imencode('.png', img) # Encode image into png
    content = encoded_image.tobytes()   # Convert into bytes
    image = vision.types.Image(content = content)   # Apply image type
    response = client.text_detection(image=image, image_context = { "language_hints" : ["en"]}) # Apply text detection as language hint English(en)

    docText = response.full_text_annotation.text # From JSON return, take text which are detected.
    return docText

def Document_Text_Recognize(img):
    '''
    This function take an argument as image

    It convert image(numpy array) into bytes and apply text 
    detection method to detect document text for english language.
    '''
    success, encoded_image = cv.imencode('.png', img) # Encode image into png
    content = encoded_image.tobytes()  # Convert into bytes
    image = vision.types.Image(content = content)  # Apply image type
    response = client.document_text_detection(image=image, image_context = { "language_hints" : ["en"]}) # Apply document text detection as language hint English(en)

    docText = response.full_text_annotation.text # From JSON return, take text which are detected.
    return docText