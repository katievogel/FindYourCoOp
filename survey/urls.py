from django.urls import path
from . import views


urlpatterns = [
    path("",views.index, name = "index"),
    path("<int:survey_question_id>/detail", views.detail, name="detail"),
    path("<int:survey_question_id>/results/", views.results, name="results"),
    path("<int:survey_question_id>/choose_answer/", views.choose_answer, name="choose_answer"),
    ]