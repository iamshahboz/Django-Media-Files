from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage, name='homepage'),

    path('api/Dog',views.DogListCreate.as_view()),
    path('api/Dog/<int:pk>',views.DogDetail.as_view()),

    path('api/Book',views.BookListCreate.as_view()),
    path('api/Book/<int:pk>',views.BookDetail.as_view()),

    path('api/Author',views.AuthorListCreate.as_view()),
    path('api/Author/<int:pk>',views.AuthorDetail.as_view()),

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

