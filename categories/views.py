from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer

class CategoriesView(ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer