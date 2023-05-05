from django.contrib import admin


class CommonAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
