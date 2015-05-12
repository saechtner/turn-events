from django.core.urlresolvers import reverse
from django.db import models


class CertificateRule(models.Model):
  
    content = models.CharField(max_length=128)# might be a choice field ()
    vertical_position = models.CharField(max_length=50, null=True, blank=True)# center or x mm / x cm / x m has to be parsed (better option?)
    horizontal_position = models.CharField('Horizontal position (in mm/cm)', max_length=50, default='150 mm')# center or x mm / x cm / x m has to be parsed (better option?)

    certificate = models.ForeignKey('Certificate')


    class Meta:
        db_table = 'gymnastics_certificate_rules'