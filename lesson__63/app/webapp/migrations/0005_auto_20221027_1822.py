# Generated by Django 3.2 on 2022-10-27 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0004_alter_article_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=50, verbose_name='Текстовая заметка')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_users', to='webapp.article', verbose_name='Избранное')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_articles', to=settings.AUTH_USER_MODEL, verbose_name='Избранное')),
            ],
            options={
                'verbose_name': 'Избранная запись',
                'verbose_name_plural': 'Избранные записи',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='users',
            field=models.ManyToManyField(related_name='articles', through='webapp.Favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
