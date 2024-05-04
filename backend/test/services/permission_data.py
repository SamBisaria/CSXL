"""Mock data for permissions in the system."""

import pytest
from sqlalchemy.orm import Session
from ...entities.permission_entity import PermissionEntity

from ...models.permission import Permission

from . import role_data
from .reset_table_id_seq import reset_table_id_seq

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

root_role_permission = Permission(id=1, action="*", resource="*")
ambassador_permission = Permission(id=2, action="checkin.create", resource="checkin")
ambassador_permission_coworking_reservation = Permission(
    id=3, action="coworking.reservation.*", resource="*"
)
poster_role_permission = Permission(id=4, action="news.post", resource="*")
announcer_role_permission_post = Permission(id=5, action="news.post", resource="*")
announcer_role_permission = Permission(id=6, action="news.announce", resource="*")

permissions = [
    root_role_permission,
    ambassador_permission,
    ambassador_permission_coworking_reservation,
    poster_role_permission,
    announcer_role_permission_post,
    announcer_role_permission
]


def insert_fake_data(session: Session):
    root_permission_entity = PermissionEntity(
        id=root_role_permission.id,
        role_id=role_data.root_role.id,
        action=root_role_permission.action,
        resource=root_role_permission.resource,
    )
    session.add(root_permission_entity)

    # WTF why are you using fixed loop ranges???
    for i in range(1, 2):
        ambassador_permission_entity = PermissionEntity(
            id=permissions[i].id,
            role_id=role_data.ambassador_role.id,
            action=permissions[i].action,
            resource=permissions[i].resource,
        )
        session.add(ambassador_permission_entity)

    post_permission_entity = PermissionEntity(
        id=poster_role_permission.id,
        role_id=role_data.poster_role.id,
        action=poster_role_permission.action,
        resource=poster_role_permission.resource,
    )
    session.add(post_permission_entity)

    announce_permission_entity1 = PermissionEntity(
        id=announcer_role_permission_post.id,
        role_id=role_data.announcer_role.id,
        action=announcer_role_permission_post.action,
        resource=announcer_role_permission_post.resource,
    )
    announce_permission_entity2 = PermissionEntity(
        id=announcer_role_permission.id,
        role_id=role_data.announcer_role.id,
        action=announcer_role_permission.action,
        resource=announcer_role_permission.resource,
    )
    session.add(announce_permission_entity1)
    session.add(announce_permission_entity2)

    reset_table_id_seq(
        session, PermissionEntity, PermissionEntity.id, len(permissions) + 1
    )


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()
    yield
