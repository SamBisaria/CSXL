from pydantic import BaseModel

from backend.models.user import User

__authors__ = ["Ajay Gandecha", "Jade Keegan", "Brianna Ta", "Audrey Toney"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class NewsComments(BaseModel):
    """
    Pydantic model to represent an `News Posts`.

    This model is based on the `PostEntity` model, which defines the shape
    of the `NewsPost` database in the PostgreSQL database.
    """

    id: int | None = None
    content: str
    upvote: int
    downvote: int
    publish_date: str
    mod_date: str

    parent_comment: int
    parent_post: int
    user_id: int
