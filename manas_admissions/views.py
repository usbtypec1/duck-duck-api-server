from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from manas_admissions.models import Applicant
from manas_admissions.selectors import get_applicant_by_user
from manas_admissions.services import (
    get_available_departments_info,
    upsert_applicant,
)
from users.services.users import get_or_create_user


class ApplicantCreateUpdateApi(APIView):
    class InputSerializer(serializers.Serializer):
        user_id = serializers.IntegerField()
        application_number = serializers.CharField(max_length=8, min_length=8)
        natural_sciences_score = serializers.FloatField()
        humanitarian_sciences_score = serializers.FloatField()
        general_sciences_score = serializers.FloatField()
        ort_score = serializers.IntegerField(required=False, allow_null=True)
        english_score = serializers.FloatField(required=False, allow_null=True)

    def post(self, request: Request) -> Response:
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serialized_data = serializer.data

        user_id: int = serialized_data['user_id']
        application_number: str = serialized_data['application_number']
        natural_sciences_score: float = (
            serialized_data['natural_sciences_score']
        )
        humanitarian_sciences_score: float = (
            serialized_data['humanitarian_sciences_score']
        )
        general_sciences_score: float = (
            serialized_data['general_sciences_score']
        )
        ort_score: int | None = serialized_data.get('ort_score')
        english_score: float | None = serialized_data.get('english_score')

        user, _ = get_or_create_user(user_id=user_id)

        upsert_applicant(
            user=user,
            application_number=application_number,
            natural_sciences_score=natural_sciences_score,
            humanitarian_sciences_score=humanitarian_sciences_score,
            general_sciences_score=general_sciences_score,
            ort_score=ort_score,
            english_score=english_score,
        )
        return Response({'ok': True})


class ApplicantAvailableDepartmentsListApi(APIView):

    def get(self, request: Request, user_id: int) -> Response:
        user, _ = get_or_create_user(user_id=user_id)

        try:
            applicant = get_applicant_by_user(user)
        except Applicant.DoesNotExist:
            raise NotFound({'detail': 'Applicant not found'})

        departments = get_available_departments_info(applicant)

        return Response({'ok': True, 'result': departments})
