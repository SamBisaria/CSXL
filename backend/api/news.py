from fastapi import APIRouter, Depends

from ..services import NewsService
from ..models.news_post import NewsPost
from ..models.news_comments import NewsComments
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


@api.get("", response_model=list[NewsPost], tags=["News"])
def get_newsPosts(
    news_service: NewsService = Depends(),
) -> list[NewsPost]:
    """
    Get all organizations

    Parameters:
        organization_service: a valid OrganizationService

    Returns:
        list[Organization]: All `Organization`s in the `Organization` database table
    """

    # Return all organizations
    return news_service.all_posts()


@api.get("/{id}", response_model=list[NewsPost], tags=["News"])
def get_newsPost(
    id: int,
    subject: User = Depends(registered_user),
    news_service: NewsService = Depends(),
) -> NewsPost:
    return news_service.get_post(subject, id)


@api.post("", response_model=list[NewsPost], tags=["News"])
def create_newsPost(
    newsPost: NewsPost,
    subject: User = Depends(registered_user),
    news_service: NewsService = Depends(),
) -> NewsPost:
    return news_service.add_post(subject, newsPost)


@api.put("", response_model=list[NewsPost], tags=["News"])
def update_newsPost(
    newsPost: NewsPost,
    subject: User = Depends(registered_user),
    news_service: NewsService = Depends(),
) -> NewsPost:
    return news_service.update_post(subject, newsPost)


@api.delete("/{id}", response_model=list[NewsPost], tags=["News"])
def delete_newsPost(
    id: int,
    subject: User = Depends(registered_user),
    news_service: NewsService = Depends(),
) -> NewsPost:
    return news_service.delete_post(subject, id)
