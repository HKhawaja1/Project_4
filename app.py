from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
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
app.secret_key = 'your_secret_key'

# Initialize the database with the Flask app
db.init_app(app)

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
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Validation
        if not name or not email or not message:
            flash("All fields are required!", "error")
            return redirect("/contact")

        try:
            # Save the inquiry to the database
            new_inquiry = ContactInquiry(name=name, email=email, message=message)
            db.session.add(new_inquiry)
            db.session.commit()

            flash("Thank you for your message! We'll get back to you soon.", "success")
        except Exception as e:
            flash("An error occurred while saving your message. Please try again.", "error")
            print(f"Error: {e}")

        return redirect("/contact")

    return render_template("contact.html")

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
