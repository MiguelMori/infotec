# Generated by Django 4.0.3 on 2022-05-31 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlador', '0005_alter_like_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='Hola, estoy usando Infotec', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='tony.jpg', upload_to=''),
        ),
    ]