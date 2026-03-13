# Import dependencies
from flask import Flask, render_template, request


# Create an instance of the Flask class in the app variable
app = Flask(__name__)


# Define the route for the index page at domain root
@app.route("/", methods=["GET", "POST"])
def index_page():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        check = request.form.get("check")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print(f"Check: {check}")
    return render_template("index.html"), 200


# Initialize the Flask application
if __name__ == "__main__":
    app.run(debug=True)
