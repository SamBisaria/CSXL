from pydantic import BaseModel

__authors__ = ["Ajay Gandecha", "Jade Keegan", "Brianna Ta", "Audrey Toney"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class NewsPostUsers(BaseModel):
    """
    Pydantic model to represent an `News Posts`.

    This model is based on the `PostEntity` model, which defines the shape
    of the `NewsPost` database in the PostgreSQL database.
    """

    id: int | None = None
    headline: str
    synopsis: str
    main_story: str
    author: str
    slug: str
    state: str
    image_url: str
    publish_date: str
    mod_date: str
    announcement: bool
    category: str
    upvote: int
    downvote: int
    organization_id: str
    post_users: dict[int, int]
