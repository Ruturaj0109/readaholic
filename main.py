from flask import Flask, render_template
from forms import AdminRegisterationForms, AdminLoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key_33'
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

@app.route("/register", methods=["GET", "POST"])
def register():
    form = AdminRegisterationForms()
    if form.validate_on_submit():
        print(form.data)
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form= AdminLoginForm()
    return render_template("login.html", form =form)

    
# @app.route("/name1")
# @app.route("/name2")
# @app.route("/name3")
# def name1():
#     return f"<h1>{msg}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
