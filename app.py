from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from models import db, ContactInquiry
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up the Flask application object
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

# Initialize database and CSRF protection
db.init_app(app)
csrf = CSRFProtect(app)

# Define the ContactForm class using Flask-WTF
class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Define the UpdateContactForm class using Flask-WTF
class UpdateContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Update")

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

# Create inquiry route
@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        try:
            new_inquiry = ContactInquiry(name=name, email=email, message=message)
            db.session.add(new_inquiry)
            db.session.commit()
            flash("Thank you for your message! We'll get back to you soon.", "success")
        except Exception as e:
            flash("An error occurred while saving your message. Please try again.", "error")
            print(f"Error: {e}")
        return redirect(url_for("contact"))

    return render_template("contact.html", form=form)

# Read: List all inquiries
@app.route("/list_contacts")
def list_contacts():
    page = request.args.get("page", 1, type=int)
    per_page = 5
    inquiries = ContactInquiry.query.paginate(page=page, per_page=per_page)
    return render_template("list_contacts.html", inquiries=inquiries)

# Update an inquiry
@app.route("/update_contact/<int:inquiry_id>", methods=["GET", "POST"])
def update_contact(inquiry_id):
    inquiry = ContactInquiry.query.get_or_404(inquiry_id)
    form = UpdateContactForm(obj=inquiry)

    if form.validate_on_submit():
        inquiry.name = form.name.data
        inquiry.email = form.email.data
        inquiry.message = form.message.data

        try:
            db.session.commit()
            flash("Contact updated successfully.", "success")
            return redirect(url_for("list_contacts"))
        except Exception as e:
            flash("An error occurred while updating the contact.", "error")
            print(f"Error: {e}")

    return render_template("update_contact.html", form=form, inquiry=inquiry)

# Delete an inquiry
@app.route("/delete_contact/<int:inquiry_id>", methods=["POST"])
def delete_contact(inquiry_id):
    inquiry = ContactInquiry.query.get_or_404(inquiry_id)

    try:
        db.session.delete(inquiry)
        db.session.commit()
        flash("Contact deleted successfully.", "success")
    except Exception as e:
        flash("An error occurred while deleting the contact.", "error")
        print(f"Error: {e}")

    return redirect(url_for("list_contacts"))

@app.route('/candy')
def candy():
    return render_template('candy.html')

@app.route('/chocolate')
def chocolate():
    return render_template('chocolate.html')

@app.route('/cookies')
def cookies():
    return render_template('cookies.html')

if __name__ == "__main__":
    app.run(debug=True)
