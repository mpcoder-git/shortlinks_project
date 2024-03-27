from django.urls import path
from .views import add_link,user_links

urlpatterns = [
    path('add_link/', add_link, name = 'add_link'),
    path('user/<int:user>', user_links, name = 'user_links')
]