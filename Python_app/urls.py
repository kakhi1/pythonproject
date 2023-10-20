from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles, name='articles'),
    path('clients/', views.clients, name='clients'),
    path('filterwords/', views.filterwords, name='filterwords'),
    path('sites/', views.sites, name='sites'),
 ]
# from django.urls import path, include

# urlpatterns = [
#     path('', include('admin_volt.urls')),
# ]