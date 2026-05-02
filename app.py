from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary storage (list)
classmates = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        section = request.form["section"]
        subject = request.form["subject"]

        classmates.append({
            "name": name,
            "section": section,
            "subject": subject
        })

        return redirect("/")

    return render_template("index.html", classmates=classmates)

if __name__ == "__main__":
    app.run(debug=True)