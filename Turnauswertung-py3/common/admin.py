from typing import Any

from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from common.models import Address, Discipline, Performance
from utils.admin import CommonAdmin


@admin.register(Discipline)
class DisciplineAdmin(CommonAdmin):
    pass


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    raw_id_fields = ("athlete", "discipline")

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).select_related("athlete", "discipline")


admin.site.register(Address)
