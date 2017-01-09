from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy


class Club(models.Model):
  
    name = models.CharField(ugettext_lazy('Name'), max_length=50)

    address = models.ForeignKey('gymnastics.Address', null=True, blank=True, verbose_name=ugettext_lazy('Address'))

    slug = models.SlugField(max_length=128, blank=True)

    class Meta:
        db_table = 'gymnastics_clubs'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = str(slugify(str(self)))
        return super(Club, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('clubs.detail', kwargs={ 'id': self.id, 'slug': self.slug })

    def get_edit_url(self):
        return reverse('clubs.edit', kwargs={ 'pk': self.id, 'slug': self.slug })

    def get_delete_url(self):
        return reverse('clubs.delete', kwargs={ 'pk': self.id, 'slug': self.slug })