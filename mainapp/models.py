from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='products'
    )

    name = models.CharField(max_length=127)
    description = models.TextField()
    price = models.PositiveBigIntegerField(default=0)
    discount = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.name
    
    @property
    def final_price(self):
        if self.discount > 0:
            return round(self.price - (self.price / 100 * self.discount))
        return self.price