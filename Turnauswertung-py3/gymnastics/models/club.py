from django.db import models


class Club(models.Model):
  
    name = models.CharField(max_length=50)

    contact_name = models.CharField(max_length=50, null=True, blank=True)
    contact_mail = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=50, null=True, blank=True)
    contact_street = models.CharField(max_length=100, null=True, blank=True)
    contact_zip_code = models.CharField(max_length=10, null=True, blank=True)
    contact_city = models.CharField(max_length=50, null=True, blank=True)


    class Meta:
        db_table = 'gymnastics_clubs'

    def __str__(self):
        return self.name