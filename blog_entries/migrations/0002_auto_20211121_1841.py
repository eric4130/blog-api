# Generated by Django 3.2.9 on 2021-11-21 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_entries', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('title',)},
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
