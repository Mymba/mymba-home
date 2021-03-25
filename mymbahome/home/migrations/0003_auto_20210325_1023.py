# Generated by Django 3.1.7 on 2021-03-25 13:23

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210324_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(max_length=250, verbose_name='Assunto')),
                ('message', models.TextField(verbose_name='Mensagem')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
        ),
        migrations.AlterField(
            model_name='modeltestimony',
            name='image',
            field=models.ImageField(blank=True, upload_to='home\\testimonials', validators=[home.models.validador_image_size], verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='modeltestimony',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='modeltestimony',
            name='profession',
            field=models.CharField(blank=True, max_length=50, verbose_name='Profissão'),
        ),
        migrations.AlterField(
            model_name='modeltestimony',
            name='social_media_link',
            field=models.URLField(max_length=50, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='modeltestimony',
            name='testimony',
            field=models.CharField(max_length=200, verbose_name='Depoimento'),
        ),
    ]
