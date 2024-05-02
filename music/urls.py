from django.urls import path, include
from .views import LandingPageAPIView, ArtistDetailAPIView, SongAPIViewSet, AlbomDetailAPIView, ArtistAPIView, AlbomAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('song', viewset=SongAPIViewSet)

urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name='landing'),
    path('artist/', ArtistAPIView.as_view(), name='artist'),
    path('artist/<int:id>/', ArtistDetailAPIView.as_view(), name='artist-detail'),
    path('albom/', AlbomAPIView.as_view(), name='artist'),
    path('albom/<int:id>/', AlbomDetailAPIView.as_view(), name='albom-detail'),
    path('', include(router.urls)),
]
