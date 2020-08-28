from .models import *
from django.contrib import admin


@admin.register(Days)
class ExtraCSS(admin.ModelAdmin):
    class Media:
        css = {
             'all': ('/static/css/admin-extra.css ',)
        }


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_filter = ['category']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'message', 'created_date')
    list_display = ('name', 'email', 'message', 'created_date')
    list_filter = ['name', 'email', 'created_date']
    ordering = ('-created_date',)

# admin.site.register(Food, FoodAdmin)
# admin.site.register(Days, MyModelAdmin)
# admin.site.register(Weeks)
# admin.site.register(Feedback)
