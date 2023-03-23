from django.urls import path
from api.views import MyObtainTokenPairView, RegisterView, UserApiView, ChangePasswordView , AccountMovementListView, AccountMovementDetailView , AMOptionsListView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', UserApiView.as_view(), name='user' ),
    path('api/register/',RegisterView.as_view(), name='auth_register'),
    path('api/change_password/<int:pk>', ChangePasswordView.as_view(), name='auth_change_password'),
    path("api/accountMovement/", AccountMovementListView.as_view(), name="AccountMovementList"),
    path("api/accountMovement/<int:pk>", AccountMovementDetailView.as_view(), name="AccountMovementId" ),
    path("api/accountMovement/options/", AMOptionsListView.as_view(), name="options"),
]