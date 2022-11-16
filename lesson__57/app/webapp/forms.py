from django import forms
from .models import *
from django.core.exceptions import ValidationError


class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].empty_label = 'Заголовок'

    class Meta:
        model = Article
        fields = ['title', 'author', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 73, 'rows': 5, 'class': ''})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 2:
            raise ValidationError('Длина превышает 200 символов')

        return title
