from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='projects'),
    path('articles/', views.article_list, name='articles'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)