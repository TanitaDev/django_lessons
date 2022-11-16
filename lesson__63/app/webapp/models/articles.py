from django.db import models
from django.contrib.auth.models import User

from webapp.managers import ArticleManager


class Article(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Заголовок"
    )
    text = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name='Текст'
    )
    author = models.CharField(
        max_length=40,
        null=False,
        blank=False,
        default='Unknown',
        verbose_name='Автор'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Время изменения'
    )
    tags = models.ManyToManyField(
        to='webapp.Tag',
        related_name='articles',
        blank=True
    )

    users = models.ManyToManyField(
        through='webapp.Favourite',
        to=User,
        related_name='articles'
    )

    objects = ArticleManager()

    def __str__(self):
        return "{}. {}".format(self.pk, self.title)

    class Meta:
        permissions = [
            ('сan_have_piece_of_pizza', 'Может съесть кусочек пиццы')
        ]
