# Generated by Django 3.2 on 2022-10-06 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20221006_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tags',
            new_name='tags_old',
        ),
    ]