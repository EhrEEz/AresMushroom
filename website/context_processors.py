from .models import Gallery, FAQ, Message


def is_detail(request):
    x = request.path
    v = x.split("/")
