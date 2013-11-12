from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def landing():
    view = 'landing'
    
    return render_template('landing.html', view=view)

@app.route('/graph/')
def graph():
    view = 'graph'
    graph = request.args.get('graph')
    
    return render_template('graph.html', view=view, graph=graph)

if __name__ == "__main__":
    app.run()
    