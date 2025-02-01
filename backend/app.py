import os
from dotenv import load_dotenv
import flask
import flask_cors

load_dotenv()

# flask app
app = flask.Flask(__name__)
flask_cors.CORS(app)

# routes
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/hello")
def hello_api():
    return flask.jsonify({"message": "Hello World!"})

if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG'), port=os.environ.get('PORT'))
