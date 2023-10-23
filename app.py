from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__,)


@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
            print(transcript)
    return render_template('index.html', transcript=transcript)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template('contact.html')


@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
