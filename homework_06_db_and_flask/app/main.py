from flask import Flask, request, render_template
from flask_migrate import Migrate

from views.items import items_app
from views.products import products_app

import config
from models import db

app = Flask(__name__)

# python -c 'import secrets; print(secrets.token_hex())'

app.config.update(
    SECRET_KEY="6fc01f2db60feff0f53537060",
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_ECHO=config.SQLALCHEMY_ECHO,
)

app.register_blueprint(
    items_app,
)
app.register_blueprint(
    products_app,
)
db.init_app(app)
migrate = Migrate(app, db)


@app.get("/", endpoint="index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
