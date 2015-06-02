from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy


class CertificateRule(models.Model):
  
    content = models.CharField(max_length=128, 
        choices=(
            ('{{ athlete }}', ugettext_lazy('Athlete Name')),
            ('{{ athlete_performance }}', ugettext_lazy('Athlete Performance')),
            ('{{ athlete_rank }}', ugettext_lazy('Athlete Rank')),
            ('{{ team }}', ugettext_lazy('Team Name')),
            ('{{ team_performance }}', ugettext_lazy('Team Performance')),
            ('{{ team_rank }}', ugettext_lazy('Team Rank')),
            ('{{ team_member }}', ugettext_lazy('Team Member')))
    horizontal_position = models.DecimalField('Horizontal position in cm (most bottom)', decimal_places=1, null=True, blank=True)
    vertical_position = models.DecimalField('Vertical position in cm (most left)', decimal_places=1, default=150.0)

    prefix = models.CharField(max_length=128, null=True, blank=True)
    suffix = models.CharField(max_length=128, null=True, blank=True)

    font = models.CharField(
        choices=(
            ('', '')
        ))
    font_size = models.IntegerField('Font size in pt', default=24)

    certificate = models.ForeignKey('Certificate')


    class Meta:
        db_table = 'gymnastics_certificate_rules'

    def __str__(self):
        return "{0} '{1}' {2} (Position: {3}@{4}, Font: {5}, Font size: {6})".format(self.prefix, self.content, self.suffix, self.horizontal_position, self.vertical_position, self.font, self.font_size)