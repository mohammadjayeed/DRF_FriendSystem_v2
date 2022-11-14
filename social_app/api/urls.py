from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('friend',views.ProfileViewSet,basename='friends')

urlpatterns = [

    path('',include(router.urls)),
    path('user/',views.AllProfileList.as_view(),name='profile_list'),
    path('invite/<int:pk>',views.send_invite,name='invite'),
    path('decline/<int:pk>',views.decline_invite,name='decline')
    
]

# urlpatterns  = router.urls 
# http://localhost:8000/app/invite/?search=