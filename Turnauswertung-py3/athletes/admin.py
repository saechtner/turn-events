from typing import Any

from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from athletes.models import Athlete, AthletesImport
from utils.admin import CommonAdmin


@admin.register(Athlete)
class AthleteAdmin(CommonAdmin):
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
