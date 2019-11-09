from django.shortcuts import render

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post

from .serializer import PostSerializer
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# class PostList(generics.ListAPIView):
#     serializer_class = PostSerializer
#     def get_queryset(self):
#         borough = self.request.GET['borough']
#         return Post.objects.filter(borough_code=borough)


class PostList(APIView):
    def get(self, request):
        posts = Post.objects.filter(borough_code=request.GET['borough'])
        serializer = PostSerializer(posts, many=True) # 다수의 쿼리셋을 시리얼라이징 할때는 many=True
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'result':False}, status=status.HTTP_200_OK)