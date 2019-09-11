from django.urls import path
from .views import (
    HomeView,
    GalleryView,
    GalleryDetailView,
    FAQView,
    FAQDetailView,
    MessageView,
    ContactUsView,
    AboutUsView,
    ProductsView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("gallery/<int:pk>/", GalleryDetailView.as_view(), name="detail"),
    path("faq/", FAQView.as_view(), name="faq"),
    path("faq/<int:pk>/", FAQDetailView.as_view(), name="faq_detail"),
    path("message/", MessageView.as_view(), name="new_message"),
    path("contact/", ContactUsView.as_view(), name="contact"),
    path("about-us/", AboutUsView.as_view(), name="about"),
    path("products/", ProductsView.as_view(), name="products"),
]
