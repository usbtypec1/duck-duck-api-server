from django.db import models

from users.models import User

__all__ = ('Relationship',)


class Relationship(models.Model):
    first_user = models.ForeignKey(User, on_delete=models.CASCADE)
    second_user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    broke_up_at = models.DateTimeField(null=True, blank=True)
