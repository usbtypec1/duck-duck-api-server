from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from manas_admissions.models import Applicant, Application, Department


class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department


@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    resource_class = DepartmentResource
    list_display = ('name', 'main_score_type')


class ApplicationResource(resources.ModelResource):
    class Meta:
        model = Application


@admin.register(Application)
class Application(ImportExportModelAdmin):
    resource_class = ApplicationResource
    list_display = ('number', 'department', 'rating', 'main_score', 'stage')


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    pass
