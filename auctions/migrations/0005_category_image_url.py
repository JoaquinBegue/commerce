# Generated by Django 5.0.3 on 2024-04-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_listing_active_alter_listing_image_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image_url',
            field=models.TextField(blank=True, default='https://www.freeiconspng.com/thumbs/no-image-icon/no-image-icon-15.png', null=True),
        ),
    ]
