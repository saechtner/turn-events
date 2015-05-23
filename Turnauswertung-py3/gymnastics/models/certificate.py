from django.core.urlresolvers import reverse
from django.db import models


class Certificate(models.Model):
  
    name = models.CharField(max_length=128)
    certificate_height = models.DecimalField('Paper height in cm', decimal_places=1, default=29.7)
    certificate_width = models.DecimalField('Paper width in cm', decimal_places=1, default=21.0)


    class Meta:
        db_table = 'gymnastics_certificates'