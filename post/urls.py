from django.urls import path
from post import views as post_views

app_name = 'post'

urlpatterns = [
    path('', post_views.IndexView.as_view(), name='index'),
    path('about/', post_views.about, name='about'),
    path('contact/', post_views.contact, name='contact'),
    path('post/<pk>', post_views.PostView.as_view(), name='detail'),
]