# pylint: disable=print-statement

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("WhatsMyName.html")

@app.route("/process", methods=['POST'])
def process():
    print "Got Post Info"
    name = request.form["name"]
    email = request.form["email"]
    print "Name:", name, "Email:", email
    return redirect("/")
app.run(debug=True)
