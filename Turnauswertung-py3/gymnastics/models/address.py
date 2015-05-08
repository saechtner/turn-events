
from django.db import models
from django.utils.translation import ugettext_lazy

class Address(models.Model):
    street = models.TextField(ugettext_lazy('street'), max_length=128)
    city = models.TextField(ugettext_lazy('city'), max_length=128)
    province = models.TextField(ugettext_lazy('province'), max_length=128)
    zip_code = models.TextField(ugettext_lazy('zip code'), max_length=10)