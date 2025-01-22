from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, UserRegistrationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Set up router for the Todo viewset
router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [
    # User registration endpoint
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    
    # JWT token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Todo endpoints
    path('api/', include(router.urls)),  # Include the router for TodoViewSet
]
