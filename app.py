from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# uploads folder automatically create karega
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():

    name = request.form["name"]
    email = request.form["email"]
    details = request.form["details"]

    file = request.files["file"]

    if file and file.filename != "":

        file.save(
            os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )
        )

        print("Name:", name)
        print("Email:", email)
        print("Details:", details)

        return """
        <h1>Thank You!</h1>
        <p>Your project has been submitted successfully.</p>
        """

    return "No file selected"

if __name__ == "__main__":
    app.run(debug=True)