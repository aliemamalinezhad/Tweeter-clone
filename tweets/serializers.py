from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Tweet
        fields =['id','owner','title','content']