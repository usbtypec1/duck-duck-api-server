from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(f'{settings.ROOT_PATH}admin/', admin.site.urls),
    path(f'{settings.ROOT_PATH}', include('users.urls')),
    path(f'{settings.ROOT_PATH}', include('secret_messages.urls')),
    path(f'{settings.ROOT_PATH}economics/', include('economics.urls')),
    path(f'{settings.ROOT_PATH}', include('food_menu.urls')),
    path(f'{settings.ROOT_PATH}holidays/', include('holidays.urls')),
    path(f'{settings.ROOT_PATH}quizzes/', include('quizzes.urls')),
    path(f'{settings.ROOT_PATH}mining/', include('mining.urls')),
    path(f'{settings.ROOT_PATH}', include('user_characteristics.urls')),
    path(f'{settings.ROOT_PATH}admissions/', include('manas_admissions.urls')),
]
