from django.contrib import admin

from athletes.models import Athlete
from squads.models import Squad
from utils.admin import CommonAdmin


class AthletesSquadInline(admin.TabularInline):
    model = Athlete
    fields = ("first_name", "last_name", "stream", "club", "team", "squad_position")
    readonly_fields = ("first_name", "last_name", "stream", "club", "team")
    extra = 0
    can_delete = False

    def has_change_permission(self, request, obj=None):
        return True


@admin.register(Squad)
class SquadAdmin(CommonAdmin):
    inlines = [AthletesSquadInline]
