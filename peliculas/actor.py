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
        """SELECT first_name,last_name, actor_id AS idActor FROM actor"""
    ).fetchall()
    pagina = render_template('actores.html', actor=lista_actores)

    return pagina


@bp.route('/detalle/<int:id>')
def detalle(id):
    db = get_db()
    consulta1 = """
        SELECT ac.first_name,ac.last_name,
        ac.actor_id
        FROM actor ac
        WHERE ac.actor_id = ?;
    """

    consulta2 = """
        SELECT ac.first_name,f.title as Titulo, f.film_id,ac.actor_id AS idAct
        FROM actor ac
        JOIN film_actor fa ON ac.actor_id = fa.actor_id
		JOIN film f ON f.film_id = fa.film_id
        WHERE ac.actor_id = ?;
    """
  
    resultado = db.execute(consulta1, (id,))
    actor = resultado.fetchone()
    resultado = db.execute(consulta2, (id,))
    lista_peliculas = resultado.fetchall()
    

    pagina = render_template("detalleActor.html", 
                           actor=actor,
                           listaPeliculas=lista_peliculas)
    return pagina 