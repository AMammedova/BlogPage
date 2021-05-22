
from django.urls import path
from .views import BlogPageView,BlogDetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(),name = 'post'),
    path('', BlogPageView.as_view(),name = 'index'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)