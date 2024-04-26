from fastapi import APIRouter, Depends

from ..services.news import NewsService
from ..models.news_post import PostModel

# from ..models.news_comments import NewsComments
from ..api.authentication import registered_user
from ..models.user import User

__authors__ = ["Ajay Gandecha", "Jade Keegan", "Brianna Ta", "Audrey Toney"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

api = APIRouter(prefix="/api/news")
openapi_tags = {
    "name": "News",
    "description": "Create, update, delete, and retrieve CS News Posts.",
}


@api.get("/get", response_model=list[PostModel], tags=["News"])
def get_posts(
    subject: User = Depends(registered_user),
    news_service: NewsService = Depends(),
) -> list[PostModel]:
    """
    Gets a list of all the drafts a user has saved.

    Parameters:
        subject: a valid User model representing the currently logged-in User
        news_service: a valid NewsService

    Returns:
        list[PostModel]: All `NewsPost`s in the `PostEntity` table who's current state == draft and
        the id of the author is the id of the user.
    """
    return news_service.get_posts()


@api.get("/date", response_model=list[PostModel], tags=["News"])
def get_posts_by_date(
    subject: User = Depends(registered_user),
    news_service: NewsService = Depends(),
) -> list[PostModel]:
    """
    Gets a list of all the drafts a user has saved.

    Parameters:
        subject: a valid User model representing the currently logged-in User
        news_service: a valid NewsService

    Returns:
        list[PostModel]: All `NewsPost`s in the `PostEntity` table who's current state == draft and
        the id of the author is the id of the user.
    """
    return news_service.get_posts_by_date()


@api.get("/draft/get", response_model=list[PostModel], tags=["News"])
def get_drafts(
    subject: User = Depends(registered_user),
    news_service: NewsService = Depends(),
) -> list[PostModel]:
    """
    Gets a list of all the drafts a user has saved.

    Parameters:
        subject: a valid User model representing the currently logged-in User
        news_service: a valid NewsService

    Returns:
        list[PostModel]: All `NewsPost`s in the `PostEntity` table who's current state == draft and
        the id of the author is the id of the user.
    """
    return news_service.get_drafts(subject)


@api.get("/get/{post_id}", response_model=PostModel, tags=["News"])
def get_post(
    post_id: int,
    subject: User = Depends(registered_user),
    news_service: NewsService = Depends(),
) -> PostModel:
    """
    Gets a specific post by id

    Parameters:
        post_id (int): id of the post the user is attempting to get
        subject: a valid User model representing the currently logged-in User
        news_service: a valid NewsService

    Returns:
        PostModel: The `NewsPost` in the `PostEntity` whose id matches the post_id, if it exists.

    Raises:
        HTTPException 404 if get_draft() raises an Exception
    """
    return news_service.get_post(subject, post_id)


@api.get("/draft/get/{post_id}", response_model=PostModel, tags=["News"])
def get_draft(
    post_id: int,
    subject: User = Depends(registered_user),
    news_service: NewsService = Depends(),
) -> PostModel:
    """
    Gets a specific draft by id

    Parameters:
        post_id (int): id of the draft the user is attempting to get
        subject: a valid User model representing the currently logged-in User
        news_service: a valid NewsService

    Returns:
        PostModel: The `NewsPost` in the `PostEntity` whose id matches the post_id, if it exists.

    Raises:
        HTTPException 404 if get_draft() raises an Exception
    """
    return news_service.get_draft(subject, post_id)


@api.post("/draft/post", response_model=PostModel, tags=["News"])
def create_draft(
    post: PostModel,
    subject: User = Depends(registered_user),
    news_service: NewsService = Depends(),
) -> PostModel:
    """
    Creates a new draft

    Parameters:
        post (PostModel): object representing the draft being made
        subject: a valid User model representing the currently logged-in User
        news_service: a valid NewsService

    Returns:
        PostModel: The `NewsPost` in the `PostEntity` table representing the draft which
        has just been created
    """
    return news_service.add_post(subject, post)


# @api.post("/publish/post", response_model=PostModel, tags=["News"])
# def create_post(
#     post: PostModel,
#     subject: User = Depends(registered_user),
#     news_service: NewsService = Depends(),
# ) -> PostModel:
    """
    Creates a new draft

    Parameters:
        post (PostModel): object representing the draft being made
        subject: a valid User model representing the currently logged-in User
        news_service: a valid NewsService

    Returns:
        PostModel: The `NewsPost` in the `PostEntity` table representing the draft which
        has just been created
    """
    # post.author = subject.id
    # return news_service.add_post(subject, post)


@api.put("/draft/edit/{post_id}", response_model=PostModel, tags=["News"])
def update_draft(
    post_id: int,
    post: PostModel,
    subject: User = Depends(registered_user),
    news_service: NewsService = Depends(),
) -> PostModel:
    """
    Edits an existing draft

    Parameters:
        post_id (int): id of the post/draft being updated
        post (PostModel): object representing the content of the post being updated
        subject: a valid User model representing the currently logged-in User
        news_service: a valid NewsService

    Returns:
        PostModel: The `NewsPost` in the `PostEntity` table representing the draft which
        has just been updated
    """
    return news_service.update_draft(subject, post, post_id)


# @api.put("/publish/{post_id}", response_model=PostModel, tags=["News"])
# def publish_news_post(
#     post_id: int,
#     subject: User = Depends(registered_user),
#     news_service: NewsService = Depends(),
# ) -> PostModel:
    """
    Publicizes an existing draft

    Parameters:
        post_id (int): id of the draft being updated
        subject: a valid User model representing the currently logged-in User
        news_service: a valid NewsService

    Returns:
        PostModel: The `NewsPost` in the `PostEntity` table representing the draft which
        has just been made public
    """
    # return news_service.publish_post(subject, post_id)


@api.delete("/delete/{post_id}", response_model=PostModel, tags=["News"])
def delete_news_post(
    post_id: int,
    subject: User = Depends(registered_user),
    news_service: NewsService = Depends(),
) -> PostModel:
    """
    Deletes an existing post, including published posts and drafts. Marks the
    author and content as empty/deleted but preserves child posts and structures
    of children.

    Parameters:
        post_id (int): id of the post being deleted
        subject: a valid User model representing the currently logged-in User
        news_service: a valid NewsService

    Returns:
        PostModel: The `NewsPost` in the `PostEntity` table representing the post which
        has just been deleted.
    """
    return news_service.delete_post(subject, post_id)


@api.put("/upvote/{slug}", response_model=PostModel, tags=["News"])
def upvote_news_post(
    slug: str,
    subject: User = Depends(registered_user),
    news_service: NewsService = Depends(),
) -> PostModel:
    """
    Upvotes a post by the slug if it hasn't already been upvtoed by the user. If a post has
    already been upvoted by the user, will remove the upvote. If the post has been
    downvoted by the user, will remove the downvote.

    Parameters:
        slug (str): A string of random characters used to denote a unique url for
        posts
        subject: a valid User model representing the currently logged-in User
        news_service: a valid NewsService

    Returns:
        PostModel: The `NewsPost` in the `PostEntity` table representing the post which
        has just been upvoted (or un-upvoted) by the user.
    """
    return news_service.like_post(subject, slug)


@api.put("/downvote/{slug}", response_model=PostModel, tags=["News"])
def downvote_news_post(
    slug: str,
    subject: User = Depends(registered_user),
    news_service: NewsService = Depends(),
) -> PostModel:
    """
    Downvotes a post by the slug if it hasn't already been upvoted by the user. If a post has
    already been downvoted by the user, will remove the downvote. If the post has been
    upvoted by the user, will remove the upvote.

    Parameters:
        slug (str): A string of random characters used to denote a unique url for
        posts
        subject: a valid User model representing the currently logged-in User
        news_service: a valid NewsService

    Returns:
        PostModel: The `NewsPost` in the `PostEntity` table representing the post which
        has just been downvoted (or un-downvoted) by the user.
    """
    return news_service.dislike_post(subject, slug)
