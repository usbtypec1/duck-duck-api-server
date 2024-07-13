from manas_admissions.models import Applicant
from users.models import User

__all__ = ('get_applicant_by_user',)


def get_applicant_by_user(user: User) -> Applicant:
    return Applicant.objects.get(user=user)
