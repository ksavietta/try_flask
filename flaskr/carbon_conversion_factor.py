from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('carbon_conversion_factor', __name__)

@bp.route('/')
def index():
    db = get_db()
    carbon_conversion_factors = db.execute(
        'SELECT *'
        ' FROM carbon_conversion_factor factor '
        ' ORDER BY created DESC'
    ).fetchall()
    print('factors:')
    print(carbon_conversion_factors)
    return render_template('carbon_conversion_factor/index.html', carbon_conversion_factors=carbon_conversion_factors)

def get_conversion_factor(id):
    factor = get_db().execute(
        'SELECT f.id, display_name, api_name'
        ' FROM carbon_conversion_factor f '
        ' WHERE f.id = ?',
        (id,)
    ).fetchone()

    if factor is None:
        abort(404, "Carbon Conversion Factor id {0} doesn't exist.".format(id))

    return factor
