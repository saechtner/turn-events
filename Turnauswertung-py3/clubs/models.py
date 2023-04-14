from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy


class Club(models.Model):

    name = models.CharField(gettext_lazy('Name'), max_length=50)

    address = models.ForeignKey(
        'common.Address', null=True, blank=True, on_delete=models.CASCADE,
        verbose_name=gettext_lazy('Address')
    )

    slug = models.SlugField(max_length=128, blank=True)

    class Meta:
        app_label = "clubs"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = str(slugify(str(self)))
        return super(Club, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'clubs.detail', kwargs={'id': self.id, 'slug': self.slug})

    def get_edit_url(self):
        return reverse('clubs.edit', kwargs={'pk': self.id, 'slug': self.slug})

    def get_delete_url(self):
        return reverse(
            'clubs.delete', kwargs={'pk': self.id, 'slug': self.slug})
