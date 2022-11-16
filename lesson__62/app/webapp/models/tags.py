from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Тег'
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
        return self.name
