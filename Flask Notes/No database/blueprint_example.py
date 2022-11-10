from flask import Blueprint
from auth import auth


# inside of "blueprint_example" string should be the name of the file
example_blueprint = Blueprint("example_blueprint", __name__)


# It's recomended to add /example to every route as the main path of the blueprint routes to seperate the routes by path
@example_blueprint.route('/example', methods=['GET'])
@auth.login_required
def example():
    return {"message": 'This is a blueprint example'}
