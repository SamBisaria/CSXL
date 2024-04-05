"""Tests for the NewsFeed feature and class."""

from ..fixtures import news_service


__authors__ = ["Aaron Wang"]
__copyright__ = "Copyright 2024"
__license__ = "MIT"

from ....services.news import NewsService


def test_get_all(news_service: NewsService):
    """Test that all organizations can be retrieved."""
    news_posts = news_service.all_posts()
    assert news_posts is not None
    assert len(news_posts) > 0

