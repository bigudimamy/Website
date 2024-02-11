from django.db import models

class CategoryProducts(models.Model):
    name_category = models.CharField('Название', max_length=70, unique=True)

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name_category

class Products(models.Model):
    name_product = models.CharField('Название', max_length=70)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество', default=0)
    image = models.ImageField('Фото', upload_to='products_image', blank=True, null=True)
    category = models.ForeignKey(to=CategoryProducts, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name_product