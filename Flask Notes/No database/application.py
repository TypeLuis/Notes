import os
from flask import Flask
from flask_cors import CORS

# imports from blueprint
from example import example_blueprint

app = Flask(__name__)
CORS(app)

# connects blueprint to the app routes
app.register_blueprint(example_blueprint)

# This is how a route works


@app.route('/', methods=['GET'])
def root():
    return {"message": 'ok'}


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
