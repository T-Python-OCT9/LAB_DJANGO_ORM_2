# Generated by Django 4.1.3 on 2022-11-03 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppORM', '0003_alter_post_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Title',
            new_name='title',
        ),
    ]
