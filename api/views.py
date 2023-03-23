from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView , ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import LoginSerializer ,UserSerializer, ChangePasswordSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User
from .serializers import RegisterSerializer , AccountMovementSerializer, AMOptionsSerializer
from rest_framework import generics
from .models import AccountMovement, AMOptions



# login
class  MyObtainTokenPairView(TokenObtainPairView):
    permission_classes=(AllowAny,)
    serializer_class= LoginSerializer
# userDetail
class UserApiView (RetrieveAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user
# signup
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes= [AllowAny,]
    serializer_class = RegisterSerializer
#change Password
class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class= ChangePasswordSerializer

class AccountMovementListView(ListCreateAPIView):
    serializer_class = AccountMovementSerializer
    queryset = AccountMovement.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(owner = self.request.user)
    
class AccountMovementDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = AccountMovementSerializer
    queryset = AccountMovement.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class AMOptionsListView(ListCreateAPIView):
    serializer_class= AMOptionsSerializer
    queryset= AMOptions.objects.all()
    permission_classes = [IsAuthenticated]