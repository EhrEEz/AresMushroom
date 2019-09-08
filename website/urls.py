from django.urls import path, include
from .views import (
    HomeView,
    BaseView,
    GalleryView,
    GalleryDetailView,
    FAQView,
    FAQDetailView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("gallery/<int:pk>/", GalleryDetailView.as_view(), name="detail"),
    path("faq/", FAQView.as_view(), name="faq"),
    path("faq/<int:pk>/", FAQDetailView.as_view(), name="faq_detail"),
]
