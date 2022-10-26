from django.urls import path
from django.contrib import admin
from main.views import index, blog, posting, new_post

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>/', posting, name='posting'),
    path('blog/new_post/', new_post),
]

# set the image url
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
