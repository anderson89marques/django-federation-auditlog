from django.contrib import admin

from django_federation_auditlog.models import LogEntry
from django_federation_auditlog.mixins import LogEntryAdminMixin
from auditlog.filters import ResourceTypeFilter


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin, LogEntryAdminMixin):
    list_display = [
        "created",
        "resource_url",
        "action",
        "msg_short",
        "user_url",
    ]
    search_fields = [
        "timestamp",
        "object_repr",
        "changes",
        "actor",
    ]
    list_filter = ["action", ResourceTypeFilter]
    readonly_fields = ["created", "resource_url", "action", "user_url", "msg"]
    fieldsets = [
        (None, {"fields": ["created", "user_url", "resource_url"]}),
        ("Changes", {"fields": ["action", "msg"]}),
    ]
