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
        """SELECT title, film_id as idPelis FROM film"""
    ).fetchall()
    pagina = render_template('pelis.html', film =lista_peliculas)

    return pagina



@bp.route('/detalle/<int:id>')
def detalle(id):
    db = get_db()
    consulta1 = """
        SELECT f.title,
        f.film_id
        FROM film f
        WHERE f.film_id = ?;
    """

    consulta2 = """
        SELECT f.title, c.name AS Nombre, c.category_id AS idCat, f.film_id  AS idF
        FROM film f
        JOIN film_category fc ON f.film_id = fc.film_id 
		JOIN category c ON fc.category_id = c.category_id
        WHERE f.film_id = ?;
    """
  
    resultado = db.execute(consulta1, (id,))
    film = resultado.fetchone()
    resultado = db.execute(consulta2, (id,))
    lista_generos = resultado.fetchall()
    

    pagina = render_template("detalleFilm.html", 
                           film=film,
                           listaGeneros=lista_generos)
    return pagina 