from django import forms
from .models import BlogPost

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': '', 'text': ''}
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Add title'}),
            'text': forms.Textarea(attrs={'placeholder': 'Add text'}),
        }