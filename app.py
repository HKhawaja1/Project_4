from flask import Flask, render_template

# Set up the Flask application object
app = Flask(__name__)

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

@app.route("/contact")
def contact():
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
