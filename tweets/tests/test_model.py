import pytest
from tweets.models import Tweet
from django.contrib.auth.models import User



@pytest.mark.django_db
def test_tweet_contact_create():
    user = User.objects.create(username="ali", password="ali@12345")
    user.save()
    tweet = Tweet.objects.create(
        creator = user,
        title = "Title number one",
        content = "Content number one",

    )
    tweet.save()
    assert tweet.title == "Title number one"
    assert tweet.content == "Content number one"

git 