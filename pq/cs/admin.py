from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import cs, CSApproved

class CSApprovedInline(admin.StackedInline):
    model = CSApproved
    extra = 0

class tsResource(resources.ModelResource):

    class Meta:
        model = cs
        fields = ('CSNo', 'IDate', 'DLine')
# @admin.register(cs)
class YourModelAdmin(ImportExportModelAdmin):
    inlines = [
        CSApprovedInline,
    ]
    pass

admin.site.register(cs,YourModelAdmin)