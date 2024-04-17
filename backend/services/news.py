from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database import db_session
from ..models.news_comments import NewsComments
from ..models.news_post import NewsPost
from ..models import User
from .permission import PermissionService
from ..entities.news_entity import NewsPostEntity

from .exceptions import ResourceNotFoundException

__authors__ = ["Ajay Gandecha", "Jade Keegan", "Brianna Ta", "Audrey Toney"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class NewsService:

    def __init__(
        self,
        session: Session = Depends(db_session),
        permission: PermissionService = Depends(),
    ):
        """Initializes the `OrganizationService` session, and `PermissionService`"""
        self._session = session
        self._permission = permission

    def all_posts():
        query = select(NewsPost)
        entities = self._session.scalars(query).all()

        # Convert entries to a model and return
        return [entity.to_model() for entity in entities]

    def get_post(self, subject: User, id: int):
        obj = (
            self._session.query(NewsPostEntity)
            .filter(NewsPostEntity.id == id)
            .one_or_none()
        )

        # Ensure object exists
        if obj is None:
            raise ResourceNotFoundException(
                f"No News Post found with matching id: {id}"
            )

        return obj.to_model()

    def add_post(self, subject: User, newsPost: NewsPost):
        postEntity = NewsPostEntity.from_model(newsPost)
        self._session.add(postEntity)
        self._session.commit()

        return postEntity.to_model()

    def update_post(self, subject: User, newsPost: NewsPost):
        obj = self._session.get(NewsPostEntity, newsPost.id)

        # Check if result is null
        if obj is None:
            raise ResourceNotFoundException(
                f"No organization found with matching ID: {newsPost.id}"
            )

        # Update organization object
        obj.headline = newsPost.headline
        obj.synopsis = newsPost.synopsis
        obj.main_story = newsPost.main_story
        obj.author = newsPost.author
        obj.slug = newsPost.slug
        obj.state = newsPost.state
        obj.image_url = newsPost.image_url
        obj.publish_date = newsPost.publish_date
        obj.mod_date = newsPost.mod_date
        obj.announcement = newsPost.announcement
        obj.upvote = newsPost.upvote
        obj.downvote = newsPost.downvote
        obj.organization_id = newsPost.organization_id

        # Save changes
        self._session.commit()

        # Return updated object
        return obj.to_model()

    def delete_post(self, subject: User, id: int):

        obj = (
            self._session.query(NewsPostEntity)
            .filter(NewsPostEntity.id == id)
            .one_or_none()
        )

        # Ensure object exists
        if obj is None:
            raise ResourceNotFoundException(
                f"No News Post found with matching id: {id}"
            )

        # Delete object and commit
        self._session.delete(obj)
        # Save changes
        self._session.commit()
