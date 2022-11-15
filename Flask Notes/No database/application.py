import os
from flask import Flask
from flask_cors import CORS

from blueprint_example import example_blueprint  # imports from blueprint
from auth import auth

from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
CORS(app)

# connects blueprint to the app routes
app.register_blueprint(example_blueprint)


# This is how a route works
@app.route('/', methods=['GET'])
@auth.login_required
def root():
    user = auth.current_user()
    print(user)
    return {"message": 'ok bro'}


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
