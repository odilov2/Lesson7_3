from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Albom, Songs
from .serialisers import ArtistSerializer, AlbomSerializer, SongsSerializer


class LandingPageAPIView(APIView):
    def get(self, request):
        return Response(data={"get api": "get"})

    def post(self, request):
        return Response(data={"post api": "post"})


class ArtistAPIView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(data=serializer.data)


class AlbomAPIView(APIView):
    def get(self, request):
        albom = Albom.objects.all()
        serializer = AlbomSerializer(albom, many=True)
        return Response(data=serializer.data)


class SongsAPIView(APIView):
    def get(self, request):
        songs = Songs.objects.all()
        serializer = SongsSerializer(songs, many=True)
        return Response(data=serializer.data)
