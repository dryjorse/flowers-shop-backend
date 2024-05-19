from rest_framework.viewsets import ModelViewSet
from .models import Flower
from .serializers import FlowerSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, pagination

class FlowersView(ModelViewSet):
  queryset = Flower.objects.all()
  serializer_class = FlowerSerializer
  pagination_class = pagination.LimitOffsetPagination
  filter_backends = [DjangoFilterBackend, filters.SearchFilter]
  filterset_fields = ['category', 'is_promotion', 'is_seasonal']
  search_fields = ['title', 'materials']

