from flask_frozen import Freezer
from app import app, get_csv
freezer = Freezer(app)

@freezer.register_generator
def detail():
	for row in get_csv():
		yield {"loc":row['loc']}

if __name__ == '__main__':
	freezer.freeze()