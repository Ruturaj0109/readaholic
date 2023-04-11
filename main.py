from flask import Flask, render_template

app = Flask(__name__)

# msg = "Hello, Ruturaj"
# website_name = "Readaholic"
data = {
    "website_name": "Readaholic",
    "Author" : "Ruturaj Jadhav"
}

@app.route("/")
def home():
    # return render_template("home.html", website_name=website_name)
    return render_template("home.html", data=data)


@app.route("/about")
def about():
    return "<h1>About Page</h1>"

# @app.route("/name1")
# @app.route("/name2")
# @app.route("/name3")
# def name1():
#     return f"<h1>{msg}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
