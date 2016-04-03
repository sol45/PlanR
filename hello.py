import json
from flask import Flask, render_template

app = Flask("PlanR")

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		write_data(request.form)
		return render_template("thankyou.html")
	else:
		return render_template("websiteform.html")

def write_data(data):
	
	
		
if __name__ == '__main__':
	app.debug = True
	app.run()
	

	
