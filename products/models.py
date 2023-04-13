from django.db import models
# always two lines in between according to pep8 guide

class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    stock = models.IntegerField()
    # 2083 max length of an url
    image_url = models.CharField(max_length = 2083)


class Offer(models.Model):
    code = models.CharField(max_length = 10)
    description = models.CharField(max_length = 255)
    discount = models.FloatField()



