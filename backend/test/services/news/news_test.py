import pytest
import sys

from backend.models.news_post import PostModel
from backend.services.news import NewsService
from ..core_data import setup_insert_data_fixture
from ..user_data import users
from ..core_data import setup_insert_data_fixture
from ..fixtures import news_svc
from .news_data import posts, post3

from backend.services.exceptions import (
    ResourceNotFoundException,
    UserPermissionException,
)


def test_all_posts(news_svc: NewsService):
    result = news_svc.get_posts()
    assert len(result) == 1


def test_all_drafts(news_svc: NewsService):
    result = news_svc.get_drafts(users[1])
    assert len(result) == 1


def test_get_post(news_svc: NewsService):
    result = news_svc.get_post(users[0], 1)
    assert result is not None
    assert result.id == 1
    assert result.headline == posts[0].headline
    assert result.synopsis == posts[0].synopsis
    assert result.main_story == posts[0].main_story
    # Check more I guess?


def test_get_post_not_exists(news_svc: NewsService):
    with pytest.raises(ResourceNotFoundException):
        news_svc.get_post(users[0], 1000)


def test_add_post(news_svc: NewsService):

    result = news_svc.add_post(users[0], post3)
    assert result is not None
    assert post3.headline == result.headline
    assert post3.synopsis == result.synopsis
    assert post3.main_story == result.main_story
    # Check more attributes as needed


def test_update_draft(news_svc: NewsService):
    updated_post2 = PostModel(
        id=1,
        headline="updated",
        synopsis="updated",
        main_story="updated",
        author_id=2,
        slug="sl",
        state="draft",
        image_url="",
        published_timestamp=1712184104,
        modified_timestamp=1713912104,
        announcement=True,
        category="cat",
        organization_id=3,
    )
    result = news_svc.update_draft(users[1], updated_post2, updated_post2.id)
    assert updated_post2.headline == result.headline  # Check more?


def test_update_post(news_svc: NewsService):
    updated_post1 = PostModel(
        id=2,
        headline="updated",
        synopsis="updated",
        main_story="updated",
        author_id=1,
        slug="sl",
        state="published",
        image_url="",
        published_timestamp=1712184104,
        modified_timestamp=1713912104,
        announcement=True,
        category="cat",
        organization_id=3,
    )

    result = news_svc.update_post(users[0], updated_post1)
    assert updated_post1.headline == result.headline  # Check more?


def test_update_draft_not_exists(news_svc: NewsService):
    with pytest.raises(ResourceNotFoundException):
        news_svc.update_post(
            users[0],
            PostModel(
                id=1000,
                headline="Fake Post",
                synopsis="Fake Synopsis",
                main_story="Fake Story",
            ),
        )


def test_delete_post(news_svc: NewsService):
    news_svc.delete_post(users[0], 2)
    with pytest.raises(ResourceNotFoundException):

        result = news_svc.get_post(users[0], 2)


def test_upvote_post_3_times(news_svc: NewsService):
    news_svc.like_post(users[0], "s")
    news_svc.like_post(users[0], "s")
    news_svc.like_post(users[0], "s")

    result = news_svc.get_post(users[0], 2)
    assert result.upvote == 1


def test_upvote_post_twice(news_svc: NewsService):
    news_svc.like_post(users[0], "s")
    news_svc.like_post(users[0], "s")

    result = news_svc.get_post(users[0], 2)
    assert result.upvote == 0


def test_upvote_post_once(news_svc: NewsService):
    news_svc.like_post(users[0], "s")

    result = news_svc.get_post(users[0], 2)
    assert result.upvote == 1


def test_downvote_post(news_svc: NewsService):
    news_svc.dislike_post(users[0], "s")
    news_svc.dislike_post(users[0], "s")
    news_svc.dislike_post(users[0], "s")

    result = news_svc.get_post(users[0], 2)
    assert result.downvote == 1


def test_upvote_then_downvote(news_svc: NewsService):
    news_svc.dislike_post(users[0], "s")
    news_svc.like_post(users[0], "s")

    result = news_svc.get_post(users[0], 2)
    assert result.downvote == 0
    assert result.upvote == 1


def test_two_users_upvote(news_svc: NewsService):
    news_svc.like_post(users[0], "s")
    news_svc.like_post(users[1], "s")

    result = news_svc.get_post(users[0], 2)
    assert result.upvote == 2


def test_delete_post_not_exists(news_svc: NewsService):
    with pytest.raises(ResourceNotFoundException):
        news_svc.delete_post(users[0], 1000)
