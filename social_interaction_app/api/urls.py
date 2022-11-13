from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('self-posts',views.PostViewSet,basename='self-post')
router.register('posts',views.FriendsPostViewSet,basename='posts')

urlpatterns = [

    path('',include(router.urls)),
    path('like-unlike/<int:pk>/',views.like_unlike_post,name='like-unlike')
   
    
]

# urlpatterns  = router.urls 
# http://localhost:8000/app/invite/?search=