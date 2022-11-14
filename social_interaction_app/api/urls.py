from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('self-posts',views.PostViewSet,basename='self-post')
router.register('friends-posts',views.FriendsPostViewSet,basename='posts')

extended_router = routers.NestedSimpleRouter(router, r'friends-posts', lookup='posts')
extended_router.register(r'comment', views.CommentViewSet)


urlpatterns = [

    path('',include(router.urls)),
    path('',include(extended_router.urls)),
    path('friends-posts/react/<int:pk>/',views.like_unlike_post,name='react'),
   
  
]

# urlpatterns  = router.urls 
# http://localhost:8000/app/invite/?search=