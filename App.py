from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)
#app.debug = True


@app.route('/')
def landing():
    view = 'landing'
    
    return render_template('landing.html', view=view)

@app.route('/graph/')
def graph():
    view = 'graph'
    graph_type = request.args.get('graph_type')
    graph_name = request.args.get('graph_name')
    
    if graph_type == None or graph_name == None:
        return redirect('/graph?graph_type=node&graph_name=Node Location')
    
    return render_template('graph.html', view=view, graph_type=graph_type, graph_name=graph_name)

if __name__ == "__main__":
    app.run()
    