from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Hi"
if __name__ == "__main__":
    app.run("0.0.0.0", "5050")
# 8080->5050