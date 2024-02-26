from django.urls import path

from . import views

urlpatterns = [
    # Listing related.
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("place_bid/<int:listing_id>", views.place_bid, name="place_bid"),
    path("add_comment/<int:listing_id>", views.add_comment, name="add_comment"),
    path("manage_closing/<int:listing_id>", views.manage_closing, name="manage_closing"),

    # Categories related.
    path("categories", views.categories, name="categories"),
    path("<str:category>/listings", views.category_listings, name="category_listings"),
    
    # Watchlist related.
    path("watchlist", views.watchlist, name="watchlist"),
    path("manage_watchlist/<int:listing_id>", views.manage_watchlist, name="manage_watchlist"),

    # User related.
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
]
