from flask import Flask, Response

app = Flask(__name__)

def plaintext(s):
    return Response(s, mimetype="text/plain")

@app.route("/")
def index():
    return plaintext("Hello world!")

if __name__ == '__main__':
    app.run(debug=True)