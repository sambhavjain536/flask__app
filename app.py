from unicodedata import name
from flask import Flask
app= Flask(__name__)

@app.route('/')
def testme():
    return "Welcome to the flask application"
@app.route('/user/<name>')
def show_name(name):
   return "Welcome %s to flask app" % name
if __name__=='__main__':
    app.run()