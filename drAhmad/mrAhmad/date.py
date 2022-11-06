
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrAhmad', 'RENAME'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=1024),
        ),
    ]