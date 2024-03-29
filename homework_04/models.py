"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
from __future__ import annotations

import os
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Text
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://username:passwd@localhost:5433/blog"
DB_ECHO = False

async_engine = create_async_engine(PG_CONN_URI)

Session = async_sessionmaker(
    bind=async_engine,
    autocommit=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


association_table = Table(
    "association_table",
    Base.metadata,
    Column("user_id", ForeignKey("user_table.id"), primary_key=True),
    Column("post_id", ForeignKey("post_table.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "user_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name = Column(String(50), nullable=False)
    username = Column(String(30), nullable=False)
    email = Column(String, nullable=False)
    posts: Mapped[List["Post"]] = relationship(back_populates="user")

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


class Post(Base):
    __tablename__ = "post_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    title = Column(String(100), nullable=False, default="", server_default="",)
    body = Column(Text, nullable=False, default="", server_default="",)
    user: Mapped[List["User"]] = relationship(back_populates="posts")

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"Post(id={self.id}, "
            f"title={self.title!r}, "
            f"user_id={self.user_id})"
            f"body={self.body}, "
        )


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
