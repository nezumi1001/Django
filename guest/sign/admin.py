from django.contrib import admin
from sign.models import Event, Guest

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'limit', 'address', 'status', 'start_time']
    search_fields = ['name'] # 搜索
    list_filter = ['status'] # 过滤

class GuestAdmin(admin.ModelAdmin):
    list_display = ['real_name', 'phone', 'email', 'sign', 'event']
    list_display_links = ['real_name', 'phone'] # 链接
    search_fields = ['real_name', 'phone']  # 搜索
    list_filter = ['event_id']  # 过滤

admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)