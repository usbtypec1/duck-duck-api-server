from django.db.models import Min

from manas_admissions.models import Applicant, Application, Department
from users.models import User

__all__ = ('upsert_applicant', 'get_available_departments_info')


def upsert_applicant(
        *,
        user: User,
        application_number: str,
        natural_sciences_score: float,
        humanitarian_sciences_score: float,
        general_sciences_score: float,
        ort_score: int | None,
        english_score: float | None,
) -> Applicant:
    applicant, _ = Applicant.objects.update_or_create(
        user=user,
        defaults={
            'number': application_number,
            'natural_sciences_score': natural_sciences_score,
            'humanitarian_sciences_score': humanitarian_sciences_score,
            'general_sciences_score': general_sciences_score,
            'ort_score': ort_score,
            'english_score': english_score,
        },
    )
    return applicant


def get_available_departments_info(applicant: Applicant) -> dict:
    min_scores_by_department = (
        Application.objects
        .values('department__name', 'department__main_score_type')
        .annotate(
            min_ort_score=Min('ort_score'),
            min_english_score=Min('english_score'),
            min_main_score=Min('main_score')
        )
    )

    available_departments = []

    for department in min_scores_by_department:
        min_ort_score = department['min_ort_score']
        min_english_score = department['min_english_score']
        min_main_score = department['min_main_score']
        main_score_type = department['department__main_score_type']

        if main_score_type == Department.MainScoreType.NATURAL_SCIENCES:
            applicant_main_score = applicant.natural_sciences_score
        elif main_score_type == Department.MainScoreType.HUMANITARIAN_SCIENCES:
            applicant_main_score = applicant.humanitarian_sciences_score
        elif main_score_type == Department.MainScoreType.GENERAL_SCIENCES:
            applicant_main_score = applicant.general_sciences_score
        else:
            raise ValueError(f'Unknown main score type: {main_score_type}')

        if applicant_main_score < min_main_score:
            continue

        if min_ort_score is not None and applicant.ort_score is not None:
            if applicant.ort_score < min_ort_score:
                continue

        if min_english_score is not None and applicant.english_score is not None:
            if applicant.english_score < min_english_score:
                continue

        available_departments.append({
            'department_name': department['department__name'],
            'applicant_main_score': applicant_main_score,
            'applicant_ort_score': applicant.ort_score,
            'applicant_english_score': applicant.english_score,
            'main_score_type': main_score_type,
            'min_ort_score': min_ort_score,
            'min_english_score': min_english_score,
            'min_main_score': min_main_score,
        })

    return available_departments
