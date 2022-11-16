from django.contrib.auth.models import User
from django.db import models

from webapp.models import Article


class Favourite(models.Model):
    user = models.ForeignKey(to=User, related_name='favourite_articles', verbose_name='Избранное', null=False,
                             on_delete=models.CASCADE)
    article = models.ForeignKey(to=Article, related_name='favourite_users', verbose_name='Избранное', null=False,
                                on_delete=models.CASCADE)
    note = models.CharField(max_length=50, verbose_name='Текстовая заметка', null=False, blank=True)

    class Meta:
        verbose_name = 'Избранная запись'
        verbose_name_plural = 'Избранные записи'

    def __str__(self):
        return f'{self.user} {self.article}'
