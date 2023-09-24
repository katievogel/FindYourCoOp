from distutils.command.upload import upload
from django.db import models

#update in the terminal by running 'python manage.py shell'

class Friend(models.Model):
    '''
    Class that manages the user instances, or 'friends'.
    '''
    username = models.CharField(max_length = 50)
    user_image = models.URLField()
    survey_results = models.JSONField()

class SurveyQuestion(models.Model):
    '''
    Class that manages the survey questions for friend matching
    '''
    question_text = models.CharField(max_length = 250)

class SurveyChoice(models.Model):
    '''
    Class that manages the possible responses for survey questions. Value is used to quantify survey results for friend matching.
    '''
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 250)
    choice_value = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text
