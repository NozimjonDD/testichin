from django.contrib import admin

# Register your models here.
from survey.models import Survey, SurveyVariant, SurveyResult

admin.site.register(Survey)
admin.site.register(SurveyVariant)
admin.site.register(SurveyResult)
