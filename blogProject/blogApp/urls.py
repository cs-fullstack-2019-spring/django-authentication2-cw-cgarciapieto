from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_blogs, name='allblogs'),
    path('myblog/', views.blog_entry, name='blogentry'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]