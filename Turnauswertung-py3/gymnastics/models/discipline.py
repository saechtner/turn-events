from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify


class Discipline(models.Model):
  
    name = models.CharField(max_length=50, null=False)

    slug = models.SlugField(max_length=128, blank=True)
    
    class Meta:
        db_table = 'gymnastics_disciplines'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = str(slugify(str(self)))
        return super(Discipline, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('disciplines.detail', kwargs={ 'id': self.id, 'slug': self.slug })

    def get_edit_url(self):
        return reverse('disciplines.edit', kwargs={ 'pk': self.id, 'slug': self.slug })

    def get_delete_url(self):
        return reverse('disciplines.delete', kwargs={ 'pk': self.id, 'slug': self.slug })