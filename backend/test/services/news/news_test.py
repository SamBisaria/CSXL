import pytest
import sys

from backend.models.news_post import NewsPost
from ....services import NewsService
from ..fixtures import news_svc_integration
from ..core_data import setup_insert_data_fixture
from ..user_data import user, root
from ..core_data import setup_insert_data_fixture
from ..fixtures import news_svc, user_svc_integration, permission_svc_mock
from .news_data import posts

from backend.services.exceptions import (
    ResourceNotFoundException,
    UserPermissionException,
)


def test_all_posts(news_svc_integration: NewsService):
    result = news_svc_integration.get_drafts()
    assert len(result) == len(posts)


def test_get_post(news_svc_integration: NewsService):
    result = news_svc_integration.get_post(user, 1)
    assert result is not None
    assert result.id == 1
    assert result.headline == posts[0].headline
    assert result.synopsis == posts[0].synopsis
    assert result.main_story == posts[0].main_story
    # Check more I guess?


def test_get_post_not_exists(news_svc_integration: NewsService):
    with pytest.raises(ResourceNotFoundException):
        news_svc_integration.get_post(user, 1000)


def test_add_post(news_svc_integration: NewsService):
    result = news_svc_integration.add_post(user, posts[1])
    assert result is not None
    assert new_post.headline == result.headline
    assert new_post.synopsis == result.synopsis
    assert new_post.main_story == result.main_story
    # Check more attributes as needed


def test_update_post(news_svc_integration: NewsService):
    result = news_svc_integration.update_post(user, updated_post1)
    assert updated_post1.headline == result.headline
    assert updated_post1.synopsis == result.synopsis
    assert updated_post1.main_story == result.main_story
    # Check more?


def test_update_post_not_exists(news_svc_integration: NewsService):
    with pytest.raises(ResourceNotFoundException):
        news_svc_integration.update_post(
            user,
            NewsPost(
                id=1000,
                headline="Fake Post",
                synopsis="Fake Synopsis",
                main_story="Fake Story",
            ),
        )


def test_delete_post(news_svc_integration: NewsService):
    news_svc_integration.delete_post(user, 1)
    result = news_svc_integration.get_post(user, 1)
    assert result is None


def test_delete_post_not_exists(news_svc_integration: NewsService):
    with pytest.raises(ResourceNotFoundException):
        news_svc_integration.delete_post(user, 1000)
