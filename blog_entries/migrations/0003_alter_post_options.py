# Generated by Django 3.2.9 on 2021-12-28 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_entries', '0002_auto_20211121_1841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',)},
        ),
    ]
