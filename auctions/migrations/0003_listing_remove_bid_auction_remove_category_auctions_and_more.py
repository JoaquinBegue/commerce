# Generated by Django 4.2.7 on 2023-12-18 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auction_watchlist_comment_category_bid_auction_categ_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image_url', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='bid',
            name='auction',
        ),
        migrations.RemoveField(
            model_name='category',
            name='auctions',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='auction',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='auctions',
        ),
        migrations.DeleteModel(
            name='Auction',
        ),
        migrations.AddField(
            model_name='listing',
            name='categ',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auctions.category'),
        ),
        migrations.AddField(
            model_name='listing',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='listing',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='won', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bid',
            name='listing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.listing'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='listings',
            field=models.ManyToManyField(blank=True, to='auctions.listing'),
        ),
        migrations.AddField(
            model_name='comment',
            name='listing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.listing'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchlist',
            name='listings',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to='auctions.listing'),
        ),
    ]
