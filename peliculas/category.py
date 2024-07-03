from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from peliculas.db import get_db

bp = Blueprint('category', __name__, url_prefix='/generos')


@bp.route('/')
def index():
    db = get_db()
    lista_generos = db.execute(
        """SELECT name FROM category"""
    ).fetchall()
    pagina = render_template('genero.html', category =lista_generos)

    return pagina