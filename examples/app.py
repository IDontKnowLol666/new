from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def projects():
    return 'I hate flask'


if __name__ == "__main__":
    app.run(debug=True)
