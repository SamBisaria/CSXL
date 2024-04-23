from typing import Optional, Self, Tuple

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

from backend.entities.comment_entity import CommentEntity
from backend.entities.entity_base import EntityBase
from backend.entities.user_entity import UserEntity
from backend.models.news_comments_no_user import NewsComments
from backend.models.user import User


__authors__ = ["Ajay Gandecha", "Jade Keegan", "Brianna Ta", "Audrey Toney"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class UserCommentAssociation(EntityBase):
    __tablename__ = "user_comment_association"
    num: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    news_comment: Mapped[int] = mapped_column(Integer, ForeignKey("news_comments.id"))
    score: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    _comments: Mapped["CommentEntity"] = relationship(back_populates="users")
    # users: Mapped["UserEntity"] = relationship(back_populates="comments")

    @classmethod
    def from_model(cls, user: int, comment: int, value: int) -> Self:
        return cls(user=user, news_comment=comment, score=value)

    @classmethod
    def get_user(self) -> int:
        return self.user

    @classmethod
    def get_score(self) -> int:
        return self.score
