from rest_framework import serializers
from .models import Tweet

from accounts.serializers import UserSerializer

class TweetSerializer(serializers.ModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField(read_only=True)
    owner = UserSerializer(source='creator',read_only=True)
    class Meta:
        model = Tweet
        fields =['id','title','content','owner']