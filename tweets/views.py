from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import TweetSerializer
from .models import Tweet


class TweetListCreateApiView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if content is None:
            content = title 

        serializer.save(creator = self.request.user, title = title,content = content)

product_list_create_view = TweetListCreateApiView.as_view()