from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', language_view, name="language"),
    path('education/', education_view, name="education"),
    path('skills/', skills_view, name='skills'),
    path('projects/', project_view, name='project'),
    path('personal-information/', personal_information_view, name="personal-information")
]

