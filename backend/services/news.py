import datetime
import random
import sys
import time

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqids import Sqids;
from datetime import datetime, timezone

from backend.entities.post_entity import PostEntity
from backend.entities.user_post_association import UserPostAssociation

from ..database import db_session

# from ..models.news_comments import NewsComments
from ..models.news_post import PostModel
from ..models import news_post
from ..models import User
from .permission import PermissionService

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
        """Initializes the `NewsService` session, and `PermissionService`"""
        self._session = session
        self._permission = permission
        self._sqids = Sqids(alphabet="BLzxKTuIslpgY5Xy0FSWa1VNtcvwMm4D8jk9hbAEfdJriZ273GQ6HqPoenCROU")
        self._random = random.Random()

    """
    THE BELOW METHODS ARE ALL FOR POSTS BEING CURRENTLY 
    BEING EDITED/WORKED ON
    """

    def get_drafts(self, subject: User):
        query = select(PostEntity).where(
            PostEntity.state == "draft", PostEntity.creation_author_id == subject.id
        )
        entities = self._session.scalars(query).all()
        # TOdo return empty list instead of erroring when no drafts
        if entities is None:
            raise ResourceNotFoundException(
                f"No News Post found"
            )  # Convert entries to a model and return
        return [entity.to_model() for entity in entities]

    def get_draft(self, subject: User, post_id: int):
        query = select(PostEntity).where(
            PostEntity.state == "draft",
            PostEntity.creation_author_id == subject.id,
            PostEntity.id == post_id,
        )
        obj = self._session.scalar(query)
        # Ensure object exists
        if obj is None or obj.creation_author_id != subject.id:
            raise ResourceNotFoundException(
                f"No News Post found with matching id: {post_id}"
            )
        return obj.to_model()

    def add_post_draft(self, subject: User, news_post: PostModel):
        news_post.author = subject.id
        # Slugs are generated as sqids from the last modified
        news_post.state = "draft"
        news_post.slug = ""  # Prevents null error on flush
        news_post.published_timestamp = int(datetime.now(tz=timezone.utc).timestamp())
        news_post.modified_timestamp = news_post.published_timestamp
        # TODO check if user has permission to make post announcement
        post_entity = PostEntity.from_model(news_post)
        self._session.add(post_entity)
        self._session.flush()
        post_entity.slug = self._sqids.encode([post_entity.id, 0])
        # self._session.add(post_entity)
        # self._session.expire(post_entity, ['slug'])
        self._session.commit()
        return post_entity.to_model()

    def update_draft(self, subject: User, post: PostModel, post_id: int):

        obj = self._session.get(PostEntity, post_id)

        # Check if result is null
        if obj is None:
            raise ResourceNotFoundException(
                f"No organization found with matching ID: {post.id}"
            )

        if subject.id == obj.creation_author_id:
            obj.headline = post.headline
            obj.synopsis = post.synopsis
            obj.main_story = post.main_story
            obj.image_url = post.image_url
            obj.state = post.state
            obj.announcement = post.announcement
            obj.category = post.category
            obj.organization_id = post.organization_id
            obj.modified_timestamp = int(datetime.now(tz=timezone.utc).timestamp())
            self._session.add(obj)
            self._session.commit()

        # Return updated object
        return obj.to_model()

    def publish_post(self, subject: User, post_id: int):

        obj = self._session.get(PostEntity, post_id)

        # Check if result is null
        if obj is None or subject.id != obj.creation_author_id:
            raise ResourceNotFoundException(
                f"No organization found with matching ID: {post_id}"
            )
        # Return updated object
        obj.state = "published"

        self._session.commit()

        return obj.to_model()

    def delete_post(self, subject: User, post_id: int):
        obj = (
            self._session.query(PostEntity)
            .filter(
                PostEntity.id == post_id, PostEntity.creation_author_id == subject.id
            )
            .one_or_none()
        )
        # Ensure object exists
        if obj is None:
            raise ResourceNotFoundException(
                f"No News Post found with matching id: {post_id}"
            )
        # Delete object and commit
        self._session.delete(obj)
        # Save changes
        self._session.commit()
        return obj.to_model()

    """
    THE BELOW METHODS ARE FOR POSTS THAT ARE 
    GOING TO BE DISPLAYED PUBLICLY
    """

    def like_post(self, subject: User, post_slug: str):
        querypost = select(PostEntity).where(PostEntity.slug == post_slug)
        post = self._session.scalar(querypost)
        queryassoc = (
            select(UserPostAssociation)
            .where(
                UserPostAssociation.news_post == post.id,
                UserPostAssociation.user == subject.id,
            )
            .limit(1)
        )

        rel = self._session.scalar(queryassoc)

        if post is None or post.state != "published":
            raise ResourceNotFoundException(
                f"No News Post found with matching id: {post.id}"
            )
        if rel is None:
            obj = UserPostAssociation(news_post=post.id, user=subject.id, score=1)
            self._session.add(obj)
            post.upvote += 1

        elif rel.score == 0:
            post.upvote += 1
            rel.score = 1
        elif rel.score == 1:
            post.upvote -= 1
            rel.score = 0
        elif rel.score == -1:
            post.upvote += 1
            post.downvote -= 1
            rel.score = 1

        self._session.commit()
        return self._session.scalar(querypost).to_model()

    def dislike_post(self, subject: User, post_slug: str):
        querypost = select(PostEntity).where(PostEntity.slug == post_slug)
        post = self._session.scalar(querypost)
        queryassoc = (
            select(UserPostAssociation)
            .where(
                UserPostAssociation.news_post == post.id,
                UserPostAssociation.user == subject.id,
            )
            .limit(1)
        )
        rel = self._session.scalar(queryassoc)

        if post is None or post.state != "published":
            raise ResourceNotFoundException(
                f"No News Post found with matching id: {post.id}"
            )
        if rel is None:
            obj = UserPostAssociation(news_post=post.id, user=subject.id, score=-1)
            self._session.add(obj)
            post.downvote += 1
        elif rel.score == 0:
            post.downvote += 1
            rel.score = -1
        elif rel.score == -1:
            post.downvote -= 1
            rel.score = 0
        elif rel.score == 1:
            post.upvote -= 1
            post.downvote += 1
            rel.score = -1

        self._session.commit()
        return post.to_model()

    def get_posts(self):
        query = select(PostEntity).where(PostEntity.state == "finished")
        entities = self._session.scalars(query).all()
        if entities is None:
            raise ResourceNotFoundException(
                f"No News Post found"
            )  # Convert entries to a model and return
        return [entity.to_model() for entity in entities]

    def get_posts_by_date(self):
        query = (
            select(PostEntity)
            .where(PostEntity.state == "finished")
            .order_by(PostEntity.published_timestamp.desc())
        )
        entities = self._session.scalars(query).all()
        if entities is None:
            raise ResourceNotFoundException(
                f"No News Post found"
            )  # Convert entries to a model and return
        return [entity.to_model() for entity in entities]

    def get_popular_posts(self, subject: User, page_num: int):
        query = (
            select(PostEntity)
            .where(state="finished", author=subject.id)
            .order_by(PostEntity.upvote)
        )
        entities = self._session.scalars(query).all()

        # Convert entries to a model and return
        return [entity.to_model() for entity in entities]

    def get_post(self, subject: User, id: int):
        obj = self._session.query(PostEntity).filter(PostEntity.id == id).one_or_none()

        # Ensure object exists
        if obj is None:
            raise ResourceNotFoundException(
                f"No News Post found with matching id: {id}"
            )

        return obj.to_model()

    def add_post(self, subject: User, newsPost: PostModel):

        obj = (
            self._session.query(PostEntity)
            .filter(PostEntity.id == newsPost.id)
            .one_or_none()
        )
        while obj is not None:
            newsPost.id += 1
            obj = (
                self._session.query(PostEntity)
                .filter(PostEntity.id == newsPost.id)
                .one_or_none()
            )
        newsPost.author = subject.id
        newsPost.state = "published"

        postEntity = PostEntity.from_model(newsPost)
        postEntity.users = []
        self._session.add(postEntity)
        self._session.commit()
        return postEntity.to_model()

    def update_post(self, subject: User, newsPost: PostModel):
        obj = self._session.get(PostEntity, newsPost.id)

        # Check if result is null
        if obj is None:
            raise ResourceNotFoundException(
                f"No organization found with matching ID: {newsPost.id}"
            )

        # Update organization object
        obj.headline = newsPost.headline
        obj.synopsis = newsPost.synopsis
        obj.main_story = newsPost.main_story
        obj.creation_author_id = newsPost.author
        obj.slug = newsPost.slug
        obj.state = newsPost.state
        obj.image_url = newsPost.image_url
        obj.published_timestamp = newsPost.published_timestamp
        obj.modified_timestamp = newsPost.mod_date
        obj.announcement = newsPost.announcement
        obj.upvote = newsPost.upvote
        obj.downvote = newsPost.downvote
        obj.organization_id = newsPost.organization_id

        # Save changes
        self._session.commit()

        # Return updated object
        return obj.to_model()

    def delete_post(self, subject: User, id: int):

        obj = self._session.query(PostEntity).filter(PostEntity.id == id).one_or_none()

        # Ensure object exists
        if obj is None or subject.id != obj.creation_author_id:
            raise ResourceNotFoundException(
                f"No News Post found with matching id: {id}"
            )

        # Delete object and commit
        self._session.delete(obj)
        # Save changes
        self._session.commit()
        return obj.to_model()
