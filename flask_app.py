

from flask import Flask,render_template

app=Flask(__name__)


@app.route("/")
def home():
	return "Andella level up"

@app.route("/website")
def mugabe():
    return render_template('WEB.html')

if __name__ == '__main__':
	app.run()
