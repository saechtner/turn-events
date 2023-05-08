from typing import Any

from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from clubs.models import Club
from utils.admin import CommonAdmin


@admin.register(Club)
class ClubAdmin(CommonAdmin):
    raw_id_fields = ("address",)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return (
            super()
            .get_queryset(request)
            .select_related(
                "address",
            )
        )
