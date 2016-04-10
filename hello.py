import os, json, logging
from flask import Flask, render_template, request


THIS_DIR = os.path.dirname(__file__)


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

app = Flask("PlanR", template_folder=tmpl_dir, static_folder=static_dir)


@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		write_data(request.form)
		return "thankyou" #render_template("thankyou.html")
	else:
		return render_template("websiteform.html")

		
def data_filepath(phone_number):
	file_name = "{}.json".format(phone_number)
	file_path = os.path.join(THIS_DIR, "data", file_name)
	return file_path
	
def write_data(data):
	phone_number = data["phone"]
	file_path = data_filepath(phone_number)
	f = open(file_path, "w")
	datastring = json.dumps(request.form)
	f.write(datastring)
	f.close
	
	
#def read_data(name):
#	o = open(name, "r")
#	readfile = o.read
	
	
		
if __name__ == '__main__':
	app.debug = True
	app.run()
	


