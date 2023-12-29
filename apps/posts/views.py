from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer, PostCreateSerializer
from apps.posts.permissions import PostPermission

# Create your views here.
class PostAPIView(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny, )
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('title', 'description', 'user')
    shearch_fields = ('title', 'description', 'user__username')

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action == "create":
            return PostCreateSerializer
        return PostSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (PostPermission(), )
        return (AllowAny(), )