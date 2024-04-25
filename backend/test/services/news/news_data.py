import pytest
from sqlalchemy.orm import Session

from ....models.user import User
from ...services import reset_table_id_seq
from ....models.news_post import PostModel
from ....entities.user_entity import UserEntity
from ....entities.post_entity import PostEntity
from ....entities.user_role_table import user_role_table


__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

post1 = PostModel(
    id=1,
    headline="head",
    synopsis="synopsi",
    main_story="storyeee",
    author=2,
    slug="sl",
    state="edit",
    image_url="",
    published_timestamp=1712184104,
    modified_timestamp=1713912104,
    announcement=True,
    category="cat",
    organization_id=3,
)

post2 = PostModel(
    id=2,
    headline="head1",
    synopsis="synopsi1",
    main_story="storyeee1",
    author=1,
    slug="sl",
    state="edit1",
    image_url="",
    published_timestamp=1712184104,
    modified_timestamp=1713912104,
    announcement=True,
    category="cat",
    organization_id=3,
)

root = User(
    id=1,
    pid=999999999,
    onyen="root",
    email="root@unc.edu",
    first_name="Rhonda",
    last_name="Root",
    pronouns="She / Her / Hers",
    accepted_community_agreement=True,
)

root1 = User(
    id=2,
    pid=999999999,
    onyen="root",
    email="root@unc.edu",
    first_name="Rhonda",
    last_name="Root",
    pronouns="She / Her / Hers",
    accepted_community_agreement=True,
)
users = [root, root1]
posts = [post1, post2]


def insert_fake_data(session: Session):
    global users
    entities = []
    for user in users:
        entity = UserEntity.from_model(user)
        session.add(entity)
        entities.append(entity)
    reset_table_id_seq(session, UserEntity, UserEntity.id, len(users) + 1)
    session.commit()  # Commit to ensure User IDs in database

    # Associate Users with the Role(s) they are in
    for post in posts:
        ent = PostEntity.from_model(post)
        session.add(ent)
        entities.append(ent)
    session.commit()


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()
