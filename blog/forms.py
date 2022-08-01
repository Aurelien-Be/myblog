from django import forms 
from .models import Comments
from django.utils.translation import gettext_lazy


class CommentForm(forms.ModelForm):
    class Meta: #meta class to configure it
        model = Comments
        exclude = ['post']
        labels = {
        "user_name" : (gettext_lazy("Your Name")),
        "email" : (gettext_lazy("Your Email")),
        "body": (gettext_lazy("Your Comment"))
        }
        widgets = {            
            'body': forms.Textarea(
                attrs={'placeholder':(gettext_lazy('Enter your comment here (you can use bbcode)'))}),
        }