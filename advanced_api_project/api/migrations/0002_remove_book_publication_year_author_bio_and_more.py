# Generated by Django 5.1.7 on 2025-03-31 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publication_year',
        ),
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(default='No bio available'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(default='No bio available'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
