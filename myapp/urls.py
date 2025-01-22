from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, UserRegistrationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Set up router for TodoViewSet
router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='user_register'),  # Registration endpoint
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Token obtain endpoint
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh endpoint
    path('', include(router.urls)),  # Todo endpoints
]
