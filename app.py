from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return("<p>This is a test page to check how AWS-elastic-bean-stalk based deplyoment works</p>")


if __name__ == "__main__":
    app.run()
