# Generated by Django 4.0.3 on 2022-06-06 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlador', '0020_comment_approved_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
