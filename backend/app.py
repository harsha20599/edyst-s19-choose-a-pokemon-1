from flask import Flask,render_template
import simplejson as json
app=Flask(__name__)

# error handler for invalid url
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html")

@app.route('/api/pokemon/',methods=['GET','POST'])
def pokeman():
	data={'pokeman':["bulbasaur","charmander","squirtle"]}
	return json.dumps(data)
		
if (__name__=='__main__'):
	app.run(port=8006)
