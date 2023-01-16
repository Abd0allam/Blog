from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:category_slug>/<slug:post_slug>/<comment_id>/', views.reply, name='comment_detail'),
    path('<slug:slug>/', views.category, name='category_detail')
]
