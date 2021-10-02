"""Post application module."""


from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Post appication settings."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    varbose_name = 'Posts'
