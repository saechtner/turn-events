from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy


class Performance(models.Model):
    value = models.DecimalField(
        ugettext_lazy("Value"), null=False, max_digits=5, decimal_places=3, default=0.0
    )
    value_final = models.DecimalField(
        ugettext_lazy("Final Value"),
        null=True,
        blank=True,
        max_digits=5,
        decimal_places=3,
    )

    athlete = models.ForeignKey(
        "athletes.Athlete", verbose_name=ugettext_lazy("Athlete")
    )
    discipline = models.ForeignKey(
        "Discipline", verbose_name=ugettext_lazy("Discipline")
    )

    class Meta:
        unique_together = (("athlete", "discipline"),)

    def __str__(self):
        return "{}, {}".format(self.athlete, self.discipline)  # old
        # return "{0}, {1}: {2}".format(self.athlete, self.discipline, self.value)  # noqa


class Discipline(models.Model):
    name = models.CharField(ugettext_lazy("Name"), max_length=50, null=False)

    slug = models.SlugField(max_length=128, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = str(slugify(str(self)))
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("disciplines.detail", kwargs={"id": self.id, "slug": self.slug})

    def get_edit_url(self):
        return reverse("disciplines.edit", kwargs={"pk": self.id, "slug": self.slug})

    def get_delete_url(self):
        return reverse("disciplines.delete", kwargs={"pk": self.id, "slug": self.slug})


class Address(models.Model):
    contact_name = models.CharField(ugettext_lazy("Contact name"), max_length=64)
    phone = models.CharField(
        ugettext_lazy("Contact phone"), max_length=15, null=True, blank=True
    )
    email = models.EmailField(ugettext_lazy("Contact email"), null=True, blank=True)
    street = models.CharField(ugettext_lazy("Street"), max_length=128)
    city = models.CharField(ugettext_lazy("City"), max_length=128)
    province = models.CharField(ugettext_lazy("Province"), max_length=128)
    zip_code = models.CharField(ugettext_lazy("Zip code"), max_length=10)

    @property
    def address_formatted(self):
        return "{}\n{} {}\n{}".format(
            self.street, self.zip_code, self.city, self.province
        )


class StreamDisciplineJoin(models.Model):
    position = models.IntegerField(null=True)

    stream = models.ForeignKey("streams.Stream")
    discipline = models.ForeignKey("Discipline")

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return "No {}: {} in {}".format(self.position, self.discipline, self.stream)
