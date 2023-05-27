from typing import Any

from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.utils.translation import gettext_lazy as _

from athletes.models import Athlete, AthletesImport
from utils.admin import CommonAdmin


class HasTeamListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _("Team")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "team"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return [
            ("yes", _("Team")),
            ("no", _("No team")),
        ]

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == "yes":
            return queryset.filter(team__isnull=False)
        if self.value() == "no":
            return queryset.filter(team__isnull=True)


@admin.register(Athlete)
class AthleteAdmin(CommonAdmin):
    list_display = ["__str__", "stream", "club", "team"]
    list_filter = [HasTeamListFilter]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return (
            super()
            .get_queryset(request)
            .select_related("club", "stream", "team", "squad", "athletes_import")
        )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "team":
            kwargs["queryset"] = db_field.related_model.objects.all().select_related(
                "stream"
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(AthletesImport)
