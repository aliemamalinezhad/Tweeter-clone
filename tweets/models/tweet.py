import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from utils import GeneralModel

User = get_user_model()


class Tweet(GeneralModel):
    creator = models.ForeignKey(
        User,
        verbose_name=_('creator'),
        on_delete=models.CASCADE,
        related_name='tweets',
    )
    title = models.CharField(
        verbose_name =_('title'),
        max_length=200,
    )
    content = models.TextField(
        verbose_name =_('content'),
        max_length=400,
    )


    def __str__(self):
        return f'{self.title}-{self.creator.username}'