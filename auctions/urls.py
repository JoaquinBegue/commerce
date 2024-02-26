from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("create", views.create, name="create"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("place_bid/<int:listing_id>", views.place_bid, name="place_bid"),
    path("manage_watchlist/<int:listing_id>", views.manage_watchlist, name="manage_watchlist"),
    path("manage_closing/<int:listing_id>", views.manage_closing, name="manage_closing"),
    path("categories", views.categories, name="categories"),
    path("<str:category>/listings", views.category_listings, name="category_listings"),
]
