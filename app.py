from distutils.log import debug
import flask
from flask import Flask

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "Starting Machine learning Project flow with CI/CD pipeline"

if __name__=="__main__":
    app.run(debug=True)
