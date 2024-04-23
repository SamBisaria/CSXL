"""Definition of SQLAlchemy table-backed object mapping entity for Organizations."""

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.entities import user_post_association
from backend.entities.organization_entity import OrganizationEntity
from backend.entities.user_entity import UserEntity
from backend.entities.user_post_association import UserPostAssociation
from backend.models.news_post_user import NewsPostUsers
from backend.models.user import User
from .entity_base import EntityBase
from typing import Self
from ..models.news_post import NewsPost

__authors__ = ["Ajay Gandecha", "Jade Keegan", "Brianna Ta", "Audrey Toney"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class PostEntity(EntityBase):
    """Serves as the database model schema defining the shape of the `Organization` table"""

    # Name for the organizations table in the PostgreSQL database
    __tablename__ = "news_post"

    # Organization properties (columns in the database table)

    # Unique ID for the organization
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    # Name of the organization
    headline: Mapped[str] = mapped_column(String, nullable=False, default="")
    # Short hand name of the organization
    synopsis: Mapped[str] = mapped_column(String, nullable=False, default="")
    # Slug of the organization
    main_story: Mapped[str] = mapped_column(String, nullable=False, default="")
    # Logo of the organization
    creation_author_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))

    # Long description of the organization
    state: Mapped[str] = mapped_column(String)
    # Website of the organization
    slug: Mapped[str] = mapped_column(String)
    # Contact email for the organization
    image_url: Mapped[str] = mapped_column(String)
    # Instagram username for the organization
    pub_date: Mapped[str] = mapped_column(String)
    # LinkedIn for the organization
    mod_date: Mapped[str] = mapped_column(String)
    # YouTube for the organization
    announcement: Mapped[bool] = mapped_column(String)
    # Heel Life for the organization
    category: Mapped[str] = mapped_column(String)
    # Whether the organization can be joined by anyone or not
    upvote: Mapped[int] = mapped_column(Integer)

    downvote: Mapped[int] = mapped_column(Integer)

    # NOTE: This field establishes a one-to-many relationship between the organizations and events table.
    organization_id: Mapped[int] = mapped_column(ForeignKey("organization.id"))

    # organization: Mapped["OrganizationEntity"] = relationship(back_populates="posts")

    # check whether the author is always the organization??? or the people who have edited it?

    users: Mapped[list["UserPostAssociation"]] = relationship()
    # comments: Mapped["OrganizationEntity"] = relationship(back_populates="posts")

    # author: Mapped["UserEntity"] = relationship(back_populates="posts")

    @classmethod
    def from_model(cls, model: NewsPost) -> Self:
        """
        Class method that converts an `NewsPosst` model into a `PostEntity`

        Parameters:
            - model (Organization): Model to convert into an entity
        Returns:
            OrganizationEntity: Entity created from model
        """
        return cls(
            id=model.id,
            headline=model.headline,
            synopsis=model.synopsis,
            main_story=model.main_story,
            creation_author_id=model.author,
            slug=model.slug,
            state=model.state,
            image_url=model.image_url,
            pub_date=model.publish_date,
            mod_date=model.mod_date,
            announcement=model.announcement,
            category=model.category,
            upvote=model.upvote,
            downvote=model.downvote,
            organization_id=model.organization_id,
            users=[],
        )

    def from_model_users(cls, model: NewsPostUsers) -> Self:

        return cls(
            id=model.id,
            headline=model.headline,
            synopsis=model.synopsis,
            main_story=model.main_story,
            creation_author_id=model.author,
            slug=model.slug,
            state=model.state,
            image_url=model.image_url,
            pub_date=model.publish_date,
            mod_date=model.mod_date,
            announcement=model.announcement,
            upvote=model.upvote,
            downvote=model.downvote,
            organization_id=model.organization_id,
            users=[
                UserPostAssociation.from_model(i.key, model.id, i.value)
                for i in model.post_users
            ],
        )

    def to_model_users(self) -> NewsPost:
        """
        Converts a `OrganizationEntity` object into a `Organization` model object

        Returns:
            Organization: `Organization` object from the entity
        """
        return NewsPostUsers(
            id=self.id,
            headline=self.headline,
            synopsis=self.synopsis,
            main_story=self.main_story,
            author=self.creation_author_id,
            slug=self.slug,
            state=self.state,
            image_url=self.image_url,
            publish_date=self.pub_date,
            mod_date=self.mod_date,
            announcement=self.announcement,
            upvote=self.upvote,
            downvote=self.downvote,
            organization_id=self.organization_id,
            post_users={i.get_user(): i.get_score for i in self.users},
        )

    def to_model(self) -> NewsPost:
        """
        Converts a `OrganizationEntity` object into a `Organization` model object

        Returns:
            Organization: `Organization` object from the entity
        """
        return NewsPost(
            id=self.id,
            headline=self.headline,
            synopsis=self.synopsis,
            main_story=self.main_story,
            author=self.creation_author_id,
            slug=self.slug,
            state=self.state,
            image_url=self.image_url,
            publish_date=self.pub_date,
            mod_date=self.mod_date,
            announcement=self.announcement,
            upvote=self.upvote,
            downvote=self.downvote,
            organization_id=self.organization_id,
        )
