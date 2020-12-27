from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('properties/', properties, name='properties'),
    path("properties/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path('services/', services, name='services'),
    path('articles/', articles, name='articles'),
    path("articles/<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path('videos/', videos, name='videos'),
    path("videos/<slug:slug>/", VideoDetailView.as_view(), name="video_detail"),
]
