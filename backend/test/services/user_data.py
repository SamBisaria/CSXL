"""Mock data for users.

Three users are setup for testing and development purposes:

1. Rhonda Root (root user with all permissions)
2. Amy Ambassador (staff of XL with elevated permissions)
3. Sally Student (standard user without any special permissions)"""

import pytest
from sqlalchemy.orm import Session
from ...models.user import User
from ...entities.user_entity import UserEntity
from ...entities.user_role_table import user_role_table
from .reset_table_id_seq import reset_table_id_seq
from . import role_data

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

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

ambassador = User(
    id=2,
    pid=888888888,
    onyen="xlstan",
    email="amam@unc.edu",
    first_name="Amy",
    last_name="Ambassador",
    pronouns="They / Them / Theirs",
    accepted_community_agreement=True,
)

user = User(
    id=3,
    pid=111111111,
    onyen="user",
    email="user@unc.edu",
    first_name="Sally",
    last_name="Student",
    pronouns="She / They",
    accepted_community_agreement=True,
)

poster = User(
    id=4,
    pid=222222222,
    onyen="xlstanperry",
    email="xlstanperry@unc.edu",
    first_name="Perry",
    last_name="Poster",
    pronouns="He / Him / His",
    accepted_community_agreement=True,
)

announcer = User(
    id=5,
    pid=333333333,
    onyen="xlstanannouncer",
    email="xlstanannouncer@unc.edu",
    first_name="Adam",
    last_name="Announcer",
    pronouns="He / Him / His",
    accepted_community_agreement=True,
)

users = [root, ambassador, user, poster, announcer]

roles_users = {
    role_data.root_role.id: [root],
    role_data.ambassador_role.id: [ambassador],
    role_data.poster_role.id: [poster],
    role_data.announcer_role.id: [announcer]
}


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
    for role_id, members in roles_users.items():
        for user in members:
            session.execute(
                user_role_table.insert().values(
                    {"role_id": role_id, "user_id": user.id}
                )
            )


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()
    yield
