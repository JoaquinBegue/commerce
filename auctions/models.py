from django.contrib.auth.models import AbstractUser
from django.db import models as m


class User(AbstractUser):
    pass


class Listing(m.Model):
    title = m.CharField(max_length=64)
    description = m.TextField()
    price = m.FloatField()
    categ = m.ForeignKey('Category', on_delete=m.SET_NULL, blank=True, null=True)
    date = m.DateTimeField(auto_now_add=True)
    image_url = m.TextField(blank=True)
    creator = m.ForeignKey(User, related_name="listings", on_delete=m.CASCADE)
    winner = m.ForeignKey(User, related_name="won", on_delete=m.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"({self.id}) {self.title}"


class Bid(m.Model):
    amount = m.FloatField()
    listing = m.ForeignKey(Listing, related_name='bids', on_delete=m.CASCADE)
    author = m.ForeignKey(User, related_name='bids', on_delete=m.CASCADE)

    def __str__(self):
        return f"({self.id}) {self.author} bids ${self.amount} for {self.listing}"


class Comment(m.Model):
    text = m.TextField()
    listing = m.ForeignKey(Listing, related_name='comments', on_delete=m.CASCADE)
    author = m.ForeignKey(User, related_name='comments', on_delete=m.SET_NULL, null=True)
    date = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.id}) Author: {self.author} about {self.listing}"


class Category(m.Model):
    name = m.CharField(max_length=30)
    listings = m.ManyToManyField(Listing, blank=True)

    def __str__(self):
        return f"({self.id}) {self.name}"


class Watchlist(m.Model):
    owner = m.ForeignKey(User, related_name='watchlist', on_delete=m.CASCADE)
    listings = m.ManyToManyField(Listing, related_name='watchlist', blank=True)

    def __str__(self):
        return f"({self.id}) {self.owner}"