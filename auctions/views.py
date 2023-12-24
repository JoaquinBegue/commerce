from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *
from .forms import *
from .util import *


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()})


def listing(request, listing_id):
    try:
        l = Listing.objects.get(pk=listing_id)
    except Listing.DoesNotExist:
        return render(request, "auctions/error.html", {"error": 1})
    
    if request.method == "POST":
        form = PlaceBidForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data["amount"]
            if amount < round(l.price * 1.1, 1):
                return render(request, "auctions/error.html", {"error": 2})

            l.price = amount
            l.save()

            instance = form.save(commit=False)
            instance.listing = l
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect(reverse("listing", kwargs={
                "listing_id": listing_id}))     

    else:
        form = PlaceBidForm()
        form.fields["amount"].widget.attrs["min"] = round(l.price * 1.1, 1)
        return render(request, "auctions/listing.html", {
            "listing": l, "form": form})
            


def categories(request):
    ...


def watchlist(request):
    ...


def create(request):
    if request.method == "POST":
        form = CreateListingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.save()
            return HttpResponseRedirect(reverse("index"))

    else:
        form = CreateListingForm(initial={'categ': 'Category'})

    return render(request, "auctions/create.html", {"form": form})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
        
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    
    else:
        return render(request, "auctions/register.html")
