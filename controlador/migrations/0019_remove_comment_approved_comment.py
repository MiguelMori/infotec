# Generated by Django 4.0.3 on 2022-06-06 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controlador', '0018_alter_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
    ]
