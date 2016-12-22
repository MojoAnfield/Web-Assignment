#import necessary libraries
import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)

def get_csv():
	csv_path = './static/info.csv'			#load info.csv
	with open(csv_path,"r") as csv_file:	
		csv_obj = csv.DictReader(csv_file)	#DictReader is a built-in func to create dict
		csv_list = list(csv_obj) 			#convert to list for parsing 
		return csv_list

@app.route("/")		#from base directory, access index.html via "/"
def index():
	template = "index.html"
	return render_template(template)

@app.route("/<loc>/")	#from base directory, access detailed file via "/loc"(e.g./丹青学园)
def detail(loc):
	template = "detail.html"
	loc_list = get_csv()	#retrieve full info
	for row in loc_list:
		if row['loc']==loc:
			return render_template(template, full_info=row)
	abort(404)	#404 Not Found if the location doesn't exist

if __name__=='__main__':
	app.run(debug=True, use_reloader= True)
