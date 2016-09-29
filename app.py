import random
from flask import Flask, render_template, request
app = Flask(__name__)




@app.route("/")
def pagetwo():
    print "\n\n\n"
    print ":::DIAG::: this flask obj"
    print app
    print ":::DIAG::: this request object obj"
    print request
    print ":::DIAG::: this request.args object obj"
    #print request.args["username"]

    return render_template("login.html")

@app.route("/auth", methods=['POST'])
def authenitcate():
    if (request.form["username"] == "patrick" and request.form["password"] == "star" ):
        return render_template("success.html")
    else:
        return render_template("failed.html")
    

    


if __name__=="__main__":
    app.run(debug = True)

