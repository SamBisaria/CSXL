from typing import Optional, Self, Tuple

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

from backend.entities.entity_base import EntityBase


__authors__ = ["Ajay Gandecha", "Jade Keegan", "Brianna Ta", "Audrey Toney"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class UserPostAssociation(EntityBase):
    __tablename__ = "user_post_assocation"
    num: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    user: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    news_post: Mapped[int] = mapped_column(Integer, ForeignKey("news_post.id"))
    score: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    # _posts: Mapped["PostEntity"] = relationship()
    # backref="posts"
    # users: Mapped["UserEntity"] = relationship(back_populates="posts")

    @classmethod
    def from_model(cls, user: int, post: int, value: int) -> Self:
        return cls(user=user, news_post=post, score=value)

    @classmethod
    def get_user(self) -> int:
        return self.user

    @classmethod
    def get_score(self) -> int:
        return self.score
