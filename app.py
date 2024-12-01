from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from models import db, ContactInquiry  # Import models from models.py
from dotenv import load_dotenv  # Import for loading environment variables
import os  # Import for accessing environment variables

# Load environment variables from .env file
load_dotenv()

# Set up the Flask application object
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')  # Load database URL from .env
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')  # For CSRF protection

# Initialize the database with the Flask app
db.init_app(app)

# Define the ContactForm class using Flask-WTF
class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Define routes for different sections of the website
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/collections")
def collections():
    return render_template("collections.html")

@app.route("/catalog")
def catalog():
    return render_template("catalog.html")

@app.route("/sale")
def sale():
    return render_template("sale.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():  # Validate the form on POST
        name = form.name.data
        email = form.email.data
        message = form.message.data

        try:
            # Save the inquiry to the database
            new_inquiry = ContactInquiry(name=name, email=email, message=message)
            db.session.add(new_inquiry)
            db.session.commit()
            flash("Thank you for your message! We'll get back to you soon.", "success")
        except Exception as e:
            flash("An error occurred while saving your message. Please try again.", "error")
            print(f"Error: {e}")
        return redirect(url_for("contact"))

    return render_template("contact.html", form=form)

@app.route('/candy')
def candy():
    return render_template('candy.html')

@app.route('/chocolate')
def chocolate():
    return render_template('chocolate.html')

@app.route('/cookies')
def cookies():
    return render_template('cookies.html')

# Run the application in debug mode (for development purposes)
if __name__ == "__main__":
    app.run(debug=True)
