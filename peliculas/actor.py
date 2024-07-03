from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from peliculas.db import get_db

bp = Blueprint('actor', __name__, url_prefix='/actores')


@bp.route('/')
def index():
    db = get_db()
    lista_actores = db.execute(
        """SELECT first_name,last_name FROM actor"""
    ).fetchall()
    pagina = render_template('actores.html', actor=lista_actores)

    return pagina