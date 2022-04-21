from flask import Blueprint, render_template, request
from libs.logic import Logic

crslist = Blueprint('courses_list', __name__)
logic = Logic()


@crslist.route('/crslist.php', methods=['GET'])
def crs_list():
    return render_template(f'./{request.args.get("username")}.html')
