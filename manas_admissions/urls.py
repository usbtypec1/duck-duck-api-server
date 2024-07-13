from django.urls import path

from manas_admissions.views import (
    ApplicantCreateUpdateApi,
    ApplicantAvailableDepartmentsListApi,
)

urlpatterns = [
    path(
        r'applicants/',
        ApplicantCreateUpdateApi.as_view(),
        name='applicant-create-update',
    ),
    path(
        r'applicants/<int:user_id>/available-departments/',
        ApplicantAvailableDepartmentsListApi.as_view(),
        name='applicant-available-departments',
    )
]
