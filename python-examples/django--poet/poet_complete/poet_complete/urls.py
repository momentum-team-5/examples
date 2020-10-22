"""poet_in_class URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from poems import views as poems_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('contact/', poems_views.contact, name='contact'),
    path('', poems_views.poems_list, name='poems_list'),
    path('poems/<int:pk>/', poems_views.poems_detail, name='poems_detail'),
    path('poems/add/', poems_views.add_poem, name='add_poem'),
    path('poems/<int:pk>/edit/', poems_views.edit_poem, name='edit_poem'),
    path('poems/<int:pk>/delete/', poems_views.delete_poem, name='delete_poem'),
    path('poems/search/', poems_views.search, name='poems_search'),
    path('poems/favorite/<int:pk>/<int:user_pk>/', poems_views.add_favorite, name='poems_add_favorite')
]
