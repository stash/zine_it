# Generated by Django 5.1.2 on 2024-12-08 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_zine_page_index_page_zine'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(null=True, upload_to='uploaded_images/'),
        ),
    ]