from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from .entity_base import EntityBase
from typing import Self
from ..models.news_post import PostModel


class NewsPostEntity(EntityBase):
    """Serves as the database model schema defining the shape of the `NewsPost` table"""

    # Name for the news_posts table in the PostgreSQL database
    __tablename__ = "news_posts"

    # NewsPost properties (columns in the database table)

    # Unique ID for the news post
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    # Headline of the news post
    headline: Mapped[str] = mapped_column(String, nullable=False)
    # Synopsis of the news post
    synopsis: Mapped[str] = mapped_column(String, nullable=False)
    # Main story content of the news post
    main_story: Mapped[str] = mapped_column(String, nullable=False)
    # Author of the news post
    author: Mapped[str] = mapped_column(String, nullable=False)
    # Slug of the news post
    slug: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    # State of the news post
    state: Mapped[str] = mapped_column(String, nullable=False)
    # Image URL of the news post
    image_url: Mapped[str] = mapped_column(String, nullable=False)
    # Publish date of the news post
    publish_date: Mapped[str] = mapped_column(String, nullable=False)
    # Modification date of the news post
    mod_date: Mapped[str] = mapped_column(String, nullable=False)
    # Announcement status of the news post
    announcement: Mapped[bool] = mapped_column(Boolean, nullable=False)
    # Upvote count of the news post
    upvote: Mapped[int] = mapped_column(Integer, nullable=False)
    # Downvote count of the news post
    downvote: Mapped[int] = mapped_column(Integer, nullable=False)
    # Organization ID related to the news post
    organization_id: Mapped[str] = mapped_column(String, nullable=False)

    @classmethod
    def from_model(cls, model: PostModel) -> Self:
        """
        Class method that converts a `NewsPost` model into a `NewsPostEntity`

        Parameters:
            - model (NewsPost): Model to convert into an entity
        Returns:
            NewsPostEntity: Entity created from model
        """
        return cls(
            id=model.id,
            headline=model.headline,
            synopsis=model.synopsis,
            main_story=model.main_story,
            author=model.author,
            slug=model.slug,
            state=model.state,
            image_url=model.image_url,
            publish_date=model.published_timestamp,
            mod_date=model.mod_date,
            announcement=model.announcement,
            upvote=model.upvote,
            downvote=model.downvote,
            organization_id=model.organization_id,
        )

    def to_model(self) -> PostModel:
        """
        Converts a `NewsPostEntity` object into a `NewsPost` model object

        Returns:
            PostModel: `NewsPost` object from the entity
        """
        return PostModel(
            id=self.id,
            headline=self.headline,
            synopsis=self.synopsis,
            main_story=self.main_story,
            author=self.author,
            slug=self.slug,
            state=self.state,
            image_url=self.image_url,
            publish_date=self.publish_date,
            mod_date=self.mod_date,
            announcement=self.announcement,
            upvote=self.upvote,
            downvote=self.downvote,
            organization_id=self.organization_id,
        )
