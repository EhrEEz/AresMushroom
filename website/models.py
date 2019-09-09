from django.db import models


class BaseModel(models.Model):
    upload_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Gallery(BaseModel):
    photo = models.ImageField(upload_to="gallery")
    caption = models.CharField(max_length=100)
    description = models.TextField()
    credit = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
        ordering = ["-upload_date", "-modify_date"]


class FAQ(BaseModel):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    photo = models.ImageField(upload_to="Problem Image", null=True, blank=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ["-upload_date", "-modify_date"]

    def __str__(self):
        return self.title


class Message(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=10, null=False, blank=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to="Problem Image", null=True, blank=True)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ["-upload_date", "-modify_date"]

    def __str__(self):
        return self.title
