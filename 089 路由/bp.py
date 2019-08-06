from flask import Blueprint

bp = Blueprint('app01', __name__, url_prefix='/app01')


@bp.route('/user')
def user():
    return 'I am app01!'
