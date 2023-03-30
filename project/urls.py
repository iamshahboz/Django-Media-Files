from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views import DogListCreate,DogAction


urlpatterns = [
    path('',include('app.urls')),
    path('admin/', admin.site.urls),

    path('api/Dog',DogListCreate.as_view()),
    path('api/Dog/<int:pk>',DogAction.as_view()),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
