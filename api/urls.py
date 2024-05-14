from django.urls import path, include
from .views import (SongAPIViewSet, AlbomAPIViewSet, ArtistAPIViewSet, ProductsAPIViewSet, UsersAPIViewSet,
                    FeaturedProductsAPIViewSet, CategoryAPIViewSet)
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('songs', viewset=SongAPIViewSet)
router.register('alboms', viewset=AlbomAPIViewSet)
router.register('artists', viewset=ArtistAPIViewSet)
router.register('products', viewset=ProductsAPIViewSet)
router.register('categories', viewset=CategoryAPIViewSet)
router.register('featuredproducts', viewset=FeaturedProductsAPIViewSet)
router.register('users', viewset=UsersAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
]
