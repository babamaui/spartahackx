import os
from dotenv import load_dotenv
import flask
import flask_cors
from rag import query

load_dotenv()

# flask app
app = flask.Flask(__name__)
flask_cors.CORS(app)

# routes
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/query")
def send_query():
    return query("What were the main reasons for the fall of the Roman Empire?")

@app.route("/ingest")
def ingest():
    return "Ingesting data..."

if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG'), port=os.environ.get('PORT'))