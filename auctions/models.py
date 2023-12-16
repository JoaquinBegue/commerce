from django.contrib.auth.models import AbstractUser
from django.db import models as m


class User(AbstractUser):
    pass


class Auction(m.Model):
    title = m.CharField(max_length=64)
    description = m.TextField()
    price = m.FloatField()
    categ = m.ForeignKey('Category', on_delete=m.SET_NULL, blank=True, null=True)
    date = m.DateTimeField(auto_now_add=True)
    image_url = m.TextField(blank=True)
    creator = m.ForeignKey(User, related_name="auctions", on_delete=m.CASCADE)
    winner = m.ForeignKey(User, related_name="won", on_delete=m.SET_NULL, blank=True, null=True)


class Bid(m.Model):
    amount = m.FloatField()
    auction = m.ForeignKey(Auction, related_name='bids', on_delete=m.CASCADE)
    author = m.ForeignKey(User, related_name='bids', on_delete=m.CASCADE)


class Comment(m.Model):
    text = m.TextField()
    auction = m.ForeignKey(Auction, related_name='comments', on_delete=m.CASCADE)
    author = m.ForeignKey(User, related_name='comments', on_delete=m.SET_NULL, null=True)
    date = m.DateTimeField(auto_now_add=True)


class Category(m.Model):
    name = m.CharField(max_length=30)
    auctions = m.ManyToManyField(Auction, blank=True)


class Watchlist(m.Model):
    owner = m.ForeignKey(User, related_name='watchlist', on_delete=m.CASCADE)
    auctions = m.ManyToManyField(Auction, related_name='watchlist', blank=True)