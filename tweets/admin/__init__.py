from django.contrib import admin

from tweets.admin.tweet import TweetAdmin
from tweets.models import (
    Tweet as TweetModel,
)

admin.site.register(TweetModel, TweetAdmin)