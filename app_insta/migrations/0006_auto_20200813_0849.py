# Generated by Django 3.1 on 2020-08-13 05:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_insta', '0005_auto_20200812_1511'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.RenameModel(
            old_name='Relations',
            new_name='Relation',
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='Hi, my name is <django.db.models.query_utils.DeferredAttribute object at 0x7f633e475c18>', max_length=500),
        ),
    ]