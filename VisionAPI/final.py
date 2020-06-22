import sys
import cv2 as cv
from flask import Flask, request, render_template, url_for, redirect, make_response, session
from VisionModule import PDF2IMG as pi
from flask_pymongo import PyMongo
import time
import json

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://kpkhant:keyurkhant123@ocrhack-j1wkq.mongodb.net/OCRHack?retryWrites=true&w=majority"
mongo = PyMongo(app)
app.secret_key = 'kpkhant007'

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/upload', methods = ["POST"])
def upload_file():
	dict1 = json.load(open('data.json','r'))
	pdf = request.files['UploadDocument']
	pi.toImg(pdf)
	return render_template("second.html", dict1 = dict1, filename = pdf.filename)

@app.route('/part1', methods = ["POST"])
def part1():
	if request.method == "POST":
		result = request.form.to_dict()
		with open('result1.json', 'w') as fp:
			json.dump(result, fp)
		dict1 = json.load(open('data.json','r'))
		id = mongo.db.form1.insert_one(result)
		return render_template('third.html', req = request, dict1 = dict1)

@app.route('/part2', methods = ["POST"])
def part2():
	if request.method == "POST":
		result = request.form.to_dict()
		with open('result2.json', 'w') as fp:
			json.dump(result, fp)
		id = mongo.db.form2.insert_one(result)
		return render_template('fourth.html', req = request)


@app.route("/second", methods = ["POST"])
def home2():
    dict1 = {'hconame': 'Exact Science', 'provider': 'K Khant', 'npi': '1548862593', 'address': '81, Sarita Vihar', 'city': 'Surat', 'phone': '9016243435', 'fax': '459335'}
    return render_template("second.html", dict1 = dict1)


if __name__ == "__main__":
    app.run(debug=True)