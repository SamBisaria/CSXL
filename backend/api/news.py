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
def get_organizations(
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
    return news_service.all()
