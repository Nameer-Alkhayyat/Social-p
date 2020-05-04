from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post, get_posts
from jinja2 import Environment 





app = Flask(__name__)
CORS(app)


#make a request to send or recive data!
@app.route("/", methods= ["GET", "POST"])
def index(): 
    posts = get_posts()
    print(posts)
#when the user request infon from our db or website
    if request.method == "GET":
        #return render_template("index.html", posts=posts)
        pass   
    

    #when the user is sending data back to the server or db
    if request.method == "POST":
        name=request.form.get("name")
        post=request.form.get("post")
        create_post(name, post)
    posts = get_posts
    return render_template("index.html", posts=posts)



if __name__ == "__main__":
    app.run(debug=True)
