from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('posts',views.PostViewSet,basename='posts')
router.register('friend-posts',views.FriendsPostViewSet,basename='friend-posts')

urlpatterns = [

    path('',include(router.urls)),
   
    
]

# urlpatterns  = router.urls 
# http://localhost:8000/app/invite/?search=