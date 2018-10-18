from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'apps.images'
    verbose_name = 'Image bookmarks'

    def ready(self):
        # import signal handlers
        import apps.images.signals  # noqa: F401
