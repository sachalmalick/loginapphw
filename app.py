import random, csv
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

def readcsv():
    with open('data.csv', 'rb') as csvfile:
        read = csv.reader(csvfile)
        listify = list(read)
        return listify


def writecsv(username,password):
    with open('data.csv','a') as csvfile:
        write = csv.writer(csvfile)
        write.writerow([username,password])

def checkexist(username):
    checklist = readcsv()
    for x in checklist:
        if(x[0] == username):
            return True
    return False

def login(username,password):
    if(checkexist(username)):
        for x in filelist:
            if(x[0] == username):
                if(x[1] == password):
                    return render_template("success.html")
                else:
                    return render_template("login.html",displaymessage = "Incorrect password")
                
    else:
        return render_template("login.html",displaymessage = "That username doesnt exist")
    
@app.route("/sort", methods=['POST'])
def sort():
    username = request.form["username"]
    password = request.form["password"]
    filelist = readcsv()
    if (request.form["go"] == "login"):
        if(checkexist(username)):
            for x in filelist:
                if(x[0] == username):
                    if(x[1] == password):
                        return render_template("success.html")
                    else:
                        return render_template("login.html",displaymessage = "Incorrect password")
                
        else:
            return render_template("login.html",displaymessage = "That username doesnt exist")
    else:
        if(checkexist(username)):
            return render_template("login.html",displaymessage = "That username already exists")
        else:
            writecsv(username,password)
            
            return render_template("login.html",displaymessage = "Account successfully created")
        
    
        
            
    

@app.route("/auth", methods=['POST'])
def authenitcate(username,password):
    #username = request.form["username"]
    #password = request.form["password"]
    if(checkexist(username)):
        for x in filelist:
            if(x[0] == username):
                if(x[1] == password):
                    return render_template("success.html")
                else:
                    return render_template("login.html",displaymessage = "Incorrect password")

    else:
        return render_template("login.html",displaymessage = "That username doesnt exist")

    
@app.route("/register", methods=['POST'])
def register(username,password):
    #username = request.form["username"]
    #password = request.form["password"]
    if(checkexist(username)):
        return render_template("login.html",displaymessage = "That username already exists")
    else:
        writecsv(username,password)
        return render_template("login.html",displaymessage = "Account successfully created")
        
    

    

    


if __name__=="__main__":
    app.run(debug = True)

