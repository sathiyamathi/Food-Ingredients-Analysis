from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import pickle
import pandas as pd
import numpy as np
from flask import session
import uuid
import json
from datetime import datetime
from PIL import Image
import pytesseract
import cv2
import os
import os
import google.generativeai as genai




genai.configure(api_key="AIzaSyD6X8T-QPhObaJntlQyjUvaDQjoHlt65-c")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  safety_settings=safety_settings,
  generation_config=generation_config,
  system_instruction="from the given ingredients list, check whether that the product is suitable for a diabetic person. At last say that it can or cant be consumed by the diabetic. dont need to give any advice or suggestion."
)



chat_session = model.start_chat(
    history=[]
)

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

CORS(app, resources={r"/*": {"origins": "*"}}) 

@app.route('/')
def hello():
    message= ''
    return render_template("ocr.html",message = message,name="Food Label")

@app.route('/index')
def index():
    message= ''
    return render_template("ocr.html",message = message,name="Food Label")


@app.route('/ocr')
def ocr():
    message= ''
    return render_template("ocr.html",message = message,name="Food Label")



@app.route('/ocrdetect', methods=['POST'])
def ocrdetect():
    photo=request.files["photo"]
    photo_name = photo.filename
    photo.save("static/foodlabel/" + photo_name)
    image=cv2.imread("static/foodlabel/"+ photo_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)
    message= text
    message=message+ " Explain each ingredients and last tell whether it can or cant be consumed by the diabetic"
    response = chat_session.send_message(message)

    model_response = response.text
    print(model_response)
    chat_session.history.append({"role": "user", "parts": [message]})
    chat_session.history.append({"role": "model", "parts": [model_response]})

    return render_template("ocrresult.html",message = message)
  
 
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print("get_bot_response:- " + userText)

    response = chat_session.send_message(userText)

    model_response = response.text
    print(model_response)
    chat_session.history.append({"role": "user", "parts": [userText]})
    chat_session.history.append({"role": "model", "parts": [model_response]})

    return model_response

@app.route('/home')
def home():
    message= ''
    return render_template("ocr.html",message = message,name="Food Label")



if __name__ == '__main__':
    app.run(debug=True)
