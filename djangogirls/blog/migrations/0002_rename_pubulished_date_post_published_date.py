# Generated by Django 3.2.13 on 2022-05-17 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pubulished_date',
            new_name='published_date',
        ),
    ]
