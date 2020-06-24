from django.conf import settings
from django.db import models

from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel


class Article(TitleSlugDescriptionModel, TimeStampedModel, models.Model):
    content = models.TextField()
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
