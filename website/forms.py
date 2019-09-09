from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("name", "email", "phone", "title", "description", "photo")
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-name",
                    "id": "name",
                    "placeholder": "Enter your Full Name",
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "form-email",
                    "id": "email",
                    "placeholder": "Enter your email address",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-phone",
                    "id": "phone",
                    "placeholder": "Phone Number",
                }
            ),
            "title": forms.TextInput(
                attrs={
                    "class": "form-title",
                    "id": "title",
                    "placeholder": "Your message title",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-description",
                    "id": "description",
                    "placeholder": "Describe your message",
                }
            ),
        }
        labels = {
            "name": "Full Name: ",
            "email": "Email: ",
            "phone": "Phone Number: ",
            "title": "Subject:    ",
            "description": "Description: ",
            "photo": "Photo:",
        }
