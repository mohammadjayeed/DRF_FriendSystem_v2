from django.urls import path
from .views import RegistrationAPIView,  MyTokenObtainPairView, LogoutBlacklistTokenUpdateView, DemoView #VerifyOTPAPIView,  DemoView2,
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    # ---- Not providing refresh functionality as requirement did not mention explicitly---
    # path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('logout/', LogoutBlacklistTokenUpdateView.as_view(), name='logout'),
    path('register/', RegistrationAPIView.as_view(), name='registration'),
    path('experiment/',DemoView.as_view(),name='demo'),
    # path('experiment2/',DemoView2.as_view(),name='demo2')

]