from django.contrib import admin

from squads.models import Squad
from utils.admin import CommonAdmin


@admin.register(Squad)
class SquadAdmin(CommonAdmin):
    pass
