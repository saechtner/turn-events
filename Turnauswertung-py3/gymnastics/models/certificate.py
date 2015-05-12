from django.core.urlresolvers import reverse
from django.db import models


class Certificate(models.Model):
  
    name = models.CharField(max_length=128)
    certificate_height = models.IntegerField('Paper height in mm', default=297)
    certificate_width = models.IntegerField('Paper width in mm', default=210)


    class Meta:
        db_table = 'gymnastics_certificates'