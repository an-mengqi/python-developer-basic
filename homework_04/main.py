"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from homework_04.models import User, Post, Session, create_tables
from sqlalchemy.ext.asyncio import AsyncSession
from jsonplaceholder_requests import get_users_data, get_posts_data
from typing import List


async def create_users(session: AsyncSession, data: List[dict]):
    for user_parameter in data:
        user = User(id=user_parameter['id'], name=user_parameter['name'], username=user_parameter['username'],
                    email=user_parameter['email'])
        session.add(user)
    await session.commit()


async def create_posts(session: AsyncSession, data: List[dict]):
    for post_parameters in data:
        post = Post(title=post_parameters['title'], body=post_parameters['body'], user_id=post_parameters['userId'])
        session.add(post)
    await session.commit()


async def async_main():
    await create_tables()
    user_fetch, posts_fetch = await asyncio.gather(
        get_users_data(),
        get_posts_data()
    )

    async with Session() as session:
        await create_users(
            session,
            user_fetch
        )
        await create_posts(
            session,
            posts_fetch
        )


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
