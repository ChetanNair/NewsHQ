# Generated by Django 4.0 on 2021-12-30 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_headline_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('url', models.TextField()),
                ('count', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Headline',
        ),
        migrations.AddField(
            model_name='article',
            name='parent_website',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.website'),
        ),
    ]
