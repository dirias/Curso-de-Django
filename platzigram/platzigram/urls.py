# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from platzigram import views as local_views
from  posts import views as posts_views
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-word/', local_views.hello_word),
    path('hi/', local_views.hi),
    path('name/<str:name>/<int:age>/', local_views.say_hi),
    path('posts/', posts_views.list_posts)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
