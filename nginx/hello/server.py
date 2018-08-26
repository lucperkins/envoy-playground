from flask import Flask, Response

PORT = 1111

app = Flask(__name__)

@app.route('/')
def hello():
    return Response('Hello world!', mimetype='text/plain')

if __name__ == '__main__':
    print('Starting up on port %d' % PORT)
    app.run(debug=True, host='0.0.0.0', port=PORT)