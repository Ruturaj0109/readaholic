from flask import Flask, render_template
from forms import AdminRegisterationForms, AdminLoginForm, AddBookForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key_33'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"

data = {
    "website_name": "Readaholic",
    "Author" : "Ruturaj Jadhav"
}

db= SQLAlchemy(app)
with app.app_context():
    db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return f"User(email:{self.email})"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120), nullable= False)
    author = db.Column(db.String(120), nullable= False)
    isbn = db.Column(db.Integer, unique= True, nullable= False)
    genre = db.Column(db.String(60), nullable= False)
    shoplink = db.Column(db.String(120), nullable= True)
    rating = db.Column(db.Float, nullable= False)
    cover_image = db.Column(db.String(120), nullable= True, default="default.jpg")
    summary = db.Column(db.Text, nullable= False)

    def __repr__(self):
        return f"Book(title: {self.title}, isbn: {self.isbn})"


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
        _email = form.data['email']
        _password = form.data['password']
        user = User(email= _email, password= _password)
        db.session.add(user)
        db.session.commit()
        print("User added")
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form= AdminLoginForm()
    return render_template("login.html", form =form)

@app.route("/add_books", methods=["GET", "POST"])
def add_book():
    form= AddBookForm()
    if form.validate_on_submit():
        print(form.data)
    return render_template("add_book.html", form=form)

    
# @app.route("/name1")
# @app.route("/name2")
# @app.route("/name3")
# def name1():
#     return f"<h1>{msg}</h1>"

if __name__ == "__main__":
    app.run(debug=True)