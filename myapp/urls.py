from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('todos/', views.todos, name="todos"),
    path('booking/', views.book, name="book"),
    path('contact/', views.contact, name="contact"),
    path('news/', views.news_list, name='news_list'),
    path('accounts/', include('allauth.urls')),

    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)