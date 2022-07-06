from django import forms 
from .models import Comments 

class CommentForm(forms.ModelForm):
    class Meta: #meta class to configure it
        model = Comments
        exclude = ['post']
        labels = {
        "user_name" : "Your Name",
        "email" : "Your Email",
        "body": "Your Comment"
        }
        widgets = {            
        'body': forms.Textarea(
         attrs={'placeholder': 'Enter your comment here (you can use bbcode)'}),
        }
