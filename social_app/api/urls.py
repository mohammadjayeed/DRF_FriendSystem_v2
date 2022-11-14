from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('friend',views.ProfileViewSet,basename='friends')

urlpatterns = [

    path('',include(router.urls)),
    path('user/',views.AllProfileList.as_view(),name='profile_list'),
    path('user/<int:pk>/invites/',views.send_invite,name='invite'),
    path('user/<int:pk>/declines/',views.decline_invite,name='decline'),
    path('user/<int:pk>/accepts/',views.accept_invite,name='accept')
    
]

# urlpatterns  = router.urls 
# http://localhost:8000/app/invite/?search=