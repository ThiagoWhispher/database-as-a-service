# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django_services import admin
from ..service.database import DatabaseService
from ..forms import DatabaseForm


class DatabaseAdmin(admin.DjangoServicesAdmin):
    service_class = DatabaseService
    search_fields = ("name", "databaseinfra__name")
    list_display = ("name", "databaseinfra",)
    list_filter = ("databaseinfra", "project",)
    change_form_template = "logical/database_change_form.html"
    fieldsets = (
        (None, {
            'fields': ('name', 'project', 'plan')
            }
        ),
    )
    form = DatabaseForm


    def get_readonly_fields(self, request, obj=None):
        """
        if in edit mode, name is readonly.
        """
        if obj: #In edit mode
            return ('name',) + self.readonly_fields

        return self.readonly_fields


    def add_view(self, request, form_url='', extra_context=None, **kwargs):
        return super(DatabaseAdmin, self).add_view(request, form_url, extra_context, **kwargs)


    def change_view(self, request, object_id, form_url='', extra_context=None):
        return super(DatabaseAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)


