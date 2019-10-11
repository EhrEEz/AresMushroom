from .models import Gallery, FAQ, Message, Post


def total_posts(request):
    if request.user.is_authenticated:
        return {
            "total_posts": Post.objects.filter(
                creator=request.user, is_published=True
            ).count()
        }
    return {}


def is_detail(request):
    x = request.path
    v = x.split("/")
