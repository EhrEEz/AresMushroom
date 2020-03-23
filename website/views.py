from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView

from django.urls import reverse

from django.contrib import messages

from django.contrib.auth.models import User

from el_pagination.views import AjaxListView

from .models import Gallery, FAQ, Message, Product

from .forms import MessageForm

from django.shortcuts import render, get_object_or_404

from django.urls import reverse


class BaseView(TemplateView):
    template_name = "base.html"
    model = User


class HomeView(TemplateView):
    model = Gallery
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carousel_data"] = Gallery.objects.filter(photo__isnull=False).exclude(
            photo=""
        )[:5]
        context["product_data"] = Product.objects.all()[:2]
        return context


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


class MessageView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = "create_message.html"

    def get_success_url(self):
        messages.success(self.request, "Your message has been posted")
        return reverse("gallery")


class ContactUsView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = "contact.html"

    def get_success_url(self):
        messages.success(self.request, "Your message has been posted")
        return reverse("gallery")


class AboutUsView(TemplateView):
    model = Message
    template_name = "about_us.html"


class ProductView(AjaxListView):
    context_object_name = "products_list"
    template_name = "products.html"

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_details.html"
