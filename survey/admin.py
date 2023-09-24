from django.contrib import admin

# Register your models here.
from .models import SurveyQuestion, SurveyChoice, Friend

admin.site.register(SurveyQuestion)
admin.site.register(SurveyChoice)
admin.site.register(Friend)