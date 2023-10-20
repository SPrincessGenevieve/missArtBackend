from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from form import views as form_views
from about import views as about_views
from photos import views as photos_views
from django.conf import settings
from django.conf.urls.static import static


form_router = routers.DefaultRouter()
form_router.register(r'tasks', form_views.FormView, 'task') 

about_router = routers.DefaultRouter()
about_router.register(r'tasks', about_views.AboutView) 

photos_router = routers.DefaultRouter()
photos_router.register(r'tasks', photos_views.PhotosView) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/form', include(form_router.urls)),
    path('api/about/', include(about_router.urls)),
    path('api/photos/', include(photos_router.urls)), 
    path('api/upload/image/', include(photos_router.urls), name='upload_image'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)