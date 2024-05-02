from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
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
        return Response(serializer.data)


class ArtistDetailAPIView(APIView):
    def get(self, request, id):
        try:
            artist = Artist.objects.get(id=id)
            serializer = ArtistSerializer(artist)
            return Response(data=serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        artist = Artist.objects.get(id=id)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbomAPIView(APIView):
    def get(self, request):
        alboms = Albom.objects.all()
        serializer = AlbomSerializer(alboms, many=True)
        return Response(serializer.data)


class AlbomDetailAPIView(APIView):
    def get(self, request, id):
        try:
            albom = Albom.objects.get(id=id)
            serializer = AlbomSerializer(albom)
            return Response(data=serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        albom = Albom.objects.get(id=id)
        serializer = AlbomSerializer(instance=albom, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        albom = Albom.objects.get(id=id)
        serializer = AlbomSerializer(instance=albom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        albom = Albom.objects.get(id=id)
        albom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SongAPIViewSet(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

