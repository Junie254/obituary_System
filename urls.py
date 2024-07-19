from django.contrib import admin
from django.urls import path
from obituaries import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('submit/', views.submit_obituary, name='submit_obituary'),
    path('view/', views.view_obituaries, name='view_obituaries'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
