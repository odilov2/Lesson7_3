from django.db.transaction import atomic
from rest_framework.response import Response
from rest_framework.decorators import action

from music.models import Songs, Albom, Artist
from products.models import Categories, Products, FeaturedProducts
from users.models import Users
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serialisers import (CategoriesSerializer, ProductsSerializer,
                          FeaturedProductsSerializer, UsersSerializer, ArtistSerializer, AlbomSerializer, SongsSerializer)

from rest_framework import filters, status
from rest_framework.pagination import LimitOffsetPagination


class ArtistAPIViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', ]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def search(self, request, *args, **kwargs):
        artist = self.get_object()
        with atomic():
            artist.search += 1
            artist.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['GET'])
    def member(self, request, *args, **kwargs):
        member = self.get_object()
        with atomic():
            member.member += 1
            member.save()
            return Response(status=status.HTTP_204_NO_CONTENT)


class AlbomAPIViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', ]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def artist(self, request, *args, **kwargs):
        albom = self.get_object()
        artist = albom.artist
        serializer = ArtistSerializer(artist)
        return Response(data=serializer.data)


class SongAPIViewSet(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['title', ]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def listen(self, request, *args, **kwargs):
        song = self.get_object()
        with atomic():
            song.listened += 1
            song.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        songs = self.get_queryset()
        songs = songs.order_by('-listened')
        serializer = SongsSerializer(songs, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET'])
    def alboms(self, request, *args, **kwargs):
        songs = self.get_object()
        alboms = songs.albom
        serializer = AlbomSerializer(alboms)
        return Response(data=serializer.data)


class ProductsAPIViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['title', 'price']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def category(self, request, *args, **kwargs):
        products = self.get_object()
        category = products.category_id
        serializer = CategoriesSerializer(category)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET'])
    def product(self, request, *args, **kwargs):
        products = self.get_queryset()
        products = products.order_by('price')
        serializer = ProductsSerializer(products, many=True)
        return Response(data=serializer.data)


class FeaturedProductsAPIViewSet(ModelViewSet):
    queryset = FeaturedProducts.objects.all()
    serializer_class = FeaturedProductsSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['title', 'price']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def featuredproducts(self, request, *args, **kwargs):
        featuredproducts = self.get_queryset()
        featuredproducts = featuredproducts.order_by('price')
        serializer = FeaturedProductsSerializer(featuredproducts, many=True)
        return Response(data=serializer.data)


class UsersAPIViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['first_name', ]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def user(self, request, *args, **kwargs):
        users = self.get_queryset()
        users = users.order_by('-id')
        serializer = UsersSerializer(users)
        return Response(data=serializer.data)


class CategoryAPIViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['title', ]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def category(self, request, *args, **kwargs):
        category = self.get_queryset()
        category = category.order_by('id')
        serializer = CategoriesSerializer(category, many=True)
        return Response(data=serializer.data)