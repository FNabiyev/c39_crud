from django.db import models


class Kasblar(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Hodimlar(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birthday = models.DateField()
    kasb = models.ForeignKey(Kasblar, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name
