from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def hello():
    return Response('Hello world!', mimetype='text/plain')

if __name__ == '__main__':
    print('Starting up on port 5000')
    app.run(debug=True, host='0.0.0.0', port=5000)