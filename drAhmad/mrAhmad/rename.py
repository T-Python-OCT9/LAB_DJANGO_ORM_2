
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrAhmad', '0001_init'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Content',
            new_name='Post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Content',
            new_name='content',
        ),
    ]