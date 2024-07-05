from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views
from .views import VersionView, ProductView

router = SimpleRouter()
router.register('Version', VersionView)
router.register('Product', ProductView)

urlpatterns = [
    path('', views.main),
    path('Wrap', views.Wrap, name='Wrap'),
    path('ZWrap', views.ZWrap, name='ZWrap'),
    path('Wrap4D', views.Wrap4D, name='Wrap4D'),
]

urlpatterns += router.urls
