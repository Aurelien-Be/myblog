from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
#with include imported, we can register another path coming from our app blog 
from django.conf import settings
<<<<<<< HEAD
from django.utils.translation import gettext_lazy as _


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
        path('rosetta/', include('rosetta.urls'))
    ]
=======
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls"))
    #"" is the leading path segment 
    #in the second agument the blog urls, blog is the app and folder name, urls the file
    #we let the first string empty in order to access to the blog without adding /blog in the navigator 
>>>>>>> parent of 0f510d4 (rosetta)




#to access to images uploaded   :
] 
#  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
#  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
