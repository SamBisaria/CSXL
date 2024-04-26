from pydantic import BaseModel

__authors__ = ["Ajay Gandecha", "Jade Keegan", "Brianna Ta", "Audrey Toney"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class PostModel(BaseModel):
    """
    Pydantic model to represent an `Post`.

    This model is based on the `PostEntity` model, which defines the shape
    of the `NewsPost` database in the PostgreSQL database.
    """

    id: int = None
    headline: str = None
    synopsis: str = ""
    main_story: str = None
    author_id: int = None
    author_name: str = ""
    slug: str = None
    state: str = None
    image_url: str = ""
    published_timestamp: int = None
    modified_timestamp: int = None
    announcement: bool = None
    category: str = ""
    upvote: int = 0
    downvote: int = 0
    organization_id: int = 1
