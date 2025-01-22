from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Set up router
router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Token obtain
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh
    path('', include(router.urls)),  
]
