from django.contrib import admin

from .models import PDU


class PDUAdmin(admin.ModelAdmin):
    list_display = ['name','location','state']
admin.site.register(PDU,PDUAdmin)
