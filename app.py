from flask import Flask, render_template, request
import dirac

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    #return str(english_bot.get_response(userText))
    return str(dirac.ask(userText))


if __name__ == "__main__":
    app.run(app.run(host= '0.0.0.0'))