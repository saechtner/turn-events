from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy


class CertificateRule(models.Model):
  
    content = models.CharField(max_length=128, null=False, 
        choices=(
            ('{{ athlete }}', ugettext_lazy('Athlete Name')),
            ('{{ athlete_performance }}', ugettext_lazy('Athlete Performance')),
            ('{{ athlete_rank }}', ugettext_lazy('Athlete Rank')),
            ('{{ team }}', ugettext_lazy('Team Name')),
            ('{{ team_performance }}', ugettext_lazy('Team Performance')),
            ('{{ team_rank }}', ugettext_lazy('Team Rank')),
            ('{{ team_Mitglieder? }}', ugettext_lazy('Team Mitglieder!?')))# might be a choice field ()
    horizontal_position = models.DecimalField('Horizontal position in cm', decimal_places=1, null=True, blank=True)
    vertical_position = models.DecimalField('Vertical position in cm', decimal_places=1, default=150.0)

    certificate = models.ForeignKey('Certificate')


    class Meta:
        db_table = 'gymnastics_certificate_rules'