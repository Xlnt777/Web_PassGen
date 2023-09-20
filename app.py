from flask import Flask, render_template, jsonify, request
from gen_func import *
from string import ascii_lowercase, ascii_uppercase, digits
import json

app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html')


@app.route("/clicked", methods=['POST'])
def clicked():
	alphabet = ascii_lowercase
	length_pass = request.form.get('length_Input')
	count = request.form.get('password_Count')
	button_value1 = request.form.get('button_value1')
	button_value2 = request.form.get('button_value2')
	button_value3 = request.form.get('button_value3')

	if button_value1 == 'true': 
		alphabet += ascii_uppercase
	if button_value2 == 'true':
		alphabet += digits
	if button_value3 == 'true':
		alphabet += punctuation

	password = []
	
	for _ in range(int(count)):
		password.append(create_new(int(length_pass),alphabet))
	return jsonify(password=password)


if __name__ == '__main__':
	app.run(host="127.0.0.1", port="5000", debug=True)
