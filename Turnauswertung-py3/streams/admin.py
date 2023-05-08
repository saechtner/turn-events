from django.contrib import admin

from streams.models import Stream
from utils.admin import CommonAdmin


@admin.register(Stream)
class StreamAdmin(CommonAdmin):
    pass
