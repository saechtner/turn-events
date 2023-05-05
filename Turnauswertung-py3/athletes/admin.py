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


admin.site.register(AthletesImport)
