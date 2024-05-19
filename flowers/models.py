from django.db import models
from categories.models import Category

class Flower(models.Model):
  title = models.CharField("Название", max_length=250)
  size = models.CharField("Размер", max_length=250)
  materials = models.CharField("Материалы", max_length=250)
  price = models.DecimalField("Цена", max_digits=7, decimal_places=2, default=0)
  discount_percentage = models.IntegerField("Процент скидки", default=0)
  in_stock = models.BooleanField("В наличии", default=True)
  description = models.TextField("Описание", blank=True)
  date = models.DateTimeField("Дата публикации")
  is_promotion = models.BooleanField("В акции", default=False)
  is_seasonal = models.BooleanField("Сезонный", default=False)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

  class Meta:
    verbose_name = "Цветы"
    verbose_name_plural = "Цветы"

  def __str__(self):
    return self.title
  
class Image(models.Model):
  flower = models.ForeignKey(Flower, on_delete=models.CASCADE, related_name="images")
  image = models.ImageField(upload_to="images/flowers")
