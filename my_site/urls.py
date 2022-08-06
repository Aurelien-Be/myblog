"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
#with include imported, we can register another path coming from our app blog 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

#we include all the urls of the app blog, and we add the prefix language
urlpatterns += i18n_patterns (
    path("", include("blog.urls"))
)

#to edit the translations in an admin-like module
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]



#to access to images uploaded   :
#  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
#  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
