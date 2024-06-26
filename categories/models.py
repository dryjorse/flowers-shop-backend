from django.db import models

class Category(models.Model):
  title = models.CharField("Название", max_length=250)

  class Meta:
    verbose_name = "Категории"
    verbose_name_plural = "Категории"

  def __str__(self):
    return self.title
