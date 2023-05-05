from django.contrib import admin

from tournaments.models import Tournament
from utils.admin import CommonAdmin


@admin.register(Tournament)
class TournamentAdmin(CommonAdmin):
    pass
