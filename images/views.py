from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import ImageModel
from .serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all().order_by("-id")
    serializer_class = ImageSerializer
    search_fields = ("code",)
    filterset_fields = ("code",)
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    http_method_names = ["get", "post", "patch", "delete"]
