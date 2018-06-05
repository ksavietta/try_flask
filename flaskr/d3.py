from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('d3', __name__)

@bp.route('/d3')
def index():
    db = get_db()
    return render_template('d3/index.html')
