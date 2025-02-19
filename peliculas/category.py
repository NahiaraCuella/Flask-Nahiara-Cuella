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
        """SELECT name, category_id AS idG FROM category"""
    ).fetchall()
    pagina = render_template('genero.html', category =lista_generos)

    return pagina




@bp.route('/detalle/<int:id>')
def detalle(id):
    db = get_db()
    consulta1 = """
        SELECT c.name,
        c.category_id
        FROM category c
        WHERE c.category_id = ?;
    """

    consulta2 = """
        SELECT c.name , f.title AS Titulo, f.film_id AS idF, c.category_id  AS idCat
        FROM category c
        JOIN film_category fc ON f.film_id = fc.film_id 
		JOIN film f ON fc.film_id = f.film_id
        WHERE c.category_id = ?;
    """
  
    resultado = db.execute(consulta1, (id,))
    category = resultado.fetchone()
    resultado = db.execute(consulta2, (id,))
    lista_peliculas = resultado.fetchall()
    

    pagina = render_template("detalleCategory.html", 
                           category=category,
                           listaPeliculas=lista_peliculas)
    return pagina 