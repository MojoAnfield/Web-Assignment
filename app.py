import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)

def get_csv():
	csv_path = './static/info.csv'
	with open(csv_path,"r") as csv_file:
		csv_obj = csv.DictReader(csv_file)
		csv_list = list(csv_obj)
		return csv_list

@app.route("/")
def index():
	template = "index.html"
	return render_template(template)

@app.route("/<loc>/")
def detail(loc):
	template = "detail.html"
	loc_list = get_csv()
	for row in loc_list:
		if row['loc']==loc:
			return render_template(template, full_info=row)

if __name__=='__main__':
	app.run(debug=True, use_reloader= True)
