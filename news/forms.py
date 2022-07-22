from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'preview', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': "News title"
            }),
            'preview': TextInput(attrs={
                'class': "form-control",
                'placeholder': "News preview"
            }),
            'full_text': Textarea(attrs={
                'class': "form-control",
                'placeholder': "News full text"
            }),
            'date': DateTimeInput(attrs={
                'class': "form-control",
                'placeholder': "Publication date"
            })
        }
