# Generated by Django 4.0 on 2021-12-23 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_remove_headline_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='text',
            field=models.TextField(default='Test'),
            preserve_default=False,
        ),
    ]
