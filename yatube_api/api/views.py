from rest_framework import (
    viewsets,
    pagination,
    permissions,
    mixins,
    exceptions,
    filters
)
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from posts.models import Post, Group, Follow
from api.serializers import (
    PostSerializer,
    CommentSerializer,
    GroupSerializer,
    FollowSerializer,
)
from api.permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.select_related()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.AllowAny,)


class FollowViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    serializer_class = FollowSerializer
    search_fields = ('following__username', 'user__username')
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        return self.request.user.followings.select_related()

    def perform_create(self, serializer):
        following = serializer.validated_data.get('following')
        if following == self.request.user.username:
            raise exceptions.ValidationError({
                "detail": "Вы не можете подписаться на самого себя."
            })
        following_user = User.objects.filter(username=following)
        if not following_user:
            raise exceptions.ValidationError({
                "following": [
                    "Обязательное поле."
                ]
            })
        if Follow.objects.filter(
                user=self.request.user.id,
                following=following_user.first().id
        ).exists():
            raise exceptions.ValidationError({
                "detail": "На этого автора вы уже подписаны."
            })
        serializer.save(
            user=self.request.user, following=following_user.first())
