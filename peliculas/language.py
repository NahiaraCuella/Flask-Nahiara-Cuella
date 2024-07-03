from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from peliculas.db import get_db

bp = Blueprint('language', __name__, url_prefix='/lenguajes')


@bp.route('/')
def index():
    db = get_db()
    lista_lenguajes = db.execute(
        """SELECT name FROM language"""
    ).fetchall()
    pagina = render_template('lenguaje.html', language=lista_lenguajes)

    return pagina