from django.urls import path

from listings.views import (
    search,
    listings,
    listing
)

urlpatterns = [
    path('', listings, name="listings"),
    path('<int:listing_id>', listing, name="listing"),
    path('search/', search, name='search')
]
