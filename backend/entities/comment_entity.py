"""Definition of SQLAlchemy table-backed object mapping entity for Organizations."""

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.news_comments import NewsCommentsUser
from backend.models.news_comments_no_user import NewsComments
from backend.models.user import User
from .entity_base import EntityBase
from typing import Self
from ..models.news_post import PostModel

__authors__ = ["Ajay Gandecha", "Jade Keegan", "Brianna Ta", "Audrey Toney"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class CommentEntity(EntityBase):
    """Serves as the database model schema defining the shape of the `Organization` table"""

    # Name for the organizations table in the PostgreSQL database
    __tablename__ = "news_comments"

    # Organization properties (columns in the database table)

    # Unique ID for the organization
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    # Name of the organization
    content: Mapped[str] = mapped_column(String, nullable=False, default="")
    # Short hand name of the organization
    upvote: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    downvote: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    publish_date: Mapped[str] = mapped_column(String)
    mod_date: Mapped[str] = mapped_column(String)

    # all of the foreign key mapping
    # the way this works is if the parent comment is null, then the post has to be populated, and
    # if the post is null then it has to have a parent comment.
    parent_comment: Mapped[int] = mapped_column(
        ForeignKey("news_comments.id"), nullable=True
    )

    parent_post: Mapped[int] = mapped_column(ForeignKey("news_post.id"), nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    # figure out if we want thi later:
    # user: Mapped["UserEntity"] = relationship(back_populates="posts")

    users: Mapped[list["UserCommentAssociation"]] = relationship(backref="comments")

    @classmethod
    def from_model(cls, model: PostModel) -> Self:
        """
        Class method that converts an `Organization` model into a `OrganizationEntity`

        Parameters:
            - model (Organization): Model to convert into an entity
        Returns:
            OrganizationEntity: Entity created from model
        """
        return cls(
            id=model.id,
            content=model.content,
            upvote=model.upvote,
            downvote=model.downvote,
            publish_date=model.published_timestamp,
            mod_date=model.mod_date,
            parent_comment=model.parent_comment,
            parent_post=model.parent_post,
            user_id=model.user_id,
            upvote_users=model.upvote_users,
        )

    def from_model_user(cls, model: PostModel) -> Self:
        """
        Class method that converts an `Organization` model into a `OrganizationEntity`

        Parameters:
            - model (Organization): Model to convert into an entity
        Returns:
            OrganizationEntity: Entity created from model
        """
        return cls(
            id=model.id,
            content=model.content,
            upvote=model.upvote,
            downvote=model.downvote,
            publish_date=model.published_timestamp,
            mod_date=model.mod_date,
            parent_comment=model.parent_comment,
            parent_post=model.parent_post,
            user_id=model.user_id,
            upvote_users=model.upvote_users,
            users=[
                user_comment_association.UserCommentAssociation.from_model(
                    i, model.id, k
                )
                for i, k in model.comment_users
            ],
        )

    def to_model_user_data(self) -> NewsComments:
        """
        Converts a `OrganizationEntity` object into a `Organization` model object

        Returns:
            Organization: `Organization` object from the entity
        """
        return NewsCommentsUser(
            id=self.id,
            content=self.content,
            upvote=self.upvote,
            downvote=self.downvote,
            publish_date=self.publish_date,
            mod_date=self.mod_date,
            parent_comment=self.parent_comment,
            parent_post=self.parent_post,
            user_id=self.user_id,
            comment_users={i.get_user(): i.get_score for i in self.users},
        )

    def to_model_normal(self) -> NewsComments:
        """
        Converts a `CommentEntity` object into a `NewsComments` model object

        Returns:
        """
        return NewsComments(
            id=self.id,
            content=self.content,
            upvote=self.upvote,
            downvote=self.downvote,
            publish_date=self.publish_date,
            mod_date=self.mod_date,
            parent_comment=self.parent_comment,
            parent_post=self.parent_post,
            user_id=self.user_id,
        )
