import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():

    dbname=os.environ.get('DB_NAME');
    
    if dbname==None:
        return "Hello, Flask! This is mainprog.py ! ENV DB_NAME IS NOT DEFINED"
    else:    
        return "Hello, Flask! This is mainprog.py ! ENV DB_NAME =" + dbname