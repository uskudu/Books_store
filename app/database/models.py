from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Book(Base):
    title: Mapped[str] = mapped_column(nullable=False, index=True)
    author: Mapped[str] = mapped_column(nullable=False, index=True)
    year: Mapped[int] = mapped_column(nullable=False)  # when was written
    description: Mapped[str]
    price: Mapped[int] = mapped_column(nullable=False, index=True)
    bought: Mapped[int] = mapped_column(nullable=False)  # how many times bought
    returned: Mapped[int] = mapped_column(nullable=False)  # how many times returned
    rating: Mapped[float] = mapped_column(nullable=False, default=0, index=True)  # 0 - 5


class User(Base):
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    money: Mapped[int] = mapped_column(nullable=False, default=0, index=True)

    history: Mapped[list['UserHistory']] = relationship(back_populates='user')


class UserHistory(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'))
    action: Mapped[str] # what happened (eg: user_id bought book_id / user_id returned book_id)

    user: Mapped['User'] = relationship(back_populates='history')
