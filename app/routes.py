from flask import Flask, render_template  #from the flask "module" import

app = Flask(__name__)    # instaniate the flask class into the app variable (object)


                     
#@app.get("/")                            # decorator that allows us to map routes to "view function"
#def index():                             # flask calls these "view functions"
    #return "<h1>hellow, world!</h1>"     # return statment


@app.get("/")
def index():
   return render_template("index.html")

@app.get("/about")
def about():
    me = {
        "first_name": "bret",
        "last_name": "patterson",
        "hobbies": "jj",
        "bio": "my name is bret patterson and i am a student"
    }
    return render_template("about.html", about_dict=me)

@app.get("/objects")
def objects():
    return render_template("objects.html")