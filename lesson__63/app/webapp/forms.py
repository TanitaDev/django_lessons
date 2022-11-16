from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator, MinLengthValidator

from accounts.models import Profile
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


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class FavouriteForm(forms.Form):
    note = forms.CharField(max_length=50, required=True, label='Заметка')


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
