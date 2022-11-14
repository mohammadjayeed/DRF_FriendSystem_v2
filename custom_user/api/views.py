from .serializers import RegistrationSerializer, MyTokenObtainPairSerializer 
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegistrationAPIView(generics.GenericAPIView):
    
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        data = {}
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data['response'] = "Registration Successful!"

            # -------- token feedback disabled to meet requirement -----
            # refresh = RefreshToken.for_user(user=user)
            # data['refresh'] = str(refresh)
            # data['access'] = str(refresh.access_token)


        return Response(data, status.HTTP_201_CREATED)

class LogoutBlacklistTokenUpdateView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)

            token.blacklist()
           
            return Response(status=status.HTTP_205_RESET_CONTENT)
            
        except Exception as e:

            return Response(status=status.HTTP_400_BAD_REQUEST)

# class DemoView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
    
    
#     def get(self,request):
#         try:
#             return Response("accessed")
#         except Exception as e:
#             print(e)
#             return Response("no access given")