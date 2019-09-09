from django.urls import path
from .views import (
    HomeView,
    GalleryView,
    GalleryDetailView,
    FAQView,
    FAQDetailView,
    MessageView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("gallery/<int:pk>/", GalleryDetailView.as_view(), name="detail"),
    path("faq/", FAQView.as_view(), name="faq"),
    path("faq/<int:pk>/", FAQDetailView.as_view(), name="faq_detail"),
    path("message/", MessageView.as_view(), name="new_message"),
]
