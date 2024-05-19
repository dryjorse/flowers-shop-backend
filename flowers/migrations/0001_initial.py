# Generated by Django 5.0.2 on 2024-05-16 23:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('size', models.CharField(max_length=250, verbose_name='Размер')),
                ('materials', models.CharField(max_length=250, verbose_name='Материалы')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Цена')),
                ('discount_percentage', models.IntegerField(default=0, verbose_name='Процент скидки')),
                ('in_stock', models.BooleanField(default=True, verbose_name='В наличии')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
                ('is_promotion', models.BooleanField(default=False, verbose_name='В акции')),
                ('is_seasonal', models.BooleanField(default=False, verbose_name='Сезонный')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category')),
            ],
            options={
                'verbose_name': 'Цветы',
                'verbose_name_plural': 'Цветы',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/flowers')),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='flowers.flower')),
            ],
        ),
    ]
