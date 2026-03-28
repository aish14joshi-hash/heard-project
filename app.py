from flask import Flask, render_template

# Create Flask app
app = Flask(__name__)

# ------------------------
# ROUTES
# ------------------------

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Gesture to Text page
@app.route("/gesture")
def gesture_to_text():
    return render_template("gesture_to_text.html")

# Text to Gesture page
@app.route("/text")
def text_to_gesture():
    return render_template("text_to_gesture.html")

# Learn page
@app.route("/learn")
def learn():
    return render_template("learn.html")

# Emergency page
@app.route("/emergency")
def emergency():
    return render_template("emergency.html")

# 404 Error page
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


# ------------------------
# IMPORTANT FOR RENDER
# ------------------------

if __name__ == "__main__":
    app.run(debug=True)
