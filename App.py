from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/landing/')
def landingPage():
    view = request.args.get('view')
    
    return render_template('landing.html', view=view)

if __name__ == "__main__":
    app.run()
    