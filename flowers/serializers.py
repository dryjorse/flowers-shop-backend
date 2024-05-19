from rest_framework import serializers
from .models import Flower, Image
from decimal import Decimal

class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Image
    fields = ["id", "image"]

class DiscountedPrice(serializers.Field):
  def to_representation(self, instance):
    discounted_price = instance.price - (instance.price * (Decimal(instance.discount_percentage) / 100))
    float_digits = discounted_price % 1
    total_price = Decimal(str(int(discounted_price))[:-1] + "0") + float_digits
    return total_price

class FlowerSerializer(serializers.ModelSerializer):
  images = ImageSerializer(many=True, read_only=True)
  total_price = DiscountedPrice(source='*', read_only=True)

  class Meta:
    model = Flower
    fields = "__all__"