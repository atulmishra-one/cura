from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32, null=True)
    roll_number = models.CharField(max_length=40)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

