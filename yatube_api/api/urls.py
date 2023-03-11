from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


v1_router = SimpleRouter()
v1_router.register('posts', PostViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')
v1_router.register('groups', GroupViewSet)
v1_router.register('follow', FollowViewSet, basename='follow')

jwt_patterns = [
    path('create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify')
]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/jwt/', include(jwt_patterns)),
]
