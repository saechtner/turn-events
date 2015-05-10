from django.db import models
from django.utils.translation import ugettext_lazy


class Address(models.Model):

    contact_name = models.CharField(ugettext_lazy('Contact name'), max_length=64)
    phone = models.CharField(ugettext_lazy('Contact phone'), max_length=15, null=True, blank=True)
    email = models.EmailField(ugettext_lazy('Contact email'), null=True, blank=True)
    street = models.CharField(ugettext_lazy('Street'), max_length=128)
    city = models.CharField(ugettext_lazy('City'), max_length=128)
    province = models.CharField(ugettext_lazy('Province'), max_length=128)
    zip_code = models.CharField(ugettext_lazy('Zip code'), max_length=10)


    class Meta:
        db_table = 'gymnastics_addresses'


    @property
    def address_formatted(self):
        return '{0}\n{1} {2}\n{3}'.format(self.street, self.zip_code, self.city, self.province)
    