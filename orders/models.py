from django.db import models

class Orders(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    price = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    warehouse = models.CharField(max_length=50, null=False, blank=False)
    order_date = models.DateField(auto_now_add=True)
    approved = models.BooleanField('Approved', default=False)

    def __str__(self) -> str:
        return self.description