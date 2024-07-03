import os

from flask import Flask

app = Flask(__name__)

with app.app_context():
   from . import db
   db.init_app(app)

from . import actor
app.register_blueprint(actor.bp)

from . import film
app.register_blueprint(film.bp)

from . import category
app.register_blueprint(category.bp)


