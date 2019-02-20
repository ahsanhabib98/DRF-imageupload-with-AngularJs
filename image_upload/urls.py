from django.views.generic.base import RedirectView
from django.urls import path, include
from rest_framework import routers
from .views import UploadImageViewSet, index

router = routers.DefaultRouter()
router.register('images', UploadImageViewSet, 'images')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='static/index.html', permanent=False), name='index'),
    # path('', index, name='index'),
]
