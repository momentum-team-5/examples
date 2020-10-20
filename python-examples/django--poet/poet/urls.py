"""poet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path
from poems import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contact_us'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.poems_list, name='poems_list'),
    path('<int:pk>/', views.poems_detail, name='poems_detail'),
    path('create/', views.poems_create, name='poems_create'),
    path('update/<int:pk>/', views.poems_update, name='poems_update'),
    path('delete/<int:pk>/', views.poems_delete, name='poems_delete'),
    path('<int:pk>/add_comment/', views.add_comment, name='add_comment')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
