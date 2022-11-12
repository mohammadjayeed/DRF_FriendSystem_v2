from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('profile',views.ProfileViewSet,basename='profile')

urlpatterns  = router.urls 