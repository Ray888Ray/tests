from django.urls import path
from api.views.api_authentication_views import MyTokenObtainPairView, MyTokenRefreshView
from api.views.api_protect_views import ProtectedView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('protected/', ProtectedView.as_view(), name='protected_view'),
]