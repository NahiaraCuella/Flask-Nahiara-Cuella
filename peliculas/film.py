from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from peliculas.db import get_db

bp = Blueprint('film', __name__, url_prefix='/peliculas')


@bp.route('/')
def index():
    db = get_db()
    lista_peliculas = db.execute(
        """SELECT title FROM film"""
    ).fetchall()
    pagina = render_template('pelis.html', film =lista_peliculas)

    return pagina