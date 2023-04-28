from flask import render_template, flash, redirect, url_for, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from readaholic.forms import AdminRegisterationForms, AdminLoginForm, AddBookForm, AddComment
from readaholic import app, db, bcrypt
from readaholic.models import User, Comment, Book
import os
from uuid import uuid4

@app.route("/")
@login_required
def home():
    book_data=Book.query.all()
    for b in book_data:
        print(b.cover_image)
    # return render_template("home.html", website_name=website_name)
    return render_template("home.html", data=book_data)
    # return render_template("home.html", data=book_data)


@app.route("/about")
def about():
    return "<h1>About Page</h1>"

@app.route("/register", methods=["GET", "POST"])
def register():
    form = AdminRegisterationForms()
    if form.validate_on_submit():
        _email = form.data['email']
        _password = form.data['password']
        _password = bcrypt.generate_password_hash(_password).decode("utf-8")
        user = User(email= _email, password= _password)
        try:
            db.session.add(user)
            db.session.commit()
            # print("User added")
            flash("Account successfully created, you may now login", "success")
            return redirect(url_for('login'))
        except:
            # print("Failed to add user")
            flash("Something went wrong with database", "warning")
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in!", "info")
        return redirect(url_for('home'))

    form= AdminLoginForm()
    if form.validate_on_submit():
        _email = form.data['email']
        _password = form.data['password']
        user = User.query.filter_by(email=_email).first()
        if not user:
            flash(f"No user with email {_email} found! Register today.", "danger" )
            return redirect(url_for("register"))
        else:
            if bcrypt.check_password_hash(user.password, _password):
                login_user(user)
                flash("Successfully logged in!", "success")
                return redirect(url_for("home"))
            else:
                flash("You've entered wrong password, please try again!", "danger")

    return render_template("login.html", form =form)

def save_cover_image(cover_image):
    f = cover_image.data
    filename = f"picture-{str(uuid4())}.{f.filename.split('.')[1].lower()}"
    f.save(os.path.join(app.instance_path, "uploads", filename))
    return filename


@app.route("/add_books", methods=["GET", "POST"])
@login_required
def add_book():
    form= AddBookForm()
    if form.validate_on_submit():
        _title = form.data['title']
        _author = form.data['author']
        _isbn = form.data['isbn']
        _genre = form.data['genre']
        _shoplink = form.data['shoplink']
        _rating = form.data['rating']
        _cover_image = save_cover_image(form.cover_image)
        _summary = form.data['summary']
        book = Book(
            title = _title, author = _author, isbn = _isbn, genre=_genre, shoplink=_shoplink, rating=_rating, cover_image=_cover_image ,summary=_summary)
        try:
            db.session.add(book)
            db.session.commit()
            flash("Book added successfully!", "success")
        except:
            flash("Something went wrong", "warning")

    return render_template("add_book.html", form=form)

@app.route("/comment", methods=["GET", "POST"])
def comment():
    form= AddComment()
    if form.validate_on_submit():
        _name = form.data['name']
        _email = form.data['email']
        _summary = form.data['summary']
        comment = Comment(name = _name, email = _email, summary = _summary)
        db.session.add(comment)
        db.session.commit()
        # print("Comment added")
        
    return render_template("comment.html", form=form)

@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    flash("You've successfully logged out", "success")
    return redirect(url_for("login"))

@app.route("/uploads/<filename>", methods=["GET"])
def send_image_file(filename):
    return send_from_directory(os.path.join(app.instance_path, "uploads"), filename)
