from django.urls import path
from pages.views import (
    index,
    about,
)

urlpatterns = [
    path('',index),
    path('about/',about)
]
