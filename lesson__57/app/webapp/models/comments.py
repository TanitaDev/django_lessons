from django.db import models


class Comment(models.Model):
    article = models.ForeignKey(
        'webapp.Article',
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Статья'
    )
    text = models.TextField(
        max_length=400,
        verbose_name='Комментарий'
    )
    author = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        default='Аноним',
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

    def __str__(self):
        return f'{self.author} : {self.text[:20]}'
