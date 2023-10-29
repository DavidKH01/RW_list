import flask
from flask import Flask, request, render_template
import json
# import flask_cors 
from flask_cors import CORS
import sys
sys.path.append("C:/Users/Danny/Documents/Code/read_watch_list/rw_backend")
import rw_dbqueires as rwq

app = Flask(__name__)
CORS(app)

@app.route("/") #methods=['GET','POST'])
def hello_world():
    
     return (json.dumps(rwq.getList()))
    # return (rwq.getList())
    # return flask.jsonify("Hello, World! / app is running",) 


if __name__ == '__main__':
    app.debug = True
    app.run()