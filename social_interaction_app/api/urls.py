from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('posts',views.PostViewSet,basename='posts')
router.register('friend-posts',views.FriendsPostViewSet,basename='friend-posts')

urlpatterns = [

    path('',include(router.urls)),
    path('like-unlike/<int:pk>/',views.like_unlike_post,name='like-unlike')
   
    
]

# urlpatterns  = router.urls 
# http://localhost:8000/app/invite/?search=