from django.contrib import admin
from .models import ContactMessage

# Customize admin site headers
admin.site.site_header = 'RMGB Maritime Services'
admin.site.site_title = 'RMGB Admin'
admin.site.index_title = 'Welcome, Marilyn! Manage your website here.'

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'sent_at', 'short_message')
    list_filter = ('sent_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'phone', 'message', 'sent_at')
    ordering = ('-sent_at',)

    def short_message(self, obj):
        return obj.message[:60] + '...' if len(obj.message) > 60 else obj.message
    short_message.short_description = 'Message Preview'

    def has_add_permission(self, request):
        return False