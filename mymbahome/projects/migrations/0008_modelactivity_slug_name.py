# Generated by Django 3.1.7 on 2021-04-05 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20210402_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelactivity',
            name='slug_name',
            field=models.SlugField(default='', max_length=100, verbose_name='URL do conteúdo'),
            preserve_default=False,
        ),
    ]
