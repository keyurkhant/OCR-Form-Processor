import sys
import os
import cv2 as cv
from flask import Flask, request, render_template, url_for, redirect, make_response, session
from VisionModule import PDF2IMG as pi
from VisionModule import recognize
from flask_pymongo import PyMongo
import time
import json
import pdfkit
from bson.json_util import dumps
from bson import ObjectId
from datetime import datetime


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://kpkhant:keyurkhant123@ocrhack-j1wkq.mongodb.net/OCRHack?retryWrites=true&w=majority"
mongo = PyMongo(app)
app.secret_key = 'kpkhant007'

# GLOBAL VARIABLE
form1_dict = {}
form2_dict = {}
final_dict = {}
gid = ""
update_dict1 = {}
update_dict2 = {}
update_final = {}
filename = ""
data = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/upload', methods = ["POST"])
def upload_file():
	global filename,data
	pdf = request.files['UploadDocument']
	filename = pdf.filename
	start1 = time.time()
	images = pi.toImg(pdf)
	data = recognize.recognize(images[0])
	return render_template("second.html", dict1 = data, filename = filename)

@app.route('/part1', methods = ["POST"])
def part1():
	if request.method == "POST":
		global data
		global form1_dict,filename
		form1_dict = request.form.to_dict()
		race = request.form.getlist('pt_race1')
		form1_dict['pt_race1'] = race
		if 'esign' in form1_dict:
			pass
		else:
			form1_dict['esign'] = 'No'
		return render_template('third.html', dict1 = data, filename = filename)

@app.route('/part2', methods = ["POST"])
def part2():
	if request.method == "POST":
		global form2_dict
		global form1_dict
		global final_dict
		global filename
		success = False
		form2_dict = request.form.to_dict()
		if 'isallextracted' in form2_dict:
			pass
		else:
			form2_dict['isallextracted'] = 'No'
		now = datetime.now()
		now = now.strftime("%d/%m/%Y %H:%M:%S")
		formentry = {'formentry_time' : now}
		final_dict = {"form1": form1_dict, "form2": form2_dict, "metadata": formentry}
		id = mongo.db.form.insert_one(final_dict)
		os.remove('static/temp_storage/'+ filename)
		os.remove('static/temp_storage/'+ filename +'1.jpg')
		try:
			os.remove('static/temp_storage/'+ filename +'2.jpg')
		except Exception as e:
			pass
		if(id):
			success = True
		return redirect(url_for('home'))
		#return render_template('index.html',success = success)


@app.route("/second", methods = ["POST"])
def home2():
    dict1 = {'hconame': 'Exact Science', 'provider': 'K Khant', 'npi': '1548862593', 'address': '81, Sarita Vihar', 'city': 'Surat', 'phone': '9016243435', 'fax': '459335'}
    return render_template("second.html", dict1 = dict1)

@app.route("/datalist", methods = ["POST", "GET"])
def datalist():
	users = mongo.db.form.find()
	return render_template("datalist.html", users = users)

@app.route("/delete/<id>/", methods = ["POST", "GET"])
def delete(id):
	my_data = mongo.db.form.find_one({"_id": ObjectId(id)})
	mongo.db.form.delete_one(my_data)
	return redirect(url_for('datalist'))

@app.route("/download/<id>/", methods = ["POST", "GET"])
def download(id):
	my_data = mongo.db.form.find_one({"_id": ObjectId(id)})
	rendered = render_template('/pdfdownload.html', dict1 = my_data)
	css = ["static/css/pdfstyle.css"]
	pdf = pdfkit.from_string(rendered,False, css = css)
	response = make_response(pdf)
	response.headers['Content-Type'] = 'application/pdf'
	response.headers['Content-Disposition'] = 'inline, filename = PatientForm.pdf'
	return response

@app.route("/view/<id>/", methods = ["POST", "GET"])
def view(id):
	my_data = mongo.db.form.find_one({"_id": ObjectId(id)})
	return render_template('viewform.html', dict1 = my_data)

@app.route("/edit/<id>/", methods = ["POST", "GET"])
def edit(id):
	global gid
	my_data = mongo.db.form.find_one({"_id": ObjectId(id)})
	gid = id
	return render_template('editform1.html', dict1 = my_data)

@app.route("/update1", methods = ["POST" , "GET"])
def update1():
	if request.method == "POST":
		global gid
		global update_dict1
		my_data = mongo.db.form.find_one({"_id": ObjectId(gid)})
		update_dict1 = request.form.to_dict()
		race = request.form.getlist('pt_race1')
		update_dict1['pt_race1'] = race
		if 'esign' in update_dict1:
			pass
		else:
			update_dict1['esign'] = 'No'
		return render_template('editform2.html', dict1 = my_data)

@app.route("/update2", methods = ["POST" , "GET"])
def update2():
	if request.method == "POST":
		global update_dict1
		global update_dict2
		global update_final
		global gid
		success = False
		update_dict2 = request.form.to_dict()
		if 'isallextracted' in update_dict2:
			pass
		else:
			update_dict2['isallextracted'] = 'No'
		now = datetime.now()
		now = now.strftime("%d/%m/%Y %H:%M:%S")
		formentry = {'formentry_time' : now}
		update_final = {"form1": update_dict1, "form2": update_dict2, "metadata": formentry}
		mongo.db.form.update({"_id" : ObjectId(gid)}, {"$set": update_final })
		return redirect(url_for('datalist'))


if __name__ == "__main__":
    app.run(debug=True)