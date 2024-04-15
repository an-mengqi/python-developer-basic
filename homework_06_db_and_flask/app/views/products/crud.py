"""
Create
Read
Update
Delete
"""
from sqlalchemy import select

from models import db, Product


def create_product(name: str) -> Product:
    product = Product(name=name)
    db.session.add(product)
    db.session.commit()
    return product


def get_products() -> list[Product]:
    return list(db.session.scalars(select(Product)).all())
