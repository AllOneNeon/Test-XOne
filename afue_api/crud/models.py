from django.db import models
from django.core.validators import MinValueValidator
from django.db import models

from config.models import SpecialInformation
from accounts.models import User

class Category(SpecialInformation):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=50)
    total_amount = models.DecimalField(
        default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)]
    )

    def __str__(self):
        return f"{self.user} | {self.name}"

class Transaction(SpecialInformation):
    amount = models.DecimalField(
        default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)]
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    organization = models.CharField(default="", max_length=100)

    def __str__(self):
        return f"{self.category} | {self.amount}"


