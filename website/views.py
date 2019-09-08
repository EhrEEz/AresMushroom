from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.models import User

from el_pagination.views import AjaxListView

from .models import Gallery, FAQ, Message


class BaseView(TemplateView):
    template_name = "base.html"
    model = User


class HomeView(TemplateView):
    model = Gallery
    template_name = "home.html"


class GalleryView(AjaxListView):
    context_object_name = "object_list"
    model = Gallery
    template_name = "gallery.html"

    def get_queryset(self):
        return Gallery.objects.all()


class GalleryDetailView(DetailView):
    model = Gallery
    template_name = "gallery_details.html"


class FAQView(AjaxListView):
    context_object_name = "object_list"
    template_name = "faq.html"

    def get_queryset(self):
        return FAQ.objects.all()


class FAQDetailView(DetailView):
    model = FAQ
    template_name = "faq_details.html"
