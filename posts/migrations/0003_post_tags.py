# Generated by Django 3.2.9 on 2022-01-09 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('posts', '0002_post_spondored'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='tags.Tag'),
        ),
    ]
