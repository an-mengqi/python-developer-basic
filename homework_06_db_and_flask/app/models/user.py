from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from models.db import db
from models.mixins.created_at_mixin import CreatedAtMixin


class User(CreatedAtMixin, db.Model):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str | None] = mapped_column(unique=True)
    full_name: Mapped[str | None] = mapped_column(String(50), index=True)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            "User("
            f"id={self.id}"
            f", username={self.username!r}"
            f", email={self.email!r}"
            ")"
        )
