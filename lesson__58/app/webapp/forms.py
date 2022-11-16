from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator, MinLengthValidator

from .models import *


def max_length_validator(string):
    if len(string) > 10:
        raise ValidationError('Слишком длинно')
    return string


class CustomLengthValidator(BaseValidator):
    def __init__(self, limit_value=20, message=''):
        message = 'Максимальное %(limit_value)s, вы ввели %(show_value)s'
        super(CustomLengthValidator, self).__init__(limit_value=limit_value, message=message)

    def compare(self, value, max_value):
        return max_value < value

    def clean(self, value):
        return len(value)


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200, label='Заголовок',
        validators=(MinLengthValidator(limit_value=2, message='dsad'),
                    CustomLengthValidator())
    )

    class Meta:
        model = Article
        fields = ['title', 'author', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 73, 'rows': 5, 'class': ''})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 2:
            raise ValidationError('Длина маленькая')
        if Article.objects.filter(title=title).exists():
            raise ValidationError('уже есть')
        return title
