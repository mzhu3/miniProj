from flask import Flask,flash,redirect,render_template,request,session,abort, url_for #Imports the Flask class from the flask package that we installed
app = Flask(__name__) #Creates an instance of this class

@app.route("/") #Makes hello_world show up when the root folder ("/") of the server is accessed by a user
def hello_world():
    return "This is the homepage"

@app.route("/members/")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return render_template('template.html',name =name)

if __name__ == "__main__": #Ensures that the app will only start if this file is not being imported from somewhere else but rather being accessed directly
    app.run()


