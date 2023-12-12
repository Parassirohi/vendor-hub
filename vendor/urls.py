
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('vendors', views.VendorViewSet)
router

urlpatterns = [
    router.urls
]

